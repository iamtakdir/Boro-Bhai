// var timer;
// $(
//     '#id_search'
// ).keyup(function () {
//     clearTimeout(timer);
//     $('#search_results').text('');
//     timer = setTimeout(function () {
//         var text = $('#id_search').val();
//         $.ajax({
//             url: '/video/search',
//             data: {
//                 'search': text
//             },
//             dataType: 'json',
//             success: function (data) {

//                 var results = '';
//                 $('#search_result').text('');

//                 data['items'].forEach(function (video) {
//                     results += video['snippet']['title']
//                 });
//                 $('#search_results').append(results);
//             }
//         });
//     }, 2000);

// });


var delayTimer;
$('#id_search').keyup(function () {
    clearTimeout(delayTimer);
    $('#search_results').text('<h4>Loading ... ...</h4>');
    delayTimer = setTimeout(function () {
        var text = $('#id_search').val();
        $.ajax({
            url: '/video/search',
            data: {
                'search': text
            },
            dataType: 'json',
            success: function (data) {
                var results = '';
                $('#search_results').text('');
                results += '<div class="row">';
                data['items'].forEach(function (video) {
                    results += '<div class="col-md-4 mt-3"><div class="card mb-4 shadow-sm">';
                    results += '<iframe width="100%" height="225" src="https://www.youtube.com/embed/' + video['id']['videoId'] +
                        '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
                    results += '<div class="card-body"><p class="card-text">' + video['snippet']['title'] + '</p>';
                    results += '<a href="#" class="btn btn-primary" onclick="addVideo(\'' + video['id']['videoId'] + '\')">Add</a></div></div></div>';

                });
                results += '</div>';
                $('#search_results').append(results);
            }
        });
    }, 3000);
});

function addVideo(video_id) {
    $('#id_url').val('https://www.youtube.com/watch?v=' + video_id);
    $('#submit_video').submit();
}