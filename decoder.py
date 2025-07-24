"""
BotSpeak Decoder Module
Converts BotSpeak codes back to human-readable text
"""

import re
from botspeak_dict import botspeak_dict

class BotSpeakDecoder:
    def __init__(self):
        self.dictionary = botspeak_dict
    
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
    
    def decode_with_validation(self, encoded_text):
        """Decode with validation and error reporting"""
        if not encoded_text.strip():
            return {
                'decoded_text': "",
                'success': True,
                'unknown_codes': [],
                'total_codes': 0,
                'recognized_codes': 0
            }
        
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
    
    def batch_decode(self, encoded_texts):
        """Decode multiple encoded texts"""
        results = []
        
        for i, encoded_text in enumerate(encoded_texts):
            result = self.decode_with_validation(encoded_text)
            result['index'] = i
            result['input'] = encoded_text
            results.append(result)
        
        return results

# Example usage and testing
if __name__ == "__main__":
    decoder = BotSpeakDecoder()
    
    # Test encoded sentences
    test_encoded = [
        "237 245",  # "hello I'm fine"
        "103 377 147 C01 0001 0002",  # "I want see in addition artificial intelligence"  
        "242 779 F17 382",  # "thank you very much for your help"
        "255 380 A04 377",  # "what is love you like want"
        "190 174 662 600",  # "today hot weather business"
        "103 A13 D06 820",  # "I what should I I need to go morning"
    ]
    
    print("=== BotSpeak Decoder Test Results ===\n")
    
    for i, encoded in enumerate(test_encoded, 1):
        result = decoder.decode_with_validation(encoded)
        
        print(f"Test {i}:")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {result['decoded_text']}")
        print(f"Success:  {result['success']}")
        print(f"Recognition: {result['recognition_rate']}% ({result['recognized_codes']}/{result['total_codes']})")
        
        if result['unknown_codes']:
            print(f"Unknown codes: {result['unknown_codes']}")
        print()
    
    # Test code information lookup
    print("=== Code Information Lookup ===")
    test_codes = ["237", "A01", "0001", "999", "Z99", "invalid"]
    
    for code in test_codes:
        info = decoder.get_code_info(code)
        print(f"Code '{code}': {info}")
    
    # Test with sentence separators
    print("\n=== Multi-sentence Test ===")
    multi_sentence = "237 245 | 242 F17 382 | 190 174"
    result = decoder.decode_with_validation(multi_sentence)
    print(f"Encoded: {multi_sentence}")
    print(f"Decoded: {result['decoded_text']}")
    print(f"Recognition: {result['recognition_rate']}%")
