html = '''
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="renderer" content="ie-stand" />
<title>考试页面</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<!--easyui css-->
<link rel="stylesheet" type="text/css" href="/base/vendor/easyui14/themes/easyui.css" />
<link rel="stylesheet" type="text/css" href="/base/vendor/easyui14/themes/icon.css" />
<!--public css-->
<link rel="stylesheet" type="text/css" href="/base/style/public.css?v=20160618" />
<!--首先加载jquery,没有修改响应304-->
<script src="//hm.baidu.com/hm.js?183898d755583f6b54c8491f9c451ef5"></script><script src="/base/vendor/jquery/jquery.min.js"></script>
<!--兼容IE浏览器版本低不支持JSON-->
<script src="/base/vendor/json2.min.js"></script>

<script type="text/javascript">
var base=base||{};
var cssVersion = "20150607";
base.resources = {
	"url":{
		postPointUrl:"/pss/service/postPoint",
		//authControlUrl:"/demo/common/data/auth.json"
		authControlUrl:"/useris/service/getauth"
		
	}
};
/**
 * 加载脚本工具  
 * @param scripts script请求URL数组
 * @param cache 是否使用缓存，默认为不使用（推荐开源组件使用缓存）
 * @param callback  加载完成之后的回调函数
 * @returns
 */
base.scriptsArray = new Array();
base.loadScripts=function(scripts,cache,callback){
	var len=scripts.length;
	if(cache==null){cache=false}
	for(var i=0;i&lt;len;i++){
		if(base.scriptsArray[scripts[i]]==null){
			$.ajax({ 
				 type: 'get',
				 async:false,
				 url: scripts[i],
				 dataType: "script",
				 cache: cache
			 });
			base.scriptsArray[scripts[i]]=true;
		}
	}
	if (typeof callback == 'function') {
		callback.call();
	}
}
/**
 * 加载css样式工具  
 */
base.loadstyles=function(styles){
	var len=styles.length;
	var html_doc = document.getElementsByTagName('head')[0];
	for(var i=0;i&lt;len;i++){
		var css_file = styles[i] + "?v=" + cssVersion;
		var css = document.createElement('link');
	    css.setAttribute('rel', 'stylesheet');
	    css.setAttribute('type', 'text/css');
	    css.setAttribute('href', css_file);
	    html_doc.appendChild(css);
	}
}
//加载jquery.cookie,jsrender,easyui;使用本地缓存
base.loadScripts(['/base/vendor/jquery/jquery.cookie.js','/base/vendor/jsrender.js','/base/vendor/easyui14/lib/base.js'],true);
</script>
<!--加载自定义资源,利用浏览器机制检查,如果服务器修改响应304-->
<script src="/base/vendor/jquery/jquery.cookie.js"></script>
<script src="/base/js/comm_util.js"></script>
<script src="/base/js/comm_cookies.js"></script>
<script src="/base/js/comm_serv.js"></script>
<script type="text/javascript">
base.loginCheck = function(type){
	var obj = base.getCookie("loginUser");
	if(!obj){
		location = "/bps/index.html";
	}
}
</script>
<link rel="stylesheet" type="text/css" href="/base/style/common/popwin_style.css" />
<script type="text/javascript">
	//自定义,刷新页面时更新
	base.loadScripts(['/base/js/widget/comm_popwin.js']);
</script>
<link href="/baseui/style/exam/exam.css?v=20170421" rel="stylesheet" type="text/css" />
<link href="/baseui/style/orhonmatrixfont.css?v=20170421" rel="stylesheet" type="text/css" />
<style type="text/css">
b, em, strong, i,h1,h2,h3,h4,h5,h6{font-style:normal; font-weight:normal;}
</style>
<script type="text/javascript" charset="UTF-8">
	//加载业务私有JS
	 base.loadScripts(['/eps/common/comm_resources.js','/eps/examination/s/examination_3_s.js','/eps/examination/v/examination_3_v.js','/eps/common/epstime.js','/eps/common/timer.js','/eps/common/windowopen.js','/baseui/js/index/orhonmclib.min.js','/baseui/js/index/orhon-U2M.js']);
	 //本页权限编号
	$(function(){ 
		eps.beginExam();
		eps.exefSizeshow();
		eps.exebColorshow();
		eps.hexamtime();
		eps.exechangeBcolor();
		eps.exechangeSize();
	});	
	 //下面这段js禁止了页面内容被选中，防止内容被复制
	if(document.all){
	    document.onselectstart= function(){return false;}; 
	}else{
	    document.onmousedown= function(){return false;};
	    document.onmouseup= function(){return true;};
	}
	document.onselectstart = new Function('event.returnValue=false;');
</script>
<!-- 百度站长统计代码，请勿删除  放在/head之前-->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?183898d755583f6b54c8491f9c451ef5";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
</head>

<body oncopy="return false;" oncontextmenu="return false;" onkeypress="return false;" onkeydown="return false;" onkeyup="return false;" style="background:url('') no-repeat scroll center top">
	<div class="examcontainer exampage" style="padding-top: 129px;">
		<div class="examtime clear">
			<div class="clear">
				<span>剩余时间：<strong id="onlineTimer">01:00:00</strong></span>
				<div class="fSize">
					字号
					<div id="fSizecontainer">
						<img src="/baseui/images/lesson/up.gif" width="18" height="10" />
						<ul class="clear">
							<li><a href="javascript:void(0)">缩小</a></li>
							<li><a href="javascript:void(0)">默认</a></li>
							<li><a href="javascript:void(0)">放大</a></li>
						</ul>
					</div>
				</div>
				<div class="bColor">
					背景色
					<div id="bColorcontainer">
						<img src="/baseui/images/lesson/up.gif" width="18" height="10" />
						<ul class="clear">
							<li><a href="javascript:void(0)" class="bj1"></a></li>
							<li><a href="javascript:void(0)" class="bj2"></a></li>
							<li><a href="javascript:void(0)" class="bj3"></a></li>
							<li><a href="javascript:void(0)" class="bj4"></a></li>
							<li><a href="javascript:void(0)" class="bj5"></a></li>
							<li><a href="javascript:void(0)" class="bj6"></a></li>
						</ul>
					</div>
				</div>
				<a id="myExamCommitBtnId" onclick="eps.commitBefore();" href="javascript:;">交卷</a>
			</div>
		</div>
		<h1 id="kanameId" title="江苏省百万党员学宪法学党章考法活动">江苏省百万党员学宪法学党章考法活动</h1>
		
		<!-- 学员姓名 -->
		<div class="ksname"><span>学员姓名：</span>管理员</div>
		
		<!-- 单选题,多选题 ,判断题-->
		<div class="timu"><span class="dx1">单选题：共<i>20</i>题，总分<i>40</i></span><span class="dx2">多选题：共<i>10</i>题，总分<i>20</i></span><span class="pd">判断题：共<i>20</i>题，总分<i>40</i></span></div>
		<!-- 考试内容部分 -->
		<div id="timucontent"><h2>1、（单选题）根据《宪法》的规定，村民委员会的委员由（ ）。</h2><ul><li><input name="option" type="radio" value="A" /> A.街道办事处任命</li><li><input name="option" type="radio" value="B" /> B.居民选举</li><li><input name="option" type="radio" value="C" /> C.上级选举</li><li><input name="option" type="radio" value="D" /> D.群众推荐上级任命</li></ul><span><a href="javascript:" id="nextButton" onclick="eps.switchQuestion(1,1,0,268136)">下一题</a></span></div>

		<div class="selecttimu">
			<div class="title clear">
				答题卡
				<div class="info">
					<span class="yhd">已回答：<i>0</i></span>
					<span class="whd">未回答：<i>50</i></span>
				</div>
			</div>
			<div class="xtcontent clear"><ul id="practice"><li id="icofront1_268136"><a id="aid1" href="javascript:;">1</a></li><li id="icofront2_268129"><a id="aid2" href="javascript:;">2</a></li><li id="icofront3_268135"><a id="aid3" href="javascript:;">3</a></li><li id="icofront4_268121"><a id="aid4" href="javascript:;">4</a></li><li id="icofront5_268124"><a id="aid5" href="javascript:;">5</a></li><li id="icofront6_268120"><a id="aid6" href="javascript:;">6</a></li><li id="icofront7_268127"><a id="aid7" href="javascript:;">7</a></li><li id="icofront8_268125"><a id="aid8" href="javascript:;">8</a></li><li id="icofront9_268134"><a id="aid9" href="javascript:;">9</a></li><li id="icofront10_268132"><a id="aid10" href="javascript:;">10</a></li><li id="icofront11_268139"><a id="aid11" href="javascript:;">11</a></li><li id="icofront12_268131"><a id="aid12" href="javascript:;">12</a></li><li id="icofront13_268133"><a id="aid13" href="javascript:;">13</a></li><li id="icofront14_268138"><a id="aid14" href="javascript:;">14</a></li><li id="icofront15_268123"><a id="aid15" href="javascript:;">15</a></li><li id="icofront16_268126"><a id="aid16" href="javascript:;">16</a></li><li id="icofront17_268122"><a id="aid17" href="javascript:;">17</a></li><li id="icofront18_268130"><a id="aid18" href="javascript:;">18</a></li><li id="icofront19_268137"><a id="aid19" href="javascript:;">19</a></li><li id="icofront20_268128"><a id="aid20" href="javascript:;">20</a></li><li id="icofront21_268167"><a id="aid21" href="javascript:;">21</a></li><li id="icofront22_268162"><a id="aid22" href="javascript:;">22</a></li><li id="icofront23_268158"><a id="aid23" href="javascript:;">23</a></li><li id="icofront24_268159"><a id="aid24" href="javascript:;">24</a></li><li id="icofront25_268164"><a id="aid25" href="javascript:;">25</a></li><li id="icofront26_268165"><a id="aid26" href="javascript:;">26</a></li><li id="icofront27_268161"><a id="aid27" href="javascript:;">27</a></li><li id="icofront28_268163"><a id="aid28" href="javascript:;">28</a></li><li id="icofront29_268160"><a id="aid29" href="javascript:;">29</a></li><li id="icofront30_268166"><a id="aid30" href="javascript:;">30</a></li><li id="icofront31_268278"><a id="aid31" href="javascript:;">31</a></li><li id="icofront32_268212"><a id="aid32" href="javascript:;">32</a></li><li id="icofront33_268277"><a id="aid33" href="javascript:;">33</a></li><li id="icofront34_268204"><a id="aid34" href="javascript:;">34</a></li><li id="icofront35_268207"><a id="aid35" href="javascript:;">35</a></li><li id="icofront36_268203"><a id="aid36" href="javascript:;">36</a></li><li id="icofront37_268210"><a id="aid37" href="javascript:;">37</a></li><li id="icofront38_268208"><a id="aid38" href="javascript:;">38</a></li><li id="icofront39_268276"><a id="aid39" href="javascript:;">39</a></li><li id="icofront40_268215"><a id="aid40" href="javascript:;">40</a></li><li id="icofront41_268281"><a id="aid41" href="javascript:;">41</a></li><li id="icofront42_268214"><a id="aid42" href="javascript:;">42</a></li><li id="icofront43_268216"><a id="aid43" href="javascript:;">43</a></li><li id="icofront44_268280"><a id="aid44" href="javascript:;">44</a></li><li id="icofront45_268206"><a id="aid45" href="javascript:;">45</a></li><li id="icofront46_268209"><a id="aid46" href="javascript:;">46</a></li><li id="icofront47_268205"><a id="aid47" href="javascript:;">47</a></li><li id="icofront48_268213"><a id="aid48" href="javascript:;">48</a></li><li id="icofront49_268279"><a id="aid49" href="javascript:;">49</a></li><li id="icofront50_268211"><a id="aid50" href="javascript:;">50</a></li></ul></div>
		</div>
	</div>



</body></html>
'''.replace('xmlns', 'another_attr')
from pyquery import PyQuery as pq
doc = pq(html)
options = doc('#timucontent li').items()
for sel in options:
    print(sel.text())