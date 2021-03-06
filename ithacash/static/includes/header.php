<!DOCTYPE html>
<html lang="en" class="clear">
	<head>
		<meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
		
		<title>ithacash &mdash; Money Made for Main St.</title>

		<link href='//fonts.googleapis.com/css?family=Maven+Pro:500,400,700' rel='stylesheet' type='text/css'>
		<link href='//fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>

		<link rel="stylesheet" href="/css/ithacash.css">
		<link rel="stylesheet" href="/js/slick/slick.css">
		<link rel="stylesheet" href="/css/mobile.css" media="only screen and (max-device-width:800px)"/>

		<link rel="icon" type="image/x-icon" href="/img/IthaCash_icon_2color.png">

		{% block head %}
		{% endblock %}

	</head>
	<body class="clear">
	
	<div id="container" class="clear">
		<header>
			<h1><a href="/"><img src="/img/ithacash_logo_rgb_325x124.png" alt="ithacash"></a></h1>

			<ul id="nav-menu">
				<li><a href="/#how-it-works">How It Works</a></li>
				<li><a href="/#how-to-get-started">Get Started</a></li>
				<li><a href="/#the-circuit">The Circuit</a></li>
				<li><a href="/#core-services">Core Services</a></li>
				<li><a href="/#accounts">Accounts</a></li>
				<li><a href="/#contact">Contact</a></li>
				<li id="buy-i-dollars"><a href="/apply/" class="green-button">Sign Up</a></li>
				<li id="sign-up"><a href="https://squareup.com/market/ithacash/ithaca-dollars" target="_blank" class="green-button dark-green-button">Buy i$</a></li>
			</ul>
		</header>

		{% block content %}
		{% endblock %}

	</div>

	<footer>

	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	<script>if (!window.jQuery) { document.write('<script src="/js/jquery-1.11.3.min.js"><\/script>'); }</script>
	
	<script src="/js/ithacash.js"></script>
	<script src="/js/slick/slick.min.js"></script>

	{% block foot %}
	{% endblock %}
	
	</footer>

	</body>
</html>