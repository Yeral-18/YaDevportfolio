var isMobile = false;
var isDesktop = false;


$(window).on("load resize",function(e){

		
		
		//mobile detection
		if(Modernizr.mq('only all and (max-width: 767px)') ) {
			isMobile = true;
		}else{
			isMobile = false;
		}


		//tablette and mobile detection
		if(Modernizr.mq('only all and (max-width: 1024px)') ) {
			isDesktop = false;
		}else{
			isDesktop = true;
		}
        toTop(isMobile);
});


/*
|--------------------------------------------------------------------------
| DOCUMENT READY
|--------------------------------------------------------------------------
*/  
$(document).ready(function() {


/*
|--------------------------------------------------------------------------
| APPEAR
|--------------------------------------------------------------------------
*/
if($('.activateAppearAnimation').length){
	nekoAnimAppear();


	$('.reloadAnim').click(function (e) {

		$(this).parent().parent().find('img').removeClass().addClass('img-responsive');

		nekoAnimAppear();
		e.preventDefault();
	});
}


/*
|--------------------------------------------------------------------------
| REVOLUTION SLIDER
|--------------------------------------------------------------------------
*/ 
if($('#rsDemoWrapper').length){


    	$('.tp-banner').revolution(
                {
                    delay:12000,
                    startwidth:1920,
                    startheight:713,
                    hideThumbs:10,
					navigationType:"none",
                    fullWidth:"on",
                    forceFullWidth:"on"
                });

    	$('#rsDemoWrapper').css('visibility', 'visible');
    }


/*
|--------------------------------------------------------------------------
| OWL CAROUSEL
|--------------------------------------------------------------------------
*/ 
//funcion owl galeria
  var owl_slide = $("#owl-slide");
 
  owl_slide.owlCarousel({
      items : 4, //10 items above 1000px browser width
      itemsDesktop : [1000,3], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,2], // betweem 900px and 601px
      itemsTablet: [600,1], //2 items between 600 and 0
      itemsMobile : false, // itemsMobile disabled - inherit from itemsTablet option
	  pagination : false,
	  //Basic Speeds
      smartSpeed : 200,
      paginationSpeed : 800,
      rewindSpeed : 1000,
      //Autoplay
      autoPlay : 17000,
      stopOnHover : false,
  });
  
// Custom Navigation Events
    $(".owl-carousel-arrows .next").click(function() {
        owl_slide.trigger('owl.next');
    });
	
    $(".owl-carousel-arrows .prev").click(function() {
        owl_slide.trigger('owl.prev');
    });
	
	
	//funcion owl galeria
  var owl_home = $("#owl-home");
 
  owl_home.owlCarousel({
      items : 1, //10 items above 1000px browser width
      itemsDesktop : [1000,1], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,1], // betweem 900px and 601px
      itemsTablet: [600,1], //2 items between 600 and 0
      itemsMobile : false, // itemsMobile disabled - inherit from itemsTablet option
	  pagination : true,
	  //Basic Speeds
      smartSpeed : 200,
      paginationSpeed : 800,
      rewindSpeed : 1000,
      //Autoplay
      autoPlay : 17000,
      stopOnHover : false,
  });
  
// Custom Navigation Events
    $(".owl-home-arrows .next").click(function() {
        owl_home.trigger('owl.next');
    });
	
    $(".owl-home-arrows .prev").click(function() {
        owl_home.trigger('owl.prev');
    });
	
