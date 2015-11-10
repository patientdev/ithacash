vcl 4.0;

backend default {
    .host = "127.0.0.1";
    .port = "8000";
}

sub vcl_recv {
    if ( !req.url ~ "^/accounts/" &&
        !req.url ~ "^/page-creator(.*)") {
      unset req.http.Cookie;
    }
}
