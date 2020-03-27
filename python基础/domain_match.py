#coding:utf8
html = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="http://xqctk.jtys.sz.gov.cn/templates/default/images/favicon.ico" />
<title>深圳小汽车增量调控管理信息系统</title>
<link href="http://xqctk.jtys.sz.gov.cn/templates/default/css/style.css" rel="stylesheet" type="text/css" />
<link href="http://xqctk.jtys.sz.gov.cn/templates/default/css/public.css" rel="stylesheet" type="text/css" />
<script type='text/javascript' src="http://xqctk.jtys.sz.gov.cn/templates/default/js/jquery/dropdown.js"></script>
<script type='text/javascript' src="http://xqctk.jtys.sz.gov.cn/templates/default/js/jquery/jquery.js"></script>
<script type='text/javascript' src="http://xqctk.jtys.sz.gov.cn/templates/default/js/jquery/jquery.jsonp.js"></script>
<script type='text/javascript' src="http://xqctk.jtys.sz.gov.cn/templates/default/js/jquery/base64.js"></script>
<script type='text/javascript' src="http://xqctk.jtys.sz.gov.cn/templates/default/js/jquery/aes.js"></script>
<script type='text/javascript'>
var base64 = new Base64();
var loc = document.location.href;
if(loc.indexOf("message") > 0){
	var hh = loc.substring(loc.indexOf("message"));
	if(hh.indexOf("&") > 0)
		hh = hh.substring(8,hh.indexOf("&"));
	else
		hh = hh.substring(8);
    
	alert(base64.decode(hh));
	window.location.search="";
}
var validCodeCount=0;
function getValidCode(){
	validCodeCount++;
	if(validCodeCount>20){
		alert("切换验证码太频繁了")
		return;
	}
    $("#incrementGetValidCodeImg").html("<a href='#none'><img style='width:75px;height:25px;' src='http://apply.jtys.sz.gov.cn/apply/app/validCodeImage?ee="+validCodeCount+"' /></a>");
    $("#renewGetValidCodeImg").html("<a href='#none'><img style='width:75px;height:25px;' src='http://apply.jtys.sz.gov.cn/apply/app/validCodeImage?ee="+validCodeCount+"' /></a>");
}

