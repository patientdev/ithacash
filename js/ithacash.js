$('#login a').click(function() {
	$(this, '#login input, #login button').css('transform', 'translate(0)');
});

// $(window).on('scroll', function() {
// 	console.log($(window).scrollTop());
// 	if ($(window).scrollTop() > 39 ) {
// 		$('header').css('border-bottom', '1px solid black')
// 	}
// 	else {
// 		$('header').css('border-bottom', 'none')
// 	}
// });

$(function() {
	$('#branding-pitch').css('background-position', '0% 0%');
});

$(window).on('scroll', function() {

	var paralax = 0;
	var windowScroll = $(window).scrollTop();

	if ( $(window).width() > 840 ) { paralax = windowScroll/60; }

	else { paralax = $(window).scrollTop()/30; }
	
	$('#branding-pitch').css('background-position', '0% ' + (paralax + 10) + '%');
});