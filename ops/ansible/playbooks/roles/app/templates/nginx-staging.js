server {
       listen 80;
       server_name localhost;

       location / {
               proxy_pass   http://localhost:1337; # Apache
               proxy_set_header Host       $host;
       }
}

