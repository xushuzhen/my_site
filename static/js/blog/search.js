/**
 * Created by xiaoshu on 2017/7/24.
 */
$('#search-article-button').on('click', function () {
    var key_words = $('#search-article-input').val();
    key_words = key_words.replace(/ /g, '').replace(/，/g, '').replace(/,/g, '').replace(/\./g, '').replace(/。/g, '');
    window.location.href = '/search/' + key_words + '/1/';
});