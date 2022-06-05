/*
Last modification: 06/05/2022
Created: 06/05/2022
Author Rodrigo Carmona Mendoza
Supported by lidisen.com
*/

/* Custom nav bar scrolled behavior */
$(window).scroll(function () {
  $('nav').toggleClass('scrolled', $(this).scrollTop() > 400);  if($(this).scrollTop() > 400){
    $('.title-name').addClass('new-color-title-name');
  }
  else{
    $('.title-name').removeClass('new-color-title-name');
  }
});