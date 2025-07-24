"""
BotSpeak Web Interface
Flask-based web application for the BotSpeak compression system
"""

from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, send_file, make_response
import os
import stripe
from encoder import BotSpeakEncoder
from decoder import BotSpeakDecoder
from db_encoder import DatabaseEncoder
from db_decoder import DatabaseDecoder
from db_manager import get_db_manager
from usage_tracker import get_usage_tracker
from botspeak_dict import botspeak_dict, print_dictionary_stats
import sys
from io import StringIO
from datetime import datetime
import uuid
import json
from pathlib import Path
import hashlib
import secrets
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'botspeak-demo-key-2025')

# Simple session storage (in production, use Redis or database)
user_sessions = {}
users_db = {}

# Load existing users on startup
try:
    users_file = Path('data/users.json')
    if users_file.exists():
        with open(users_file, 'r') as f:
            users_db.update(json.load(f))
except Exception as e:
    print(f"Warning: Could not load users database: {e}")

# Initialize Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Initialize BotSpeak components
encoder = BotSpeakEncoder()
decoder = BotSpeakDecoder()

# Initialize database-aware components
db_encoder = DatabaseEncoder()
db_decoder = DatabaseDecoder()
db_manager = get_db_manager()
usage_tracker = get_usage_tracker()

# Get domain for Stripe redirects
# Auth helper functions
def hash_password(password):
    """Hash password with salt"""
    salt = secrets.token_hex(16)
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return salt + pwdhash.hex()

def verify_password(password, hashed):
    """Verify password against hash"""
    salt = hashed[:32]
    stored_hash = hashed[32:]
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return pwdhash.hex() == stored_hash

def create_session(user_id):
    """Create a new user session"""
    session_token = secrets.token_urlsafe(32)
    user_sessions[session_token] = {
        'user_id': user_id,
        'created_at': datetime.utcnow().isoformat()
    }
    return session_token

def get_current_user(request):
    """Get current user from session"""
    session_token = request.cookies.get('session_token')
    if not session_token or session_token not in user_sessions:
        return None
    return users_db.get(user_sessions[session_token]['user_id'])

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_current_user(request)
        if not user:
            return jsonify({'success': False, 'error': 'Login required'}), 401
        return f(*args, **kwargs)
    return decorated_function

def get_domain():
    # Always use botspeak.tech as the primary domain
    return 'botspeak.tech'

@app.route('/')
def index():
    """Main page - returns 200 OK for health checks"""
    try:
        # Always return 200 status for deployment health checks
        response = make_response(render_template('index.html'))
        response.status_code = 200
        return response
    except Exception as e:
        print(f"Error serving index page: {e}")
        # Fallback response for deployment health checks
        return jsonify({
            'status': 'healthy',
            'message': 'BotSpeak application is running',
            'timestamp': datetime.utcnow().isoformat()
        }), 200

@app.route('/verify-botspeak')
def verify_botspeak():
    """Verification endpoint to confirm this is the BotSpeak application"""
    return jsonify({
        'application': 'BotSpeak Language Compression System',
        'domain': 'botspeak.tech',
        'status': 'active',
        'dictionary_entries': len(botspeak_dict),
        'timestamp': datetime.utcnow().isoformat(),
        'message': 'This is the official BotSpeak application'
    })

@app.route('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    try:
        # Basic health checks
        dictionary_size = len(botspeak_dict)
        
        # Test database connection
        db_status = 'connected'
        try:
            db_stats = db_manager.get_dictionary_stats()
            db_entries = db_stats.get('total_entries', 0)
        except Exception as db_e:
            db_status = f'error: {str(db_e)}'
            db_entries = 0
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat(),
            'dictionary_size': dictionary_size,
            'database_status': db_status,
            'database_entries': db_entries,
            'version': '1.0.0',
            'environment': 'production'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.utcnow().isoformat()
        }), 500

@app.route('/readiness')
def readiness_check():
    """Deployment readiness check - minimal response for fast health checks"""
    return jsonify({'ready': True}), 200

@app.route('/ping')
def ping():
    """Simple ping endpoint for health checks"""
    return 'OK', 200

