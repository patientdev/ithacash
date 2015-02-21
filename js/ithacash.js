$('#login button').click(function() {
	$(this).css('opacity', '0');
	$('#input').css('opacity', '1');
	$(this).css('z-index', '-1')
	$('#login input').focus();
})