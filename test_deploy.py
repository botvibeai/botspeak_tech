#!/usr/bin/env python3
import subprocess
import sys
import os

print("Testing deployment readiness...")

# Test 1: Import check
try:
    from web_interface import app
    print("✓ Flask app imports successfully")
except Exception as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

# Test 2: Gunicorn config check
try:
    result = subprocess.run(['gunicorn', '--check-config', 'web_interface:app'], 
                          capture_output=True, text=True, timeout=10)
    if result.returncode == 0:
        print("✓ Gunicorn config is valid")
    else:
        print(f"✗ Gunicorn config error: {result.stderr}")
except Exception as e:
    print(f"✗ Gunicorn test failed: {e}")

# Test 3: Basic Flask response
try:
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("✓ Root endpoint returns 200")
        else:
            print(f"✗ Root endpoint failed: {response.status_code}")
            
        health_response = client.get('/health')
        if health_response.status_code == 200:
            print("✓ Health endpoint returns 200")
        else:
            print(f"✗ Health endpoint failed: {health_response.status_code}")
except Exception as e:
    print(f"✗ Flask test failed: {e}")

print("Deployment test complete.")