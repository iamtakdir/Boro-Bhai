var timer;
$(
    '#id_search'
).keyup(function () {
    clearTimeout(timer);
    $('#search_results').text('Loading......');
    timer = setTimeout(function () {
        var text = $('#id_search').val();
        $.ajax({
            url: '/video/search',
            data: {
                'search': text
            },
            dataType: 'json',
            success: function (data) {
                $('#search_results').text(data['hello']);
            }
        });
    }, 2000);

});