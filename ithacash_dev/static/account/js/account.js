$(function() {
	if ( $('#id_account_type').val() != '' ) {
		$('#account-type-selection').css('display', 'block');

        if ( $('#id_account_type').val()  == 'Individual' ) {
            $('#id_entity_name').hide();
        }
	}

    $('#id_account_type').change(function() {
        if ( $(this).val()  == 'Individual') {
            $('#id_entity_name').val('n/a').hide();
            $('#id_full_name').attr('placeholder', 'Your Name');
        } 

        else {

            if ( $(this).val() == 'Standard Business' || $(this).val() == 'Premier Business' || $(this).val() == 'Freelancer') {
           		$('#id_entity_name').attr('placeholder', 'Business Name');
            } 

            else {
                $('#id_entity_name').attr('placeholder', 'Organization Name');
            }

            $('#id_full_name').attr('placeholder', 'Contact Name');
            $('#id_entity_name').val('').show();

        }

        $('#account-type-selection').slideDown();
    })

    $('form#account').submit(function( event ) {

    	event.preventDefault();

    	form = $(this);

    	data = form.serialize();
		action_url = '';

		$.ajax({
			url: action_url, 
			method: 'POST',
			data: data
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
	        	$('form').replaceWith('<p>An error occured. Please refresh the page and try again.</p>');
	        }


	    })
		.success(function(){
		     $('form').unbind().submit(); 
		})
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
