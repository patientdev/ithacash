$(function() {
	if ( $('#id_account_type').val() != '' ) {
		$('#account-type-selection').css('display', 'block');

        if ( $('#id_account_type').val()  == 'Individual' || $('#id_account_type').val() == 'Freelancer' ) {
            $('#id_entity_name').hide();
        }
	}

    $('#id_account_type').change(function() {
        if ( $(this).val()  == 'Individual' || $(this).val() == 'Freelancer' ) {
            $('#id_entity_name').val('n/a').hide();
            $('#id_full_name').attr('placeholder', 'Your Name');
        } else {

            if ( $(this).val() == 'Standard Business' || $(this).val() == 'Premium Business' ) {
            $('#id_entity_name').attr('placeholder', 'Business Name');
            } else {
                $('#id_entity_name').attr('placeholder', 'Organization Name');
            }
            $('#id_full_name').attr('placeholder', 'Contact Name');
            $('#id_entity_name').show();

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
		.success(function( response ){

			if ( typeof response.errors != 'undefined') {

	            errors = $.parseJSON(response.errors);

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

	            return false;
	        }

	     $('form').unbind().submit(); 

	    })
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
