"""
BotSpeak Database-Aware Decoder Module
Converts BotSpeak codes back to human-readable text using database
"""

import re
from db_manager import get_db_manager
import time

class DatabaseDecoder:
    def __init__(self):
        self.db_manager = get_db_manager()
        self.dictionary = None
        self._load_dictionary()
    
    def _load_dictionary(self):
        """Load dictionary from database"""
        self.dictionary = self.db_manager.get_dictionary_as_dict()
    
    def _is_valid_code(self, code):
        """Check if a code exists in the dictionary"""
        return code in self.dictionary
    
    def _normalize_code(self, code):
        """Normalize code format for consistent lookup"""
        code = code.strip()
        
        # Handle different code formats
        if code.isdigit():
            # Pure numeric codes - ensure proper formatting
            if len(code) == 3 and code.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
                return code  # 100-999 range
            elif len(code) == 4 and code.startswith('0'):
                return code  # 0001-9999 range
            elif len(code) <= 3:
                return code.zfill(3)  # Pad with zeros if needed
            elif len(code) == 4:
                return code
        
        # Alphanumeric codes (A01-Z99)
        elif len(code) == 3 and code[0].isalpha() and code[1:].isdigit():
            return code.upper()
        
        return code
    
    def decode_codes(self, encoded_text):
        """Decode BotSpeak codes back to human text"""
        if not encoded_text.strip():
            return ""
        
        # Split by sentence separators first
        sentences = encoded_text.split(' | ')
        decoded_sentences = []
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # Split codes by spaces
            codes = sentence.split()
            decoded_words = []
            
            for code in codes:
                if not code.strip():
                    continue
                
                normalized_code = self._normalize_code(code)
                
                if self._is_valid_code(normalized_code):
                    decoded_words.append(self.dictionary[normalized_code])
                else:
                    # Unknown code - keep as is (might be a word that wasn't encoded)
                    decoded_words.append(code)
            
            if decoded_words:
                decoded_sentence = ' '.join(decoded_words)
                # Capitalize first letter of sentence
                decoded_sentence = decoded_sentence[0].upper() + decoded_sentence[1:] if decoded_sentence else ""
                decoded_sentences.append(decoded_sentence)
        
        # Join sentences with periods
        result = '. '.join(decoded_sentences)
        if result and not result.endswith('.'):
            result += '.'
        
        return result
    
    def decode_with_validation(self, encoded_text, track_usage=True):
        """Decode with validation and error reporting"""
        if not encoded_text.strip():
            return {
                'decoded_text': "",
                'success': True,
                'unknown_codes': [],
                'total_codes': 0,
                'recognized_codes': 0
            }
        
        start_time = time.time()
        
        # Split by sentence separators
        sentences = encoded_text.split(' | ')
        decoded_sentences = []
        unknown_codes = []
        total_codes = 0
        recognized_codes = 0
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            codes = sentence.split()
            decoded_words = []
            
            for code in codes:
                if not code.strip():
                    continue
                    
                total_codes += 1
                normalized_code = self._normalize_code(code)
                
                if self._is_valid_code(normalized_code):
                    decoded_words.append(self.dictionary[normalized_code])
                    recognized_codes += 1
                else:
                    # Unknown code
                    decoded_words.append(f"[{code}]")  # Mark unknown codes
                    unknown_codes.append(code)
            
            if decoded_words:
                decoded_sentence = ' '.join(decoded_words)
                decoded_sentence = decoded_sentence[0].upper() + decoded_sentence[1:] if decoded_sentence else ""
                decoded_sentences.append(decoded_sentence)
        
        result = '. '.join(decoded_sentences)
        if result and not result.endswith('.'):
            result += '.'
        
        recognition_rate = (recognized_codes / total_codes * 100) if total_codes > 0 else 100
        
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Log operation to database if tracking is enabled
        if track_usage:
            try:
                self.db_manager.log_decoding_operation(
                    input_codes=encoded_text,
                    output_text=result,
                    recognition_rate=recognition_rate,
                    processing_time=processing_time
                )
            except Exception as e:
                print(f"Warning: Could not log decoding operation: {e}")
        
        return {
            'decoded_text': result,
            'success': len(unknown_codes) == 0,
            'unknown_codes': unknown_codes,
            'total_codes': total_codes,
            'recognized_codes': recognized_codes,
            'recognition_rate': round(recognition_rate, 2)
        }
    
    def get_code_info(self, code):
        """Get information about a specific code"""
        normalized_code = self._normalize_code(code)
        
        if not self._is_valid_code(normalized_code):
            return {
                'code': code,
                'valid': False,
                'text': None,
                'code_type': None
            }
        
        # Determine code type
        code_type = "unknown"
        if normalized_code.isdigit():
            if 100 <= int(normalized_code) <= 999:
                code_type = "numeric (common words/phrases)"
            elif 1 <= int(normalized_code) <= 9999:
                code_type = "4-digit (technical/specialized)"
        elif len(normalized_code) == 3 and normalized_code[0].isalpha():
            code_type = "alphanumeric (moderately common)"
        
        return {
            'code': normalized_code,
            'valid': True,
            'text': self.dictionary[normalized_code],
            'code_type': code_type
        }
    
    def refresh_dictionary(self):
        """Reload dictionary from database (useful if dictionary is updated)"""
        self._load_dictionary()