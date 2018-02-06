$(function(){
    
    // var twoToneButton = document.querySelector('.twoToneButton');
    // var preloaderButton = document.querySelector('.preloader');
    // preloaderButton.classList.remove('preloader');
     
    // twoToneButton.addEventListener("click", function() {
    //     twoToneButton.innerHTML = "처리 중";
    //     twoToneButton.classList.add('spinning');
    //     preloaderButton.classList.add('preloader');
        
    //   setTimeout( 
    //         function  (){  
    //             twoToneButton.classList.remove('spinning');
    //             twoToneButton.innerHTML = "처리 완료";
    //             preloaderButton.classList.remove('preloader');
    //         }, 10000);
    // }, false);
    
    
    var twoToneButton = document.querySelector('.loading');
    var preloaderButton = document.querySelector('.status_1');
    var preloaderButton2 = document.querySelector('.preloader_1');
     
    twoToneButton.addEventListener("click", function() {
        preloaderButton.classList.remove('status_1');
        preloaderButton.classList.add('status');
        
        preloaderButton2.classList.remove('preloader_1');
        preloaderButton2.classList.add('preloader');
        
      setTimeout( 
            function  (){  
                preloaderButton.classList.remove('status');
                preloaderButton2.classList.remove('preloader');
            }, 4000);
    }, false);
});
