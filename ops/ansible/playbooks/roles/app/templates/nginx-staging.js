server {
       listen 80;
       server_name localhost;

       location / {
               proxy_pass   http://localhost:8000; # Apache
               proxy_set_header Host       $host;
       }
}

