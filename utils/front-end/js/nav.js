$(function() {
	$('#nav-how-it-works').hover(function() {
		$('> ul', this).slideDown('fast');
	}, function() {
		$('> ul', this).slideUp('fast');
	});

	$('#nav-menu ul li ul li ul li').hover(function() {
		if ( $('> ul', this).length > 0 ) {
			$(this).css('border-bottom', 'none');
			$('> ul', this).slideDown('fast');
		}
	}, function() {
		if ( $('> ul', this).length > 0 ) {
			$(this).css('border-bottom', 'none');
			$('> ul', this).slideUp('fast');
		}
	});
})