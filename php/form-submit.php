<?php

if ( isset($_POST) ) {
	$which = $_POST["which"];

	$to = "shane@shanecav.net";
	$email = $_POST["email"]
	$name = $_POST["name"];
	$from = $_POST["name"] . " <" . $email . ">";
	$subject = "";

	$body = "<!doctype html><html><head><title>$subject</title></head><body><table>"
	for ( $_POST as $key => $value ) {
			$body .= "<tr><td style=\"text-align: right\"><strong>$key:</strong></td><td>$value</td></tr>"
	}
	$body .="</table></body></html>"

	$body 

	switch($which)

	case "email":
		$subject = "Ithacash email sign-up";
		break;

	case "message":
		$subject = "Ithacash message";
		break;

	case "apply":
		$subject = "Ithacash Application";
		break;

	$header = "From: $from\r\n"; 
	$header.= "MIME-Version: 1.0\r\n"; 
	$header.= "Content-Type: text/html; charset=utf-8\r\n"; 
	$header.= "X-Priority: 1\r\n";

	if ( !mail($to, $subject, $message, $header) ) { echo "fail"; }
	else { echo "Received!"; }
}

?>