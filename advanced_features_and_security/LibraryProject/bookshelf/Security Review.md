# HTTPS and Security Configuration

## Django Settings
- SECURE_SSL_REDIRECT=True → redirects all HTTP requests to HTTPS
- SECURE_HSTS_SECONDS=31536000 → enforces HTTPS for 1 year in browsers
- SECURE_HSTS_INCLUDE_SUBDOMAINS=True → applies HSTS to all subdomains
- SECURE_HSTS_PRELOAD=True → allows HSTS preloading
- SESSION_COOKIE_SECURE=True → cookies sent only over HTTPS
- CSRF_COOKIE_SECURE=True → CSRF cookies sent only over HTTPS
- X_FRAME_OPTIONS='DENY' → prevents clickjacking
- SECURE_CONTENT_TYPE_NOSNIFF=True → prevents MIME type sniffing
- SECURE_BROWSER_XSS_FILTER=True → enables browser XSS filter

## Deployment
- Nginx configured to redirect HTTP to HTTPS
- SSL certificates installed via Let's Encrypt
- SECURE_PROXY_SSL_HEADER set to handle HTTPS behind a proxy

## Testing
- Verified HTTP → HTTPS redirects
- Confirmed secure cookies in browser dev tools
- Checked security headers using browser developer tools
