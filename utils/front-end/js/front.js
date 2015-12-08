$(function() {

    $('#panels').slick({
          infinite: true,
          autoplay: true,
          autoplaySpeed: 7000,
          prevArrow: $('#left-arrow button'),
          nextArrow: $('#right-arrow button'),
          pauseOnHover: false
    }).on('afterChange', function() {
        var currentSlide = $(this).slick('slickCurrentSlide');
        if ( currentSlide === 0 ) { $(this).slick('slickPlay'); }
    });

    $('#intro .banners').slick({
        autoplay: true,
        infinite: true,
        autoplaySpeed: 5000,
        pauseOnHover: false,
        dots: true
    });

    $('#more-arrow').click(function() {
        windowHeight = $(window).height();
        sectionHeight = $('#invigorating-our-economy').height();
        offset = $('#invigorating-our-economy').offset().top + 150 - ((windowHeight - sectionHeight)/2);

        $('html, body').animate({
            scrollTop: offset + 'px'
        });
    });
});
