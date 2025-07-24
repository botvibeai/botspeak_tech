"""
BotSpeak Database Manager
Handles database operations for dictionary entries and usage tracking
"""

from models import DictionaryEntry, EncodingHistory, SystemStats, get_database_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc
from datetime import datetime, timedelta
import time
from functools import lru_cache
import threading

class DatabaseManager:
    """Manages database operations for BotSpeak"""
    
    def __init__(self):
        self.session = None
        self._search_cache = {}
        self._cache_lock = threading.Lock()
        self._cache_size_limit = 100  # Limit cache to 100 search results
        self._connection_pool = None
        self._session_factory = None
        self._in_memory_dict = None  # For fast searching
        self._dict_loaded = False
    
    def get_session(self):
        """Get database session"""
        if not self.session:
            self.session = get_database_session()
        return self.session
    
    def close_session(self):
        """Close database session"""
        if self.session:
            self.session.close()
            self.session = None
    
    # Dictionary operations
    def get_dictionary_entries(self, active_only=True):
        """Get all dictionary entries"""
        session = self.get_session()
        query = session.query(DictionaryEntry)
        
        if active_only:
            query = query.filter(DictionaryEntry.is_active == True)
        
        return query.all()
    
    def get_dictionary_as_dict(self):
        """Get dictionary entries as a Python dict (code -> text)"""
        entries = self.get_dictionary_entries()
        return {entry.code: entry.text for entry in entries}
    
    def get_reverse_dictionary_as_dict(self):
        """Get reverse dictionary entries as a Python dict (text -> code)"""
        entries = self.get_dictionary_entries()
        return {entry.text: entry.code for entry in entries}
    
    def _load_dictionary_in_memory(self):
        """Load dictionary into memory for fast searching"""
        if self._dict_loaded and self._in_memory_dict:
            return
        
        try:
            # Load from static dictionary for speed
            from botspeak_dict import botspeak_dict
            self._in_memory_dict = []
            
            for code, text in botspeak_dict.items():
                # Determine code type
                code_type = "unknown"
                if code.isdigit():
                    if 100 <= int(code) <= 999:
                        code_type = "numeric"
                    elif 1 <= int(code) <= 9999:
                        code_type = "4-digit"
                elif len(code) == 3 and code[0].isalpha():
                    code_type = "alphanumeric"
                
                self._in_memory_dict.append({
                    'code': code,
                    'text': text,
                    'code_type': code_type,
                    'frequency': 0,  # Default frequency
                    'word_count': len(text.split())
                })
            
            self._dict_loaded = True
            print(f"Loaded {len(self._in_memory_dict)} dictionary entries into memory")
            
        except Exception as e:
            print(f"Warning: Could not load dictionary into memory: {e}")
            self._dict_loaded = False
    
    def search_dictionary(self, query, limit=50):
        """Search dictionary entries using in-memory search for maximum speed"""
        search_term = query.lower()
        cache_key = f"{search_term}:{limit}"
        
        # Check cache first
        with self._cache_lock:
            if cache_key in self._search_cache:
                cached_data = self._search_cache[cache_key]
                # Move to end (LRU behavior)  
                self._search_cache[cache_key] = self._search_cache.pop(cache_key)
                
                # Convert cached data back to mock objects for compatibility
                result = []
                for data in cached_data:
                    class MockEntry:
                        def __init__(self, data):
                            for key, value in data.items():
                                setattr(self, key, value)
                    result.append(MockEntry(data))
                return result
        
        # Ensure dictionary is loaded in memory
        self._load_dictionary_in_memory()
        
        if not self._in_memory_dict:
            # Fallback to empty results if memory loading failed
            return []
        
        # Perform in-memory search - much faster than database queries
        results = []
        seen_codes = set()
        
        # Priority 1: Exact matches
        for entry in self._in_memory_dict:
            if len(results) >= limit:
                break
            if entry['code'].lower() == search_term or entry['text'].lower() == search_term:
                if entry['code'] not in seen_codes:
                    results.append(entry.copy())
                    seen_codes.add(entry['code'])
        
        # Priority 2: Prefix matches (if we need more results)
        if len(results) < limit:
            for entry in self._in_memory_dict:
                if len(results) >= limit:
                    break
                if entry['code'] not in seen_codes:
                    code_lower = entry['code'].lower()
                    text_lower = entry['text'].lower()
                    if code_lower.startswith(search_term) or text_lower.startswith(search_term):
                        results.append(entry.copy())
                        seen_codes.add(entry['code'])
        
        # Priority 3: Contains matches (if we still need more)
        if len(results) < limit:
            for entry in self._in_memory_dict:
                if len(results) >= limit:
                    break
                if entry['code'] not in seen_codes:
                    code_lower = entry['code'].lower()
                    text_lower = entry['text'].lower()
                    if search_term in code_lower or search_term in text_lower:
                        results.append(entry.copy())
                        seen_codes.add(entry['code'])
        
        # Sort by frequency (desc) then code
        results.sort(key=lambda x: (-x['frequency'], x['code']))
        
        # Cache the results
        with self._cache_lock:
            # Simple LRU cache management
            if len(self._search_cache) >= self._cache_size_limit:
                oldest_key = next(iter(self._search_cache))
                del self._search_cache[oldest_key]
            self._search_cache[cache_key] = results[:limit]
        
        # Convert to mock objects for compatibility
        mock_results = []
        for data in results[:limit]:
            class MockEntry:
                def __init__(self, data):
                    for key, value in data.items():
                        setattr(self, key, value)
            mock_results.append(MockEntry(data))
        
        return mock_results
    
    def get_random_dictionary_entries(self, count=20):
        """Get random dictionary entries using in-memory data for speed"""
        cache_key = f"random:{count}"
        
        # Check cache first
        with self._cache_lock:
            if cache_key in self._search_cache:
                cached_data = self._search_cache[cache_key]
                # Move to end (LRU behavior)
                self._search_cache[cache_key] = self._search_cache.pop(cache_key)
                
                # Convert cached data back to mock objects for compatibility
                result = []
                for data in cached_data:
                    class MockEntry:
                        def __init__(self, data):
                            for key, value in data.items():
                                setattr(self, key, value)
                    result.append(MockEntry(data))
                return result
        
        # Ensure dictionary is loaded in memory
        self._load_dictionary_in_memory()
        
        if not self._in_memory_dict:
            return []
        
        import random
        
        # Get random entries from in-memory dictionary
        random_entries = random.sample(self._in_memory_dict, min(count, len(self._in_memory_dict)))
        
        # Cache the result
        with self._cache_lock:
            # Simple LRU cache management
            if len(self._search_cache) >= self._cache_size_limit:
                oldest_key = next(iter(self._search_cache))
                del self._search_cache[oldest_key]
            self._search_cache[cache_key] = random_entries
        
        # Convert to mock objects for compatibility
        mock_results = []
        for data in random_entries:
            class MockEntry:
                def __init__(self, data):
                    for key, value in data.items():
                        setattr(self, key, value)
            mock_results.append(MockEntry(data))
        
        return mock_results
    
    def increment_code_frequency(self, code):
        """Increment usage frequency for a code"""
        session = self.get_session()
        try:
            entry = session.query(DictionaryEntry).filter_by(code=code).first()
            if entry:
                entry.frequency += 1
                session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error updating frequency for {code}: {e}")
    
    def batch_increment_frequencies(self, codes):
        """Increment frequencies for multiple codes"""
        session = self.get_session()
        try:
            for code in codes:
                entry = session.query(DictionaryEntry).filter_by(code=code).first()
                if entry:
                    entry.frequency += 1
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error updating frequencies: {e}")
    
    # Usage tracking
    def log_encoding_operation(self, input_text, output_text, compression_ratio, 
                             processing_time, ip_address=None, user_agent=None):
        """Log an encoding operation"""
        session = self.get_session()
        try:
            operation = EncodingHistory(
                operation_type='encode',
                input_text=input_text,
                output_text=output_text,
                compression_ratio=str(compression_ratio),
                processing_time=str(processing_time),
                ip_address=ip_address,
                user_agent=user_agent
            )
            session.add(operation)
            session.commit()
            
            # Update code frequencies
            codes = output_text.split()
            self.batch_increment_frequencies([code for code in codes if code in self.get_dictionary_as_dict()])
            
        except Exception as e:
            session.rollback()
            print(f"Error logging encoding operation: {e}")
    
    def log_decoding_operation(self, input_codes, output_text, recognition_rate,
                             processing_time, ip_address=None, user_agent=None):
        """Log a decoding operation"""
        session = self.get_session()
        try:
            operation = EncodingHistory(
                operation_type='decode',
                input_text=input_codes,
                output_text=output_text,
                recognition_rate=str(recognition_rate),
                processing_time=str(processing_time),
                ip_address=ip_address,
                user_agent=user_agent
            )
            session.add(operation)
            session.commit()
            
            # Update code frequencies
            codes = input_codes.split()
            self.batch_increment_frequencies([code for code in codes if code in self.get_dictionary_as_dict()])
            
        except Exception as e:
            session.rollback()
            print(f"Error logging decoding operation: {e}")
    
    # Statistics
    def get_dictionary_stats(self):
        """Get comprehensive dictionary statistics"""
        session = self.get_session()
        
        total_entries = session.query(DictionaryEntry).filter(DictionaryEntry.is_active == True).count()
        numeric_count = session.query(DictionaryEntry).filter(
            DictionaryEntry.is_active == True,
            DictionaryEntry.code_type == 'numeric'
        ).count()
        alphanumeric_count = session.query(DictionaryEntry).filter(
            DictionaryEntry.is_active == True,
            DictionaryEntry.code_type == 'alphanumeric'
        ).count()
        four_digit_count = session.query(DictionaryEntry).filter(
            DictionaryEntry.is_active == True,
            DictionaryEntry.code_type == '4-digit'
        ).count()
        
        return {
            'total_entries': total_entries,
            'numeric_codes': numeric_count,
            'alphanumeric_codes': alphanumeric_count,
            'four_digit_codes': four_digit_count
        }
    
    def get_usage_stats(self, days=30):
        """Get usage statistics for the last N days"""
        session = self.get_session()
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        
        total_operations = session.query(EncodingHistory).filter(
            EncodingHistory.created_at >= cutoff_date
        ).count()
        
        encoding_operations = session.query(EncodingHistory).filter(
            EncodingHistory.created_at >= cutoff_date,
            EncodingHistory.operation_type == 'encode'
        ).count()
        
        decoding_operations = session.query(EncodingHistory).filter(
            EncodingHistory.created_at >= cutoff_date,
            EncodingHistory.operation_type == 'decode'
        ).count()
        
        # Most frequently used codes
        popular_codes = session.query(
            DictionaryEntry.code,
            DictionaryEntry.text,
            DictionaryEntry.frequency
        ).filter(
            DictionaryEntry.is_active == True,
            DictionaryEntry.frequency > 0
        ).order_by(desc(DictionaryEntry.frequency)).limit(10).all()
        
        return {
            'total_operations': total_operations,
            'encoding_operations': encoding_operations,
            'decoding_operations': decoding_operations,
            'popular_codes': [(code, text, freq) for code, text, freq in popular_codes],
            'days': days
        }
    
    def get_system_health(self):
        """Get system health information"""
        session = self.get_session()
        
        # Recent operations (last hour)
        recent_cutoff = datetime.utcnow() - timedelta(hours=1)
        recent_operations = session.query(EncodingHistory).filter(
            EncodingHistory.created_at >= recent_cutoff
        ).count()
        
        # Database size info
        total_entries = session.query(DictionaryEntry).count()
        active_entries = session.query(DictionaryEntry).filter(DictionaryEntry.is_active == True).count()
        total_operations = session.query(EncodingHistory).count()
        
        return {
            'recent_operations_1h': recent_operations,
            'total_dictionary_entries': total_entries,
            'active_dictionary_entries': active_entries,
            'total_operations_logged': total_operations,
            'database_connection': True  # If we got this far, connection is working
        }

# Global database manager instance
db_manager = DatabaseManager()

def get_db_manager():
    """Get the global database manager instance"""
    return db_manager