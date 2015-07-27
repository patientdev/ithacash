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
		padding: 150px 0;
		text-align: center;
		color: white;
	}

	h2 {
		color: white;
		margin: 0;
	}

	#rows {
		width: 75%;
		margin: auto;
	}

	.row {
		padding: 0 40px;
		color: rgb(88, 122, 70);
		font-size: 1.8em;
		line-height: 1.2em;
		margin: 20px 0;
	}

	.image {
		width: 45%;
		display: inline-block;
	}

	.image {
		max-width: 100%;
	}

	.row:nth-of-type(odd) .image {
		float: right;
	}

	.row:nth-of-type(even) .image {
		float: left;
	}

	.copy {
		width: 50%;
		display: inline-block;
		vertical-align: middle;
	}

	.row:nth-of-type(odd) .copy {
		float: left;
	}

	.row:nth-of-type(even) .copy {
		float: right;
	}
</style>
CSS;

include $_SERVER["DOCUMENT_ROOT"] . "/includes/header.php"; ?>

<div id="content">

<div id="head">
	<h2>Getting an Account</h2>
</div>

<div id="rows">
	<div class="row clear">
		<div class="image">
			<img src="/account/img/WriteIcon.png">
		</div>

		<div class="copy">
			<p>Sign up for a free Ithacash account and start buying and selling with digital Ithaca Dollars (i$) anywhere they are accepted. Physical Ithaca Dollars will be available soon.</p>
		</div>
	</div>

	<div class="row clear">
		<div class="image">
			<img src="/account/img/WalkingIcon.png">
		</div>

		<div class="copy">
			<p>After you create an account, you can load it with Ithaca Dollars and start shopping. You’ll even get more bang for your buck with 125% back in i$ on your US$ purchase.</p>
		</div>
	</div>

	<div class="row clear">
		<div class="image">
			<img src="/account/img/CashIcon.png">
		</div>

		<div class="copy">
			<p>Using Ithacash is easy! Each Ithaca Dollar is valued 1 to 1 with the US Dollar. Any change due under i$1 can be made with US coins.</p>
		</div>
	</div>

	<div class="row clear">
		<div class="image">
			<img src="/account/img/PhoneIcon.png">
		</div>

		<div class="copy">
			<p>Link a cell phone number with your account to make and take payments with simple text messages.</p>
		</div>
	</div>

	<div class="row clear">
		<div class="image">
			<img src="/account/img/CompIcon.png">
		</div>

		<div class="copy">
			<p>All digital transactions are charged a flat rate of 2% to the seller.</p>
		</div>
	</div>
</div>

</div>

<?php include $_SERVER["DOCUMENT_ROOT"] . "/includes/footer.php"; ?>