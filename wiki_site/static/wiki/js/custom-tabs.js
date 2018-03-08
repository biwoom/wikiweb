'use strict';

(function() {
  $(".nav-tabs > ul > li").filter(":first").addClass("active");
  
  $('#my_iframe_1').load(function(){
        var e = $('#my_iframe_1').contents().find('.wiki-article').html();
        $('.get_iframe_1').html(e);
        $('#my_iframe_1').css('display', 'none');
  });
  $('#my_iframe_2').load(function(){
        var e = $('#my_iframe_2').contents().find('.wiki-article').html();
        $('.get_iframe_2').html(e);
        $('#my_iframe_2').css('display', 'none');
  });  
  $('#my_iframe_3').load(function(){
        var e = $('#my_iframe_3').contents().find('.wiki-article').html();
        $('.get_iframe_3').html(e);
        $('#my_iframe_3').css('display', 'none');
  });
  $('#my_iframe_4').load(function(){
        var e = $('#my_iframe_4').contents().find('.wiki-article').html();
        $('.get_iframe_4').html(e);
        $('#my_iframe_4').css('display', 'none');
  });
  $('#my_iframe_5').load(function(){
        var e = $('#my_iframe_5').contents().find('.wiki-article').html();
        $('.get_iframe_5').html(e);
        $('#my_iframe_5').css('display', 'none');
  });
  $('#my_iframe_6').load(function(){
        var e = $('#my_iframe_6').contents().find('.wiki-article').html();
        $('.get_iframe_6').html(e);
        $('#my_iframe_6').css('display', 'none');
  });
  $('#my_iframe_7').load(function(){
        var e = $('#my_iframe_7').contents().find('.wiki-article').html();
        $('.get_iframe_7').html(e);
        $('#my_iframe_7').css('display', 'none');
  });
  $('#my_iframe_8').load(function(){
        var e = $('#my_iframe_8').contents().find('.wiki-article').html();
        $('.get_iframe_8').html(e);
        $('#my_iframe_8').css('display', 'none');
  });
  $('#my_iframe_9').load(function(){
        var e = $('#my_iframe_9').contents().find('.wiki-article').html();
        $('.get_iframe_9').html(e);
        $('#my_iframe_9').css('display', 'none');
  });
  $('#my_iframe_10').load(function(){
        var e = $('#my_iframe_10').contents().find('.wiki-article').html();
        $('.get_iframe_10').html(e);
        $('#my_iframe_10').css('display', 'none');
  });  
})();