$(function(){
	$("#div_jtlc").hide();
	$("#renewTable").hide();
    $("#dh").on("mouseover",function(){
		$("#nav_ul").show();
		$("#nav_div").addClass("nav_nr_fudong_yca").removeClass("nav_nr_fudong");
	}).on("mouseout",function(){
		$("#nav_ul").hide();
		$("#nav_div").removeClass("nav_nr_fudong_yca").addClass("nav_nr_fudong");
	});
    $("#div_sblc").on("mouseover",function(){
    	$("#div_jtlc").show();
	}).on("mouseout",function(){
		$("#div_jtlc").hide();
	});
    $(".zczxClose").live("click",function(){
        $("#zczx .question").hide();
	
	});
    /*$.jsonp({
        url:"https://apply.jtys.sz.gov.cn/apply/app/zczx/index.html",
        callback:"mycallback",                          
        success:function(data){
		var ul = $("<ul></ul>");
        	$("#zczx").empty().append(ul);	
        	$.each(data,function(i,n){
			
			var li=$("<li></li>");
			ul.append(li);
			var a=$("<a>",{
				href:"#none",
				html:n.name+"："+n.question,
				click:function(){
					$("#zczx .question").hide();
					//$(this).parent().parent().next().show();
					$("#question"+i).show();	
				}
			})			
			li.append(a);
        	var question=$("<div>",{"class":"question","id":"question"+i});
        	$("#zczx").append(question);
		question.append($("<span style='float:right'><a class='zczxClose'  ><img alt='关闭' src=\"http://xqctk.jtys.sz.gov.cn/templates/default/images/an_close.png\" /></a></span>"));
        	question.append($("<span>",{
        		html:"“"+n.name+"”的问题 （"+n.questionTime+"）："
        	}));
        	question.append($("<div>",{
        		html:n.question
        		}));
        	question.append($("<span>",{
        		html:"问题回复 （"+n.answerTime+"）："
        		}));
        	question.append($("<div>",{html:n.answer.replace("\\n","<br>")}));
        	});
        	
        },
        error:function(d,msg,t){
               // alert("请稍候重试");
        }
	});*/
	
	$(document).click(function(e){
		if($(e.target).parents("#zczx").size()==0){
			$("#zczx .question").hide();
		}else if($(e.target).parents(".question").size()==0&&$(e.target).is("a")==false){
			$("#zczx .question").hide();
		}
	});
	var $incrementLi = $("#incrementLi"),
		$renewLi = $("#renewLi"),
		$incrementForm = $("#incrementForm"),
		$incrementCodeOption = $("#incrementCodeOption"),
		$incrementMobileOption = $("#incrementMobileOption"),
		$incrementForgetPasswd = $("#incrementForgetPasswd"),
		$incrementApply = $("#incrementApply"),
		$renewForm = $("#renewForm"),
		$renewForgetPasswd = $("#renewForgetPasswd"),
		$renewRegister = $("#renewRegister"),
		$myLogin = $("#myLogin");
	$incrementLi.on("click",function(){
		$("#incrementLi").addClass("main_login_qh_now").removeClass("main_login_qh_taba");
		$("#renewLi").addClass("main_login_qh_tabb").removeClass("main_login_qh_noe");
		$("#incrementTable").show();
		$("#renewTable").hide();
	});
	$renewLi.on("click",function(){
		$("#incrementLi").addClass("main_login_qh_taba").removeClass("main_login_qh_now");
		$("#renewLi").addClass("main_login_qh_noe").removeClass("main_login_qh_tabb");
		$("#incrementTable").hide();
		$("#renewTable").show();
	});
	$("#incrementLoginButton").on("click",function(){
		var loginCode = $("#incrementLoginCode").val();
		var loginType = $("#select > option:selected");
		if($.trim(loginCode) == ''){
			alert(loginType.text()+"不能为空");
			return false;
		}
		var pw=$("#incrementPassword").val();
		if($.trim(pw)===''){
			alert('密码不能为空');
			return false;
		}
		var vc=$("#incrementValidCode").val();
		if($.trim(vc)==''){
			alert('验证码不能为空');
			return false;
		}
		if(vc.length!=4){
			alert('验证码错误');
			return false;
		}
		$("#incrementPwd").val(checkParameter(pw));
		$incrementForm.trigger("submit");	
		return false;
	});
	$("#renewLoginButton").on("click",function(){
		var loginCode = $("#renewLoginCode").val();
		if($.trim(loginCode) == ''){
			alert("手机号码不能为空");
			return false;
		}
		var pw=$("#renewPassword").val();
		if($.trim(pw)===''){
			alert('密码不能为空');
			return false;
		}
		var vc=$("#renewValidCode").val();
		if($.trim(vc)==''){
			alert('验证码不能为空');
			return false;
		}
		if(vc.length!=4||$("#checkRenewCode").hasClass("falseCode")){
			alert('验证码错误');
			return false;
		}
		$("#renewPwd").val(checkParameter(pw));
		$renewForm.trigger("submit");	
		return false;
	});
	///
	$("#incrementValidCode").bind('input propertychange',  function(){
		var code = $(this).val();
		if(code.length!=4){
			$("#checkIncrementCode").html("");
		}else{
			$.jsonp({
				url:"https://apply.jtys.sz.gov.cn/apply/app/check/validCode",
				data:{"validCode":code},
				callback:"myCallBack",
				success: function(data){
					if(data.result=="true"){
						$("#checkIncrementCode").html('<img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/note_yes.png" />');
					}
					else{
						$("#checkIncrementCode").html('<img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/note_no.png" />'); 
						getValidCode();
					}
				}
			});
		}
		
	});
	$("#renewValidCode").bind('input propertychange',  function(){
		var code = $(this).val();
		if(code.length!=4){
			$("#checkRenewCode").html("");
		}else{
			$.jsonp({
				url:"https://apply.jtys.sz.gov.cn/apply/app/check/validCode",
				data:{"validCode":code},
				callback:"myCallBack",
				success: function(data){
					if(data.result=="true"){
						$("#checkRenewCode").html('<img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/note_yes.png" />');
					}
					else{
						$("#checkRenewCode").html('<img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/note_no.png" />'); 
						getValidCode();
					}
				}
			});
		}
	
		
	});
	
	$("#select").on("change",function(){
		
		if( $("input[name='incrementSelect']:checked").val()!='GR'&&$("#select").val()=='LONGCODE'&&$incrementCodeOption.text()=="证件号码"){
			$("#incrementLoginCode").attr("placeholder","统一社会信用代码（机构代码）");
		}
		else{
			$("#incrementLoginCode").attr("placeholder","");
		}
	});
	$(".incrementSelect").on("change",function(){
		var incrementRadio = $("input[name='incrementSelect']:checked").val();
		$incrementCodeOption.attr("checked",false);
		
		switch(incrementRadio){
		case "GR":
			$incrementForm.attr("action","https://apply.jtys.sz.gov.cn/apply/app/increment/person/login");
			$incrementCodeOption.text("申请编码");
			$incrementForgetPasswd.attr("href","http://apply.jtys.sz.gov.cn/apply/app/increment/person/forget/passwd");
			$incrementApply.attr("href","https://apply.jtys.sz.gov.cn/apply/app/increment/ballot/affair");
			break;
		case "QY":
			$incrementForm.attr("action","https://apply.jtys.sz.gov.cn/apply/app/increment/enterprise/login");
			$incrementCodeOption.text("证件号码");
			$incrementForgetPasswd.attr("href","http://apply.jtys.sz.gov.cn/apply/app/increment/enterprise/forget/passwd");
			$incrementApply.attr("href"," https://apply.jtys.sz.gov.cn/apply/app/increment/ballot/affair");
			break;
		case "ST":
			$incrementForm.attr("action","https://apply.jtys.sz.gov.cn/apply/app/increment/org/login");
			$incrementCodeOption.text("证件号码");
			$incrementForgetPasswd.attr("href","http://apply.jtys.sz.gov.cn/apply/app/increment/org/forget/passwd");
			$incrementApply.attr("href"," https://apply.jtys.sz.gov.cn/apply/app/increment/ballot/affair");
			break;
		default:
			break;
		}
		if( $("input[name='incrementSelect']:checked").val()!='GR'&&$("#select").val()=='LONGCODE'&&$incrementCodeOption.text()=="证件号码"){
			$("#incrementLoginCode").attr("placeholder","统一社会信用代码（机构代码）");
		}
		else{
			$("#incrementLoginCode").attr("placeholder","");
		}
	});	
	$(".renewSelect").on("change",function(){
		var renewRadio = $("input[name='renewSelect']:checked").val();
		switch(renewRadio){
		case "GR":
			$renewForm.attr("action","https://apply.jtys.sz.gov.cn/apply/app/renew/person/login");
			$renewForgetPasswd.attr("href","http://apply.jtys.sz.gov.cn/apply/app/renew/person/forget/passwd");
			$renewRegister.attr("href"," https://apply.jtys.sz.gov.cn/apply/app/renew/person/affair");
			break;
		case "DW":
			$renewForm.attr("action","https://apply.jtys.sz.gov.cn/apply/app/renew/unit/login");
			$renewForgetPasswd.attr("href","http://apply.jtys.sz.gov.cn/apply/app/renew/unit/forget/passwd");
			$renewRegister.attr("href"," https://apply.jtys.sz.gov.cn/apply/app/renew/unit/affair");
			break;
		default:
			break;
		}
	});
	
	var count=0;
	if(count < 1){
		getValidCode();
		count++;
	}
	
});
function isNew(PubDate)  
	{   
	
		var currentDate = new Date();
	    var currentMonth = currentDate.getMonth()+1;
	    var currentDay = currentDate.getDate();
	    var currentYear = currentDate.getFullYear();  
	  
	    var pubMonth = PubDate.substring(5,PubDate.lastIndexOf ('-'));  
	    var pubDay = PubDate.substring(PubDate.length,PubDate.lastIndexOf ('-')+1);  
	    var pubYear = PubDate.substring(0,PubDate.indexOf ('-'));  
		
	    var cha=((Date.parse(currentMonth+'/'+currentDay+'/'+currentYear)- Date.parse(pubMonth+'/'+pubDay+'/'+pubYear))/86400000); 
			
	    return Math.abs(cha)<7;  
	}
