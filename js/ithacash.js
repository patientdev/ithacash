$(function() {

	$('#nav-menu a').click(function( event ) {
		event.preventDefault();
		section = $(this).attr('href');
		sectionOffset = $(section).offset().top;

		scrollTo = sectionOffset - parseInt($('header').css('height'));

		$('html, body').animate({ scrollTop: scrollTo + 'px' });
	});

	$('#accounts li').hover(function() {
		$(this).toggleClass('selected');
	})

	$('#accounts li').blur(function() {
		$(this).toggleClass('selected');
	})

	$('#accounts li').click(function() {
		selection = $(this).attr('id');

		$('#' + selection + '-info').toggle();

		$('#accounts > div > div').each(function() {
			if ( $(this).attr('id') != (selection + '-info') ) {
				$(this).css('display', 'none');
			}

			else { $(this).css('display', 'block'); }
		})
	})

	$('#contact-form form').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();

		$.post('/php/form-submit.php', data, function( success ) {
			console.log(success);
		});
	});

	$('#join-email-list').submit(function( event ) {
		event.preventDefault();

		data = $(this).serialize();

		$.post('/php/form-submit.php', data, function( success ) {
			console.log(success);
		});
	});

});

function JSONinify( inputArray ) {

}