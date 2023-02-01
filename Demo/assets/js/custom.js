(function ($) {
	"use strict";
	// /*========== Nice Select ==========*/
		$('select').niceSelect();
	// /*==========  wow  ==========*/
	new WOW().init();		
	// /*========== Responsive Menu  ==========*/
	$('.header__area-menubar-main-menu').meanmenu({
		meanMenuContainer: '.responsive-menu',
		meanScreenWidth: '991',
		meanMenuOpen: '<span></span><span></span><span></span>',
		meanMenuClose: '<i class="flaticon-close"></i>'
	});
	/*========== menu-bar sticky  ==========*/
	$(window).on('scroll', function () {
		var scrollDown = $(window).scrollTop();
		if (scrollDown < 135) {
			$(".header__area-menubar-area").removeClass("header__area-menubar-area-sticky-menu");
		} else {
			$(".header__area-menubar-area").addClass("header__area-menubar-area-sticky-menu");
		}
	});
	/*==========  counterUp  ==========*/
	var counter = $('.counter');
	counter.counterUp({
		time: 2500,
		delay: 100
	});
	/*==========  Search  =========*/
	$('.header__area-menubar-right-search-icon.open').on('click', function () {
		$('.header__area-menubar-right-search-box').fadeIn().addClass('active');
	});
	$('.header__area-menubar-right-search-box-icon').on('click', function () {
		$(this).fadeIn().removeClass('active');
	});
	$('.header__area-menubar-right-search-box-icon i').on('click', function () {
		$('.header__area-menubar-right-search-box').fadeOut().removeClass('active');
	});
	$('.header__area-menubar-right-search-box form').on('click', function (e) {
		e.stopPropagation();
	});
	// /*==========  sidebar popup  ==========*/
	$('.hamburger-icon i').on("click", function () {
		$('.hamburger-popup').addClass('active');
	});
	$('.hamburger-popup .hamburger-close-btn').on("click", function () {
		$('.hamburger-popup').removeClass('active');
	});
	$('.hamburger-icon i').on("click", function () {
		$('.hamburger-overlay').addClass('show');
	});
	$('.hamburger-popup .hamburger-close-btn').on("click", function () {
		$('.hamburger-overlay').removeClass('show');
	});
	/*==========  img-popup  ==========*/
	$('.img-popup').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});
		/*==========  Skill Bar Two  ==========*/
		if ($('.about__two-right-skill-area-skill-item-bar').length) {
			$('.about__two-right-skill-area-skill-item-bar').appear(function () {
				var el = $(this);
				var percent = el.data('width');
				$(el).css('width', percent + '%');
			}, {
				accY: 0
			});
		};	
	/*==========  video-popup  ==========*/
	$('.video-popup').magnificPopup({
		type: 'iframe'
	});
	/*==========  background  ==========*/
	$("[data-background]").each(function () {
		$(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
	})
	// /*==========  testimonial  ==========*/
	var swiper = new Swiper(".testimonial-slider", {
		slidesPerView: 1,
		loop: true,
		spaceBetween: 50,
		pagination: {
			el: ".dots",
			clickable: true,
		},
		breakpoints: {
			991: {
				spaceBetween: 50,
			},
		}
	});
	// /*==========  testimonial  ==========*/
	var swiper = new Swiper(".reviews", {
		slidesPerView: 1,
		loop: true,
		speed: 1000,
		spaceBetween: 30,
		pagination: {
			el: ".reviews-pagination",
			clickable: true,
		},
	});	
	// /*==========  Brand  ==========*/
	var swiper = new Swiper(".sponsors-slider", {
		slidesPerView: 3,
		loop: true,
		speed: 1500,
		spaceBetween: 120,
		breakpoints: {
			0: {
				spaceBetween: 50,
				slidesPerView: 2
			},
			575: {
				spaceBetween: 80,
				slidesPerView: 3
			},
			992: {
				slidesPerView: 4
			},
			1200: {
				slidesPerView: 3
			},
		}
	});	
	/*========== scroll to top  ==========*/
	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 200) {
			$('.scroll-top').fadeIn(200);
		} else {
			$('.scroll-top').fadeOut(200);
		}
	});
	$('.scroll-top').on('click', function (event) {
		event.preventDefault();
		$('html, body').animate({
			scrollTop: 0
		}, 1000);
	});
	/*==========  theme loader  ==========*/
	$(window).on("load", function () {
		$(".theme-loader").fadeOut(500);
	/*==========  Progress Bar  ==========*/  
	if($('.skilbar__area-bar').length) {
	  $('.skilbar__area-bar').appear(function(){
		  var el = $(this);
		  var percent = el.data('width');
		  $(el).css('width', percent+'%');
	  }, {accY: 0});
  	};
		/*========== FAQ  ==========*/
		$(".faq__area-collapse-item-card-header").click(function () {
			if ($(this).next(".faq__area-collapse-item-card-header-content").hasClass("active")) {
				$(this).next(".faq__area-collapse-item-card-header-content").removeClass("active").slideUp()
				$(this).children("i").removeClass("flaticon-minus").addClass("flaticon-plus")
			} else {
				$(".faq__area-collapse-item-card .faq__area-collapse-item-card-header-content").removeClass("active").slideUp()
				$(".faq__area-collapse-item-card .faq__area-collapse-item-card-header i").removeClass("flaticon-minus").addClass("flaticon-plus");
				$(this).next(".faq__area-collapse-item-card-header-content").addClass("active").slideDown()
				$(this).children("i").removeClass("flaticon-plus").addClass("flaticon-minus")
			}
		});
	/*========== Active Hover  ==========*/
	$(".project__area-item").hover(function () {
		$(".project__area-item").removeClass("project__area-item-hover");
		$(this).addClass("project__area-item-hover");
	});
	/*========== Active Hover  ==========*/
	$(".choose__ua-right-list-icon").hover(function () {
		$(".choose__ua-right-list-icon").removeClass("choose__ua-right-list-icon-hover");
		$(this).addClass("choose__ua-right-list-icon-hover");
	});

	});
})(jQuery);