</script>
<style type="text/css">
	#zczx .question{
	background: none repeat scroll 0 0 white;
    border: 3px solid #cccccc;
    border-radius: 8px;
    display: none;
    font-size: 12px;
    margin: 0;
    min-height: 32px;
    padding: 12px;
    position: absolute;
    top:710px;
    left:500px;
    text-align: left;
    width: 650px;
    z-index: 1;
    line-height: 22px
    }
    #zczx .question div{
    	background: #CBFFC4;
    	border: 1px solid #4DD07A;
    }
    #zczx .question span{
    font-weight: bold;
    line-height: 28px;
    }

</style>

<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>

<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d5330a3aab1f8681bd4f82488c72714c";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>

</head>

<body>
<div class="wrap">

  <div class="header">
    <div class="header_left"><a href="http://xqctk.jtys.sz.gov.cn"><img style="height:84px;width:615px;" src="http://xqctk.jtys.sz.gov.cn/templates/default/images/top_bt.png" /></a></div>
    <div class="header_right"><a href="http://www.sz.gov.cn/"><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/szzx.png" /></a></div>
     
  </div>
  <div class="nav width_1002">
     <div class="nav_nr_fudong_yc" id="dh"  style="display:block">
      <div class="nav_nr_fudong" id="nav_div">咨询导航</div>
      <div class="nav_nr_fudong_ycb" id="nav_ul" style="display:none">
		<div class="nav_nr_fudong_ycb_a"><a href="http://xqctk.jtys.sz.gov.cn/zxgd">暂行规定</a></div>
        <div class="nav_nr_fudong_ycb_a"><a href="http://xqctk.jtys.sz.gov.cn/glbf">实施细则</a></div>
        <!--<div class="nav_nr_fudong_ycb_a"><a href="http://apply.sztb.gov.cn/apply/app/zczx/result">政策咨询</a></div> -->
        <div class="nav_nr_fudong_ycb_d" id="div_sblc"><a href="#">申报流程说明</a> 
        <div class="nav_nr_fudong_three" id="div_jtlc">
	             <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/ywlc/2015121/1421854116658_1.html">申报流程</a></div>
                     <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/grsqlc">个人申请</a></div>
		     <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/qysqlc">企业申请</a></div>
		     <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/stqtsqlc">社会团体、其它组织申请</a></div>
		     <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/grgxlc">个人更新车辆申请</a></div>
		     <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/dwgxlc">单位更新车辆申请</a></div>
			 <div class="nav_nr_fudong_three_a"><a href="http://xqctk.jtys.sz.gov.cn/esc">存量二手车申请</a></div>
	</div>
        </div>
      </div>
    </div>

     <div class="indextop2">
	<div id="navaa">
	<div id="navMenu">
		<ul>
			<li><a href="#" rel='dropmenu1'><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/dh_01.png" width="132" height="89" /></a></li> 
			<li><a href="#" rel='dropmenu2'><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/dh_02.png" width="132" height="89" /></a></li> 
			<li><a href="#" rel='dropmenu3'><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/dh_03.png" width="132" height="89" /></a></li> 
			<li><a href="#" rel='dropmenu4'><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/dh_04.png" width="132" height="89" /></a></li>
			<li><a href="http://www.szxqcjj.com" rel='dropmenu5'><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/dh_05.png" width="132" height="89" /></a></li>
	        </ul>
	  </div>
		
