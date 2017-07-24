$(document).ready(function () {
    var now_path = window.location.href;
    if (now_path.indexOf('change') > 0 && now_path.indexOf('article') > 0) {
        var article_id = now_path.split('article/')[1].split('/')[0];
        var href = now_path.split('article/')[0] + 'change_article/' + article_id + '/';
        $('#change_article_btn').attr('href', href);
        return;
    }
    else if (now_path.indexOf('add') > 0 && now_path.indexOf('article') > 0) {
        var href = now_path.split('article/')[0] + 'add_article/';
        $('#change_article_btn').attr('href', href);
        return;
    }
    $('#change_article_btn').text('');
});