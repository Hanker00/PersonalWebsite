
$(document).ready(function() {
	$(window).scroll(function() {
  	if($(document).scrollTop() > 10) {
    	$('#nav').addClass('shrink');
    }
    else {
    $('#nav').removeClass('shrink');
    }
  });
});

$(function() {
  $('.material-icons').click (function() {
    $('html, body').animate({scrollTop: $('div.journey').offset().top }, 'slow');
    return false;
  });
});

function toggleMenu(){
  var element = document.querySelector(".menu");
  element.classList.toggle("show");

  element = document.querySelector(".fade-layer");
  element.classList.toggle("fade");
}