//funcion owl clientes

 //funcion owl clientes

  var owl_cliente = $("#owl-cliente");
 
  owl_cliente.owlCarousel({
      items :1, //10 items above 1000px browser width
      itemsDesktop : [1000,1], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,2], // betweem 900px and 601px
      itemsTablet: [600,1], //2 items between 600 and 0
      itemsMobile : false, // itemsMobile disabled - inherit from itemsTablet option	
      slideSpeed : 200,	  
	 //transitionStyle : "fadeOut",
      paginationSpeed : 800,
      rewindSpeed : 1000,
      //Autoplay	  
      autoPlay : true,
      stopOnHover : false,
  });
  
	
	//funcion owl clientes

  var owl_serviciosmovil = $("#owl-serviciosmovil");
 
  owl_serviciosmovil.owlCarousel({
      items :1, //10 items above 1000px browser width
      itemsDesktop : [1000,1], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,1], // betweem 900px and 601px
      itemsTablet: [600,1], //2 items between 600 and 0
      itemsMobile : false, // itemsMobile disabled - inherit from itemsTablet option	
      slideSpeed : 200,	  
	 //transitionStyle : "fadeOut",
      paginationSpeed : 800,
      rewindSpeed : 1000,
      //Autoplay	  
      autoPlay : true,
      stopOnHover : false,
  });
  
 //funcion owl clientes

  var owl_homemovil = $("#owl-homemovil");
 
  owl_homemovil.owlCarousel({
      items :1, //10 items above 1000px browser width
      itemsDesktop : [1000,1], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,1], // betweem 900px and 601px
      itemsTablet: [600,1], //2 items between 600 and 0
      itemsMobile : false, // itemsMobile disabled - inherit from itemsTablet option	
      slideSpeed : 200,	  
	 //transitionStyle : "fadeOut",
      paginationSpeed : 800,
      rewindSpeed : 1000,
      //Autoplay	  
      autoPlay : true,
      stopOnHover : false,
  });
  
	
	//SYNCL owlCarousel
  
  var sync1 = $("#sync1");
  var sync2 = $("#sync2");
 
  sync1.owlCarousel({
    singleItem : true,
    slideSpeed : 1000,
    navigation: false,
    pagination:false,
    afterAction : syncPosition,
    responsiveRefreshRate : 200,
  });
 
  sync2.owlCarousel({
    items : 8,
    itemsDesktop      : [1199,4],
    itemsDesktopSmall     : [979,3],
    itemsTablet       : [768,3],
    itemsMobile       : [479,2],
    pagination:false,
    responsiveRefreshRate : 100,
    afterInit : function(el){
      el.find(".owl-item").eq(0).addClass("synced");
    }
  });
 
  function syncPosition(el){
    var current = this.currentItem;
    $("#sync2")
      .find(".owl-item")
      .removeClass("synced")
      .eq(current)
      .addClass("synced")
    if($("#sync2").data("owlCarousel") !== undefined){
      center(current)
    }
  }
 
  $("#sync2").on("click", ".owl-item", function(e){
    e.preventDefault();
    var number = $(this).data("owlItem");
    sync1.trigger("owl.goTo",number);
  });
 
  function center(number){
    var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
    var num = number;
    var found = false;
    for(var i in sync2visible){
      if(num === sync2visible[i]){
        var found = true;
      }
    }
 
    if(found===false){
      if(num>sync2visible[sync2visible.length-1]){
        sync2.trigger("owl.goTo", num - sync2visible.length+2)
      }else{
        if(num - 1 === -1){
          num = 0;
        }
        sync2.trigger("owl.goTo", num);
      }
    } else if(num === sync2visible[sync2visible.length-1]){
      sync2.trigger("owl.goTo", sync2visible[1])
    } else if(num === sync2visible[0]){
      sync2.trigger("owl.goTo", num-1)
    }
    
  }

//END DOCUMENT READY   
});


/*
|--------------------------------------------------------------------------
| EVENTS TRIGGER AFTER ALL IMAGES ARE LOADED
|--------------------------------------------------------------------------
*/
$(window).load(function() {

"use strict";
    
    /*
    |--------------------------------------------------------------------------
    | PRELOADER
    |--------------------------------------------------------------------------
    */
    if($('#status').length){
        $('#status').fadeOut(); // will first fade out the loading animation
        $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
        $('body').delay(350).css({'overflow':'visible'});
    }



//END WINDOW LOAD
});


/*
|--------------------------------------------------------------------------
| FUNCTIONS
|--------------------------------------------------------------------------
*/

/* Appear function */
function nekoAnimAppear(){
	$("[data-nekoAnim]").each(function() {

		var $this = $(this);

		$this.addClass("nekoAnim-invisible");
		
		if($(window).width() > 767) {
			
			$this.appear(function() {

				var delay = ($this.data("nekodelay") ? $this.data("nekodelay") : 1);
				if(delay > 1) $this.css("animation-delay", delay + "ms");

				$this.addClass("nekoAnim-animated");
				$this.addClass('nekoAnim-'+$this.data("nekoanim"));

				setTimeout(function() {
					$this.addClass("nekoAnim-visible");
				}, delay);

			}, {accX: 0, accY: -150});

		} else {
			$this.addClass("nekoAnim-visible");
		}
	});
}



/* scroll function */
//jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

//jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});


/* TO TOP BUTTON */

function toTop(mobile){
    
   if(mobile == false){

        if(!$('#nekoToTop').length)
        $('body').append('<a href="#" id="nekoToTop"><i class="fa fa-arrow-up"></i></a>');

        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('#nekoToTop').slideDown('fast');
            } else {
                $('#nekoToTop').slideUp('fast');
            }
        });

        $('#nekoToTop').click(function (e) {
            e.preventDefault();
            $("html, body").animate({
                scrollTop: 0
            }, 800, 'easeInOutCirc');
            
        });
   }else{

        if($('#nekoToTop').length)
        $('#nekoToTop').remove();

    }

}


