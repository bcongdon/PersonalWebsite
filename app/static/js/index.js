window.addEventListener("scroll", function() {
    if (window.scrollY > 400) {
        $('.navbar').fadeIn();
    }
    else {
        $('.navbar').fadeOut();
    }
},false);

$(document).ready(function(){
	if (window.scrollY < 400) {
        $('.navbar').hide();
    }
});

$('#about').
    click(function(){
        var target = $('a[name=about]');
        if (target.length)
        {
            var top = target.offset().top;
            $('html,body').animate({scrollTop: top - 100}, 'slow');
            return false;
        }
    });