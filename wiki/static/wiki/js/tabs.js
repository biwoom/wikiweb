'use strict';

(function() {
  $(".nav-tabs > ul > li").filter(":first").addClass("active");
  
  var getval = $('#my_iframe').find('.wiki-article');
  $('.get_iframe').html(getval);
  
})();