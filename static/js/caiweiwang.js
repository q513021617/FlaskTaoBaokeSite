$(function(){
	var sWidth = $("#focus").width(); //获取焦点图的宽度（显示面积）  
    var len = $("#focus ul li").length; //获取焦点图个数  
    var index = 0;  
    var picTimer; 
	$('[data-toggle="tooltip"]').tooltip()
	$('[data-toggle="popover"]').popover()

	$("#R1 a").mouseenter(function(){
		$(this).addClass("active");
	}).mouseleave(function(){
    //鼠标移出
 	$(this).removeClass("active");
});


//百度分享
window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{},"image":{"viewList":["qzone","tsina","tqq","renren","weixin"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","tsina","tqq","renren","weixin"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus();
});





//选择器 导航条鼠标效果
	$("#IT li").mouseenter(function(){
		$(this).addClass("active");
	}).mouseleave(function(){
    //鼠标移出
 	$(this).removeClass("active");
});

//选择器 分页鼠标效果
	$("#FY ul li").mouseenter(function(){
		$(this).addClass("active");
	}).mouseleave(function(){
    //鼠标移出
 	$(this).removeClass("active");
});

	$('#myModal #model1_btn').onclick(function (){
    if( $("#myModal form #userName").val() == "" || $("#myModal form #passWord").val() == "")
    {
        alert("用户名！");
        return false;
    }});

	$('myModal2 #registerBtn').onclick(function (){
    if( $("#myModal form #userName").val() == "" || $("#myModal form #passWord").val() == "")
    {
        alert("注册请填好用户名和密码");
        return false;
    }});




	//以下代码添加数字按钮和按钮后的半透明条，还有上一页、下一页两个按钮  
    var btn = "<div class='btn'>";  
    for(var i=0; i < len; i++) {btn += "<span></span>";}  
    btn += "</div>";  
    btn +="<div class='preNext pre'></div>"+"<div class='preNext next'></div>"+  
              "<span class='hidden left'></span>"+"<span class='hidden right'></span>";  
    $("#focus").append(btn);  


 //为小按钮添加鼠标滑入事件，以显示相应的内容  
    $("#focus div.btn span").css("opacity",0.4).mouseenter(function() {  
        index = $("#focus div.btn span").index(this);  
        showPics(index);  
    });  



 //图片鼠标划过  
    $('#focus span.left').hover(function(){  
        $('#focus div.pre').animate({opacity:'0.5'},500);  
    },function(){  
        $('#focus div.pre').animate({opacity:'0'},500);  
    });  
    $('#focus span.right').hover(function(){  
        $('#focus div.next').animate({opacity:'0.5'},500);  
    },function(){  
        $('#focus div.next').animate({opacity:'0'},500);  
    }); 


    //上一页按钮  
    $("#focus span.left").click(function() {  
        if(index == -1) {index = len - 1;}  
        showPics(index);  
        index--;  
    }); 



     //下一页按钮  
    $("#focus span.right").click(function() {  
        if(index == len){  
            index = 0;  
            showFirstPic();  
        }else{  
            showPics(index);  
        }  
        index ++;  
    }); 


//本例为左右滚动，即所有li元素都是在同一排向左浮动，所以这里需要计算出外围ul元素的宽度  
    $("#focus ul").css("width",sWidth * (len+1));  

//鼠标滑上焦点图时停止自动播放，滑出时开始自动播放 
$("#focus").hover(function() {  
        clearInterval(picTimer);  
    },function() {  
        picTimer = setInterval(function() {  
            if(index == len) { //如果索引值等于li元素个数，说明最后一张图播放完毕，接下来要显示第一张图，即调用showFirPic()，然后将索引值清零  
                index = 0;  
                showFirstPic();  
            } else { //如果索引值不等于li元素个数，按普通状态切换，调用showPics()  
                showPics(index);  
            }  
            index++;  
        },2000); //此2000代表自动播放的间隔，单位：毫秒  
    });  


//显示图片函数，根据接收的index值显示相应的内容  
    function showPics(index) { //普通切换  
        var nowLeft = -index*sWidth; //根据index值计算ul元素的left值  
        $("#focus ul").stop(true,false).animate({"left":nowLeft},500); //通过animate()调整ul元素滚动到计算出的position  
        $("#focus div.btn span").animate({"opacity":"0.4"},300).eq(index).animate({"opacity":"1"},100); //为当前的按钮切换到选中的效果  
    }  


    function showFirstPic() { //最后一张图自动切换到第一张图时专用  
        $("#myCarousel ol").append($("#myCarousel ol li:first").clone());//为了达到从最右边到最左边还是往左移动效果，而不是往右移动
        var nowLeft = -len*sWidth; //通过li元素个数计算ul元素的left值，也就是最后一个li元素的右边  
        $("#myCarousel ol").stop(true,false).animate({"left":nowLeft},500,function() {
            //通过callback，在动画结束后把ul元素重新定位到起点，然后删除最后一个复制过去的元素  
            $("#myCarousel ol").css("left","0");
            $("#myCarousel ol li:last").remove();
        });   
        $("#myCarousel div.btn span").animate({"opacity":"0.4"},300).eq(index).animate({"opacity":"1"},100); //为当前的按钮切换到选中的效果
    } 

});