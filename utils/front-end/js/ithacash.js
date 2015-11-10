$(function() {

    $('#nav-menu a').click(function( event ) {
        section = $(this).attr('href');

        if ( section.match('#') ) {
            sectionOffset = $(section.replace('/', '')).offset().top;
            scrollTo = sectionOffset - parseInt($('header').css('height'));
            $('html, body').animate({ scrollTop: scrollTo + 'px' });
            return false;
        }

        else { return true; }

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

    $('#send-message').submit(function( event ) {
        event.preventDefault();

        data = $(this).serialize();
        validation_url = window.location.pathname;

        $.ajax({
            url: validation_url,
            method: 'POST',
            data: data,
            statusCode: {
                200: function() {
                    $('#send-message').replaceWith('<p>Thanks for the message!</p>');
                },

                400: function() {

                    $('#send-message').append('<p class="error">Please fill out both inputs.</p>');
                },

                500: function() {
                    $('#send-message button').replaceWith('<p class="error">An error occured. Please refresh the page and try again.</p>');
                }
            }
        })
    });

    $('#join-email-list').submit(function( event ) {
        event.preventDefault();

        data = $(this).serialize();
        validation_url = window.location.pathname;

        $.ajax({
            url: validation_url,
            method: 'POST',
            data: data,
            statusCode: {
                200: function() {
                    $('#join-email-list').replaceWith('<p class="error">Thanks for signing up!</p>');
                },

                400: function( response ) {

                    errors = $.parseJSON(response.responseText);

                    if ( errors.errors == 'already exists' ) {
                        $('#join-email-list').replaceWith('<p class="error">It looks like you&rsquo;re already signed&ndash;up! Check your spam folder if you&rsquo;re not receiving our newsletter.</p>');
                    }

                    else {
                        $('#join-email-list').append('<p class="error">Please submit your email address.');
                    }
                },

                500: function() {
                    $('#join-email-list').replaceWith('<p class="error">An error occured. Please refresh the page and try again.</p>');
                }
            }
        })
    });

    $('form.standard-form').submit(function( event ) {

        event.preventDefault();
        event.stopImmediatePropagation();

        form = $(this);

        data = form.serialize();
        action_url = $(this).attr('action');
        validation_url = window.location.pathname;

        // Have AJAX handle the validation
        $.ajax({
            url: validation_url,
            method: 'POST',
            data: data
        })
        .always(function( response ) {
            console.log(response);
        })
        .fail(function( response ){

            if ( response.status == 400 ) {

                errors = $.parseJSON(response.responseText);

                // Which fields have errors
                error_indices = []
                $.each(errors, function(index) {
                    error_indices.push(index);
                    console.log(index);
                })

                inputs = $(':input', form);

                //
                // Highlight form inputs that have errors
                //
                $.each(inputs, function() {
                    input_name = $(this).attr('name');

                    // If the name of the input equals the error field index
                    if ( $.inArray(input_name, error_indices) != -1 ) {
                        error_message = errors[input_name][0];

                        // Update error message if input is still invalid
                        if ( $(this).next('.error-message').length > 0 ) {
                            $(this).next('.error-message').text(error_message);
                        }

                        else {
                            $(this).addClass('error').after('<span class="error-message">' + error_message + '</span>');
                        }
                    }

                    // De-highlight iputs that are now valid
                    else {
                        $(this).removeClass('error');
                        $(this).next('.error-message').remove();
                    }
                })

                    $('html, body').animate({
                        scrollTop: $('.error-message').first().offset().top - 170
                    })


                return false;
            }

            else if ( response.status == 500 ) {
                $('form#account').replaceWith('<p>An error occured. Please refresh the page and try again.</p>');
            }


        })
        .success(function(){
             $('form#account').unbind('submit').submit();
        })
    })

});
