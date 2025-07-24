# BotSpeak Deployment Configuration

## Health Check Endpoints

The following health check endpoints are available for deployment systems:

### Primary Health Checks
- `GET /` - Returns 200 with full HTML page (main application)
- `GET /health` - Detailed health status with database connectivity
- `GET /readiness` - Simple readiness check ({"ready": true})

### Alternative Health Checks
- `GET /ping` - Simple text response "OK"
- `GET /_health` - Alternative health endpoint ({"status": "ok"})

## Deployment Configuration

### replit.toml
```toml
[deployment]
run = "python main.py"
```

### Entry Point
- **File**: `main.py`
- **Flask App**: `web_interface:app`
- **Port**: 5000 (configurable via PORT environment variable)

## Deployment Verification

All endpoints tested and working:
- ✅ Root endpoint (/) returns 200
- ✅ Health endpoint (/health) returns detailed status
- ✅ Readiness endpoint (/readiness) returns simple ready status
- ✅ Ping endpoint (/ping) returns "OK"
- ✅ Alternative health endpoint (/_health) returns status

## Production Readiness

- Flask application imports successfully
- Gunicorn configuration is valid
- All health check endpoints respond correctly
- Database connectivity tested
- Static files served properly
- Error handling implemented