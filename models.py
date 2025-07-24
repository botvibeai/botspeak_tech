"""
BotSpeak Database Models
SQLAlchemy models for storing dictionary entries and user interactions
"""

from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class DictionaryEntry(Base):
    """Model for storing BotSpeak dictionary entries"""
    __tablename__ = 'dictionary_entries'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True, nullable=False, index=True)
    text = Column(Text, nullable=False, index=True)
    code_type = Column(String(20), nullable=False)  # 'numeric', 'alphanumeric', '4-digit'
    word_count = Column(Integer, default=1)  # Number of words in the text
    frequency = Column(Integer, default=0)  # Usage frequency
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

class EncodingHistory(Base):
    """Model for storing encoding/decoding operations"""
    __tablename__ = 'encoding_history'
    
    id = Column(Integer, primary_key=True)
    operation_type = Column(String(10), nullable=False)  # 'encode' or 'decode'
    input_text = Column(Text, nullable=False)
    output_text = Column(Text, nullable=False)
    compression_ratio = Column(String(10))  # Only for encoding operations
    recognition_rate = Column(String(10))   # Only for decoding operations
    processing_time = Column(String(20))    # Time taken in milliseconds
    ip_address = Column(String(45))
    user_agent = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class SystemStats(Base):
    """Model for storing system statistics"""
    __tablename__ = 'system_stats'
    
    id = Column(Integer, primary_key=True)
    stat_name = Column(String(50), unique=True, nullable=False)
    stat_value = Column(String(100), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Database connection and session management
def get_database_engine():
    """Create database engine with optimized settings"""
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set")
    
    # Add connection pooling and optimization parameters
    # Handle SSL connection issues for deployment
    connect_args = {}
    if database_url.startswith('postgres'):
        connect_args = {
            "sslmode": "prefer",
            "connect_timeout": 30,
            "application_name": "botspeak_web"
        }
    
    return create_engine(
        database_url, 
        echo=False,
        pool_size=3,
        max_overflow=5,
        pool_pre_ping=True,
        pool_recycle=1800,  # Recycle connections every 30 minutes
        pool_timeout=30,
        connect_args=connect_args
    )

def get_database_session():
    """Get database session"""
    engine = get_database_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def init_database():
    """Initialize database tables"""
    engine = get_database_engine()
    Base.metadata.create_all(engine)
    print("Database tables created successfully")

def populate_dictionary_from_static():
    """Populate database from static dictionary"""
    from botspeak_dict import botspeak_dict
    
    session = get_database_session()
    
    try:
        # Check if dictionary is already populated
        existing_count = session.query(DictionaryEntry).count()
        if existing_count > 0:
            print(f"Dictionary already populated with {existing_count} entries")
            return existing_count
        
        # Populate from static dictionary
        entries = []
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
            
            entry = DictionaryEntry(
                code=code,
                text=text,
                code_type=code_type,
                word_count=len(text.split()),
                frequency=0
            )
            entries.append(entry)
        
        # Batch insert
        session.add_all(entries)
        session.commit()
        
        print(f"Successfully populated database with {len(entries)} dictionary entries")
        return len(entries)
        
    except Exception as e:
        session.rollback()
        print(f"Error populating dictionary: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    # Initialize database and populate dictionary
    print("Initializing BotSpeak database...")
    init_database()
    populate_dictionary_from_static()
    print("Database setup complete!")