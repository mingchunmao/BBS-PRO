$(function(){
	$("#comment_login").bind('click',function(){
		$('#loginform').css('display','block');
	});

	$('#logint').bind('click',function(){
		$.ajax({
			url:'/acc_login/',
			data:{username:$("#username").val(),password:$("#password").val()},
			type:'post',
			success: function() {
				location.reload();
			}
		})
	});
	$('#chat-send').bind('click',function(){		
		$.ajax({
			url : '/chat_sub/',
			data : {content: $("#chat-content").val()},
			type : 'post',
			success: function(){				
				/*$.ajax({
		            url: '/chat_pub/',
		            type: 'post', 
		            success: function(data){
		                $('.chat-window').append(data);
		            }
		        })*/
			}
		})
	});
	/*setInterval("startRequest()",3000);
    */
  

/*	$("#menuactive li").each(function(){
		$(this).click(function(){			
			$("#menuactive .active").removeClass('active');
			$(this).addClass('active');
		});
	});*/
})
/*function startRequest() {
      	$.ajax({
      		alert('haha');
            url: '/chat_pub/',
            type: 'post', 
            success: function(data){
                $('.chat-window').append(data);
            }
        })
      }
*/