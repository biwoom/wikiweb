$(function() {
     function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
     }
     var csrftoken = getCookie('csrftoken'); 
    
     $('.button_save').click(function() {
            var dataURL = signaturePad.toDataURL();
            var donor_name = document.getElementById('id_name').value;
            var donor_email = document.getElementById('id_email').value;
            dataURL = dataURL+','+donor_name+','+donor_email
            // dataURL = dataURL+','+donor_email
            $.ajax({
                type: 'POST',
                url: '/regular_donation/',
                data: dataURL,
                contentType: 'text',
                
                // dataType: 'json',
                // contentType: 'application/json; charset=utf-8',
                // data: JSON.stringify({'dataURL' : dataURL, 'donor_name' : donor_name}),
                
                headers: {'X-CSRFToken': csrftoken},
                // contentType: 'application/json',
                success: function(response){
                    console.log('Success! // ' + 'response: ' + response);
                },
                error: function(request, status, error){
                    console.log('Fail! // ' + 'error :' + error.message);
              },
            });
     });
    
});