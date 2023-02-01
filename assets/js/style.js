document.addEventListener('DOMContentLoaded', ()=>{
    window.addEventListener('scroll', ()=>{
        if (window.scrollY  > 150){
            document.getElementById('fixed-nav').classList.add('header-area-menubar-area-sticky-menu');
            navbar_height  = document.querySelector('.header-area').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';
        }else{
            document.getElementById('fixed-nav').classList.remove('header-area-menubar-area-sticky-menu');
            document.body.style.paddingTop = '0';
        }
    });
});

const prog = document.querySelectorAll('.skilbar-area-bar');
prog.forEach(element => {
		document.addEventListener('DOMContentLoaded', ()=>{
			window.addEventListener('scroll', () =>{
			if (window.scrollY > 4800){
				element.style.width = `${element.dataset.width}%`;
			}
			
		})

	});
});


// let val = document.getElementsByClassName("project-area-item");
// for(let i =0; i< val.length; i++){ 
//     val[i].addEventListener('mouseover', (event) => {
//         console.log(event)
//         val[i].classList.add('project-area-item-hover')
//     })
//     val[i].addEventListener('mouseout', (event) => {
//         val[i].classList.remove('project-area-item-hover')
//     })
// }





(function ($) {
    var counter = $('.counter');
	counter.counterUp({
		time: 2500,
		delay: 100
	});



		/*==========  testimonial  ==========*/
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
		console.log(swiper);
		/*==========  testimonial  ==========*/
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
    	/*========== Active Hover  ==========*/
	$(".project-area-item").hover(function () {
		$(".project-area-item").removeClass("project-area-item-hover");
		$(this).addClass("project-area-item-hover");
	});

	/*========== Active Hover  ==========*/
	$(".choose-ua-right-list-icon").hover(function () {
		$(".choose-ua-right-list-icon").removeClass("choose-ua-right-list-icon-hover");
		$(this).addClass("choose-ua-right-list-icon-hover");
	});

})(jQuery);