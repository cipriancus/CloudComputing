$(document).ready(function() {

    $('#send_request').click(function () {
        var user_input = $('#search_input').val();

        $('#jumbotron_content').replaceWith('<div id="loader"><div class="loader center-block"></div><h1>Searching...</h1></div>');

        $.ajax({
            type : "POST",
            url : "/search",
            data: JSON.stringify(user_input, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                $('#loader').replaceWith(result);
            }
        });
    });


});