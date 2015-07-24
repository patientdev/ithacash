$(function() {

    $('.next').click(function( event ) {

        event.preventDefault();

        // Login Info
        if ( $(this).parents('#login').length > 0 ) {

            empties = verifyRequired('#login');

            if ( empties.length > 0 ) {
                $(empties).each(function() {
                    $(this).addClass('error');
                });

                return false;
            }

            else {
                $('#sign-up-1').removeClass('selected');
                $('#sign-up-2').addClass('selected');
                $('#info input').attr('disabled', false);
                $('#info').css('display', 'block');
                mapInputsToReview($('#login'));
            }
        }

        // Contact Info
        else if ( $(this).parents('#info').length > 0 ) {

            empties = verifyRequired('#info');
            console.log(empties);
            if ( empties.length > 0 ) {
                $(empties).each(function() {
                    $(this).addClass('error');
                })

                return false;
            }

            else {
                $('#sign-up-2').removeClass('selected');
                $('#sign-up-3').addClass('selected');
                $('#review').css('display', 'block');
                mapInputsToReview($('#info')); }
        }

        // Review Info
        else if ( $(this).parents('#review').length > 0 ) {
            $('#sign-up-2').removeClass('selected');
            $('#sign-up-3').addClass('selected');
        }

        // Move it along
        anchor = $(this);
        next = $(this).attr('href');

        $('#content').stop().animate({
                scrollLeft: "+=" + $(next).offset().left,
            }, {
                specialEasing: 'ease',
                duration: 750
        });
    })

    $('.back').click(function() {

        // Review Info
        if ( $(this).parents('#review').length > 0 ) {
            $('#sign-up-3').removeClass('selected');
            $('#sign-up-2').addClass('selected');
            setTimeout(function() {
                $('#review').css('display', 'none');
            }, 750)
        }

        else if ( $(this).parents('#info').length > 0 ) {
            $('#sign-up-2').removeClass('selected');
            $('#sign-up-1').addClass('selected');
            setTimeout(function() {
                $('#info').css('display', 'none');
            }, 750)
        }
        // Move it along
        anchor = $(this);
        previous = $(this).attr('href');

        $('#content').stop().animate({
                scrollLeft: "+=" + $(previous).offset().left,
            }, {
                specialEasing: 'ease',
                duration: 750
        });
    });

});

function mapInputsToReview(div) {
    inputs = $('input', div);

    $(inputs).each(function() {
        name = $(this).attr('name');
        val = $(this).val();

        $('#review-' + name).text(val);

        if ( $(this).attr('type') == 'checkbox') {
            if ( $(this).is(':checked') ) { $('#review-' + name).html('&#10004;'); }
            else { $('#review-' + name).html('&#10008;'); }
        }
    })
}

function verifyRequired(div) {
    inputs = $('input', div);

    empties = [];

    $(inputs).each(function() {
        if ( $(this).attr('required') == 'required' && $(this).val() == '') {
            empties.push($(this));
        }
    });

    return empties;
}
