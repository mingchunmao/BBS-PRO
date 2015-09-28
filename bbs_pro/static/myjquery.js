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
})
