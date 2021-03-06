<?php 

$head = <<<'CSS'
<style>

	header {
		position: relative;
	}

	#content {
		padding-top: 0;
	}

	#nav-menu { display: none; }

	#head {
		background-image: url(/img/hex-pattern.png);
		background-size: cover;
		height: 200px;
	}

	h2 {
		color: white;
		margin: 60px 0;
	}

	#sign-up-path {
		text-align: center;
		border-bottom: 2px solid rgb(88, 122, 70);
		height: 65px;
		padding: 20px 0 20px 0;
		margin-bottom: 60px;
	}

	.sign-up-step {
		width: 25%;
		float: left;
		position: relative;
		top: 5px;
	}

	.step-heading {
		color: rgb(88, 122, 70);
		font-size: 1em;
		margin: 0;
	}

	.circle {
		background-color: rgb(88, 122, 70);
		border-radius: 50%;
		width: 40px; height: 40px;
		text-align: center;
		color: white;
		font-size: 1.2em;
		line-height: 40px;
		display: inline-block;
	}

	.sign-up-step.selected {
		top: 0;
	}

	.sign-up-step.selected .step-heading {
		font-size: 1.2em;
	}

	.sign-up-step.selected .circle {
		width: 50px; height: 50px;
		font-size: 1.6em;
		line-height: 50px;
	}

	#forms {
		width: 200%;
		white-space: nowrap;
		overflow: hidden;
	}

	form {
		background-color: rgb(119, 173, 89);
		padding: 20px 0;
		text-align: center;
		transition: all 1s ease;
		width: 50%;
		right: 0;
		position: relative;
		float: left;
	}

	form p {
		margin: 20px auto;
	}

	form p:last-of-type {
		margin-top: 40px;
	}

	input, input:focus {
		text-align: center;
		background-color: white;
		border-radius: 8px;
		padding: 10px 15px;
		border: none;
		width: 20em;
		font-size: 1.1em;
		outline: none;
	}

	::-webkit-input-placeholder {
	   color: black;
	}

	:-moz-placeholder { /* Firefox 18- */
	   color: black;  
	}

	::-moz-placeholder {  /* Firefox 19+ */
	   color: black;  
	}

	:-ms-input-placeholder {  
	   color: black;  
	}

	.asterisk {
		color: white;
		font-size: 1.8em;
		margin-left: 10px;
	}

	button {
		background-color: white;
		padding: 5px 40px;
		border: none;
		color: black;
		border-radius: 8px;
		font-size: 1.6em;
	}

	.slide {
		right: 50%;
	}
</style>
CSS;

include $_SERVER["DOCUMENT_ROOT"] . "/includes/header.php"; ?>

<div id="content">

<div id="head"></div>

<div id="sign-up-path" class="clear">
	<div id="sign-up-1" class="selected sign-up-step">
		<div class="step-heading">Your Login</div>
		<div class="circle"><span>1</span></div>
	</div>
	<div id="sign-up-2" class="sign-up-step">
		<div class="step-heading">Your Info</div>
		<div class="circle">2</div>
	</div>
	<div id="sign-up-3" class="sign-up-step">
		<div class="step-heading">Your Billing</div>
		<div class="circle">3</div>
	</div>
	<div id="sign-up-4" class="sign-up-step">
		<div class="step-heading">Review</div>
		<div class="circle">4</div>
	</div>
</div>

<div id="forms">
	<form id="create-login">
		<h2>Create Your Login</h2>

		<p><input type="text" name="username" placeholder="Username"><sup class="asterisk">*</sup></p>
		<p><input type="email" name="email" placeholder="Email"><sup class="asterisk">*</sup></p>
		<p><input type="email" name="email-confirm" placeholder="Confirm Email"><sup class="asterisk">*</sup></p>
		<p><input type="password" name="password" placeholder="Password"><sup class="asterisk">*</sup></p>
		<p><input type="password" name="password" placeholder="Confirm Password"><sup class="asterisk">*</sup></p>
		<p><button>Next</button></p>
	</form>

	<form id="create-info">
		<h2>Your Information</h2>

		<p><input type="text" name="username" placeholder="Username"><sup class="asterisk">*</sup></p>
		<p><input type="email" name="email" placeholder="Email"><sup class="asterisk">*</sup></p>
		<p><input type="email" name="email-confirm" placeholder="Confirm Email"><sup class="asterisk">*</sup></p>
		<p><input type="password" name="password" placeholder="Password"><sup class="asterisk">*</sup></p>
		<p><input type="password" name="password" placeholder="Confirm Password"><sup class="asterisk">*</sup></p>
		<p><button>Next</button></p>
	</form>
</div>

</div>

<?php 

$foot = <<<'JAVASCRIPT'

<script>
	$('form').submit(function( event ) {
		event.preventDefault();

		$('form').addClass('slide');
	})
</script>

JAVASCRIPT;


include $_SERVER["DOCUMENT_ROOT"] . "/includes/footer.php"; ?>