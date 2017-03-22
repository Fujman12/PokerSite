$(function() {

	//Chrome Smooth Scroll
	try {
		$.browserSelector();
		if($("html").hasClass("chrome")) {
			$.smoothScroll();
		}
	} catch(err) {

	};

	$("img, a").on("dragstart", function(event) { event.preventDefault(); });

	$(".news-article").dotdotdot({
		ellipsis	: '...',
	});
	$(".news-description-wrapper").dotdotdot({
		ellipsis	: '...',
		watch: "window"
	});
	var sc = $('#myScroller').radiantScroller({
		elementWidth: 380,
		cols: 3,
		rows: 2,
		addPagination: true,
	});

	$('.pgwSlideshow').pgwSlideshow();

	$("#lightSlider").lightSlider({
		item: 1,
        autoWidth: false,
        slideMove: 1, // slidemove will be 1 if loop is true
        slideMargin: 10,
 
        addClass: '',
        mode: "slide",
        useCSS: true,
        cssEasing: 'ease', //'cubic-bezier(0.25, 0, 0.25, 1)',//
        easing: 'linear', //'for jquery animation',////
 
        speed: 400, //ms'
        auto: false,
        loop: true,
        slideEndAnimation: true,
        pause: 4000,
        pauseOnHover: true,

 		adaptiveHeight: true,
        thumbItem: 5,
        gallery: true,
        galleryMargin: 150,
        thumbMargin: 15,
        currentPagerPosition: 'middle',
        vThumbWidth: 100
    });

	$(".top-mnu .top-mnu-content ul li .mnu-point-nm2017").click(function() {
	  $(".nm2017-hidden-mnu").slideToggle();
	});
	// $(".top-mnu .top-mnu-content ul li .mnu-point-nmStats").hover(function() {
	//   $(".nm-stats-hidden-mnu").slideToggle();
	// });
	$(".top-mnu .top-mnu-content ul li .mnu-point-nmStats").click(function() {
	  $(".nm-stats-hidden-mnu").slideToggle();
	});
	// $(".facebook-login-button").click(function() {
	//   $(".facebook-login .facebook-login-button").css({"display": "none"});
	//   $(".facebook-login .facebook-login-button").css({"display": "none"});
	// });
});
