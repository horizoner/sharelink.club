$(function(){
	$("#content-table").hover(function(){
		$(".focus-show").stop(false,true).show("100");
	},function(){
		$(".focus-show").stop(false,true).hide("100");
	});

	$(".part-explain").hover(function(){
		$("#part-url-show").show();
	},function(){
		$("#part-url-show").hide();
	})
})