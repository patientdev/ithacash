<!doctype html>
<html>
<head>
	<style>

		body { 
			height: 2000px;
		}

		#notes {
			position: absolute;
			width: 522px;
			height: 252px;
			box-shadow: 0;
			top: 50%; right: 200px;
			background-color: transparent;
			padding: 100px;
		}


		#one-note, #five-note, #ten-note, #twenty-note {
			transition-property: -webkit-transform, box-shadow;
			transition-timing-function: ease-in;
			text-align: right;
		}

		h1 {
			padding: 10px;
			border-top: 1px solid black;
			border-bottom: 1px solid black;
			background-color: rgb(153, 200, 102);
			color: white;
			font-family: Helvetica, Arial, sans-serif;
		}

		#one-note {
			width: 400px;
			height: 100px;
			border: 1px solid black;
			position: absolute;
			top: 250px; right: 220px;
			box-shadow: 4px 0 4px #555;
			background-color: white;
			z-index: 5;
		}

		#five-note {
			width: 400px;
			height: 150px;
			border: 1px solid black;
			position: absolute;
			top: 200px; right: 180px;
			box-shadow: 4px 0 4px #555;
			background-color: white;
			z-index: 4;
		}

		#ten-note {
			width: 400px;
			height: 200px;
			border: 1px solid black;
			position: absolute;
			top: 150px; right: 140px;
			box-shadow: 4px 0 4px #555;
			background-color: white;
			z-index: 3;
		}

		#twenty-note {
			width: 400px;
			height: 250px;
			border: 1px solid black;
			position: absolute;
			right: 100px; top: 100px;
			box-shadow: 4px 0 4px #555;
			background-color: white;
			z-index: 2;
		}
	</style>
</head>
<body>

	<div id="notes">
		<div id="one-note"><h1>i$1</h1></div>
		<div id="five-note"><h1>i$5</h1></div>
		<div id="ten-note"><h1>i$10</h1></div>
		<div id="twenty-note"><h1>i$20</h1></div>
	</div>

	<?php include $_SERVER["DOCUMENT_ROOT"] . "/js/jquery.js" ?>

	<script>
		$(window).scroll(function() {

			Yscroll = $(window).scrollTop();
			Yrotate = (Yscroll/20) + 4;

			if (Yscroll < 550 && Yscroll > 100 ) {
				$('#notes').css({
					'-webkit-transform': 'rotateY(' + Yrotate + 'deg)'
				});
				$('#one-note, #five-note, #ten-note, #twenty-note').css({
						'box-shadow': (Yrotate/2) + 'px ' + '0px ' + (Yrotate/2) + 'px ' + '#555'
				});
			}
		});
	</script>

</body>
</html>