'use strict';

(function() {
  $(".nav-tabs > ul > li").filter(":first").addClass("active");
  
  $('#my_iframe').load(function(){
        var e = $('#my_iframe').contents().find('.wiki-article').html();
        $('.get_iframe').html(e);
        
        $('#my_iframe').css('display', 'none');
        
    });

})();
