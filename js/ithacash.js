$(function() {

	$('#nav-menu a').click(function( event ) {
		event.preventDefault();
		section = $(this).attr('href');
		sectionOffset = $(section).offset().top;

		scrollTo = sectionOffset - parseInt($('header').css('height'));

		$('html, body').animate({ scrollTop: scrollTo + 'px' });
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
		});
	});

	$('#join-email-list').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();

		$.post('/php/form-submit.php', data, function( success ) {
			$('#join-email-list button').replaceWith('<p>Thanks for signing up!</p>');
		});
	});

	$('#panels').slick({
		  infinite: true,
		  autoplay: true,
		  autplaySpeed: 5000,
		  prevArrow: $('#left-arrow button'),
		  nextArrow: $('#right-arrow button')
	});

});