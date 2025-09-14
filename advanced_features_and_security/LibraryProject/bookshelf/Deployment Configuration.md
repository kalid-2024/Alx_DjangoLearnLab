1. Obtain SSL/TLS Certificates

    Use Let's Encrypt (free) or purchase a certificate.

2. Nginx Example (replace example.com and paths with your own):

    server {
        listen 80;
        server_name example.com www.example.com;
        return 301 https://$host$request_uri;  # Redirect HTTP → HTTPS
    }

    server {
        listen 443 ssl;
        server_name example.com www.example.com;

        ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }


<!-- Make sure Django knows it’s behind a proxy by adding in settings.py: -->
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')