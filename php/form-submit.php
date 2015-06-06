<?php

if ( isset($_POST["message"]) ) {
	$email = $_POST["email"];
	$message = $_POST["message"];

	$to = "support@ithacash.com";
	$from = $email;
	$subject = "Ithacash.com Message";

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

	$to = "support@ithacash.com";
	$from = $name . " <" . $email . ">";
	$subject = "Ithacash.com email sign-up";

	$header = "From: $from\r\n"; 
	$header.= "MIME-Version: 1.0\r\n"; 
	$header.= "Content-Type: text/plain; charset=utf-8\r\n"; 
	$header.= "X-Priority: 1\r\n";

	if ( !mail($to, $subject, $message, $header) ) { echo "fail"; }
	else { echo "Sign-up sent"; }
}

?>