<div class="subnav">
		<ul id="dropmenu1" class="dropMenu">
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200802">个人申请</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200801">企业申请</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200801">社会团体、其他组织申请</a></li>	
			<li class="end"></li>
		</ul>
		<ul id="dropmenu2" class="dropMenu">
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/1144030069395137733442015052006">个人更新注册</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/1144030069395137733442015052011">单位更新注册</a></li>	
			<li class="end"></li>
		</ul>
		<ul id="dropmenu3" class="dropMenu">
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/1144030069395137733442015052001">高层次引进人才</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/1144030069395137733442015052007">外交人员返深自带小汽车</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200201">离婚/继承</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505201002">被盗抢车辆(个人)</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505201001">被盗抢车辆(单位)</a></li>	
					<li><a href="https://apply.jtys.sz.gov.cn/apply/app/others/apply/C6">本市重大招商引资项目</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200502">出租小汽车</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200501">教练车</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200404">企业兼并重组/划转/调拨</a></li>	
					<li><a href="https://www.gdzwfw.gov.cn/portal/guide/114403006939513773344201505200302">特种车辆(消防车/救护车等)</a></li>	
					<li><a href="https://apply.jtys.sz.gov.cn/apply/app/status/store/noteInfo">存量二手车</a></li>	
			<li class="end"></li>
		</ul>
		<ul id="dropmenu4" class="dropMenu">
					<li><a href="https://apply.jtys.sz.gov.cn/apply/app/status/norm/person">配置结果查询</a></li>	
					<li><a href="https://apply.jtys.sz.gov.cn/apply/app/status/other/apply/query">其他指标申请查询</a></li>	
					<li><a href="https://apply.jtys.sz.gov.cn/apply/app/status/other/query">其他指标查询</a></li>	
					<li><a href="https://apply.jtys.sz.gov.cn/apply/app/status/store/manage">存量二手车指标查询</a></li>	
			<li class="end"></li>
		</ul>
		<script type="text/javascript">cssdropdown.startchrome("navMenu")</script> 
	</div>
	
	</div>
