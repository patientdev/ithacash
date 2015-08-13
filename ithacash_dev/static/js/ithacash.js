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

	$('#send-message').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();
		validation_url = window.location.pathname;

		$.ajax({
			url: validation_url, 
			method: 'POST',
			data: data
		})
		.always(function( response ) {
			console.log(response);
		})
		.fail(function( response ){
			$('#send-message').replaceWith('<p>An error occured. Please refresh the page and try again.</p>');
	    })
	    .success(function(response) {
			$('#send-message button').replaceWith('<p>Thanks for the message!</p>');
	    })
	});

	$('#join-email-list').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();
		validation_url = window.location.pathname;

		$.ajax({
			url: validation_url, 
			method: 'POST',
			data: data
		})
		.always(function( response ) {
			console.log(response);
		})
		.fail(function( response ){
			$('#send-message').replaceWith('<p>An error occured. Please refresh the page and try again.</p>');
	    })
	    .success(function(response) {
	    	$('#join-email-list button').replaceWith('<p>Thanks for signing up!</p>');
	    })
	});

	$('#panels').slick({
		  infinite: true,
		  autoplay: true,
		  autoplaySpeed: 7000,
		  prevArrow: $('#left-arrow button'),
		  nextArrow: $('#right-arrow button')
	}).on('afterChange', function() {
		var currentSlide = $(this).slick('slickCurrentSlide');
		if ( currentSlide === 0 ) { $(this).slick('slickPlay'); } 
	});

});