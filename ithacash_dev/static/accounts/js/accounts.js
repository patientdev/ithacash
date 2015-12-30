$(function() {
    if ( $('#id_account_type').val() != '' ) {
        $('#account-type-selection').css('display', 'block');

        if ( $('#account-type span').data('accountType')  === 'Individual' ) {
            $('#id_entity_name, #txt2pay-phone').hide();
        }
    }

    $('#id_account_type').change(function() {
        account_type_selection = $(this).val();

        if ( account_type_selection  == 'Individual') {
            $('#id_entity_name, #account-txt2pay').hide();
            $('#id_full_name').attr('placeholder', 'Your Name');
            $('#individual-info').css('display', 'block');
        }

        else {

            $('#account-txt2pay').css('display', 'block');

            if ( account_type_selection == 'Standard Business' || account_type_selection == 'Premier Business' || account_type_selection == 'Freelancer') {
                   $('#id_entity_name').attr('placeholder', 'Business Name');

                   if ( account_type_selection == 'Standard Business') {
                    $('#standard-info').css('display', 'block');
                   }

                   else if ( account_type_selection == 'Premier Business') {
                    $('#premier-info').css('display', 'block');
                   }

                   else if ( account_type_selection == 'Freelancer') {
                    $('#freelancer-info').css('display', 'block');
                }
            }

            else {
                $('#id_entity_name').attr('placeholder', 'Organization Name');
                $('#nonprofit-info').css('display', 'block');
            }

            $('#id_full_name').attr('placeholder', 'Contact Name');
            $('#id_entity_name').show();

        }

        $('#account-type-selection').slideDown();
    })

    $('form#account').submit(function( event ) {

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
            data: data,
        })
        .always(function( response ){
            console.log(response);
        })
        .fail(function( response ){

            if ( response.status == 400 ) {

                errors = $.parseJSON(response.responseText);

                // Which fields have errors
                error_indices = []
                $.each(errors, function(index) {
                    error_indices.push(index);
                })

                inputs = $(':input', form);

                //
                // Highlight form inputs that have errors
                //
                $.each(inputs, function() {
                    input_name = $(this).attr('name');

                    // If the name of the input equals the error field index
                    if ( $.inArray(input_name, error_indices) != -1 ) {

                        $(this).addClass('error').after('<span class="error-message">' + error_message + '</span>');

                    }

                    // De-highlight inputs that are now valid
                    else {
                        $(this).removeClass('error');
                    }
                })

                return false;
            }

            else if ( response.status == 500 ) {
                $('form#account').replaceWith('<p>An error occured. Please refresh the page and try again.</p>');
            }

            else {
                $('form#account').replaceWith('<p>An error occured. Please refresh the page and try again.</p>');
            }

        })
        .success(function(){
             // Send successful form inputs to the next step
             $('form#account').unbind('submit').submit();
        })
    })

    $('form#account input').focus(function() {
        $(this).parent().siblings('.help-text').find('.text').css('opacity', '1');
        $(this).siblings('.error-message').remove();
    })
    $('form#account input').blur(function() {
        $(this).parent().siblings('.help-text').find('.text').css('opacity', '0');
    })

    $('form#account label').hover(function() {
        $(this).parent().siblings('.help-text').find('.text').css('opacity', '1');
    }, function() {
        $(this).parent().siblings('.help-text').find('.text').css('opacity', '0');
    })

    $('.help').hover(function() {
        $(this).siblings('.text').css('opacity', '1');
    }, function() {
        $(this).siblings('.text').css('opacity', '0');
    })
})

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
