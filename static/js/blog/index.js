/**
 * Created by xiaoshu on 2017/6/26.
 */

$(document).ready(function () {
    $('#welcome').fadeIn('slow');
})

$('.bug_info').click(function () {
    var id = $(this).attr('id');
    $.ajax({
        type: 'POST',
        url: 'api/get_bug_info/',
        data: {"BugID": id},
        dataType: "json",
        success: function (bug_info) {
            $('#bug_info_win').modal({backdrop: false, keyboard: false}).modal('show');
            var info_win_bug_id = document.getElementById("info_win_bug_id");
            var info_win_bug_abstract = document.getElementById("info_win_bug_abstract");
            var info_win_bug_level = document.getElementById("info_win_bug_level");
            var info_win_start_username = document.getElementById("info_win_start_username");
            var info_win_start_time = document.getElementById("info_win_start_time");
            var info_win_update_time = document.getElementById("info_win_update_time");
            var info_win_bug_status = document.getElementById("info_win_bug_status");
            var info_win_bug_file = document.getElementById("info_win_bug_file");
            var info_win_bug_position = document.getElementById("info_win_bug_position");
            var info_win_bug_info = document.getElementById("info_win_bug_info");
            info_win_bug_id.innerHTML = bug_info.BugID;
            info_win_bug_abstract.innerHTML = bug_info.BugAbstract;
            info_win_bug_level.innerHTML = bug_info.BugLevel;
            info_win_bug_level.style.color = bug_info.BugLevelColor;
            info_win_start_username.innerHTML = bug_info.Username;
            info_win_start_time.innerHTML = bug_info.CreateTime;
            if (bug_info.BugStatus === "未解决") {
                info_win_update_time.innerHTML = "";
            }
            else {
                info_win_update_time.innerHTML = bug_info.UpdateTime;
            }
            info_win_bug_status.innerHTML = bug_info.BugStatus;
            info_win_bug_status.style.color = bug_info.BugStatusColor;
            info_win_bug_file.innerHTML = bug_info.BugFile;
            info_win_bug_position.innerHTML = bug_info.BugPosition;
            info_win_bug_info.innerHTML = bug_info.BugInfo;
        },
    });
})