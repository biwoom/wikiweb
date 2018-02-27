var agent = navigator.userAgent.toLowerCase();

if ( (navigator.appName == 'Netscape' && navigator.userAgent.search('Trident') != -1) || (agent.indexOf("msie") != -1) || ( agent.search( "edge/" ) != -1 ) ){

    if ( confirm("현재 사용자님의 브라우저는 '인터넷익스플로러' 또는 '엣지'입니다. 본 싸이트는 크롬, 사파리, 파이어폭스 브라우저에 최적화 되어 있습니다. 새로운 브라우저로 안정된 싸이트 이용을 하실 수 있습니다. \n\n 확인 : 크롬설치 페이지 이동\n \n 취소 : 창닫기") ){
         location.href="https://www.google.co.kr/chrome/" }
}else {
//   alert("인터넷 익스플로러 브라우저가 아닙니다.");
}