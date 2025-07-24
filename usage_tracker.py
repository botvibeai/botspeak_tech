"""
BotSpeak Usage Tracker
Tracks daily free usage without requiring login
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path

class UsageTracker:
    def __init__(self, data_dir="data"):
        """Initialize usage tracker"""
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.usage_file = self.data_dir / "monthly_usage.json"
        self.free_monthly_limit = 100
    
    def get_client_id(self, request):
        """Generate a unique client identifier based on IP"""
        # Get client IP address
        if request.headers.get('X-Forwarded-For'):
            ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
        else:
            ip = request.remote_addr or 'unknown'
        
        # Create a simple hash for privacy (not cryptographically secure)
        import hashlib
        client_id = hashlib.md5(ip.encode()).hexdigest()[:16]
        return client_id
    
    def get_current_month(self):
        """Get current month string in UTC"""
        return datetime.utcnow().strftime('%Y-%m')
    
    def load_usage_data(self):
        """Load usage data from file"""
        if not self.usage_file.exists():
            return {}
        
        try:
            with open(self.usage_file, 'r') as f:
                data = json.load(f)
            
            # Clean old data (older than 7 days)
            current_date = datetime.utcnow()
            cutoff_date = current_date - timedelta(days=7)
            
            cleaned_data = {}
            for date_str, date_data in data.items():
                try:
                    data_date = datetime.strptime(date_str, '%Y-%m-%d')
                    if data_date >= cutoff_date:
                        cleaned_data[date_str] = date_data
                except ValueError:
                    continue
            
            return cleaned_data
        except (json.JSONDecodeError, IOError):
            return {}
    
    def save_usage_data(self, data):
        """Save usage data to file"""
        try:
            with open(self.usage_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError:
            pass  # Fail silently if can't write
    
    def get_monthly_usage(self, request):
        """Get current monthly usage for client"""
        client_id = self.get_client_id(request)
        current_month = self.get_current_month()
        
        usage_data = self.load_usage_data()
        
        if current_month not in usage_data:
            usage_data[current_month] = {}
        
        return usage_data[current_month].get(client_id, 0)
    
    def increment_usage(self, request, count=1):
        """Increment usage count for client"""
        client_id = self.get_client_id(request)
        current_month = self.get_current_month()
        
        usage_data = self.load_usage_data()
        
        if current_month not in usage_data:
            usage_data[current_month] = {}
        
        current_usage = usage_data[current_month].get(client_id, 0)
        usage_data[current_month][client_id] = current_usage + count
        
        self.save_usage_data(usage_data)
        return usage_data[current_month][client_id]
    
    def check_rate_limit(self, request):
        """Check if client has exceeded monthly limit"""
        current_usage = self.get_monthly_usage(request)
        
        return {
            'allowed': current_usage < self.free_monthly_limit,
            'current_usage': current_usage,
            'monthly_limit': self.free_monthly_limit,
            'remaining': max(0, self.free_monthly_limit - current_usage)
        }
    
    def get_usage_info(self, request):
        """Get usage information for display"""
        rate_limit_info = self.check_rate_limit(request)
        
        return {
            'is_free_user': True,
            'monthly_usage': rate_limit_info['current_usage'],
            'monthly_limit': rate_limit_info['monthly_limit'],
            'remaining_this_month': rate_limit_info['remaining'],
            'can_encode': rate_limit_info['allowed']
        }

# Global usage tracker instance
usage_tracker = UsageTracker()

def get_usage_tracker():
    """Get the global usage tracker instance"""
    return usage_tracker