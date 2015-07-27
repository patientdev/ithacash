$(function() {

    var isValid = false;
    $('form').submit(function( event ) {

        if ( !isValid ) { event.preventDefault(); }

        isValid = true;

        action_url = $(this).attr('action')
        data = $(this).serialize();


        $.post(action_url, data, function( response ){

                if ( typeof response.errors !== 'undefined' ) {
                    isValid = false;
                    errors = $.parseJSON(response.errors);

                    $.each(errors, function(index) {
                        input = index;
                        error_message = errors[input][0]['message'];

                        $('#id_' + input).addClass('error').after('<span class="error-message">*' +  error_message + '</span>');
                    })

                    event.preventDefault();
                }
        })

    })

    if ( isValid ) { $(this).submit(); }

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
