vcl 4.0;

backend default {
    .host = "127.0.0.1";
    .port = "8000";
}

sub vcl_recv {
    if ( !( req.url ~ "^/accounts/") ) {
      unset req.http.Cookie;
    }

    if ( !req.url ~ "^/" ||
        !req.url ~ "^/accounts(.*)" ) {
      return (pass);
    }
}
