(function() {
  
  var article_list_origin = $("#article_list_origin").html();
  
  // var reA = /[^a-zA-Z]/g;
  var reA = /[^가-힣a-zA-Z]/g;
  var reN = /[^0-9]/g;
  
  function sortAlphaNum(a,b) {
      var aA = $(a).text().toUpperCase().replace(reA, "");
      var bA = $(b).text().toUpperCase().replace(reA, "");
      if(aA === bA) {
          var aN = parseInt($(a).text().toUpperCase().replace(reN, ""), 10);
          var bN = parseInt($(b).text().toUpperCase().replace(reN, ""), 10);
          return aN === bN ? 0 : aN > bN ? 1 : -1;
      } else {
          return aA > bA ? 1 : -1;
      }
  }
  
  var my_lsit = $('#article_list_origin').children('li').get();
  my_lsit.reverse();
  my_lsit.sort(sortAlphaNum);
  
  $.each(my_lsit,function(index,row){ 
    $('#get-table-of-article-title').append(row);
  });
  $('li').filter(":contains('하위 문서 보기 »')").css("display", "none"); 
  $('li').filter(":contains('...그리고 더')").css("display", "none"); 
  $('#article_list_origin').html(article_list_origin);
  
})();
