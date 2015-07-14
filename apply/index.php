<?php 

$head = <<<'CSS'
<style>

	#content { text-align: center; }

	h2 {
		margin-top: 20px;
		margin-bottom: 20px;
	}

	h3 {
		margin: 20px 0;
	}

	#apply {
		display: inline-block;
		text-align: left;
	}

	#apply label {
		width: 200px;
		float: left;
		text-align: right;
		margin-right: 10px;
		margin-top: 10px;
		padding: 5px;
		vertical-align: middle;
	}

	#apply input, #apply span, #apply textarea, #apply select {
		margin-top: 10px; 
		width: 400px;
		display: inline-block;
		padding: 5px;
		line-height: 1em;
	}

	#apply select {
		padding: 0;
		margin-top: 15px;
		margin-bottom: 10px;
	}

	textarea {
		height: 10em;
	}

	#robotProof { 
		margin-top: 20px; 
		line-height: 1.2em;
		text-align: center;
	}

	#robotProof input {
		margin: 0;
		width: 8em;
		text-align: center;
	}

	form p:last-of-type {
		text-align: center;
		margin-top: 20px;
	}

	#status p {
		text-align: center;
		color: red;
		margin: 0;
	}

	#buy {
		width: 200px;
		margin: auto;
		display: none;
	}


</style>
CSS;

include_once $_SERVER["DOCUMENT_ROOT"] . "/includes/header.php"; ?>

<div id="content">

	<div id="buy">
		<p>Thank you for submitting an application! We&rsquo;ll be in touch with you shortly to gather remaining information and welcome you to the Circuit.</p>

		<p>In the meantime, why not go ahead and preload your account by purchasing some i$.</p>

		<p><a href="https://squareup.com/market/ithacash/ithaca-dollars" target="_blank" class="green-button">Buy i$</a></p>
	</div>

	<form id="apply" method="POST" action="" novalidate>
		<h2>Apply</h2>
		<input type="hidden" name="which" value="apply">
		<label for="type">Account Type: </label>
		<select name="type" required>
			<option value="">Who are you?</option>
			<option value="Individual">Individual</option>
			<option value="Freelancer">Freelancer</option>
			<option value="Business">Business</option>
			<option value="Nonprofit">Nonprofit</option></select><br>
		<label for="name">Company Name: </label><input type="text" placeholder="Company Name" name="name" required><br>
		<label for="contact">Contact Person: </label><input type="text" placeholder="Contact Person" name="contact" required><br>
		<label for="login">Login Name: </label><input type="text" placeholder="Login name" name="login" required><br>
		<label for="password">Password: </label><input type="password" placeholder="Password" name="password" required><br>
		<label for="confirm-password">Confirm Password: </label><input type="password" placeholder="Confirm Password" name="confirm-password" required><br>
		<label for="email">Email: </label><input type="email" placeholder="Email address" name="email" required><br>
		<label for="mobile">Mobile Phone: </label><input type="tel" placeholder="Mobile Phone" name="mobile"><br>
		<label for="landline">Landline Phone: </label><input type="tel" placeholder="Landline Phone" name="landline"><br>
		<label for="address1">Address 1: </label><input type="text" placeholder="Address 1" name="address1"><br>
		<label for="address2">Address 2: </label><input type="text" placeholder="Address 2" name="address2"><br>
		<label for="city">City: </label><input type="text" placeholder="City" name="city" value="Ithaca" required><br>
		<label for="State">State: </label><input type="text" placeholder="State" name="state" value="NY" required><br>
		<label for="zip">Zip Code: </label><input type="text" placeholder="Zip Code" name="zip" value="14850" required><br>
		<label for="ssn">EIN/SSN: </label> <span>Required for tax purposes. We will contact you to welcome you and collect this information securely before opening your account.</span><br>
		<label for="website">Website: </label><input type="text" placeholder="Website" name="website"><br>
		<label for="referer">Referrer: </label><input type="text" placeholder="Who can we thank for sending you our way?" name="referrer"><br>
		<label for="about">About: </label><textarea placeholder="Tell us about you or your business" name="about"></textarea>

		<div id="robotProof">
			<p>Please prove that you aren&rsquo;t a bot:</p>
		</div>

		<div id="status"></div>

		<p><button type="submit" class="green-button">Apply</button></p>
	</form>

</div>

<?php 

$foot = <<<'JAVASCRIPT'


<script>
	$(function() {

		nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'];
		num1 = Math.floor(Math.random() * 10);
		num2 = Math.floor(Math.random() * 10);
		answer = num1 + num2;

		$('#robotProof').append('<p>What is ' + nums[num1] + ' plus ' + nums[num2] + '? <br><input type="text" placeholder="e.g., 1 or one" required></p>');
	});
</script>

JAVASCRIPT;

include_once $_SERVER["DOCUMENT_ROOT"] . "/includes/footer.php"; ?>