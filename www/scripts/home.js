$(function(){
	//显示影藏输入
	$("#content-table").hover(function(){
		$(".focus-show").stop(false,true).show("100");
	},function(){
		$(".focus-show").stop(false,true).hide("100");
	});

	//显示图片
	$(".part-explain").hover(function(){
		//String.prototype.Right = function(i) { //为String对象增加一个Right方法
        //return this.slice(this.length - i,this.length);}; //返回值为 以“该字符串长度减i”为起始 到 该字符串末尾 的截取字符串
		//var urlstr = $(this).attr("href").Right(8);
		if (!$(this).attr("imgsrc")) {
			$.post(,{},function(data){
				if(data.success) {
					$("#part-url-show").find("img").attr("src","data:image/gif;base64,"+imgurlbase64);//新添加的图片
				}else{
					alert("获取图片失败！");
				}
			})
		} else {
			$("#part-url-show").find("img").attr("src","images/"+imgurl);//以前的图片	
		}
		//$("#part-url-show").find("img").attr("src","data:image/gif;base64,"+imgurlbase64);//新添加的图片
	    //$("#part-url-show").show();
	    //$("#part-url-show").show();
	},function(){
		$("#part-url-show").hide();
	})

	$(".submit").click(function(){
	    {
	    	//提交验证
	    	var strRegex = '^((https|http|ftp|rtsp|mms)?://)' 
				+ '?(([0-9a-z_!~*\'().&=+$%-]+: )?[0-9a-z_!~*\'().&=+$%-]+@)?' //ftp的user@ 
				+ '(([0-9]{1,3}.){3}[0-9]{1,3}' // IP形式的URL- 199.194.52.184 
				+ '|' // 允许IP和DOMAIN（域名） 
				+ '([0-9a-z_!~*\'()-]+.)*' // 域名- www. 
				+ '([0-9a-z][0-9a-z-]{0,61})?[0-9a-z].' // 二级域名 
				+ '[a-z]{2,6})' // first level domain- .com or .museum 
				+ '(:[0-9]{1,4})?' // 端口- :80 
				+ '((/?)|' // a slash isn't required if there is no file name 
				+ '(/[0-9a-z_!~*\'().;?:@&=+$,%#-]+)+/?)$'; 
			var re = new RegExp(strRegex); 
			var url = $("#url").val();
			var title = $("#title").val().length;
			if (re.test(url)) {
				if (title == 0) {
					alert("请输入题目")
					return false;
				};
			}else{
				alert("请输入正确的URL");
			    return false;
			}
			 
            //发送验证
	        $.ajax({
	        type:"POST",
	        url:"",
	        dataType:"json",
	        data:$("#url").val(),
	        beforeSend:function(XMLHttpRequest)
	            {
	                $("#dia-log").show();
	            },
	        success:function(data)
	            {  
	                if (data.failure) {
	                    $("#dia-log").find("h1").text("url格式错误!");
	                    $("#dia-log").find("img").hide();
	                    $("#dia-log").hide(2000);
	                    return false;
	                };
	                if (data.success) {
	                	$("#dia-log").find("h1").text("已提交");
	                    $("#dia-log").find("img").hide();
	                    $("#dia-log").hide(2000);
	                    var firpart = '<tbody><tr><td align="right" valign="top" class="part-number">1.</td><td><center><a id="part-up" href="javascript:void(0)"><div class="votearrow" title="upvote"></div></a><span class="part-down"></span></center></td><td class="title"><a imgsrc="" href="'
		                    +url+
		                    '"class="part-explain" target="_blank">'
		                    +title+
		                    '</a><span class="part-comhead">('
		                    +url+
		                    ')</span></td></tr><tr><td colspan="2"></td><td class="part-subtext"><span class="part-score">59 points</span>by<a href="#">jseliger</a>1 hour ago|<a href="#">13 comments</a></td></tr><tr style="height:20px"></tr></tbody>';
		                };
		                $(".cont-part").prepend(firpart);
		                $(".cont-part").find("tbody").eq(0).addClass("mark");
	            },
	        complete:function(XMLHttpRequest,textStatus)
	            {
	            	$("#dia-log").find("h1").text("正在验证URL,请稍等...");
	                $("#dia-log").find("img").show();
	            },
	        error:function()
	           {
	                //错误处理
	           }
            });
        };
	});


    $(window).scroll(function (){
	    if ($(window).scrollTop()==$(document).height()-$(window).height()){
	        $.ajax({
		        type:"post",
		        data:$("tbody:last").find(".part-number").text().substring(0,$("tbody:last").find(".part-number").text().length-1),
		        url:"",
		        dataType:"json",
		        success:function(data){
		        	var i = 0;
		        	var laspart = '<tbody><tr><td align="right" valign="top" class="part-number">1.</td><td><center><a id="part-up" href="javascript:void(0)"><div class="votearrow" title="upvote"></div></a> <span class="part-down"></span></center></td><td class="title"><a href="http://www.baidu.com" class="part-explain" target="_blank" imgsrc="">dsdmsfmmgm</a> <span class="part-comhead">(pasadenastarnews.com)</span></td></tr><tr><td colspan="2"></td><td class="part-subtext"><span class="part-score">59 points</span> by <a href="#">jseliger</a> 1 hour ago | <a href="#">13 comments</a></td></tr><tr style="height:20px"></tr></tbody>';
                    for (var i = 0; i < 15; i++) {
                    		if (i < data.content.length) {
	                    	$(".cont-part").append(laspart);
	                    	$("tbody:last").find(".part-explain").text(data.content[i].title);
	                    	$("tbody:last").find(".part-explain").attr("href",data.content[i].urlpart);
							$("tbody:last").find(".part-comhead").text(data.content[i].urlpart);
	                    };
                    };	
                    	
		        },
		        beforeSend: function() {
		        },
		        error: function(data) {
                }

		    });
	    }

	});
})