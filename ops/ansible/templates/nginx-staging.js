server {
       listen 6001;
       server_name localhost;


       ssl on;
       ssl_certificate /ithacash/ssl/ithacash-bundle.crt;
       ssl_certificate_key /ithacash/ssl/ithacash.key;

       ssl_session_timeout 5m;

       ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_session_cache shared:SSL:10m;
add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
ssl_session_tickets off; # Requires nginx >= 1.5.9
ssl_stapling on; # Requires nginx >= 1.3.7
ssl_stapling_verify on; # Requires nginx => 1.3.7

       location / {
               proxy_pass   http://localhost:1337; # Apache
               proxy_set_header Host       $host;
       }
}

