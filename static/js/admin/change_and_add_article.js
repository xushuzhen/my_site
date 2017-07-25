$('#save_button').on('click', function () {
    var now_path = window.location.href;
    var ArticleID = -1;
    if (now_path.indexOf('change_article') > 0) {
        ArticleID = now_path.split('change_article/')[1].split('/')[0];
    }
    var KeywordsSEO = $('#keywords_input').val();
    var DescriptionSEO = $('#description_input').val();
    var AuthorSEO = $('#author_input').val();
    var Title = $('#title_input').val();
    var Content = $('#content_input').html();
    var Class = $('#class_input').val();
    var Label = $('#lable_input').val();
    var Status = $('#status_select option:selected').val();
    var TimeLine = $('#timeline_select option:selected').val();
    var TimeLineType = $('#timeline_type_select option:selected').val();
    var article_data = {
        'ArticleID': ArticleID,
        'KeywordsSEO': KeywordsSEO,
        'DescriptionSEO': DescriptionSEO,
        'AuthorSEO': AuthorSEO,
        'Title': Title,
        'Content': Content,
        'Class': Class,
        'Label': Label,
        'Status': Status,
        'TimeLine': TimeLine,
        'TimeLineType': TimeLineType
    };
    $.ajax({
        type: 'POST',
        url: '/admin/blog/article_save/',
        data: article_data,
        dataType: 'json',
        success: function (r_msg) {
            if (r_msg.code == 200) {
                layer.open({
                    title: '系统提示',
                    content: '写入成功',
                    icon: '1',
                    end: function (layero, index) {
                        window.location.href = now_path.split('admin/')[0] + 'admin/blog/change_article/' + r_msg.msg + '/';
                    }
                });
            }
            else {
                layer.open({
                    title: '系统提示',
                    content: (r_msg.msg || "写入失败"),
                    icon: '2'
                });
            }
        }
    });
});