<?php

if ( isset($_POST["message"]) ) {
	$email = $_POST["email"];
	$message = $_POST["message"];

	$to = "shane@shanecav.net";
	$from = $email;
	$subject = "Message";

	$header = "From: $from\r\n"; 
	$header.= "MIME-Version: 1.0\r\n"; 
	$header.= "Content-Type: text/plain; charset=utf-8\r\n"; 
	$header.= "X-Priority: 1\r\n";

	if ( !mail($to, $subject, $message, $header) ) { echo "fail"; }
	else { echo "Message sent"; }
}

else if ( isset($_POST["name"]) ) {

	$email = $_POST["email"];
	$name = $_POST["name"];
	$message = "$name\n$email";

	$to = "shane@shanecav.net";
	$from = $name . " <" . $email . ">";
	$subject = "Email sign-up";

	$header = "From: $from\r\n"; 
	$header.= "MIME-Version: 1.0\r\n"; 
	$header.= "Content-Type: text/plain; charset=utf-8\r\n"; 
	$header.= "X-Priority: 1\r\n";

	if ( !mail($to, $subject, $message, $header) ) { echo "fail"; }
	else { echo "Sign-up sent"; }
}

?>