var ToC =
  "<nav role='navigation' class='table-of-contents' id='target_nav'>" +
    "<p class='table-of-contents-title'>문서목차</p>" +
    "<ul class='section table-of-contents'>";

var newLine, el, title, link, tocclass;

$("h2,h3,h4,h5,h6").each(function(i) {

  el = $(this);
  title = el.text();
  link = "#" + el.attr("id");
  toc_class = "toc_" + el.get(0).tagName;
  a_id = "toc-title_" + i
  
  newLine =
    "<li class='" + toc_class + "'>" +
      "<a class='" + a_id + "' href='" + link + "' >" +
        title +
      "</a>" +
    "</li>";

  ToC += newLine;

});

ToC +=
   "</ul>" +
  "</nav>";

$(".toc_auto").prepend(ToC);
$(".toc_auto_mobile").prepend(ToC);


jQuery(document).ready(function () {
   
    var w_height = window.innerHeight;
    jQuery('.toc_box, .side_list_box').css('height', w_height-100)
    jQuery('.toc_auto, .side_list_auto').css('max-height', w_height-190);
    // jQuery('#my_iframe').attr("height", w_height-100);
    
    jQuery( window ).resize(function() {
      var w_height = window.innerHeight;
      jQuery('.toc_box, .side_list_box').css('height', w_height-100);
      jQuery('.toc_auto, .side_list_auto').css('max-height', w_height-190);
      // jQuery('#my_iframe').attr("height", w_height-100);
    });
    
    jQuery(window).scroll(function() {
        var sclTop = $(this).scrollTop();
        if (sclTop > 70)
        {
            $('.side_list_auto, .toc_auto').css('position', 'fixed').css('top', '55px');        
        }
        else 
        {jQuery('.side_list_auto, .toc_auto').css('position','absolute').css('top','0');}
    });
});


'use strict';

(function() {
  var body = document.body;
  var burgerMenu = document.getElementsByClassName('b-menu')[0];
  var burgerContain = document.getElementsByClassName('b-container')[0];
  var burgerNav = document.getElementsByClassName('b-nav')[0];

  burgerMenu.addEventListener('click', function toggleClasses() {
    [body, burgerContain, burgerNav].forEach(function (el) {
      el.classList.toggle('open');
    });
  }, false);
})();
