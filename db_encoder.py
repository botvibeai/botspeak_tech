"""
BotSpeak Database-Aware Encoder Module
Converts human text into BotSpeak compressed codes using database
"""

import re
import string
from db_manager import get_db_manager
import time

class DatabaseEncoder:
    def __init__(self):
        self.db_manager = get_db_manager()
        self.dictionary = None
        self.reverse_dictionary = None
        self.phrase_mapping = None
        self._load_dictionary()
    
    def _load_dictionary(self):
        """Load dictionary from database"""
        self.dictionary = self.db_manager.get_dictionary_as_dict()
        self.reverse_dictionary = self.db_manager.get_reverse_dictionary_as_dict()
        self.phrase_mapping = self._create_phrase_mapping()
    
    def _create_phrase_mapping(self):
        """Create mapping for multi-word phrases (optimized for performance)"""
        phrases = {}
        for text, code in self.reverse_dictionary.items():
            if ' ' in text and len(text.split()) <= 4:  # Limit to 4 words max
                phrases[text.lower()] = code
        
        # Sort by length (longest first) for greedy matching
        return dict(sorted(phrases.items(), key=lambda x: len(x[0]), reverse=True))
    
    def _preprocess_text(self, text):
        """Clean and preprocess input text"""
        # Convert to lowercase
        text = text.lower()
        
        # Replace common contractions
        contractions = {
            "don't": "do not",
            "won't": "will not", 
            "can't": "cannot",
            "n't": " not",
            "'re": " are",
            "'ve": " have",
            "'ll": " will",
            "'d": " would",
            "'m": " am",
            "'s": " is"
        }
        
        for contraction, expansion in contractions.items():
            text = text.replace(contraction, expansion)
        
        # Remove extra punctuation but keep sentence structure
        text = re.sub(r'[^\w\s\.\!\?]', ' ', text)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def _tokenize_sentence(self, sentence):
        """Tokenize sentence into words and phrases (optimized)"""
        tokens = []
        words = sentence.split()
        i = 0
        
        while i < len(words):
            matched = False
            
            # Try to match multi-word phrases (limit to 4 words max for performance)
            max_phrase_len = min(4, len(words) - i)
            for phrase_len in range(max_phrase_len, 0, -1):
                candidate_phrase = ' '.join(words[i:i + phrase_len])
                
                if candidate_phrase in self.phrase_mapping:
                    tokens.append((candidate_phrase, self.phrase_mapping[candidate_phrase]))
                    i += phrase_len
                    matched = True
                    break
            
            if not matched:
                # Single word lookup
                word = words[i]
                if word in self.reverse_dictionary:
                    tokens.append((word, self.reverse_dictionary[word]))
                else:
                    # Unknown word - keep as is
                    tokens.append((word, word))
                i += 1
        
        return tokens
    
    def encode_sentence(self, sentence):
        """Encode a single sentence to BotSpeak codes"""
        if not sentence.strip():
            return ""
        
        # Preprocess the sentence
        processed_sentence = self._preprocess_text(sentence)
        
        # Tokenize and encode
        tokens = self._tokenize_sentence(processed_sentence)
        
        # Extract codes
        codes = [token[1] for token in tokens]
        
        return ' '.join(codes)
    
    def encode_text(self, text):
        """Encode full text (multiple sentences) to BotSpeak codes"""
        if not text.strip():
            return ""
        
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        encoded_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                encoded = self.encode_sentence(sentence)
                if encoded:
                    encoded_sentences.append(encoded)
        
        return ' | '.join(encoded_sentences)  # Use | to separate sentences
    
    def get_compression_stats(self, original_text, encoded_text):
        """Calculate compression statistics"""
        original_chars = len(original_text)
        encoded_chars = len(encoded_text)
        
        if original_chars == 0:
            return {
                'original_length': 0,
                'encoded_length': 0,
                'compression_ratio': 0,
                'space_saved': 0,
                'percentage_saved': 0
            }
        
        compression_ratio = encoded_chars / original_chars
        space_saved = original_chars - encoded_chars
        percentage_saved = (space_saved / original_chars) * 100
        
        return {
            'original_length': original_chars,
            'encoded_length': encoded_chars,
            'compression_ratio': round(compression_ratio, 3),
            'space_saved': space_saved,
            'percentage_saved': round(percentage_saved, 2)
        }
    
    def encode_with_stats(self, text, track_usage=True):
        """Encode text and return both encoded text and statistics"""
        start_time = time.time()
        
        encoded = self.encode_text(text)
        stats = self.get_compression_stats(text, encoded)
        
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Log operation to database if tracking is enabled
        if track_usage:
            try:
                self.db_manager.log_encoding_operation(
                    input_text=text,
                    output_text=encoded,
                    compression_ratio=stats['compression_ratio'],
                    processing_time=processing_time
                )
            except Exception as e:
                print(f"Warning: Could not log encoding operation: {e}")
        
        return {
            'original_text': text,
            'encoded_text': encoded,
            'statistics': stats
        }
    
    def refresh_dictionary(self):
        """Reload dictionary from database (useful if dictionary is updated)"""
        self._load_dictionary()