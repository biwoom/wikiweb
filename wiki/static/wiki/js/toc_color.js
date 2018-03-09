// 화면스크롤에 따른 목차 리스트 강조 표시
jQuery(document).ready(function () {
    

var positions = [],
    
    // 문서 세로 위치값 = get_bottom_off_content
    get_bottom_off_content = function() {
      var $content = $('.wiki-article'),
          offset   = $content.offset();
      
      return $content.outerHeight() + offset.top;
    },
    // 문서 내부 모든 header 위치값을 담은 리스트 positions 반환
    get_positions = function() {
      $('.wiki-article').find("h2,h3,h4,h5,h6").each(function( i ){
        offset = $(this).offset();
        positions[ 'title_' + i ] = offset.top - 130;
      });
      return positions;
    },
    
    set_toc_reading = function() {
      // 문서가 보여지는 화면으로 보여지는 현재 세로 위치값
      var st    = $(document).scrollTop(),
          count = 0;
      
      for (var k in positions) {
        var n        = parseInt( k.replace('title_', '') );
            // 문서의 현재 헤더 아래에 헤더가 더 있다면 True 반환
            has_next = typeof positions['title_' + ( n + 1 ) ] !== 'undefined',
            // 문서의 아래에 헤더가 있지만 보이지 않는다면 True 
            not_next = has_next && st < positions['title_' + ( n + 1 ) ] ? true : false;
        
        // 목차 css 수정
        if ( st >= positions[ k ] && not_next && has_next ) {
          $( '.toc-' + k ).addClass('toc-reading');
        } else if ( st >= positions[ k ] && ! not_next && has_next ) {
          
          $( '.toc-' + k ).removeClass('toc-reading');
        } else if ( st >= positions[ k ] && ! not_next && ! has_next ) {
          $( '.toc-' + k ).addClass('toc-reading');
        }
        
        if ( st >= positions[ k ] ) {
          $( '.toc-' + k ).addClass('toc-already-read');
        } else {
          $( '.toc-' + k ).removeClass('toc-already-read');
        }
        
        if ( st < positions[ k ] ) {
          $( '.toc-' + k ).removeClass('toc-already-read toc-reading');
        }
        
        count++;
      }
    };
    
    // first definition of positions
    get_positions();
    
    // on resize, re-calc positions
    $(window).on('resize', function(){
      get_positions();
    });
    
    $(document).on('scroll', function(){
      set_toc_reading();
    });

});