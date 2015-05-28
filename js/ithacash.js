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

	$('#right-arrow button').click(function() {
		right = parseInt($('.panel').css('right'));

		console.log(right);

		$('.panel').css('right', right + 100 + '%');
	})

	$('#left-arrow button').click(function() {
		$('.panel').css('right', '-50%');
	})

});