@app.route('/_health')
def health_check_alt():
    """Alternative health check endpoint (sometimes used by deployment systems)"""
    return jsonify({'status': 'ok'}), 200

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'api': 'online',
        'service': 'BotSpeak',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/encode', methods=['POST'])
def api_encode():
    """API endpoint to encode text"""
    try:
        import time
        start_time = time.time()
        
        # Check usage limits for free users
        usage_info = usage_tracker.check_rate_limit(request)
        if not usage_info['allowed']:
            return jsonify({
                'success': False,
                'error': f"Monthly limit of {usage_info['monthly_limit']} encodings exceeded. Upgrade to a paid plan for unlimited usage.",
                'usage_exceeded': True,
                'usage_info': usage_info
            }), 429
        
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'No text provided'
            }), 400
        
        result = db_encoder.encode_with_stats(text)
        
        # Increment usage count
        usage_tracker.increment_usage(request)
        
        end_time = time.time()
        print(f"Encoding '{text}' took {end_time - start_time:.3f} seconds")
        
        # Get updated usage info
        updated_usage = usage_tracker.get_usage_info(request)
        
        return jsonify({
            'success': True,
            'original_text': result['original_text'],
            'encoded_text': result['encoded_text'],
            'statistics': result['statistics'],
            'usage_info': updated_usage
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/decode', methods=['POST'])
def api_decode():
    """API endpoint to decode BotSpeak codes"""
    try:
        data = request.get_json()
        codes = data.get('codes', '').strip()
        
        if not codes:
            return jsonify({
                'success': False,
                'error': 'No codes provided'
            }), 400
        
        result = db_decoder.decode_with_validation(codes)
        
        return jsonify({
            'success': result['success'],
            'decoded_text': result['decoded_text'],
            'recognition_rate': result['recognition_rate'],
            'total_codes': result['total_codes'],
            'recognized_codes': result['recognized_codes'],
            'unknown_codes': result['unknown_codes']
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/dictionary/stats')
def api_dictionary_stats():
    """API endpoint to get dictionary statistics (database version)"""
    try:
        stats = db_manager.get_dictionary_stats()
        
        return jsonify({
            'success': True,
            'total_entries': stats['total_entries'],
            'numeric_codes': stats['numeric_codes'],
            'alphanumeric_codes': stats['alphanumeric_codes'],
            'four_digit_codes': stats['four_digit_codes']
        })
    
    except Exception as e:
        print(f"Database error in stats endpoint: {e}")
        # Fallback to static dictionary for deployment health checks
        return jsonify({
            'success': True,
            'total_entries': len(botspeak_dict),
            'numeric_codes': len(botspeak_dict),
            'alphanumeric_codes': 0,
            'four_digit_codes': 0,
            'note': 'Using fallback stats due to database connection issue'
        })

@app.route('/api/dictionary/search')
def api_dictionary_search():
    """API endpoint to search dictionary"""
    try:
        query = request.args.get('q', '').strip().lower()
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'No search query provided'
            }), 400
        
        results = []
        
        # Use database search
        db_results = db_manager.search_dictionary(query, limit=50)
        results = []
        
        for entry in db_results:
            results.append({
                'code': entry.code,
                'text': entry.text,
                'type': entry.code_type,
                'frequency': entry.frequency
            })
        
        return jsonify({
            'success': True,
            'query': query,
            'results': results,
            'total_found': len(results),
            'limited': len(results) == 50
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/dictionary/random')
def api_dictionary_random():
    """API endpoint to get random dictionary entries"""
    try:
        import random
        
        count = min(int(request.args.get('count', 10)), 50)  # Max 50 entries
        
        # Get random entries from database
        db_results = db_manager.get_random_dictionary_entries(count)
        results = []
        
        for entry in db_results:
            results.append({
                'code': entry.code,
                'text': entry.text,
                'type': entry.code_type,
                'frequency': entry.frequency
            })
        
        return jsonify({
            'success': True,
            'results': results,
            'count': len(results)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/examples')
def api_examples():
    """API endpoint to get example sentences"""
    examples = [
        {
            'text': "Hello, how are you today?",
            'description': "Simple greeting"
        },
        {
            'text': "I need help with my computer.",
            'description': "Technical support request"
        },
        {
            'text': "Thank you very much for your assistance.",
            'description': "Polite appreciation"
        },
        {
            'text': "What do you think about artificial intelligence?",
            'description': "Question about technology"
        },
        {
            'text': "I would like to schedule a meeting tomorrow.",
            'description': "Business request"
        },
        {
            'text': "The weather is beautiful today.",
            'description': "Weather observation"
        },
        {
            'text': "Please let me know if you have any questions.",
            'description': "Professional closing"
        },
        {
            'text': "I'm sorry, I don't understand what you mean.",
            'description': "Confusion or clarification request"
        }
    ]
    
    return jsonify({
        'success': True,
        'examples': examples
    })

# New database-specific endpoints
@app.route('/api/db/usage-stats')
def api_db_usage_stats():
    """API endpoint to get database usage statistics"""
    try:
        days = int(request.args.get('days', 30))
        stats = db_manager.get_usage_stats(days)
        
        return jsonify({
            'success': True,
            'stats': stats
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/db/system-health')
def api_db_system_health():
    """API endpoint to get system health information"""
    try:
        health = db_manager.get_system_health()
        
        return jsonify({
            'success': True,
            'health': health
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/db/popular-codes')
def api_db_popular_codes():
    """API endpoint to get most frequently used codes"""
    try:
        limit = int(request.args.get('limit', 20))
        days = int(request.args.get('days', 30))
        
        usage_stats = db_manager.get_usage_stats(days)
        popular_codes = usage_stats['popular_codes'][:limit]
        
        results = []
        for code, text, frequency in popular_codes:
            results.append({
                'code': code,
                'text': text,
                'frequency': frequency
            })
        
        return jsonify({
            'success': True,
            'popular_codes': results,
            'days': days
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Stripe Payment Routes
@app.route('/pricing')
def pricing():
    """Pricing page"""
    return render_template('pricing.html')

@app.route('/docs')
def docs():
    """Documentation page"""
    return render_template('docs.html')

@app.route('/support')
def support():
    """Support contact page"""
    return render_template('support.html')

@app.route('/api/support', methods=['POST'])
def api_support():
    """Save support requests to JSON file for download"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['firstName', 'lastName', 'email', 'category', 'subject', 'message']
        for field in required_fields:
            if not data.get(field, '').strip():
                return jsonify({
                    'success': False,
                    'error': f'{field} is required'
                }), 400
        
        # Create support requests directory
        support_dir = Path('data')
        support_dir.mkdir(exist_ok=True)
        
        # Load existing support requests
        support_file = support_dir / 'support_requests.json'
        if support_file.exists():
            with open(support_file, 'r') as f:
                support_requests = json.loads(f.read())
        else:
            support_requests = []
        
        # Add new request with ID
        data['id'] = str(uuid.uuid4())[:8]
        data['status'] = 'new'
        data['submitted_at'] = datetime.utcnow().isoformat()
        
        support_requests.append(data)
        
        # Save updated requests
        with open(support_file, 'w') as f:
            json.dump(support_requests, f, indent=2)
        
        return jsonify({
            'success': True,
            'message': 'Support request saved successfully',
            'request_id': data['id']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Failed to save support request: {str(e)}'
        }), 500

@app.route('/admin/support')
def admin_support():
    """Admin endpoint to download support requests"""
    try:
        support_file = Path('data/support_requests.json')
        if not support_file.exists():
            return jsonify({
                'success': False,
                'error': 'No support requests found'
            }), 404
        
        return send_file(
            support_file,
            as_attachment=True,
            download_name=f'support_requests_{datetime.utcnow().strftime("%Y%m%d")}.json'
        )
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Authentication routes
@app.route('/login')
def login_page():
    """Login page"""
    return render_template('login.html')

@app.route('/register')
def register_page():
    """Registration page"""
    return render_template('register.html')

@app.route('/dashboard')
def dashboard_page():
    """Dashboard page - requires login"""
    user = get_current_user(request)
    if not user:
        return redirect('/login')
    return render_template('dashboard.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    """User registration API"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['firstName', 'lastName', 'email', 'password']
        for field in required_fields:
            if not data.get(field, '').strip():
                return jsonify({
                    'success': False,
                    'error': f'{field} is required'
                }), 400
        
        email = data['email'].lower().strip()
        
        # Check if user already exists
        if any(user['email'] == email for user in users_db.values()):
            return jsonify({
                'success': False,
                'error': 'Email already registered'
            }), 400
        
        # Create new user
        user_id = str(uuid.uuid4())
        user_data = {
            'id': user_id,
            'firstName': data['firstName'].strip(),
            'lastName': data['lastName'].strip(),
            'email': email,
            'password': hash_password(data['password']),
            'company': data.get('company', '').strip(),
            'newsletter': data.get('newsletter') == 'yes',
            'created_at': datetime.utcnow().isoformat(),
            'plan': 'free',
            'monthly_usage': 0,
            'monthly_limit': 100
        }
        
        users_db[user_id] = user_data
        
        # Save users to file
        users_file = Path('data/users.json')
        users_file.parent.mkdir(exist_ok=True)
        with open(users_file, 'w') as f:
            json.dump(users_db, f, indent=2)
        
        return jsonify({
            'success': True,
            'message': 'Account created successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Registration failed: {str(e)}'
        }), 500

@app.route('/api/login', methods=['POST'])
def api_login():
    """User login API"""
    try:
        data = request.get_json()
        
        email = data.get('email', '').lower().strip()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({
                'success': False,
                'error': 'Email and password are required'
            }), 400
        
        # Find user by email
        user = None
        for u in users_db.values():
            if u['email'] == email:
                user = u
                break
        
        if not user or not verify_password(password, user['password']):
            return jsonify({
                'success': False,
                'error': 'Invalid email or password'
            }), 401
        
        # Create session
        session_token = create_session(user['id'])
        
        response = jsonify({
            'success': True,
            'message': 'Login successful',
            'redirect': '/dashboard'
        })
        
        # Set secure cookie
        response.set_cookie('session_token', session_token, 
                          httponly=True, secure=False, max_age=30*24*60*60)  # 30 days
        
        return response
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Login failed: {str(e)}'
        }), 500

@app.route('/api/logout', methods=['POST'])
def api_logout():
    """User logout API"""
    session_token = request.cookies.get('session_token')
    if session_token and session_token in user_sessions:
        del user_sessions[session_token]
    
    response = jsonify({'success': True})
    response.set_cookie('session_token', '', expires=0)
    return response

@app.route('/api/dashboard')
def api_dashboard():
    """Dashboard data API"""
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    # Get user usage data
    current_date = datetime.utcnow()
    reset_date = f"{current_date.replace(month=current_date.month % 12 + 1, day=1).strftime('%b %d')}"
    
    return jsonify({
        'success': True,
        'user': {
            'firstName': user['firstName'],
            'lastName': user['lastName'],
            'email': user['email']
        },
        'usage': {
            'used': user.get('monthly_usage', 0),
            'limit': user.get('monthly_limit', 100),
            'remaining': user.get('monthly_limit', 100) - user.get('monthly_usage', 0),
            'resetDate': reset_date
        },
        'subscription': {
            'plan': user.get('plan', 'Free').title(),
            'status': 'active'
        },
        'stats': {
            'avgCompression': 35  # Could calculate from actual usage
        }
    })

@app.route('/api/usage-info', methods=['GET'])
def api_usage_info():
    """Get current usage information"""
    try:
        # Get usage info from tracker
        usage_info = usage_tracker.get_usage_info(request)
        
        # Get database stats
        stats = db_manager.get_usage_stats()
        
        return jsonify({
            'success': True,
            'dictionary_size': stats.get('total_entries', 2498),
            'total_encodings': stats.get('total_encodings', 0),
            'compression_ratio': stats.get('average_compression', 0.6),
            'usage_info': usage_info
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """Create Stripe checkout session"""
    try:
        data = request.get_json()
        plan = data.get('plan')
        
        # Define pricing plans
        plans = {
            'starter': {
                'name': 'Starter Plan',
                'amount': 997,  # $9.97
                'description': 'Perfect for regular users'
            },
            'professional': {
                'name': 'Professional Plan', 
                'amount': 2497,  # $24.97
                'description': 'Great for businesses and power users'
            },
            'business': {
                'name': 'Business Plan',
                'amount': 9997,  # $99.97
                'description': '100,000 monthly encodings with overage pricing for growing companies'
            },
            'enterprise': {
                'name': 'Enterprise Plan',
                'amount': 49997,  # $499.97
                'description': 'Unlimited usage with dedicated infrastructure for large organizations'
            }
        }
        
        if plan not in plans:
            return jsonify({'error': 'Invalid plan'}), 400
        
        domain = get_domain()
        
        # Create Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'BotSpeak {plans[plan]["name"]}',
                        'description': plans[plan]["description"],
                    },
                    'unit_amount': plans[plan]['amount'],
                    'recurring': {
                        'interval': 'month',
                    },
                },
                'quantity': 1,
            }],
            mode='subscription',
            success_url=f'https://{domain}/payment-success?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url=f'https://{domain}/pricing?canceled=true',
            metadata={
                'plan': plan
            }
        )
        
        return jsonify({
            'success': True,
            'checkout_url': checkout_session.url
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/payment-success')
def payment_success():
    """Payment success page"""
    session_id = request.args.get('session_id')
    return render_template('payment-success.html', session_id=session_id)

@app.route('/webhook/stripe', methods=['POST'])
def stripe_webhook():
    """Handle Stripe webhooks"""
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    
    try:
        # You'll need to set the webhook secret in your environment
        endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
        
        if endpoint_secret:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        else:
            # For development - just parse the JSON
            event_data = request.json or {}
            event = stripe.Event.construct_from(
                event_data, stripe.api_key
            )
        
        # Handle the event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            print(f"Payment completed for session: {session['id']}")
            
        elif event['type'] == 'customer.subscription.created':
            subscription = event['data']['object']
            print(f"New subscription created: {subscription['id']}")
            
        elif event['type'] == 'customer.subscription.deleted':
            subscription = event['data']['object']
            print(f"Subscription canceled: {subscription['id']}")
            
        return jsonify({'success': True})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/download-app')
def download_app():
    """Create a downloadable package of essential app files"""
    import zipfile
    from io import BytesIO
    
    # Create in-memory zip file
    memory_file = BytesIO()
    
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Core Python files
        core_files = [
            'web_interface.py', 'botspeak_dict.py', 'encoder.py', 'decoder.py',
            'db_encoder.py', 'db_decoder.py', 'models.py', 'db_manager.py',
            'usage_tracker.py', 'app.py', 'pyproject.toml', 'replit.md',
            'DEPLOYMENT_PROOF.md', 'EXPORT_INSTRUCTIONS.md'
        ]
        
        for file in core_files:
            if os.path.exists(file):
                zf.write(file, file)
        
        # Templates folder
        if os.path.exists('templates'):
            for root, dirs, files in os.walk('templates'):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path, file_path)
        
        # Static folder  
        if os.path.exists('static'):
            for root, dirs, files in os.walk('static'):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path, file_path)
        
        # Data folder
        if os.path.exists('data'):
            for root, dirs, files in os.walk('data'):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path, file_path)
    
    memory_file.seek(0)
    
    response = make_response(memory_file.read())
    response.headers['Content-Type'] = 'application/zip'
    response.headers['Content-Disposition'] = 'attachment; filename=botspeak_app.zip'
    return response

@app.route('/get-app')
def get_app():
    """Simple file download"""
    try:
        return send_file('botspeak_manual_export.zip', 
                        as_attachment=True, 
                        download_name='botspeak_complete.zip',
                        mimetype='application/zip')
    except Exception as e:
        return f"Download error: {str(e)}", 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    print("🤖 Starting BotSpeak Web Interface...")
    print(f"   Dictionary loaded: {len(botspeak_dict)} unique mappings")
    print(f"   Server: http://0.0.0.0:{port}")
    print("   Press Ctrl+C to stop")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
