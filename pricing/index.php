<?php 

$head = <<<'CSS'

	<style>

		body { position: absolute; }

		#nav-menu { display: none; }

		#intro {
			height: 100hv; overflow: hidden;
			background-image: none;
			background-color: rgb(88, 122, 70);
		}

		h2 {
			background-color: rgb(115, 168, 86);
			padding: 20px 20px 20px 60px;
			text-align: left;
			color: white;
			text-transform: none;
			display: inline-block;	
		}

		#scheme {
			width: 90%; height: 100%;
			margin: auto;
			position: absolute;
			top: 40%;
			left: 50%; margin-left: -45%;
		}

		.icon {
			text-align: center;
			width: 100%;
			background-color:
			padding-bottom: 40px;
		}

		.icon img {
			width: 75px;
		}

		#plans {
			width: 100%; height: 100%;
		}

		#plans > div {
			width: calc(20% - 1px);
			height: 100%;
			float: left;
			-webkit-transition: all .2s ease-out;
			position: relative;
			top: 0;
		}

		.plan {
			width: 100%;
			padding: 10px 10px 20px 10px;
			background-color: white;
			border-right: 1px solid #ccc;
			border-left: 1px solid #ccc;
		}

		#plans > div:first-of-type .plan {
			border-top-left-radius: 30px;
		}

		#plans > div:last-of-type .plan {
			border: none;
			border-top-right-radius: 30px;
		}

		#plans > div:hover {
			-webkit-transform: scale(1.04) translateY(-10px);
			z-index: 10;
			top: -15%;
		}

		#plans > div.hover > .plan {
			border-right: 1px solid rgb(79, 115, 60);
			border-left: 1px solid rgb(79, 115, 60);
			border-top: 1px solid rgb(79, 115, 60);
		}

		#plans h3, #plans h4 {
			text-align: center;
			color: black;
			font-size: 1.8em;
			text-transform: none;
			font-weight: 600;
		}

		#plans h3 {
			margin-bottom: 60px;
			letter-spacing: -1px;
		}

		#plans h4 {
			font-weight: 200;
			letter-spacing: -2px;
			text-transform: lowercase;
		}

		#plans h4 strong {
			font-size: 2.8em;
			font-weight: 400;
		}

		#plans h5 {
			font-size: 1.3em;
			text-align: center;
			font-weight: 200;
			padding: 10px 0;
			border-top: 1px solid #ccc;
			border-bottom: 1px solid #ccc;
			color: #ccc;
		}
	</style>

CSS;

include $_SERVER["DOCUMENT_ROOT"] . "/includes/header.php"; ?>

<div id="content">

<section id="intro">
	<h2>Pricing guide</h2>

	<div id="scheme" class="clear">
		<div id="plans" class="clear">
			<div id="individual">
				<div class="icon"><img src="/img/individual.png"></div>
				<div class="plan">
					<h3>Individual</h3>
					<h4><strong>Free</strong></h4>
					<h5>Billed Every 6 Months</h5>

					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
				</div>
			</div>
			<div id="freelancer">
				<div class="icon"><img src="/img/individual.png"></div>
				<div class="plan">
					<h3>Freelancer</h3>
					<h4><strong>$10</strong>/mo</h4>
					<h5>Billed Every 6 Months</h5>

					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
				</div>
			</div>
			<div id="regular">
				<div class="icon"><img src="/img/business.png"></div>
				<div class="plan">
					<h3>Regular</h3>
					<h4><strong>$31</strong>/mo</h4>
					<h5>Billed Every 6 Months</h5>

					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
				</div>
			</div>
			<div id="premier">
				<div class="icon"><img src="/img/business.png"></div>
				<div class="plan">
					<h3>Premier</h3>
					<h4><strong>$50</strong>/mo</h4>
					<h5>Billed Every 6 Months</h5>

					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
				</div>
			</div>
			<div id="non-profit">
				<div class="icon"><img src="/img/nonprofit.png"></div>
				<div class="plan">
					<h3>Non&ndash;profit</h3>
					<h4><strong>$31</strong>/mo</h4>
					<h5>Billed Every 6 Months</h5>

					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
				</div>
			</div>
		</div>
	</div>

</section>

</div>

<?php include $_SERVER["DOCUMENT_ROOT"] . "/includes/footer.php"; ?>