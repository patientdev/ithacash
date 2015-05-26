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

});