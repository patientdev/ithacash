server {
       listen 80;
       server_name localhost;

       location / {
               proxy_pass   http://localhost:8000; # Apache
               proxy_set_header Host       $host;
       }
}

server {
       listen 443;
       server_name localhost;


       ssl on;
       ssl_certificate /etc/letsencrypt/live/staging.ithacash.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/staging.ithacash.com/privkey.pem;

       ssl_session_timeout 5m;

       ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_session_cache shared:SSL:10m;
add_header Strict-Transport-Security "max-age=63072000; preload";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
ssl_session_tickets off; # Requires nginx >= 1.5.9
ssl_stapling on; # Requires nginx >= 1.3.7
ssl_stapling_verify on; # Requires nginx => 1.3.7

    location / {
           proxy_pass   http://localhost:6081; # Varnish
           proxy_set_header Host       $host;
    }

    location /login {
           return       301 https://communities.cyclos.org/Ithacash/#login;
    }

    location /directory {
           return       301 https://communities.cyclos.org/Ithacash/#users.users.search;
    }

    location /buy {
           return       301 https://squareup.com/market/ithacash/ithaca-dollars;
    }

    location /shop {
           return       301 https://squareup.com/market/ithacash;
    }

    location /apply {
           return       301 https://staging.ithacash.com/accounts/signup/;
    }

    location /media {
        alias /ithacash/production/pages/media/;
    }

    location /static {
        alias /ithacash/production/ithacash_dev/static/;
    }
}
