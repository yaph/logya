$(function(){
  $('.nav a[href="'+document.location.pathname+'"]').parent('li').attr('class', 'active');
});