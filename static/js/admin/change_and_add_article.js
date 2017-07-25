$(document).ready(function () {
    var class_arr = $('#class_input').val().split(',');
    var label_arr = $('#label_input').val().split(',');
    var class_boxes = document.getElementsByClassName('class_checkbox');
    var label_boxes = document.getElementsByClassName('label_checkbox');
    for (var i = 0; i < class_arr.length; i++) {
        for (var j = 0; j < class_boxes.length; j++) {
            if (class_arr[i] === class_boxes[j].value) {
                class_boxes[j].checked = true;
                break;
            }
        }
    }
    for (var i = 0; i < label_arr.length; i++) {
        for (var j = 0; j < label_boxes.length; j++) {
            if (label_arr[i] === label_boxes[j].value) {
                label_boxes[j].checked = true;
                break;
            }
        }
    }

});

$('#class_select_btn').on('click', function () {
    var boxes = document.getElementsByClassName('class_checkbox');
    var class_arr = [];
    for (var i = 0; i < boxes.length; i++) {
        if (boxes[i].checked) {
            class_arr.push(boxes[i].value)
        }
    }
    var class_str = class_arr.join(',');
    $('#class_input').val(class_str)
});

$('#label_select_btn').on('click', function () {
    var boxes = document.getElementsByClassName('label_checkbox');
    var label_arr = [];
    for (var i = 0; i < boxes.length; i++) {
        if (boxes[i].checked) {
            label_arr.push(boxes[i].value)
        }
    }
    var label_str = label_arr.join(',');
    $('#label_input').val(label_str)
});

$('#save_button').on('click', function () {
    $('#class_select_btn').click();
    $('#label_select_btn').click();
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
    var Label = $('#label_input').val();
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
