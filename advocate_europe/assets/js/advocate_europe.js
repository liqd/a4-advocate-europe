/* global $ */
$(document).ready(function () {
  $('.carousel').slick({
    centerMode: false,
    slidesToShow: 4,
    slidesToScroll: 4,
    dots: false,
    arrows: true,
    centerPadding: 30,
    mobileFirst: true,
    infinite: false,
    prevArrow: '<button class="slick-prev"><i class="fa fa-chevron-left"></i></button>',
    nextArrow: '<button class="slick-next"><i class="fa fa-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 0,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          arrows: false
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3
        }
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 4
        }
      }
    ]
  })

  $('.slider-xs').slick({
    centerMode: false,
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    centerPadding: 30,
    mobileFirst: true,
    infinite: false,
    responsive: [
      {
        breakpoint: 0,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 767,
        settings: 'unslick'
      }
    ]
  })
})
