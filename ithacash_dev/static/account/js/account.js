$(function() {

    $('form').submit(function( event ) {

        e = event;
        e.preventDefault();

        action_url = $(this).attr('action')
        data = $(this).serialize();

        $.post(action_url, data, function( response ){
                if ( typeof response.errors != 'undefined') {
                    errors = $.parseJSON(response.errors);

                    // Which fields have errors
                    error_indices = []
                    $.each(errors, function(index) {
                        error_indices.push(index);
                    })

                    inputs = $('form :input');

                    //
                    // Highlight form inputs that have errors
                    //
                    $.each(inputs, function() {
                        input_name = $(this).attr('name');

                        // If the name of the input equals the invalid field index
                        if ( $.inArray(input_name, error_indices) != -1 ) {
                            error_message = errors[input_name][0]['message'];

                            // Logic for dealing with repeat errors
                            if ( $(this).next('.error-message').length > 0 ) {
                                $(this).next('.error-message').text('* ' + error_message);
                            }

                            else {
                                $(this).addClass('error').after('<span class="error-message">* ' + error_message);
                            }
                        }

                        // De-highlight iputs that are now valid
                        else {
                            $(this).removeClass('error');
                            $(this).next('.error-message').remove();
                        }
                    })

                }
        })

    })

});