</div>
    
  </div>
  <div class="banner">
  </div> <div class="clear"></div>
  <div class="main width_1002">
    <div class="main_xw_l">
      <div class="main_xw_la">

        <div class="main_xw_la_tit"><span class="font18_b_151">通知公告</span><span class="font14_509">Announcement</span></div>
        <div class="main_xw_la_nr">
		<ul id="gblwz">
				<script type='text/javascript'>
					
					if(isNew('2020-03-22')){
						var str = '深圳市2020年第3期普通小汽车增量指标摇号公告'.substring(0,18);
						$("#gblwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/gbl/20200322/1584842658490_1.html" title="深圳市2020年第3期普通小汽车增量指标摇号公告">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#gblwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/gbl/20200322/1584842658490_1.html" title="深圳市2020年第3期普通小汽车增量指标摇号公告">深圳市2020年第3期普通小汽车增量指标摇号公告</a></li>');
					}
				</script>
			
				<script type='text/javascript'>
					
					if(isNew('2020-03-16')){
						var str = '深圳市2020年第3期普通小汽车增量指标竞价公告'.substring(0,18);
						$("#gblwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/gbl/20200316/1584323412412_1.html" title="深圳市2020年第3期普通小汽车增量指标竞价公告">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#gblwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/gbl/20200316/1584323412412_1.html" title="深圳市2020年第3期普通小汽车增量指标竞价公告">深圳市2020年第3期普通小汽车增量指标竞价公告</a></li>');
					}
				</script>
			
				<script type='text/javascript'>
					
					if(isNew('2020-03-09')){
						var str = '深圳市2020年第3期普通小汽车增量指标配置数量公告'.substring(0,18);
						$("#gblwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/gbl/20200306/1583481742269_1.html" title="深圳市2020年第3期普通小汽车增量指标配置数量公告">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#gblwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/gbl/20200306/1583481742269_1.html" title="深圳市2020年第3期普通小汽车增量指标配置数量公告">深圳市2020年第3期普通小汽车增量指标配置数量公告</a></li>');
					}
				</script>
			
				<script type='text/javascript'>
					
					if(isNew('2020-02-26')){
						var str = '深圳市2020年第2期（含第1期）普通小汽车增量指标摇号结果公告'.substring(0,18);
						$("#gblwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/gbl/20200226/1582699656518_1.html" title="深圳市2020年第2期（含第1期）普通小汽车增量指标摇号结果公告">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#gblwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/gbl/20200226/1582699656518_1.html" title="深圳市2020年第2期（含第1期）普通小汽车增量指标摇号结果公告">深圳市2020年第2期（含第1期）普通小汽车增量指标摇号结果公告</a></li>');
					}
				</script>
			
		</ul>
        <div class="more"><a href="http://xqctk.jtys.sz.gov.cn/gbl">more</a></div>
        </div>
   
      </div>
      <div class="main_xw_lb">
      
      <div class="main_xw_la_tit"><span class="font18_b_151">温馨提示</span><span class="font14_509">Warm tips</span></div>
        <div class="main_xw_la_nr">
		<ul id="xwzzwz">
			<script type='text/javascript'>
					
					if(isNew('2019-12-20')){
						var str = '关于2019年单位申请编码自动失效的温馨提示'.substring(0,18);
						$("#xwzzwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/xwzz/20191219/1576720766947_1.html" title="关于2019年单位申请编码自动失效的温馨提示">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#xwzzwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/xwzz/20191219/1576720766947_1.html" title="关于2019年单位申请编码自动失效的温馨提示">关于2019年单位申请编码自动失效的温馨提示</a></li>');
					}
				</script>
			<script type='text/javascript'>
					
					if(isNew('2019-04-30')){
						var str = '转载：粤B牌指标可以继承吗？'.substring(0,18);
						$("#xwzzwz").append('<li><a  href="https://mp.weixin.qq.com/s/y3IG938OsrNd2xdYInaHPg" title="转载：粤B牌指标可以继承吗？">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#xwzzwz").append('<li><a href="https://mp.weixin.qq.com/s/y3IG938OsrNd2xdYInaHPg" title="转载：粤B牌指标可以继承吗？">转载：粤B牌指标可以继承吗？</a></li>');
					}
				</script>
			<script type='text/javascript'>
					
					if(isNew('2018-12-20')){
						var str = '关于2018年单位申请编码自动失效的温馨提示'.substring(0,18);
						$("#xwzzwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/xwzz/20181219/1545210576181_1.html" title="关于2018年单位申请编码自动失效的温馨提示">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#xwzzwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/xwzz/20181219/1545210576181_1.html" title="关于2018年单位申请编码自动失效的温馨提示">关于2018年单位申请编码自动失效的温馨提示</a></li>');
					}
				</script>
			<script type='text/javascript'>
					
					if(isNew('2018-07-26')){
						var str = '温馨提示：请认准小汽车指标摇号官方公众号'.substring(0,18);
						$("#xwzzwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/xwzz/20180726/1532590022050_1.html" title="温馨提示：请认准小汽车指标摇号官方公众号">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#xwzzwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/xwzz/20180726/1532590022050_1.html" title="温馨提示：请认准小汽车指标摇号官方公众号">温馨提示：请认准小汽车指标摇号官方公众号</a></li>');
					}
				</script>
		 </ul>
          <div class="more"><a href="http://xqctk.jtys.sz.gov.cn/xwzz">more</a></div>
        </div>
      
      </div>
    </div>
    <div class="main_login">
      <div class="main_login_qh" id="myLogin"  >
        <div class="main_login_qh_now" id="incrementLi" name="1F" style="border:0px;"><a href="#1F" name="1F"></a></div>
        <div class="main_login_qh_tabb" id="renewLi" name="2F" style="border:0px;"><a href="#2F" name="2F"></a></div>
      </div>
	<div class="main_login_nr">
          <table width="280" border="0" cellspacing="3" cellpadding="0" id='incrementTable'>
            <tr id='tr_zl'>
              <td>
              <input type="radio" id="radio" name="incrementSelect" class="incrementSelect" value="GR" checked="checked" />
                <label for="radio"></label>个人 
              <input type="radio" id="radio2" name="incrementSelect" class="incrementSelect" value="QY"/>企业 
              <input type="radio" id="radio3" name="incrementSelect" class="incrementSelect" value="ST"/>社会团体及其他</td>
            </tr>
            <tr>
              <td>
              <form action="https://apply.jtys.sz.gov.cn/apply/app/increment/person/login" method="post" name="incrementForm" id="incrementForm">
	              <table width="270" border="0" cellspacing="5" cellpadding="0">
	                <tr  id='gr'>
	                  <td width="83" height="30" align="right">
	                    <select name="loginType" id="select" style="width:115px;">
	                      <option value="MOBILE" selected="selected" id="incrementMobileOption">手机号码（账号）</option>
	                      <option value="LONGCODE" id="incrementCodeOption">申请编码</option>
	                    </select></td>
	                  <td colspan="3"><label for="textfield"></label>
	                    <input name="loginCode" type="text" class="main_login_nr_srk" id="incrementLoginCode" tabindex="1" value=""/></td>
	                </tr>
	                <tr>
	                  <td align="right">密 码：</td>
	                  <td colspan="3"><input type="password" type="text" class="main_login_nr_srk" id="incrementPassword" tabindex="2" value=""/>
						<input type="hidden" name="password" id="incrementPwd"/>
					  </td>
					</tr>
	                <tr>
	                  <td align="right">验证码：</td>
	                  <td  width="52"><input class="main_login_nr_srkb" type="text" name="validCode" id="incrementValidCode" tabindex="3" maxlength="4" value=""/></td>
                      <td width="80" align="left" id='incrementGetValidCodeImg' onclick="getValidCode()" title="点击刷新验证码"></td>
                      <td align="left" id="checkIncrementCode" ></td>
	                </tr>
	              </table>
	            </form>
              </td>
            </tr>
            <tr>
              <td>
              <table width="230" border="0" align="center" cellspacing="0" cellpadding="0">
                <tr>
                  <td align="right" class="wjmm"><a href="https://apply.jtys.sz.gov.cn/apply/app/increment/person/forget/passwd" id="incrementForgetPasswd" tabindex="5" >忘记密码</a></td>
                  <td align="center"><a href="#" id="incrementLoginButton" tabindex="6"><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/butt_01.png" width="71" height="37" border="0"/></a></td>
                  <td align="center"><a href=" https://apply.jtys.sz.gov.cn/apply/app/increment/ballot/affair" id="incrementApply" tabindex="7"><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/zww02.png" width="80" height="37" border="0"/></a></td>
                </tr>
              </table>
              </td>
            </tr>
          </table>
          <table width="280" border="0" cellspacing="3" cellpadding="0" id="renewTable">
            <tr id='tr_gx' align="center">
              <td><input type="radio" id="radio4" name="renewSelect" class="renewSelect" value="GR" checked="checked" />
                <label for="radio"></label>个人 
              <input type="radio" name="renewSelect" class="renewSelect" value="DW"/>单位 
              </td>
            </tr>
            <tr>
              <td>
              <form action="https://apply.jtys.sz.gov.cn/apply/app/renew/person/login" method="post" name="renewForm" id="renewForm">
              <table width="270" border="0" cellspacing="5" cellpadding="0">
	                <tr  id='gr'>
	                  <td width="83" height="30" align="right">
	                    <input type="hidden" name="loginType"value="MOBILE"/>手机号码：</td>
	                  <td colspan="3"><label for="textfield"></label>
	                    <input name="loginCode" type="text" class="main_login_nr_srk" id="renewLoginCode"  tabindex="1"/></td>
	                </tr>
	                <tr>
	                  <td align="right">密 码：</td>
	                  <td colspan="3">
					  <input type="password" id="renewPassword" class="main_login_nr_srk" tabindex="2"/>
					  <input type="hidden" name="password" id="renewPwd"/>
					  </td>
	                </tr>
	                <tr>
	                  <td align="right">验证码：</td>
	                  <td width="52"><input type="text" name="validCode" id="renewValidCode" class="main_login_nr_srkb" maxlength="4" tabindex="3"/></td>
                      <td width="80" align="left" id='renewGetValidCodeImg' onclick="getValidCode()" title="点击刷新验证码"></td>
		      <td align="left" id="checkRenewCode" ></td>
	                </tr>
	              </table>
              </form>
              </td>
            </tr>
            <tr>
              <td>
              <table width="230" border="0" align="center" cellspacing="0" cellpadding="0">
                <tr>
                  <td align="right" class="wjmm"><a href="https://apply.jtys.sz.gov.cn/apply/app/renew/person/forget/passwd" id="renewForgetPasswd" tabindex="4" >忘记密码</a></td>
                  <td align="center"><a href="#" id="renewLoginButton" tabindex="5"><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/butt_01.png" width="71" height="37" border="0"/></a></td>
                  <td align="center"><a href=" https://apply.jtys.sz.gov.cn/apply/app/renew/person/affair" id="renewRegister" tabindex="6"><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/zww02.png" width="80" height="37" border="0"/></a></td>
                </tr>
              </table>
              </td>
            </tr>
          </table>
        </div>
  
    </div>
    <div class="main_xw_r">
      <div class="main_xw_l_a"><div class="main_xw_la_tit"><span class="font18_b_151">办事指南</span><span class="font14_509">Guide</span></div>
        <div class="main_xw_la_nr">
                <ul id="bsznwz">
				<script type='text/javascript'>
					
					if(isNew('2018-08-27')){
						var str = '深圳市小汽车增量指标申请信息复核指引'.substring(0,18);
						$("#bsznwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/bszn/20180821/1534840697762_1.html" title="深圳市小汽车增量指标申请信息复核指引">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#bsznwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/bszn/20180821/1534840697762_1.html" title="深圳市小汽车增量指标申请信息复核指引">深圳市小汽车增量指标申请信息复核指引</a></li>');
					}
				</script>
				<script type='text/javascript'>
					
					if(isNew('2018-01-17')){
						var str = '关于修改小汽车增量调控系统账号密码或手机号业务操作指南'.substring(0,18);
						$("#bsznwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/bszn/20180116/1516085454901_1.html" title="关于修改小汽车增量调控系统账号密码或手机号业务操作指南">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#bsznwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/bszn/20180116/1516085454901_1.html" title="关于修改小汽车增量调控系统账号密码或手机号业务操作指南">关于修改小汽车增量调控系统账号密码或手机号业务操作指南</a></li>');
					}
				</script>
				<script type='text/javascript'>
					
					if(isNew('2018-01-12')){
						var str = '关于办理资产重组及调拨等其他类指标申领业务办理须知'.substring(0,18);
						$("#bsznwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/bszn/20180110/1515546035571_1.html" title="关于办理资产重组及调拨等其他类指标申领业务办理须知">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#bsznwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/bszn/20180110/1515546035571_1.html" title="关于办理资产重组及调拨等其他类指标申领业务办理须知">关于办理资产重组及调拨等其他类指标申领业务办理须知</a></li>');
					}
				</script>
				<script type='text/javascript'>
					
					if(isNew('2020-03-04')){
						var str = '深圳市小汽车增量指标竞价情况表'.substring(0,18);
						$("#bsznwz").append('<li><a  href="http://xqctk.jtys.sz.gov.cn/bszn/20171206/1512524976335_1.html" title="深圳市小汽车增量指标竞价情况表">'+str+'</a><img src="http://xqctk.jtys.sz.gov.cn/templates/default/images/new.gif" /></li>');
						}
					else{
					
						$("#bsznwz").append('<li><a href="http://xqctk.jtys.sz.gov.cn/bszn/20171206/1512524976335_1.html" title="深圳市小汽车增量指标竞价情况表">深圳市小汽车增量指标竞价情况表</a></li>');
					}
				</script>
		</ul>
          <div class="more"><a href="http://xqctk.jtys.sz.gov.cn/bszn">more</a></div>
        </div></div>
      <div class="main_xw_l_b"> <div class="main_xw_la_tit"></div>
        <div class="main_xw_la_nr">

          
        </div>
      </div>
    </div>
  </div>
  <div class="clear"></div>
</div>
<div class="footer">Copyright @ 2015 深圳市小汽车指标调控管理中心   备案号：粤ICP备 06038972号</div>
</body>
</html>
'''
import re
domains = set() # 域名去重列表，默认为空
domain = 'http://xqctk.jtys.sz.gov.cn' # 请求网址的域名
from lxml import etree
from urllib.parse import urlparse
tree = etree.HTML(html)



def match_link(links):
    for link in links:
        if not re.match(r'(//|http|https).*', link):
            continue
        if str(link).startswith('//'):
            link = domain+link
        res = urlparse(link)
        domains.add(res.netloc)

href_links = tree.xpath('//@href')
match_link(href_links)
src_link = tree.xpath('//@src')
match_link(src_link)
print(domains)
print('*'*100)