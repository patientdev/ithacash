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