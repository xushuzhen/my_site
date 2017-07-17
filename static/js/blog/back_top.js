window.onscroll = function () {
    if (document.documentElement.scrollTop + document.body.scrollTop > 100) {
        $("#go_top").fadeIn();
    }
    else {
        $("#go_top").fadeOut();
    }
}

$("#go_top").onclick(function () {
    var speed = 200;//滑动的速度
    $('body,html').animate({scrollTop: 0}, speed);
    return false;
});

$("#go_top").click(function () {
    var speed = 200;//滑动的速度
    $('body,html').animate({scrollTop: 0}, speed);
    return false;
});