<?php 

$head = <<<'CSS'

	<link rel="stylesheet" href="/css/odometer-theme-default.css">

	<style>

		header {
			position: relative;
		}

		#content {
			padding-top: 0;
		}

		#nav-menu { display: none; }

		#intro {
			background-image: none;
			background-color: rgb(88, 122, 70);
		}

		h2 {
			font-size: 5em;
			padding: 20px 20px 20px 60px;
			text-align: left;
			color: white;
			text-transform: none;
			display: inline-block;	
		}

		h6 {
			font-size: 1.3em;
			text-align: center;
			text-transform: uppercase;
			font-weight: normal;
			margin: 10px 0;
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
			width: 100%; height: 100%;
			padding-top: 10px;
			background-color: white;
			border-right: 1px solid #ccc;
			border-left: 1px solid #ccc;
			color: #333;
			-webkit-transition: all .2s ease-out;
		}

		#plans > div:first-of-type .plan {
			border-top-left-radius: 30px;
		}

		#plans > div:first-of-type .billing-cycle {
			border-bottom-left-radius: 30px;
		}

		#plans > div:last-of-type .plan {
			border: none;
			border-top-right-radius: 30px;
		}

		#plans > div:last-of-type .billing-cycle {
			border-bottom-right-radius: 30px;
		}

		#plans > div:hover {
			-webkit-transform: scale(1.04) translateY(-10px);
			z-index: 10;
			cursor: pointer;
		}

		#plans > div:hover > .plan, #plans > div:hover > .billing-cycle {
			box-shadow: 2px 5px 14px rgba(0, 0, 0, 0.4), -2px 5px 14px rgba(0, 0, 0, 0.4);
		}

		#plans > div:hover > .billing-cycle {
			-webkit-transform: translateY(-10px);
		}

		#plans > div.hover > .plan {
			border-right: 1px solid rgb(79, 115, 60);
			border-left: 1px solid rgb(79, 115, 60);
			border-top: 1px solid rgb(79, 115, 60);
		}

		#plans h3, #plans h4 {
			text-align: center;
			color: black;
			font-size: 1.4em;
			text-transform: none;
			font-weight: 600;
		}

		#plans h3 {
			margin-bottom: 40px;
			letter-spacing: -1px;
		}

		#plans h4 {
			font-weight: 200;
			letter-spacing: -1px;
			line-height: 1.4em;
			text-transform: lowercase;
			margin-top: 0;
			height: 80px;
		}

		#plans h4 strong {
			font-size: 2.8em;
			font-weight: 400;
		}

		#plans h4 span {
		line-height: 1em;
	}

		#plans h5 {
			font-size: 1.2em;
			text-align: center;
			font-weight: 200;
			padding: 10px 0;
			border-top: 1px solid #ccc;
			border-bottom: 1px solid #ccc;
			letter-spacing: -1px;
		}

		.plan ul {
			font-size: 1em;
			padding: 0 10px 0 40px;
		}

		.plan ul li {
			margin-bottom: 3px;
		}

		.billing-cycle {
			background-color: rgb(221, 234, 213);
			font-weight: 200;
			-webkit-transition: all .2s ease-out;
			border-bottom: 1px solid white;
			text-align: center;
		}

		.billing-cycle button {
			background-color: transparent;
			border: none;
			vertical-align: middle;
			height: 100%; width: 100%;
			display: block;
			padding: 20px 10px;
		}

		.billing-cycle button:focus {
			outline: none;
		}

		#under {
			width: 92%; height: 1000px;
			background-color: rgb(238, 237, 235);
			position: absolute;
			top: 100%; left: 50%;
			margin-left: -46%;
			z-index: -1;
		}
	</style>

CSS;

include $_SERVER["DOCUMENT_ROOT"] . "/includes/header.php"; ?>

<div id="content">

