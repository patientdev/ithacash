$(function() {

	$('#nav-menu a').click(function( event ) {
		section = $(this).attr('href');

		if ( section.match('#') ) {
			sectionOffset = $(section.replace('/', '')).offset().top;
			scrollTo = sectionOffset - parseInt($('header').css('height'));
			$('html, body').animate({ scrollTop: scrollTo + 'px' });
			return false;
		}

		else { return true; }

	});

	$('#accounts > ul > li').hover(function() {
		$('#accounts li').each(function() { $(this).removeClass('selected'); })
		$(this).addClass('selected');

		selection = $(this).attr('id');

		$('#' + selection + '-info').toggle();

		$('#accounts > div > div').each(function() {
			if ( $(this).attr('id') != (selection + '-info') ) {
				$(this).css('display', 'none');
			}

			else { $(this).css('display', 'table-cell'); }
		})
	})

	$('#contact-form form').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();

		$.post('/php/form-submit.php', data, function( success ) {
			$('#contact-form form button').replaceWith('<p>Thanks for the message!</p>');
			console.log(success);
		});
	});

	$('#join-email-list').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();

		$.post('/php/form-submit.php', data, function( success ) {
			$('#join-email-list button').replaceWith('<p>Thanks for signing up!</p>');
			console.log(success);
		});
	});

	$('#apply').submit(function( event ) {
		event.preventDefault();
		
		$('input, textarea', this).css('outline', 'none');
		$('#status').html('');

		isNotABot = notABot($('#robotProof input').val(), answer);
		formIsCompleted = formCompleted($('#apply'));
		passwordsMatch = passwordMatch($(':password'));

		if ( isNotABot && formIsCompleted && passwordsMatch ) { 
			data = $(this).serialize();

			$.post('/php/form-submit.php', data, function( success ) {
				$('#join-email-list button').replaceWith('<p>Thanks for signing up!</p>');
				console.log(success);
			}); 
		}
	});

	$('#panels').slick({
		  infinite: true,
		  autoplay: true,
		  autoplaySpeed: 7000,
		  prevArrow: $('#left-arrow button'),
		  nextArrow: $('#right-arrow button')
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