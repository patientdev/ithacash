<?php

if ( isset($_POST) ) {
	$which = $_POST["which"];

	$to = "shane@shanecav.net";
	$email = $_POST["email"];
	$name = $_POST["name"];
	$from = $_POST["name"] . " <" . $email . ">";
	$subject = "";

	$body = "<!doctype html><html><head><title>$subject</title></head><body><table>";
	foreach ( $_POST as $key => $value ) {
		if ( $key != "which" ) {		
			$body .= "<tr><td style=\"text-align: right\"><strong>". ucwords($key) . ":</strong></td><td>$value</td></tr>";
		}
	}
	$body .="</table></body></html>";

	switch($which) {

		case "email":
			$subject = "Ithacash email sign-up";
			break;

		case "message":
			$subject = "Ithacash message";
			break;

		case "apply":
			$subject = "Ithacash Application";
			break;
	}

	$header = "From: $from\r\n"; 
	$header.= "MIME-Version: 1.0\r\n"; 
	$header.= "Content-Type: text/html; charset=utf-8\r\n"; 
	$header.= "X-Priority: 1\r\n";

	if ( !mail($to, $subject, $body, $header) ) { echo "fail"; }
	else { echo "Received!"; }
}

?>