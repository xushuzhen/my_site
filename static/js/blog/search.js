/**
 * Created by xiaoshu on 2017/7/24.
 */
$('#search-article-button').on('click', function () {
    layer.msg('正在查询，请稍后...', {
        time: 20000, //20s后自动关闭
    });
    var key_words = $('#search-article-input').val();
    key_words = key_words.replace(/!|@|#|\$|%|\^|&|\*|\(|\)|_|-|=|\+|！|¥|……|（|）|—|——|【|】|「|」|{|}|\[|]|、|\\|\||`|~|·|～|,|\.|\/|<|>|\?|，|。|／|《|》|？/g, '').replace(/ /g, '');
    console.log(key_words);
    window.location.href = '/search/' + key_words + '/1/';
});