(function ($) {
    "use strict";
    /*----------------------------
    tooltip
------------------------------ */
    const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
    );
    const tooltipList = [...tooltipTriggerList].map(
        (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
    );

    /*----------------------------
    jQuery MeanMenu
------------------------------ */
    jQuery("nav#dropdown").meanmenu({
        meanScreenWidth: "992",
    });

    /*----------------------------
    wow js active
------------------------------ */
    new WOW().init();

    /*----------------------------
    owl active
------------------------------ */
    $(".tab-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: false,
        items: 1,
        margin: 30,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        singleItem: true,
    });
    /*----------------------------
    product-carousel
------------------------------ */
    $(".product-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 4,
        margin: 30,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        responsive: {
            0: {
                items: 1,
            },
            576: {
                items: 2,
            },
            768: {
                items: 3,
            },
            992: {
                items: 4,
            },
        },
    });

    /*----------------------------
    banner-2-carousel
------------------------------ */
    $(".banner-2-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 1,
        margin: 30,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        singleItem: true,
    });

    /*----------------------------
    news-carousel
------------------------------ */
    $(".news-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 1,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        singleItem: true,
    });

    /*----------------------------
    news-carousel
------------------------------ */
    $(".newss-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 3,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        itemsDesktop: [1199, 4],
        itemsDesktopSmall: [980, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
    });

    /*----------------------------
   most-view-carousel
------------------------------ */
    $(".most-view-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 2,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        itemsDesktop: [1199, 2],
        itemsDesktopSmall: [980, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
    });

    /*----------------------------
   most-view-carousel-2
------------------------------ */
    $(".most-view-carousel-2").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 4,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        itemsDesktop: [1199, 4],
        itemsDesktopSmall: [980, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
    });

    /*----------------------------
   brand-carousel
------------------------------ */
    $(".brand-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 6,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        responsive: {
            0: {
                items: 2,
            },
            576: {
                items: 2,
            },
            768: {
                items: 3,
            },
            992: {
                items: 4,
            },
            1200: {
                items: 6,
            },
        },
    });
    /*----------------------------
   testimonial-carousel
------------------------------ */
    $(".testimonial-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 1,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        singleItem: true,
    });
    /*----------------------------
   feature-carousel
------------------------------ */
    $(".feature-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 3,
        margin: 30,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        responsive: {
            0: {
                items: 1,
            },
            576: {
                items: 2,
            },
            768: {
                items: 3,
            },
            992: {
                items: 3,
            },
        },
    });
    /*----------------------------
   best-seller-carousel
------------------------------ */
    $(".best-seller-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 1,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        singleItem: true,
    });
    /*----------------------------
   related-product-carousel
------------------------------ */
    $(".related-product-carousel").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: false,
        nav: true,
        items: 3,
        margin: 30,
        /* transitionStyle : "fade", */ /* [This code for animation ] */
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>",
        ],
        responsive: {
            0: {
                items: 1,
            },
            576: {
                items: 2,
            },
            768: {
                items: 3,
            },
            992: {
                items: 3,
            },
        },
    });

    /*---------------------
	 countdown
	--------------------- */
    $("[data-countdown]").each(function () {
        var $this = $(this),
            finalDate = $(this).data("countdown");
        $this.countdown(finalDate, function (event) {
            $this.html(
                event.strftime(
                    '<span class="cdown days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hour</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>Min</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>Sec</p></span>'
                )
            );
        });
    });

    /*----------------------------
 price-slider active
------------------------------ */
    $("#slider-range").slider({
        range: true,
        min: 80,
        max: 2000,
        values: [80, 2000],
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        },
    });
    $("#amount").val(
        "$" +
            $("#slider-range").slider("values", 0) +
            " - $" +
            $("#slider-range").slider("values", 1)
    );

    /*--------------------------
 scrollUp
---------------------------- */
    $.scrollUp({
        scrollText: '<img src="img/scroll_top/scroll-to-top.png"/>',
        easingType: "linear",
        scrollSpeed: 900,
        animation: "fade",
    });
    /*---------------------
	 elevateZoom
--------------------- */
    $(".first-img").elevateZoom();

    /*-------------------------
  showcoupon toggle function
--------------------------*/
    $("#new-address").on("click", function () {
        $("#new-address-open").slideToggle(900);
    });
})(jQuery);