<section id="intro">
	<h2>Pricing Guide</h2>

	<div id="scheme" class="clear">
		<div id="plans" class="clear">
			<div id="individual">
				<div class="icon"><img src="/img/individual.png"></div>
				<div class="plan">
					<h3>Individual</h3>
					<h4><strong><span>Free</span></strong></h4>
					<h5>&nbsp;</h5>
					<h6>No annual fees</h6>

					<ul>
						<li>Ithacash Online</li>
						<li>&ldquo;TXT2PAY&rdquo;</li>
						<li>PayItFwd</li>
					</ul>
				</div>
				<div class="billing-cycle">
					<button>&nbsp;</button>
				</div>
			</div>
			<div id="freelancer">
				<div class="icon"><img src="/img/freelancer.png"></div>
				<div class="plan">
					<h3>Freelancer</h3>
					<h4><strong>$<span class="odometer">10</span></strong><br>+i$5/mo</h4>
					<h5>Billed Every 6 Months</h5>
					<h6>Annual fee of $25</h6>

					<ul>
						<li>Ithacash Online</li>
						<li>&ldquo;TXT2PAY&rdquo;</li>
						<li>PayItFwd</li>
						<li>Account Manager</li>
						<li>Directory Listings</li>
						<li>Voting Privileges</li>
					</ul>
				</div>
				<div class="billing-cycle">
					<button>Switch to monthly billing</button>
				</div>
			</div>
			<div id="regular">
				<div class="icon"><img src="/img/business.png"></div>
				<div class="plan">
					<h3>Regular</h3>
					<h4><strong>$<span class="odometer">30</span></strong><br>+i$15/mo</h4>
					<h5>Billed Every 6 Months</h5>
					<h6>Annual fee of $50</h6>

					<ul>
						<li>Ithacash Online</li>
						<li>&ldquo;TXT2PAY&rdquo;</li>
						<li>PayItFwd</li>
						<li>Account Manager</li>
						<li>Directory Listings</li>
						<li>Voting Privileges</li>
						<li>Visibility</li>
					</ul>
				</div>
				<div class="billing-cycle">
					<button>Switch to monthly billing</button>
				</div>
			</div>
			<div id="premier">
				<div class="icon"><img src="/img/business.png"></div>
				<div class="plan">
					<h3>Premier</h3>
					<h4><strong>$<span class="odometer">50</span></strong><br>+i$25/mo</h4>
					<h5>Billed Every 6 Months</h5>
					<h6>Annual fee of $100</h6>

					<ul>
						<li>Ithacash Online</li>
						<li>&ldquo;TXT2PAY&rdquo;</li>
						<li>PayItFwd</li>
						<li>Account Manager</li>
						<li>Directory Listings</li>
						<li>Voting Privileges</li>
						<li>Enhanced Visibility</li>
						<li>Priority Access To New Technology</li>
						<li>Higher PayItFwd Limit</li>
					</ul>
				</div>
				<div class="billing-cycle">
					<button>Switch to monthly billing</button>
				</div>
			</div>
			<div id="non-profit">
				<div class="icon"><img src="/img/nonprofit.png"></div>
				<div class="plan">
					<h3>Non&ndash;profit</h3>
					<h4><strong>$<span class="odometer">30</span></strong><br>+i$15/mo</h4>
					<h5>Billed Every 6 Months</h5>
					<h6>Annual fee of $50</h6>

					<ul>
						<li>Ithacash Online</li>
						<li>&ldquo;TXT2PAY&rdquo;</li>
						<li>PayItFwd</li>
						<li>Account Manager</li>
						<li>Directory Listings</li>
						<li>Voting Privileges</li>
						<li>Enhanced Visibility</li>
						<li>Need&ndash;based scholorships available</li>
					</ul>
				</div>
				<div class="billing-cycle">
					<button>Switch to monthly billing</button>
				</div>
			</div>
		</div>
	</div>

	<div id="under">

	</div>

</section>

</div>

<?php 

$foot = <<<JAVASCRIPT
<script src="/js/odometer.min.js"></script>

<script>
	$('.billing-cycle button').click(function() {
		plans = $('.odometer').parent().parent().parent().parent();

		plans.each(function() {
			plan = $(this).attr('id');
			odometer = $(this).find('.odometer');
			cost = odometer.text().replace('\\n', '');
			button = $(this).find('.billing-cycle button');
			
			if ( button.text() === 'Switch to monthly billing' ) {
				button.text('Switch to semiannual billing');
			}

			else button.text('Switch to monthly billing');

			if ( plan === 'freelancer' ) {
				if (cost == 10) { odometer.text(12); }
				else odometer.text(10);
			}
			else if ( plan === 'regular' || plan === 'non-profit' ) {
				if (cost == 30) { odometer.text(35); }
				else odometer.text(30);
			}
			else if ( plan === 'premier' ) {
				if (cost == 50) { odometer.text(60); }
				else odometer.text(50);
			}
		})

	})
</script>
JAVASCRIPT;

include $_SERVER["DOCUMENT_ROOT"] . "/includes/footer.php"; ?>