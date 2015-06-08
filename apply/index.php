<?php 

$head = <<<'CSS'
<style>

	#content { text-align: center; }

	h2 {
		margin-top: 20px;
		margin-bottom: 20px;
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
	}

	#apply input, #apply span, #apply textarea {
		margin-top: 10px; 
		width: 300px;
		display: inline-block;
		padding: 5px;
		line-height: 1em;
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


</style>
CSS;

include_once $_SERVER["DOCUMENT_ROOT"] . "includes/header.php"; ?>

<div id="content">

	<h2>Apply</h2>

	<form id="apply" method="POST" action="" novalidate>
		<input type="hidden" name="which" value="apply">
		<label for="name">Name: </label><input type="text" placeholder="Name" name="name" required><br>
		<label for="login">Login Name: </label><input type="text" placeholder="Login name" name="login" required><br>
		<label for="password">Password: </label><input type="password" placeholder="Password" name="password" required><br>
		<label for="confirm-password">Confirm Password: </label><input type="password" placeholder="Confirm Password" name="confirm-password" required><br>
		<label for="email">Email: </label><input type="email" placeholder="Email address" name="email" required><br>
		<label for="mobile">Mobile Phone: </label><input type="tel" placeholder="Mobile Phone" name="mobile"><br>
		<label for="landline">Landline Phone: </label><input type="tel" placeholder="Landline Phone" name="landline"><br>
		<label for="address1">Address 1: </label><input type="text" placeholder="Address 1" name="address1"><br>
		<label for="address2">Address 2: </label><input type="text" placeholder="Address 2" name="address2"><br>
		<label for="city">City: </label><input type="text" placeholder="City" name="city" required><br>
		<label for="State">State: </label><input type="text" placeholder="State" name="state" required><br>
		<label for="zip">Zip Code: </label><input type="text" placeholder="Zip Code" name="zip" required><br>
		<label for="ssn">EIN/SSN: </label> <span>Please call us to securely provide this information over the phone</span><br>
		<label for="website">Website: </label><input type="text" placeholder="Website" name="website"><br>
		<label for="contact">Contact Person: </label><input type="text" placeholder="Contact Person" name="contact" required><br>
		<label for="referer">Referer: </label><input type="text" placeholder="Who referrred you to us?" name="referrer"><br>
		<label for="about">Address: </label><textarea placeholder="Tell us about you or your business" name="about"></textarea>

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

		$('#robotProof').append('<p>What is ' + nums[num1] + ' + ' + nums[num2] + '? <br><input type="text" required></p>');

		$('#apply').submit(function( event ) {

			$('input, textarea', this).css('outline', 'none');
			$('#status').html('');

			isNotABot = notABot($('#robotProof input').val(), answer);
			formIsCompleted = formCompleted($('#apply'));
			passwordsMatch = passwordMatch($(':password'));

			if ( isNotABot && formIsCompleted && passwordsMatch ) { return true; }
			else { event.preventDefault(); }
		});
	});

	function passwordMatch(passwords) {

		password = $(passwords[0]).val();
		confirm = $(passwords[1]).val();

		if ( password === confirm ) { return true; }
		else {
			$(passwords).each(function() {
				$(this).css('outline', '1px solid red');
			});

			$('#status').append('<p>Your passwords don&rsquo;t match.</p>');
			
			return false;
		}
	}

	function notABot(value, answer) {
			if ( ( parseInt(value) === answer ) || ( value === nums[answer] ) ) { return true; }
			else { 
				$('#status').append('<p>Your math is off.</p>');
				return false; 
			}
	}

	function formCompleted(form) {
		blank = [];

		$('[required]', form).each(function() {
			if ( $(this).val() == '' ) { blank.push($(this)); }
		})

		if ( blank.length > 0 ) {
			$(blank).each(function() {
				$(this).css('outline', '1px solid red');
			})
			
			$('#status').append('<p>Please fill out all required fields.</p>');

			return false;
		}

		else { return true; }
	}
</script>

JAVASCRIPT;

include_once $_SERVER["DOCUMENT_ROOT"] . "includes/footer.php"; ?>