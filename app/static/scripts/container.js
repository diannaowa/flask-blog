/*
container
*/

$(function(){
	//stop container
	$("a.stop_c").bind("click",function(){
		var container_id = $(this).attr("data");

		$.ajax({
			url:"/docker/stop_container/"+container_id,
			type:"get",
			dataType:"json",
			success:function(data){
				if(data.state == true){
					alert("操作成功");
				}else{
					alert("操作失败");
				}
			}
		});
	});


	//run container
	$("a.run_c").bind("click",function(){
		var container_id = $(this).attr("data");

		$.ajax({
			url:"/docker/start_container/"+container_id,
			type:"get",
			dataType:"json",
			success:function(data){
				if(data.state == true){
					alert("操作成功");
				}else{
					alert("操作失败");
				}
			}
		});
	});


	//remove container
	$("a.remove_c").bind("click",function(){
		var container_id = $(this).attr("data");

		$.ajax({
			url:"/docker/remove_container/"+container_id,
			type:"get",
			dataType:"json",
			success:function(data){
				if(data.state == true){
					alert("操作成功");
				}else{
					alert("操作失败");
				}
			}
		});
	})


})