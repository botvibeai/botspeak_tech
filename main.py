#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for BotSpeak Flask Application
Deployment-ready configuration for Replit
"""

from web_interface import app
import os
import logging

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == '__main__':
    # Use environment PORT or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    print(f"🚀 Starting BotSpeak deployment server on port {port}")
    print("📊 Health check endpoint: /health")
    print("🏠 Main application: /")
    
    # Run the Flask app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        threaded=True
    )