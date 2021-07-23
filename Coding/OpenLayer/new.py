from bs4 import BeautifulSoup
import webview

html_doc = """
<!doctype html><html lang="en-ca" class="a-no-js" data-19ax5a9jf="dingo"><!-- sp:feature:head-start -->
<head><script>var aPageStart = (new Date()).getTime();</script><meta charset="utf-8"/>

<script type='text/javascript'>var ue_t0=ue_t0||+new Date();</script>
<!-- sp:feature:cs-optimization -->
<meta http-equiv='x-dns-prefetch-control' content='on'>
<link rel="dns-prefetch" href="https://images-na.ssl-images-amazon.com">
<link rel="dns-prefetch" href="https://m.media-amazon.com">
<link rel="dns-prefetch" href="https://completion.amazon.com">
<script type='text/javascript'>
window.ue_ihb = (window.ue_ihb || window.ueinit || 0) + 1;
if (window.ue_ihb === 1) {

var ue_csm = window,
    ue_hob = +new Date();
(function(d){var e=d.ue=d.ue||{},f=Date.now||function(){return+new Date};e.d=function(b){return f()-(b?0:d.ue_t0)};e.stub=function(b,a){if(!b[a]){var c=[];b[a]=function(){c.push([c.slice.call(arguments),e.d(),d.ue_id])};b[a].replay=function(b){for(var a;a=c.shift();)b(a[0],a[1],a[2])};b[a].isStub=1}};e.exec=function(b,a){return function(){try{return b.apply(this,arguments)}catch(c){ueLogError(c,{attribution:a||"undefined",logLevel:"WARN"})}}}})(ue_csm);


    var ue_err_chan = 'jserr-rw';
(function(d,e){function h(f,b){if(!(a.ec>a.mxe)&&f){a.ter.push(f);b=b||{};var c=f.logLevel||b.logLevel;c&&c!==k&&c!==m&&c!==n&&c!==p||a.ec++;c&&c!=k||a.ecf++;b.pageURL=""+(e.location?e.location.href:"");b.logLevel=c;b.attribution=f.attribution||b.attribution;a.erl.push({ex:f,info:b})}}function l(a,b,c,e,g){d.ueLogError({m:a,f:b,l:c,c:""+e,err:g,fromOnError:1,args:arguments},g?{attribution:g.attribution,logLevel:g.logLevel}:void 0);return!1}var k="FATAL",m="ERROR",n="WARN",p="DOWNGRADED",a={ec:0,ecf:0,
pec:0,ts:0,erl:[],ter:[],mxe:50,startTimer:function(){a.ts++;setInterval(function(){d.ue&&a.pec<a.ec&&d.uex("at");a.pec=a.ec},1E4)}};l.skipTrace=1;h.skipTrace=1;h.isStub=1;d.ueLogError=h;d.ue_err=a;e.onerror=l})(ue_csm,window);


var ue_id = '1KMDY2JPGP2X3R80G8WC',
    ue_url = '/rd/uedata',
    ue_navtiming = 1,
    ue_mid = 'A2EUQ1WTGCTBG2',
    ue_sid = '138-4669640-7712440',
    ue_sn = 'www.amazon.ca',
    ue_furl = 'fls-na.amazon.ca',
    ue_surl = 'https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.prod',
    ue_int = 0,
    ue_fcsn = 1,
    ue_urt = 3,
    ue_rpl_ns = 'cel-rpl',
    ue_ddq = 1,
    ue_fpf = '//fls-na.amazon.ca/1/batch/1/OP/A2EUQ1WTGCTBG2:138-4669640-7712440:1KMDY2JPGP2X3R80G8WC$uedata=s:',
    ue_sbuimp = 1,
    ue_cel_lclia = 1,
    ue_ibft = 0,
    ue_fnt = 0,
    ue_ccf = 1,

    ue_swi = 1;
var ue_viz=function(){(function(b,e,a){function k(c){if(b.ue.viz.length<p&&!l){var a=c.type;c=c.originalEvent;/^focus./.test(a)&&c&&(c.toElement||c.fromElement||c.relatedTarget)||(a=e[m]||("blur"==a||"focusout"==a?"hidden":"visible"),b.ue.viz.push(a+":"+(+new Date-b.ue.t0)),"visible"==a&&(b.ue.isl&&q("at"),l=1))}}for(var l=0,q=b.uex,f,g,m,n=["","webkit","o","ms","moz"],d=0,p=20,h=0;h<n.length&&!d;h++)if(a=n[h],f=(a?a+"H":"h")+"idden",d="boolean"==typeof e[f])g=a+"visibilitychange",m=(a?a+"V":"v")+
"isibilityState";k({});d&&e.addEventListener(g,k,0);b.ue&&d&&(b.ue.pageViz={event:g,propHid:f})})(ue_csm,ue_csm.document,ue_csm.window)};

(function(d,k,K){function G(a){return a&&a.replace&&a.replace(/^\s+|\s+$/g,"")}function q(a){return"undefined"===typeof a}function C(a,b){for(var c in b)b[t](c)&&(a[c]=b[c])}function L(a){try{var b=K.cookie.match(RegExp("(^| )"+a+"=([^;]+)"));if(b)return b[2].trim()}catch(c){}}function M(n,b,c){var f=(x||{}).type,f=2===f||1===f;(aa?"device"===c&&f:f)||(n&&(d.ue_id=a.id=a.rid=n,y=y.replace(/((.*?:){2})(\w+)/,function(a,b){return b+n})),b&&(y=y.replace(/(.*?:)(\w|-)+/,function(a,c){return c+b}),d.ue_sid=
b),c&&a.tag("page-source:"+c),d.ue_fpf=y)}function O(){var a={};return function(b){b&&(a[b]=1);b=[];for(var c in a)a[t](c)&&b.push(c);return b}}function u(d,b,c,f){if(0<v&&0<=(ba||[]).indexOf(d)&&!b){for(var g=z.now(),k=0;z.now()-g<v;)k++;a.tag("marker-delayed:"+d)}f=f||+new z;var w;if(b||q(c)){if(d)for(w in g=b?h("t",b)||h("t",b,{}):a.t,g[d]=f,c)c[t](w)&&h(w,b,c[w]);return f}}function h(d,b,c){var f=b&&b!=a.id?a.sc[b]:a;f||(f=a.sc[b]={});"id"===d&&c&&(P=1);return f[d]=c||f[d]}function Q(d,b,c,f,
g){c="on"+c;var h=b[c];"function"===typeof h?d&&(a.h[d]=h):h=function(){};b[c]=function(a){g?(f(a),h(a)):(h(a),f(a))};b[c]&&(b[c].isUeh=1)}function R(n,b,c,f){function r(b,c){var d=[b],f=0,e={},g,k;c?(d.push("m=1"),e[c]=1):e=a.sc;for(k in e)if(e[t](k)){var r=h("wb",k),l=h("t",k)||{},p=h("t0",k)||a.t0,m;if(c||2==r){r=r?f++:"";d.push("sc"+r+"="+k);for(m in l)q(l[m])||null===l[m]||d.push(m+r+"="+(l[m]-p));d.push("t"+r+"="+l[n]);if(h("ctb",k)||h("wb",k))g=1}}!v&&g&&d.push("ctb=1");return d.join("&")}
function N(b,c,f,e){if(b){var g=d.ue_err;d.ue_url&&!e&&b&&0<b.length&&(e=new Image,a.iel.push(e),e.src=b,a.count&&a.count("postbackImageSize",b.length));if(y){var h=k.encodeURIComponent;h&&b&&(e=new Image,b=""+d.ue_fpf+h(b)+":"+(+new z-d.ue_t0),a.iel.push(e),e.src=b)}else a.log&&(a.log(b,"uedata",{n:1}),a.ielf.push(b));g&&!g.ts&&g.startTimer();a.b&&(g=a.b,a.b="",N(g,c,f,1))}}function w(b){var c=x?x.type:D,d=2==c||a.isBFonMshop,c=c&&!d,e=a.bfini;P||(e&&1<e&&(b+="&bfform=1",c||(a.isBFT=e-1)),d&&(b+=
"&bfnt=1",a.isBFT=a.isBFT||1),a.ssw&&a.isBFT&&(a.isBFonMshop&&(a.isNRBF=0),q(a.isNRBF)&&(d=a.ssw(a.oid),d.e||q(d.val)||(a.isNRBF=1<d.val?0:1)),q(a.isNRBF)||(b+="&nrbf="+a.isNRBF)),a.isBFT&&!a.isNRBF&&(b+="&bft="+a.isBFT));return b}if(!a.paused&&(b||q(c))){for(var p in c)c[t](p)&&h(p,b,c[p]);a.isBFonMshop||u("pc",b,c);p=h("id",b)||a.id;var s=h("id2",b),e=a.url+"?"+n+"&v="+a.v+"&id="+p,v=h("ctb",b)||h("wb",b),A;v&&(e+="&ctb="+v);s&&(e+="&id2="+s);1<d.ueinit&&(e+="&ic="+d.ueinit);if(!("ld"!=n&&"ul"!=
n||b&&b!=p)){if("ld"==n){try{k[H]&&k[H].isUeh&&(k[H]=null)}catch(F){}if(k.chrome)for(s=0;s<I.length;s++)S(E,I[s]);(s=K.ue_backdetect)&&s.ue_back&&s.ue_back.value++;d._uess&&(A=d._uess());a.isl=1}a._bf&&(e+="&bf="+a._bf());d.ue_navtiming&&g&&(h("ctb",p,"1"),a.isBFonMshop||u("tc",D,D,J));!B||a.isBFonMshop||T||(g&&C(a.t,{na_:g.navigationStart,ul_:g.unloadEventStart,_ul:g.unloadEventEnd,rd_:g.redirectStart,_rd:g.redirectEnd,fe_:g.fetchStart,lk_:g.domainLookupStart,_lk:g.domainLookupEnd,co_:g.connectStart,
_co:g.connectEnd,sc_:g.secureConnectionStart,rq_:g.requestStart,rs_:g.responseStart,_rs:g.responseEnd,dl_:g.domLoading,di_:g.domInteractive,de_:g.domContentLoadedEventStart,_de:g.domContentLoadedEventEnd,_dc:g.domComplete,ld_:g.loadEventStart,_ld:g.loadEventEnd,ntd:("function"!==typeof B.now||q(J)?0:new z(J+B.now())-new z)+a.t0}),x&&C(a.t,{ty:x.type+a.t0,rc:x.redirectCount+a.t0}),T=1);a.isBFonMshop||C(a.t,{hob:d.ue_hob,hoe:d.ue_hoe});a.ifr&&(e+="&ifr=1")}u(n,b,c,f);c="ld"==n&&b&&h("wb",b);var m,l;
c||b&&b!==p||ca(b);c||p==a.oid||da(p,(h("t",b)||{}).tc||+h("t0",b),+h("t0",b));(f=d.ue_mbl)&&f.cnt&&!c&&(e+=f.cnt());c?h("wb",b,2):"ld"==n&&(a.lid=G(p));for(m in a.sc)if(1==h("wb",m))break;if(c){if(a.s)return;e=r(e,null)}else f=r(e,null),f!=e&&(f=w(f),a.b=f),A&&(e+=A),e=r(e,b||a.id);e=w(e);if(a.b||c)for(m in a.sc)2==h("wb",m)&&delete a.sc[m];A=0;a._rt&&(e+="&rt="+a._rt());f=k.csa;if(!c&&f)for(l in m=h("t",b)||{},f=f("PageTiming"),m)m[t](l)&&f("mark",ea[l]||l,m[l]);c||(a.s=0,(l=d.ue_err)&&0<l.ec&&
l.pec<l.ec&&(l.pec=l.ec,e+="&ec="+l.ec+"&ecf="+l.ecf),A=h("ctb",b),"ld"!==n||b||a.markers||(a.markers={},C(a.markers,h("t",b))),h("t",b,{}));a.tag&&a.tag().length&&(e+="&csmtags="+a.tag().join("|"),a.tag=O());l=a.viz||[];(m=l.length)&&(e+="&viz="+l.splice(0,m).join("|"));q(d.ue_pty)||(e+="&pty="+d.ue_pty+"&spty="+d.ue_spty+"&pti="+d.ue_pti);a.tabid&&(e+="&tid="+a.tabid);a.aftb&&(e+="&aftb=1");!a._ui||b&&b!=p||(e+=a._ui());a.a=e;N(e,n,A,c)}}function ca(a){var b=k.ue_csm_markers||{},c;for(c in b)b[t](c)&&
u(c,a,D,b[c])}function F(a,b,c){c=c||k;if(c[U])c[U](a,b,!1);else if(c[V])c[V]("on"+a,b)}function S(a,b,c){c=c||k;if(c[W])c[W](a,b,!1);else if(c[X])c[X]("on"+a,b)}function Y(){function a(){d.onUl()}function b(a){return function(){c[a]||(c[a]=1,R(a))}}var c={},f,g;d.onLd=b("ld");d.onLdEnd=b("ld");d.onUl=b("ul");f={stop:b("os")};k.chrome?(F(E,a),I.push(a)):f[E]=d.onUl;for(g in f)f[t](g)&&Q(0,k,g,f[g]);d.ue_viz&&ue_viz();F("load",d.onLd);u("ue")}function da(g,b,c){var f=d.ue_mbl,h=k.csa,q=h&&h("SPA"),
h=h&&h("PageTiming");f&&f.ajax&&f.ajax(b,c);q&&h&&(q("newPage",{requestId:g,transitionType:"soft"}),h("mark","transitionStart",b));a.tag("ajax-transition")}d.ueinit=(d.ueinit||0)+1;var a=d.ue=d.ue||{};a.t0=k.aPageStart||d.ue_t0;a.id=d.ue_id;a.url=d.ue_url;a.rid=d.ue_id;a.a="";a.b="";a.h={};a.s=1;a.t={};a.sc={};a.iel=[];a.ielf=[];a.viz=[];a.v="0.217347.0";a.paused=!1;var t="hasOwnProperty",E="beforeunload",H="on"+E,U="addEventListener",W="removeEventListener",V="attachEvent",X="detachEvent",ea={cf:"criticalFeature",
af:"aboveTheFold",fn:"functional",fp:"firstPaint",fcp:"firstContentfulPaint",bb:"bodyBegin",be:"bodyEnd",ld:"loaded"},z=k.Date,B=k.performance||k.webkitPerformance,g=(B||{}).timing,x=(B||{}).navigation,J=(g||{}).navigationStart,y=d.ue_fpf,ba=d.ue_tx_md,v=d.ue_tx_ad,aa=1===d.ue_ccf,P=0,T=0,I=[],D;a.oid=G(a.id);a.lid=G(a.id);a._t0=a.t0;a.tag=O();a.ifr=k.top!==k.self||k.frameElement?1:0;a.markers=null;a.attach=F;a.detach=S;if("000-0000000-8675309"===d.ue_sid){var Z=L("cdn-rid"),$=L("session-id");Z&&
$&&M(Z,$,"cdn")}d.uei=Y;d.ueh=Q;d.ues=h;d.uet=u;d.uex=R;a.reset=M;a.pause=function(d){a.paused=d};Y();0<v&&u("ho")})(ue_csm,ue_csm.window,ue_csm.document);


ue.stub(ue,"event");ue.stub(ue,"onSushiUnload");ue.stub(ue,"onSushiFlush");

ue.stub(ue,"log");ue.stub(ue,"onunload");ue.stub(ue,"onflush");
(function(c){var a=c.ue;a.cv={};a.cv.scopes={};a.count=function(d,c,b){var e={},f=a.cv,g=b&&0===b.c;e.counter=d;e.value=c;e.t=a.d();b&&b.scope&&(f=a.cv.scopes[b.scope]=a.cv.scopes[b.scope]||{},e.scope=b.scope);if(void 0===c)return f[d];f[d]=c;d=0;b&&b.bf&&(d=1);ue_csm.ue_sclog||!a.clog||0!==d||g?a.log&&a.log(e,"csmcount",{c:1,bf:d}):a.clog(e,"csmcount",{bf:d})};a.count("baselineCounter2",1);a&&a.event&&(a.event({requestId:c.ue_id||"rid",server:c.ue_sn||"sn",obfuscatedMarketplaceId:c.ue_mid||"mid"},
"csm","csm.CSMBaselineEvent.4"),a.count("nexusBaselineCounter",1,{bf:1}))})(ue_csm);



var ue_hoe = +new Date();
}
window.ueinit = window.ue_ihb;
</script>

<!-- htiu4 -->
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 9693)</script>
<!-- sp:feature:aui-assets -->
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,418YjvsUB+L.css,31qGOnSAToL.css,013z33uKh2L.css,017DsKjNQJL.css,01L-6KXabGL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11bGSgD5pDL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,21N4kUH7pxL.css,01oDR3IULNL.css,31MKqadzl-L.css,21j0IlW7xKL.css,01XPHJk60-L.css,014OeDQisGL.css,21aPhFy+riL.css,11gneA3MtJL.css,21fecG8pUzL.css,01RddH8vm-L.css,01CFUgsA-YL.css,31C80IiXalL.css,11qour3ND0L.css,11tRp6+0HHL.css,11MrdqKlKnL.css,11oHt2HYxnL.css,013RDhw9hoL.css,11JQtnL-6eL.css,11RKoGSb-gL.css,11jtXRmppwL.css,01QrWuRrZ-L.css,21pIv-yKhaL.css,11QyqG8yiqL.css,01890+Vwk8L.css,11kwKGWmBfL.css,11F2+OBzLyL.css,11Y05DTEL6L.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI&q7tmqwsI#page_type-Detail.not-trident.322290-T1.322288-T1.265810-T2" />
<link rel="preload" as="script" crossorigin="anonymous" href="https://images-na.ssl-images-amazon.com/images/I/61-6nKPKyWL.js?AUIClients/AmazonUIjQuery" />
<link rel="preload" as="script" crossorigin="anonymous" href="https://images-na.ssl-images-amazon.com/images/I/11Y+5x+kkTL._RC|51106gSDnJL.js,11-zXBZR6KL.js,11giXtZCwVL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,01O9dYORveL.js,21NNXfMitSL.js,11rRjDLdAVL.js,51X-X0x2aRL.js,11kWu3cNjYL.js,11UNQpqeowL.js,11OREnu1epL.js,11KbZymw5ZL.js,21r53SJg7LL.js,0190vxtlzcL.js,51GBHgW1KPL.js,31KrK+dcMcL.js,01Gf12ogmOL.js,01ezj5Rkz1L.js,11VS-C+YWGL.js,31VpWkbgc1L.js,01rpauTep4L.js,01+b9cewx1L.js_.js?AUIClients/AmazonUI&qa9N+d93#page_type-Detail.348458-T1.309035-T1" />
<link rel="preload" as="script" crossorigin="anonymous" href="https://images-na.ssl-images-amazon.com/images/I/51xLtn9VfzL.js?AUIClients/CardJsRuntimeBuzzCopyBuild" />
<script>
(function(f,h,Q,E){function F(a){v&&v.tag&&v.tag(q(":","aui",a))}function t(a,b){v&&v.count&&v.count("aui:"+a,0===b?0:b||(v.count("aui:"+a)||0)+1)}function p(a){try{return a.test(navigator.userAgent)}catch(b){return!1}}function y(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&&a.attachEvent("on"+b,c)}function q(a,b,c,e){b=b&&c?b+a+c:b||c;return e?q(a,b,e):b}function G(a,b,c){try{Object.defineProperty(a,b,{value:c,writable:!1})}catch(e){a[b]=c}return c}function ta(a,b){var c=a.length,
e=c,g=function(){e--||(R.push(b),S||(setTimeout(ca,0),S=!0))};for(g();c--;)da[a[c]]?g():(z[a[c]]=z[a[c]]||[]).push(g)}function ua(a,b,c,e,g){var d=h.createElement(a?"script":"link");y(d,"error",e);g&&y(d,"load",g);a?(d.type="text/javascript",d.async=!0,c&&/AUIClients|images[/]I/.test(b)&&d.setAttribute("crossorigin","anonymous"),d.src=b):(d.rel="stylesheet",d.href=b);h.getElementsByTagName("head")[0].appendChild(d)}function ea(a,b){return function(c,e){function g(){ua(b,c,d,function(b){T?t("resource_unload"):
d?(d=!1,t("resource_retry"),g()):(t("resource_error"),a.log("Asset failed to load: "+c));b&&b.stopPropagation?b.stopPropagation():f.event&&(f.event.cancelBubble=!0)},e)}if(fa[c])return!1;fa[c]=!0;t("resource_count");var d=!0;return!g()}}function va(a,b,c){for(var e={name:a,guard:function(c){return b.guardFatal(a,c)},guardTime:function(a){return b.guardTime(a)},logError:function(c,d,e){b.logError(c,d,e,a)}},g=[],d=0;d<c.length;d++)H.hasOwnProperty(c[d])&&(g[d]=U.hasOwnProperty(c[d])?U[c[d]](H[c[d]],
e):H[c[d]]);return g}function A(a,b,c,e,g){return function(d,h){function n(){var a=null;e?a=h:"function"===typeof h&&(p.start=w(),a=h.apply(f,va(d,k,l)),p.end=w());if(b){H[d]=a;a=d;for(da[a]=!0;(z[a]||[]).length;)z[a].shift()();delete z[a]}p.done=!0}var k=g||this;"function"===typeof d&&(h=d,d=E);b&&(d=d?d.replace(ha,""):"__NONAME__",V.hasOwnProperty(d)&&k.error(q(", reregistered by ",q(" by ",d+" already registered",V[d]),k.attribution),d),V[d]=k.attribution);for(var l=[],m=0;m<a.length;m++)l[m]=
a[m].replace(ha,"");var p=B[d||"anon"+ ++wa]={depend:l,registered:w(),namespace:k.namespace};c?n():ta(l,k.guardFatal(d,n));return{decorate:function(a){U[d]=k.guardFatal(d,a)}}}}function ia(a){return function(){var b=Array.prototype.slice.call(arguments);return{execute:A(b,!1,a,!1,this),register:A(b,!0,a,!1,this)}}}function W(a,b){return function(c,e){e||(e=c,c=E);var g=this.attribution;return function(){u.push(b||{attribution:g,name:c,logLevel:a});var d=e.apply(this,arguments);u.pop();return d}}}
function I(a,b){this.load={js:ea(this,!0),css:ea(this)};G(this,"namespace",b);G(this,"attribution",a)}function ja(){h.body?r.trigger("a-bodyBegin"):setTimeout(ja,20)}function C(a,b){a.className=X(a,b)+" "+b}function X(a,b){return(" "+a.className+" ").split(" "+b+" ").join(" ").replace(/^ | $/g,"")}function ka(a){try{return a()}catch(b){return!1}}function J(){if(K){var a={w:f.innerWidth||n.clientWidth,h:f.innerHeight||n.clientHeight};5<Math.abs(a.w-Y.w)||50<a.h-Y.h?(Y=a,L=4,(a=k.mobile||k.tablet?450<
a.w&&a.w>a.h:1250<=a.w)?C(n,"a-ws"):n.className=X(n,"a-ws")):0<L&&(L--,la=setTimeout(J,16))}}function xa(a){(K=a===E?!K:!!a)&&J()}function ya(){return K}function ma(){D.forEach(function(a){F(a)})}function na(a,b,c){if(b){a=p(/Chrome/i)&&!p(/Edge/i)&&!p(/OPR/i)&&!a.capabilities.isAmazonApp&&!p(new RegExp(Z+"bwv"+Z+"b"));var e="sw:browser:"+c+":";b.browser&&a&&(D.push(e+"supported"),b.browser.action(e,c));!a&&b.browser&&D.push(e+"unsupported")}}"use strict";var M=Q.now=Q.now||function(){return+new Q},
w=function(a){return a&&a.now?a.now.bind(a):M}(f.performance),N=w(),l=f.AmazonUIPageJS||f.P;if(l&&l.when&&l.register){N=[];for(var m=h.currentScript;m;m=m.parentElement)m.id&&N.push(m.id);return l.log("A copy of P has already been loaded on this page.","FATAL",N.join(" "))}var v=f.ue;F();F("aui_build_date:3.21.4-2021-05-27");var R=[],S=!1;var ca=function(){for(var a=setTimeout(ca,0),b=M();R.length;)if(R.shift()(),50<M()-b)return;clearTimeout(a);S=!1};var da={},z={},fa={},T=!1;y(f,"beforeunload",function(){T=
!0;setTimeout(function(){T=!1},1E4)});var ha=/^prv:/,V={},H={},U={},B={},wa=0,Z=String.fromCharCode(92),u=[],oa=f.onerror;f.onerror=function(a,b,c,e,g){g&&"object"===typeof g||(g=Error(a,b,c),g.columnNumber=e,g.stack=b||c||e?q(Z,g.message,"at "+q(":",b,c,e)):E);var d=u.pop()||{};g.attribution=q(":",g.attribution||d.attribution,d.name);g.logLevel=d.logLevel;g.attribution&&console&&console.log&&console.log([g.logLevel||"ERROR",a,"thrown by",g.attribution].join(" "));u=[];oa&&(d=[].slice.call(arguments),
d[4]=g,oa.apply(f,d))};I.prototype={logError:function(a,b,c,e){b={message:b,logLevel:c||"ERROR",attribution:q(":",this.attribution,e)};if(f.ueLogError)return f.ueLogError(a||b,a?b:null),!0;console&&console.error&&(console.log(b),console.error(a));return!1},error:function(a,b,c,e){a=Error(q(":",e,a,c));a.attribution=q(":",this.attribution,b);throw a;},guardError:W(),guardFatal:W("FATAL"),guardCurrent:function(a){var b=u[u.length-1];return b?W(b.logLevel,b).call(this,a):a},guardTime:function(a){var b=
u[u.length-1],c=b&&b.name;return c&&c in B?function(){var b=w(),g=a.apply(this,arguments);B[c].async=(B[c].async||0)+w()-b;return g}:a},log:function(a,b,c){return this.logError(null,a,b,c)},declare:A([],!0,!0,!0),register:A([],!0),execute:A([]),AUI_BUILD_DATE:"3.21.4-2021-05-27",when:ia(),now:ia(!0),trigger:function(a,b,c){var e=M();this.declare(a,{data:b,pageElapsedTime:e-(f.aPageStart||NaN),triggerTime:e});c&&c.instrument&&O.when("prv:a-logTrigger").execute(function(b){b(a)})},handleTriggers:function(){this.log("handleTriggers deprecated")},
attributeErrors:function(a){return new I(a)},_namespace:function(a,b){return new I(a,b)}};var r=G(f,"AmazonUIPageJS",new I);var O=r._namespace("PageJS","AmazonUI");O.declare("prv:p-debug",B);r.declare("p-recorder-events",[]);r.declare("p-recorder-stop",function(){});G(f,"P",r);ja();if(h.addEventListener){var pa;h.addEventListener("DOMContentLoaded",pa=function(){r.trigger("a-domready");h.removeEventListener("DOMContentLoaded",pa,!1)},!1)}var n=h.documentElement,aa=function(){var a=["O","ms","Moz",
"Webkit"],b=h.createElement("div");return{testGradients:function(){return!0},test:function(c){var e=c.charAt(0).toUpperCase()+c.substr(1);c=(a.join(e+" ")+e+" "+c).split(" ");for(e=c.length;e--;)if(""===b.style[c[e]])return!0;return!1},testTransform3d:function(){return!0}}}();l=n.className;var qa=/(^| )a-mobile( |$)/.test(l),ra=/(^| )a-tablet( |$)/.test(l),k={audio:function(){return!!h.createElement("audio").canPlayType},video:function(){return!!h.createElement("video").canPlayType},canvas:function(){return!!h.createElement("canvas").getContext},
svg:function(){return!!h.createElementNS&&!!h.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect},offline:function(){return navigator.hasOwnProperty&&navigator.hasOwnProperty("onLine")&&navigator.onLine},dragDrop:function(){return"draggable"in h.createElement("span")},geolocation:function(){return!!navigator.geolocation},history:function(){return!(!f.history||!f.history.pushState)},webworker:function(){return!!f.Worker},autofocus:function(){return"autofocus"in h.createElement("input")},
inputPlaceholder:function(){return"placeholder"in h.createElement("input")},textareaPlaceholder:function(){return"placeholder"in h.createElement("textarea")},localStorage:function(){return"localStorage"in f&&null!==f.localStorage},orientation:function(){return"orientation"in f},touch:function(){return"ontouchend"in h},gradients:function(){return aa.testGradients()},hires:function(){var a=f.devicePixelRatio&&1.5<=f.devicePixelRatio||f.matchMedia&&f.matchMedia("(min-resolution:144dpi)").matches;t("hiRes"+
(qa?"Mobile":ra?"Tablet":"Desktop"),a?1:0);return a},transform3d:function(){return aa.testTransform3d()},touchScrolling:function(){return p(/Windowshop|android|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|Chrome|Silk|Firefox|Trident.+?; Touch/i)},ios:function(){return p(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)&&!p(/trident|Edge/i)},android:function(){return p(/android.([1-9]|[L-Z])/i)&&!p(/trident|Edge/i)},mobile:function(){return qa},tablet:function(){return ra},rtl:function(){return"rtl"===
n.dir}};for(m in k)k.hasOwnProperty(m)&&(k[m]=ka(k[m]));for(var ba="textShadow textStroke boxShadow borderRadius borderImage opacity transform transition".split(" "),P=0;P<ba.length;P++)k[ba[P]]=ka(function(){return aa.test(ba[P])});var K=!0,la=0,Y={w:0,h:0},L=4;J();y(f,"resize",function(){clearTimeout(la);L=4;J()});var sa={getItem:function(a){try{return f.localStorage.getItem(a)}catch(b){}},setItem:function(a,b){try{return f.localStorage.setItem(a,b)}catch(c){}}};n.className=X(n,"a-no-js");C(n,"a-js");
!p(/OS [1-8](_[0-9]*)+ like Mac OS X/i)||f.navigator.standalone||p(/safari/i)||C(n,"a-ember");l=[];for(m in k)k.hasOwnProperty(m)&&k[m]&&l.push("a-"+m.replace(/([A-Z])/g,function(a){return"-"+a.toLowerCase()}));C(n,l.join(" "));n.setAttribute("data-aui-build-date","3.21.4-2021-05-27");r.register("p-detect",function(){return{capabilities:k,localStorage:k.localStorage&&sa,toggleResponsiveGrid:xa,responsiveGridEnabled:ya}});p(/UCBrowser/i)||k.localStorage&&C(n,sa.getItem("a-font-class"));r.declare("a-event-revised-handling",
!1);try{var x=navigator.serviceWorker}catch(a){F("sw:nav_err")}x&&(y(x,"message",function(a){a&&a.data&&t(a.data.k,a.data.v)}),x.controller&&x.controller.postMessage("MSG-RDY"));var D=[];l={reg:{},unreg:{}};l.reg.browser={action:function(a,b){x.register("/service-worker.js").then(function(){t(a+"success")}).catch(function(c){r.logError(c,"[AUI SW] Failed to "+b+" service worker: ");t(a+"failure")})}};(function(a){var b=a.reg,c=a.unreg;x&&x.getRegistrations?(O.when("A").execute(function(a){na(a,c,
"unregister")}),y(f,"load",function(){O.when("A").execute(function(a){na(a,b,"register");ma()})})):(b&&b.browser&&D.push("sw:browser:register:unsupported"),c&&c.browser&&D.push("sw:browser:unregister:unsupported"),ma())})(l);r.declare("a-fix-event-off",!1);t("pagejs:pkgExecTime",w()-N)})(window,document,Date);
(function(b){function q(a,d,g){function u(a,b,e){var c=Array(d.length);~l&&(c[l]={});~m&&(c[m]=e);for(e=0;e<n.length;e++){var r=n[e],t=a[e];c[r]=t}for(e=0;e<p.length;e++)r=p[e],t=b[e],c[r]=t;a=g.apply(null,c);return~l?c[l]:a}"string"!==typeof a&&b.P.error("C001");-1===a.indexOf("@")&&-1<a.indexOf("/")&&-1===a.indexOf("^")&&(a=a.substring(0,a.lastIndexOf("/")));if(!v[a]){v[a]=!0;g||(g=d,d=[]);a=a.split(":",2);var c=a[1]?a[0]:void 0,h=(a[1]||a[0]).replace(/@capability\//,"@c/"),k=c?b.P._namespace(c):
b.P,w=!h.lastIndexOf("@c/",0),n=[];a=[];var p=[],x=[],m=-1,l=-1;for(c=0;c<d.length;c++){var f=d[c];"module"===f&&k.error("C002");"exports"===f?l=c:"require"===f?m=c:f.lastIndexOf("@p/",0)?f.lastIndexOf("@c/",0)?(n.push(c),a.push("mix:"+f)):(p.push(c),x.push(f)):(n.push(c),a.push(f.substr(3)))}k.when.apply(k,a).register("mix:"+h,function(){var a=[].slice.call(arguments);return w||~m||p.length?{capabilities:x,cardModuleFactory:function(b,c){b=u(a,b,c);b.P=k;return b},require:~m?q:void 0}:u(a,[],function(){})});
w&&k.when("mix:@amzn/mix.client-runtime","mix:"+h).execute(function(a,b){a.registerCapabilityModule(h,b)});k.when("mix:"+h).register("xcp:"+h,function(a){return a});var q=function(a,b,c){try{var d=a[0],e=d.lastIndexOf("./",0)?d:h+"/"+d.substr(2),f=e.lastIndexOf("@p/",0)?"mix:"+e:e.substr(3);k.when(f).execute(function(a){try{b(a)}catch(z){c(z)}})}catch(y){c(y)}}}}"use strict";var v={};b.mix_d||((b.Promise?P:P.when("3p-promise")).register("@p/promise-is-ready",function(a){b.Promise=b.Promise||a}),(Array.prototype.includes?
P:P.when("a-polyfill")).register("@p/polyfill-is-ready",function(){}),b.mix_d=function(a,b,g){P.when("@p/promise-is-ready","@p/polyfill-is-ready").execute("@p/mix-d-deps",function(){q(a,b,g)})},b.xcp_d=b.mix_d,P.when("mix:@amzn/mix.client-runtime").execute(function(a){P.declare("xcp:@xcp/runtime",a)}));b.mixTimeout||(b.mixTimeout=function(a,d,g){b.mixCardInitTimeouts||(b.mixCardInitTimeouts={});b.mixCardInitTimeouts[d]&&clearTimeout(b.mixCardInitTimeouts[d]);b.mixCardInitTimeouts[d]=setTimeout(function(){P.log("Client-side initialization timeout",
"WARN",a)},g)});b.mix_csa_map=b.mix_csa_map||{};b.mix_csa=b.mix_csa||function(a){try{return b.mix_csa_map[a]=b.mix_csa_map[a]||b.csa("Content",{element:document.querySelector(a)})}catch(d){return P.logError(d,"C004","ERROR",void 0),function(){}}}})(window);
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('sp.load.js').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61-6nKPKyWL.js?AUIClients/AmazonUIjQuery');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/11Y+5x+kkTL._RC|51106gSDnJL.js,11-zXBZR6KL.js,11giXtZCwVL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,01O9dYORveL.js,21NNXfMitSL.js,11rRjDLdAVL.js,51X-X0x2aRL.js,11kWu3cNjYL.js,11UNQpqeowL.js,11OREnu1epL.js,11KbZymw5ZL.js,21r53SJg7LL.js,0190vxtlzcL.js,51GBHgW1KPL.js,31KrK+dcMcL.js,01Gf12ogmOL.js,01ezj5Rkz1L.js,11VS-C+YWGL.js,31VpWkbgc1L.js,01rpauTep4L.js,01+b9cewx1L.js_.js?AUIClients/AmazonUI&qa9N+d93#page_type-Detail.348458-T1.309035-T1');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/51xLtn9VfzL.js?AUIClients/CardJsRuntimeBuzzCopyBuild');
});
</script>
<!-- sp:feature:cookie-consent-assets -->
<!-- sp:feature:nav-inline-css -->
<!-- NAVYAAN CSS -->
<style type="text/css">
.nav-sprite-v1 .nav-sprite, .nav-sprite-v1 .nav-icon {
  background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936603_.png);
  background-position: 0 1000px;
  background-repeat: repeat-x;
}
.nav-spinner {
  background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/javascripts/lib/popover/images/snake._CB485935611_.gif);
  background-position: center center;
  background-repeat: no-repeat;
}
.nav-timeline-icon, .nav-access-image, .nav-timeline-prime-icon {
  background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/timeline_sprite_1x._CB439967808_.png);
  background-repeat: no-repeat;
}
</style>
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41KBYOkTjIL._RC|71x73qye4hL.css,21-QxUt197L.css,31YZpDCYJPL.css,21MKjoYL8wL.css,41OiMQkB+EL.css,01yCq3WXEcL.css,11kO7yAgiQL.css,31OvHRW+XiL.css,01XHMOHpK1L.css,01ucgi+I44L.css,415g7iDx4VL.css_.css?AUIClients/NavDesktopUberAsset&le/6pyxY#desktop.331932-T1" />
<!-- sp:feature:host-assets -->


















    
    
















 
 
 
 



















 
 
 
 







<!-- htmlBeginMarker -->


    





















  





    













        
        
        
        
        
    
        
        
        


  
  
































  



    































  











  



        
        
        
        

  








    






















  




















<script type="text/javascript">
  P.when('atf').execute(function(){
    P.now('dpJsAssetsLoadMarker').execute(function(markerObj){
      if(!markerObj){
        P.declare('dpJsAssetsLoadMarker', {});
        if (window.ue && ue.count) {
          ue.count("DPJsLoadedAfterATFMarkedCount", 1);
        }
      }
    });
  });
</script>























<style>
.ap_popover_unsprited .ap_body .ap_left{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_left_17._V1_.png)}.ap_popover_unsprited .ap_body .ap_right{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_right_17._V1_.png)}.ap_popover_unsprited .ap_header .ap_left{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_top_left._V1_.png)}.ap_popover_unsprited .ap_header .ap_right{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_top_right._V1_.png)}.ap_popover_unsprited .ap_header .ap_middle{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_top._V1_.png)}.ap_popover_unsprited .ap_footer .ap_left{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_bottom_left._V1_.png)}.ap_popover_unsprited .ap_footer .ap_right{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_bottom_right._V1_.png)}.ap_popover_unsprited .ap_footer .ap_middle{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/po_bottom._V1_.png)}.ap_popover_sprited .ap_body .ap_left,.ap_popover_sprited .ap_body .ap_right{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/light/sprite-v._V1_.png)}.ap_popover_sprited .ap_closebutton,.ap_popover_sprited .ap_footer .ap_left,.ap_popover_sprited .ap_footer .ap_middle,.ap_popover_sprited .ap_footer .ap_right,.ap_popover_sprited .ap_header .ap_left,.ap_popover_sprited .ap_header .ap_middle,.ap_popover_sprited .ap_header .ap_right{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/light/sprite-h._V1_.png)}.ap_popover_sprited .ap_body .ap_left-arrow,.ap_popover_sprited .ap_body .ap_right-arrow{background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/light/sprite-arrow-v._V1_.png)}.ap_popover{position:absolute;outline:0}.ap_body{height:100%;min-height:36px;position:relative;background-color:#fff;margin:0 17px}.ap_body .ap_left,.ap_popover_sprited .ap_body .ap_left-arrow{width:17px;height:100%;position:absolute;top:0;left:-17px;background-attachment:scroll;background-repeat:repeat-y}.ap_popover_sprited .ap_body .ap_left{background-position:0 top}.ap_body .ap_right,.ap_popover_sprited .ap_body .ap_right-arrow{width:17px;height:100%;position:absolute;top:0;right:-17px;background-attachment:scroll;background-repeat:repeat-y}.ap_popover_sprited .ap_body .ap_right{background-position:-51px top}.ap_footer,.ap_header{position:relative;width:100%}.ap_footer *,.ap_header *{height:26px}.ap_header .ap_left{position:absolute;top:0;left:0;width:34px;background-attachment:scroll;background-repeat:no-repeat}.ap_popover_sprited .ap_header .ap_left{background-position:left -2px}.ap_header .ap_right{width:34px;position:absolute;top:0;right:0;background-attachment:scroll;background-repeat:no-repeat}.ap_popover_sprited .ap_header .ap_right{background-position:right -2px}.ap_header .ap_middle{margin:0 34px;background-attachment:scroll;background-repeat:repeat-x}.ap_popover_sprited .ap_header .ap_middle{background-position:0 -70px}.ap_footer .ap_left{position:absolute;top:0;left:0;width:34px;background-attachment:scroll;background-repeat:no-repeat}.ap_popover_sprited .ap_footer .ap_left{background-position:left -40px}.ap_footer .ap_right{width:34px;position:absolute;top:0;right:0;background-attachment:scroll;background-repeat:no-repeat}.ap_popover_sprited .ap_footer .ap_right{background-position:right -40px}.ap_footer .ap_middle{margin:0 34px;background-attachment:scroll;background-repeat:repeat-x}.ap_popover_sprited .ap_footer .ap_middle{background-position:0 -108px}.ap_popover .ap_titlebar{display:none;position:absolute;left:0;top:0;background-color:#EAF3FE;border-bottom:1px solid #C2DDF2;font-size:14px;font-weight:700;margin:8px 18px;white-space:nowrap;overflow:hidden}.ap_popover .ap_titlebar.multiline{white-space:normal;overflow:visible}.ap_popover .ap_titlebar .ap_title{padding:4px 0;margin-left:10px;overflow:hidden}#ap_overlay,#ap_overlay div{background-color:#3F4C58;width:100%;position:absolute;top:0;left:0;z-index:99}.ap_popover .ap_close{position:absolute;right:18px;top:13px}.ap_popover .ap_close a{padding:5px;text-decoration:none;outline:0}.ap_popover .ap_close .ap_closetext{display:none;margin-right:5px;line-height:1em}.ap_popover .ap_closebutton{display:-moz-inline-box;display:inline-block;width:15px;height:15px;background-repeat:no-repeat;background-position:0 -136px;position:relative;overflow:hidden;vertical-align:top}.ap_popover .ap_closebutton span{position:absolute;top:-9999px}.ap_popover .ap_close img{vertical-align:top}.ap_classic{border-top:1px solid #ccc;border-left:1px solid #ccc;border-bottom:1px solid #2F2F1D;border-right:1px solid #2F2F1D;background-color:#EFEDD4;padding:3px}.ap_classic .ap_titlebar{color:#86875D;font-size:12px;padding:0 0 3px 0;line-height:1em}.ap_classic .ap_close{float:right}.ap_classic .ap_content{clear:both;background-color:#fff;border:1px solid #ACA976;padding:8px;font-size:11px}
</style>
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01j2xsQ1yML.css?AUIClients/DetailPageMetaAssetFixed#desktop" />
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/11xqfyHx1TL._RC|11B3-fvRFzL.css_.css?AUIClients/AmazonUICalendar#not-trident" />
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/61OvCWp7nBL._RC|11bRdV2t20L.css,518KmQy9QVL.css,01g2EoxOu-L.css,21U6+8tKunL.css,315GMAwkLiL.css,218Y6Z0tipL.css,01rdVnPkgmL.css,01KvCqKMBgL.css,11iwHtffX1L.css,41IYcMQCjlL.css,21ByukFKG4L.css,01N8OOpUZPL.css,0121zKjk26L.css,11xRy3bSkOL.css,31lgsyNHOIL.css,515MV+FiFKL.css,11kmwdXfY5L.css,01vUDet4b1L.css,01HIwjet0ZL.css,31l-Nc5zsiL.css,01bkkYjxP7L.css,01Qji-D4YPL.css,01NW8VTUeVL.css,01rgQ3jqo7L.css,01zWxM9Vh0L.css,01n8CeLW9QL.css,21jUQU6VhYL.css,31TJtSmBkXL.css,21PjfsP9YvL.css,114HJAY+ShL.css,21VgVEzltcL.css,21ZjVyQPjML.css,21ohnckzsnL.css,01iXxkJ+wuL.css,31YeUjpBngL.css,017KStdmPkL.css,11jG57OztzL.css,01eviB7YqCL.css,01goIIPoVxL.css_.css?AUIClients/MusicDetailPageMetaAsset_TURBO_DESKTOP&uPWdPvVz#desktop.ca.113788-C.336056-T1.343686-C.310456-T1.237182-T1.172402-T1.309439-T1.94145-T1.109378-T1.169593-T1" />
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/31Le0m%2BQe-L.css?AUIClients/DetailPageAllOffersDisplayAssets&O9eWV6N/#310975-T1" />



<script>
(function(d,b,m){function c(a){return"--private-amznjqshim-"+a}function e(a,l){var b=c(l);d.now(b).execute(c(a+"-"+b)+"-"+f++,function(a){void 0===a&&d.declare(b,!0)})}function h(a){e("markRequested","functionality-requested:"+a)}function g(a){e("completedStage","stage-"+a)}b.goN2Debug||(b.goN2Debug={info:function(){}});"use strict";var f=0,k=b.amznJQ=new function(){this.addLogical=this.addStyle=this.addStyles=this.PLNow=this.windowOnLoad=function(){};this.declareAvailable=function(a){e("declaring",
a)};this.available=function(a,b){a=c(a);h(a);d.when(a,c("jQuery")).execute(c("available-"+a)+"-"+f++,b)};this.onReady=function(a,b){a=c(a);h(a);d.when(a,"a-domready",c("jQuery")).execute(c("onReady-"+a)+"-"+f++,b)};this.onCompletion=function(a,b){var e=c("stage-"+a);d.when(e,c("jQuery")).execute(b)};this.completedStage=function(a){g(a)};this.addPL=function(a){d.when("a-preload").execute(c("Preloader")+"-"+f++,function(b){b.preload(a)})};this.strings={};this.chars={}};d.when("load").execute(c("fail-safe-stages"),
function(){g("amznJQ.theFold");g("amznJQ.criticalFeature")});d.when("jQuery").execute("define amznJQ jQuery",function(a){b.jQuery||(b.jQuery=a);k.jQuery||(k.jQuery=a);e("declaring","jQuery")})})(window.P||window.AmazonUIPageJS,window,document);
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('atf').execute(function(){
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/41RcpofQp-L.js?AUIClients/AmazonPopoversAUIShim#ca');
});
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('injectCalendarOnDetailPage').execute(function(){
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/31cu23aPw1L.js?AUIClients/AmazonUICalendar');
});
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('dpJsAssetsLoadMarker').execute(function(){
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61jl8YsxhUL._RC|01XginIhPBL.js,01PQKs49DyL.js_.js?AUIClients/DetailPageDesktopImageBlockMetaAsset&EIhgIZq+#169593-T1.299993-T1');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/31Nnd8dHj4L._RC|21TMrbNilEL.js,21YblE14ZTL.js,21E2aIDj6DL.js,31Nb5hZQizL.js,21KJ58XxAlL.js,219O6ZmDMOL.js,31oAl8dJC2L.js,41+DnZtRZiL.js,31TF9TzobmL.js,316nVZ1c+gL.js,21u1PnPEsML.js,318rs4piGPL.js,21yt7ipCe9L.js,41YPX4YDpjL.js,11+dypSOVUL.js,01WNBm1NhqL.js,41mj+87W1ML.js,71LXbtOXb4L.js,01X5C8pWB1L.js,01Fy9QPljuL.js,41lkyHEebjL.js,01jqyAujTwL.js,31+0pACITzL.js,318iw3j-82L.js,31KyLb404wL.js,01g2etah0NL.js,01X2zigX4kL.js,01OtvpwikQL.js,31qUdoxPE8L.js,11nOzlnr6+L.js,41p3KVnq7iL.js,11p0nLfNCcL.js,11iHZuQapKL.js,21qOGqjcM7L.js,611uA7Z80VL.js,013eoEBTVUL.js,016QFWAAdML.js,51tG8ZFBvkL.js,01hkseOXj6L.js,311A0yCIeJL.js,01iRN5bMQkL.js,51jKqMrt8zL.js,11qajewhV-L.js,01TQyo0bnIL.js,11bdX9xnYpL.js,013aNY++XJL.js,11pS0Syz0DL.js,51RL3cCksuL.js,018ZxeiHuPL.js,011VhuFIPDL.js,21IQl4blS4L.js,01HPCJZdF6L.js,61BHCbTQZEL.js,218Qx5H6s4L.js,01WEY0XphhL.js_.js?AUIClients/MusicDetailPageMetaAsset_TURBO_DESKTOP&ckAULYXW#desktop.ca.292695-C.312885-T1.195406-T1.349527-T1.322640-T1.322857-T1.317356-T1.310834-T1.184660-C.310975-T1.309439-T1.184219-T1.109378-T1.227612-T1.311239-T1.227610-T4.169593-T1');
});
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('aodIngressClick').execute(function(){
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61ujJ6QAjKL.js?AUIClients/DetailPageAllOffersDisplayAssets&Cnrj+10S#language-en.341404-T1.355883-T1.310975-T1');
});
</script>







        
    









    
    
        
        












        


    
















<script type="text/javascript">
var iUrl = "https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L.__AC_SX300_SY300_QL70_ML2_.jpg";
(function(){var i=new Image; i.src = iUrl;})();
</script>



















  

   

    







        







        <script type="a-state" data-a-state="{&quot;key&quot;:&quot;metrics-schema&quot;}">{"widgetSchema":"dp:widget:","dimensionSchema":"dp:dims:"}</script>




        






  
























 
 
 

 
 



















    

      









        







































    
    
    
    


















        





    
    






  


    












<style type="text/css">

  #cm_cr_dpwidget .a-size-micro {
    font-size: 9px;
  } 

  #cm_cr_dpwidget .c7yTopDownDashedStrike {
    border-top: 1px dashed #A9A9A9;
    border-bottom: 1px dashed #A9A9A9;
  }

  #cm_cr_dpwidget .c7yBadgeAUI {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 2px;
    white-space: nowrap;
  }

</style>







<style type="text/css"><!-- Remote config blank inline CSS -->

  
    .tagEdit {
      padding-bottom:4px;
      padding-top:4px;
    }

    .edit-tag {
      width: 155px;
      margin-left: 10px;
    }

    .list-tags {
      white-space: nowrap;
      padding: 1px 0px 0px 0px;
    }

   #suggest-table {
      display: none;
      position: absolute;
      z-index: 2;
      background-color: #fff;
      border: 1px solid #9ac;
    }

    #suggest-table tr td{
      color: #333;
      font: 11px Verdana, sans-serif;
      padding: 2px;
    }

    #suggest-table tr.hovered {
      color: #efedd4;
      background-color: #9ac;
    }

  
  .see-popular {
    padding: 1.3em 0 0 0;
  }

  .tag-cols {
    border-collapse: collapse;
  }

  .tag-cols td {
    vertical-align: top;
    width: 250px;
    padding-right: 30px;
  }

  .tag-cols .tag-row {
    padding: 0 0 7px 0px;
  }

  .tag-cols .see-all {
    white-space: nowrap;
    padding-top: 5px;
  }

  .tags-piles-feedback {
    display: none;
    color: #000;
    font-size: 0.9em;
    font-weight: bold;
    margin: 0px 0 0 0;
   }

  .tag-cols i {
    display: none;
    cursor: pointer;
    cursor: hand;
    float: left;
    font-style: normal;
    font-size: 0px;
    vertical-align: bottom;
    width: 16px;
    height: 16px;
    margin-top: 1px;
    margin-right: 3px;
  }

  .tag-cols .snake {
    display: block;
    background: url('https://images-na.ssl-images-amazon.com/images/G/15/x-locale/communities/tags/graysnake._CB485934236_.gif');
  }

  #tagContentHolder .tip {
    display: none;
    color: #999;
    font-size: 10px;
    padding-top: 0.25em;
  }

  #tagContentHolder .tip a {
    color: #999 !important;
    text-decoration: none !important;
    border-bottom: solid 1px #CCC;
  }

  .nowrap {
    white-space: nowrap;
  }

  #tgEnableVoting {
    display: none;
  }

  #tagContentHolder .count {
    color: #666;
    font-size: 10px;
    margin-left: 3px;
    white-space: nowrap;
  }

  .count.tgVoting {
    cursor: pointer;
  }

  .tgVoting .tgCounter {
    margin-right: 3px;
    border-bottom: 1px dashed #003399;
    color: #003399;
  }


.c2c-inline-sprite {
    display: -moz-inline-box;
    display: inline-block;
    margin: 0;padding: 0; 
    position: relative;
    overflow: hidden;
    vertical-align: middle;
    background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/electronics/click2call/click2call-sprite._CB485946169_.png);
    background-repeat: no-repeat;
}
.c2c-inline-sprite span {
    position:absolute;
    top:-9999px;
}

.dp-call-me-button {
    width:52px;
    height:22px;
    background-position:0px -57px; 
}


/* Different sprites/images used CSS Start */
.swSprite {background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/common/sprites/sprite-site-wide._CB485920635_.png); }
.dpSprite {background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/common/sprites/sprite-dp-2._CB485928127_.png); }
.wl-button-sprite {background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/x-locale/communities/wishlist/add-to-wl-button-sprite.gif); }
.cBoxTL, .cBoxTR, .cBoxBL, .cBoxBR { background-image:url(https://images-na.ssl-images-amazon.com/images/G/15/common/sprites/sprite-site-wide-2._CB485929249_.png); }
.auiTestSprite { background: url(https://images-na.ssl-images-amazon.com/images/G/15/nav2/images/sprite-carousel-btns-stars2.png) no-repeat scroll 0 0 transparent; }
span.amtchelp { background: url(https://images-na.ssl-images-amazon.com/images/G/15/SellerForums/amz/images/help-16x16.gif) no-repeat scroll right bottom transparent; }
.shuttleGradient { background: url(https://images-na.ssl-images-amazon.com/images/G/15/x-locale/communities/customerimage/shuttle-gradient._CB485934796_.gif); }
.twisterPopoverArrow { background: url(https://images-na.ssl-images-amazon.com/images/G/15/gateway/csw/tri-down._CB485946746_.png); }
#finderUpdateButton img, #finderShowMoreDevicesLink, #finderHideMoreDevicesLink {background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/nav2/finders/finder-fits-sprites.gif);}
.cmtySprite { background-image: url(https://images-na.ssl-images-amazon.com/images/G/15/common/sprites/sprite-communities._CB485929161_.png); background-repeat: no-repeat; }

/* Different sprites/images used CSS End */



/* Best Seller Badging */


  .medSprite { background-image: url('https://images-na.ssl-images-amazon.com/images/G/15/common/sprites/sprite-media-platform._CB485924203_.png'); background-repeat: no-repeat; }

</style>












<script language="Javascript1.1" type="text/javascript">
<!--
function amz_js_PopWin(url,name,options){
  var ContextWindow = window.open(url,name,options);
  ContextWindow.focus();
  return false;
}
//-->
</script>


        
        
        
            
        
    
    
        
        
            
            
        
        









<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />






<link rel="canonical" href="https://www.amazon.ca/Rage-Against-Machine/dp/B0000028RR" />
<meta name="description" content="Rage Against The Machine: Rage Against The Machine: Amazon.ca: Music" />
<meta name="title" content="Rage Against The Machine: Rage Against The Machine: Amazon.ca: Music" />

<meta name="keywords" content="Rage Against The Machine,Rage Against The Machine,Sony Music Canada Entertainment Inc.,Pop,Rock,Alternative,Explicit Version,Heavy Metal,Explicit Version,Heavy Metal" />
<title>Rage Against The Machine: Rage Against The Machine: Amazon.ca: Music</title>












<style type="text/css">

  #cm_cr_dpwidget .a-size-micro {
    font-size: 9px;
  } 

  #cm_cr_dpwidget .c7yTopDownDashedStrike {
    border-top: 1px dashed #A9A9A9;
    border-bottom: 1px dashed #A9A9A9;
  }

  #cm_cr_dpwidget .c7yBadgeAUI {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 2px;
    white-space: nowrap;
  }

</style>







<script type="text/javascript">

// =============================================================================
// Function Class: Show/Hide product promotions & special offers link
// =============================================================================

function showElement(id) {
  var elm = document.getElementById(id);
  if (elm) {
    elm.style.visibility = 'visible';
    if (elm.getAttribute('name') == 'heroQuickPromoDiv') {
      elm.style.display = 'block';
    }
  }
}
function hideElement(id) {
  var elm = document.getElementById(id);
  if (elm) {
    elm.style.visibility = 'hidden';
    if (elm.getAttribute('name') == 'heroQuickPromoDiv') {
      elm.style.display = 'none';
    }
  }
}
function showHideElement(h_id, div_id) {
  var hiddenTag = document.getElementById(h_id);
  if (hiddenTag) {
    showElement(div_id);
  } else {
    hideElement(div_id);
  }
}

    if(typeof P === 'object' && typeof P.when === 'function'){
    P.register("isLazyLoadWeblabEnabled", function(){
        var  isWeblabEnabled = 1;
        return isWeblabEnabled;
      });
    }

	window.isBowserFeatureCleanup = 0;
	
var touchDeviceDetected = false;



        P.register('sp.load.critical.js');
            P.when('atf').execute(function(){
              P.now('sp.load.js').execute(function(jsObj){
                if(!jsObj){
                  P.declare('sp.load.js', {});
                  if (window.ue && ue.count) {
                    ue.count("jsLoadedAfterATFMarkedCount", 1);
                  }
                }
              });
            });


var CSMReqs={af:{c:2,p:'atf'},cf:{c:2,p:'cf'},x1:{c:1,p:'x1'},x2:{c:1,p:'x2'}};
function setCSMReq(a){
    a=a.toLowerCase();
    var b=CSMReqs[a];
    if(b&&--b.c==0){
        if(typeof uet=='function'){uet(a); (a == 'af') && (typeof replaceImg === 'function') && replaceImg();};
        if(typeof P != 'undefined'){
            P.register(b.p);
            if(a == 'af') {
                if(typeof uet === 'function') {
                    uet('bb', 'TwisterAUIWait', {wb: 1});
                }
            }
        };
    }
}
if(typeof P != 'undefined') {
    P.when('A').execute(function(A) {
        if(typeof uet === 'function') {
            uet('af', 'TwisterAUIWait', {wb: 1});
        }
    });
}

var addlongPoleTag = function(marker,customtag){
    marker=marker.toLowerCase();
    var b=CSMReqs[marker];
    if(b.c == 0){
        if(window.ue && typeof ue.tag === 'function') {
            ue.tag(customtag);
        }
    }
};


var gbEnableTwisterJS  = 0;
var isTwisterPage = 0;
</script>











<style type="text/css">

/* Override for Native DropDown changes */
       #buybox_feature_div .a-native-dropdown, #buybox .a-native-dropdown { opacity: 1; filter: alpha(opacity=100); z-index: auto; position: static; display: inline; font-weight: normal;}
       #buybox_feature_div label.a-native-dropdown, #buybox label.a-native-dropdown {padding-right: 5px;}
       #buybox_feature_div .a-dropdown-container .a-button-dropdown, #buybox .a-dropdown-container .a-button-dropdown  { display: none !important;}
      #twister .a-native-dropdown { display: inline; opacity:1; filter: alpha(opacity=100); z-index: auto; position: static; } #twister .a-dropdown-container span.a-button-dropdown { display: none !important } 
     #buybox_feature_div #OneClickBox, #buybox #OneClickBox { text-align:center;}
     #buybox_feature_div #oneClickAvailable, #buybox #oneClickAvailable { text-align:center;}
     #defaultChildDropdown_feature_div .a-native-dropdown { display: inline;}
     #defaultChildDropdown_feature_div .a-dropdown-container .a-button-dropdown { display: none !important;}

</style>

<script type="text/javascript">


P.when("p-detect").execute(function() {
    var h = document.documentElement;
    h.className = h.className.replace(/(^|\b)a-touch(\b|$)/g,"");
});

window.weblabs = {};

</script>


 <script type="text/javascript">
P.now().execute('dp-create-feature-interactive-api', function () {
    if (typeof uet === 'function'){
        uet('bb', 'clickToCI', {wb: 1});
    }
    var records = [], timeToInteractiveObj;
    window.markFeatureRender = function (fName, options) {
        updateFeatureList(fName, options, 'render');
    };
    window.markFeatureInteractive = function (fName, options) {
        updateFeatureList(fName, options, 'interactive');
    };
    function updateFeatureList(fName, options, type) {
        var record = {
            name: fName,
            options: options,
            type: type,
            timestamp: +new Date
        };
        if (timeToInteractiveObj) {
            timeToInteractiveObj.updateFeatures([record]);
        } else {
            records.push(record);
        }
    }
    P.when('dp-time-to-interactive').execute('dp-update-interactive-feature-list', function (obj) {
        timeToInteractiveObj = obj;
        if (records.length) {
            timeToInteractiveObj.updateFeatures(records);
        }
    });
}); </script>

<!--&&&Portal&Delimiter&&&--><!-- sp:end-feature:host-assets -->
<script type='text/javascript'>
window.ue_ihe = (window.ue_ihe || 0) + 1;
if (window.ue_ihe === 1) {
(function(k,l,g){function m(a){c||(c=b[a.type].id,"undefined"===typeof a.clientX?(e=a.pageX,f=a.pageY):(e=a.clientX,f=a.clientY),2!=c||h&&(h!=e||n!=f)?(r(),d.isl&&l.setTimeout(function(){p("at",d.id)},0)):(h=e,n=f,c=0))}function r(){for(var a in b)b.hasOwnProperty(a)&&d.detach(a,m,b[a].parent)}function s(){for(var a in b)b.hasOwnProperty(a)&&d.attach(a,m,b[a].parent)}function t(){var a="";!q&&c&&(q=1,a+="&ui="+c);return a}var d=k.ue,p=k.uex,q=0,c=0,h,n,e,f,b={click:{id:1,parent:g},mousemove:{id:2,
parent:g},scroll:{id:3,parent:l},keydown:{id:4,parent:g}};d&&p&&(s(),d._ui=t)})(ue_csm,window,document);


(function(s,l){function m(b,e,c){c=c||new Date(+new Date+t);c="expires="+c.toUTCString();n.cookie=b+"="+e+";"+c+";path=/"}function p(b){b+="=";for(var e=n.cookie.split(";"),c=0;c<e.length;c++){for(var a=e[c];" "==a.charAt(0);)a=a.substring(1);if(0===a.indexOf(b))return decodeURIComponent(a.substring(b.length,a.length))}return""}function q(b,e,c){if(!e)return b;-1<b.indexOf("{")&&(b="");for(var a=b.split("&"),f,d=!1,h=!1,g=0;g<a.length;g++)f=a[g].split(":"),f[0]==e?(!c||d?a.splice(g,1):(f[1]=c,a[g]=
f.join(":")),h=d=!0):2>f.length&&(a.splice(g,1),h=!0);h&&(b=a.join("&"));!d&&c&&(0<b.length&&(b+="&"),b+=e+":"+c);return b}var k=s.ue||{},t=3024E7,n=ue_csm.document||l.document,r=null,d;a:{try{d=l.localStorage;break a}catch(u){}d=void 0}k.count&&k.count("csm.cookieSize",document.cookie.length);k.cookie={get:p,set:m,updateCsmHit:function(b,e,c){try{var a;if(!(a=r)){var f;a:{try{if(d&&d.getItem){f=d.getItem("csm-hit");break a}}catch(k){}f=void 0}a=f||p("csm-hit")||"{}"}a=q(a,b,e);r=a=q(a,"t",+new Date);
try{d&&d.setItem&&d.setItem("csm-hit",a)}catch(h){}m("csm-hit",a,c)}catch(g){"function"==typeof l.ueLogError&&ueLogError(Error("Cookie manager: "+g.message),{logLevel:"WARN"})}}}})(ue_csm,window);


(function(l,e){function c(b){b="";var c=a.isBFT?"b":"s",d=""+a.oid,g=""+a.lid,h=d;d!=g&&20==g.length&&(c+="a",h+="-"+g);a.tabid&&(b=a.tabid+"+");b+=c+"-"+h;b!=f&&100>b.length&&(f=b,a.cookie?a.cookie.updateCsmHit(m,b+("|"+ +new Date)):e.cookie="csm-hit="+b+("|"+ +new Date)+n+"; path=/")}function p(){f=0}function d(b){!0===e[a.pageViz.propHid]?f=0:!1===e[a.pageViz.propHid]&&c({type:"visible"})}var n="; expires="+(new Date(+new Date+6048E5)).toGMTString(),m="tb",f,a=l.ue||{},k=a.pageViz&&a.pageViz.event&&
a.pageViz.propHid;a.attach&&(a.attach("click",c),a.attach("keyup",c),k||(a.attach("focus",c),a.attach("blur",p)),k&&(a.attach(a.pageViz.event,d,e),d({})));a.aftb=1})(ue_csm,ue_csm.document);


ue_csm.ue.stub(ue,"impression");


ue.stub(ue,"trigger");



if(window.ue&&uet) { uet('bb'); }

}
</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 2729)</script>
<!-- sp:feature:head-close -->
<script>
window.P && P.register('bb');
if (typeof ues === 'function') {
  ues('t0', 'portal-bb', new Date());
  ues('ctb', 'portal-bb', 1);
}
</script>
</head><!-- sp:feature:start-body -->
<body class="a-aui_72554-c a-aui_button_aria_label_markup_348458-t1 a-aui_csa_templates_buildin_ww_exp_337518-t1 a-aui_csa_templates_buildin_ww_launch_337517-c a-aui_csa_templates_declarative_ww_exp_337521-t1 a-aui_csa_templates_declarative_ww_launch_337520-c a-aui_dynamic_img_a11y_markup_345061-c a-aui_mm_desktop_exp_291916-c a-aui_mm_desktop_launch_291918-c a-aui_mm_desktop_targeted_exp_291928-c a-aui_mm_desktop_targeted_launch_291922-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c"><div id="a-page"><script type="a-state" data-a-state="{&quot;key&quot;:&quot;a-wlab-states&quot;}">{"AUI_BUTTON_ARIA_LABEL_MARKUP_348458":"T1","AUI_MM_DESKTOP_LAUNCH_291918":"C","AUI_TNR_V2_180836":"C","AUI_PRELOAD_261698":"C","AUI_CSA_TEMPLATES_BUILDIN_WW_EXP_337518":"T1","AUI_72554":"C","AUI_MM_DESKTOP_TARGETED_EXP_291928":"C","AUI_CSA_TEMPLATES_DECLARATIVE_WW_LAUNCH_337520":"C","AUI_CSA_TEMPLATES_BUILDIN_WW_LAUNCH_337517":"C","AUI_PCI_RISK_BANNER_210084":"C","AUI_CSA_TEMPLATES_DECLARATIVE_WW_EXP_337521":"T1","AUI_MM_DESKTOP_TARGETED_LAUNCH_291922":"C","AUI_MM_DESKTOP_EXP_291916":"C","AUI_TEMPLATE_WEBLAB_CACHE_333406":"C","AUI_DYNAMIC_IMG_A11Y_MARKUP_345061":"C","AUI_REL_NOREFERRER_NOOPENER_309527":"C"}</script><script>typeof uex === 'function' && uex('ld', 'portal-bb', {wb: 1})</script>

<script>
!function(){function n(n,t){var r=i(n);return t&&(r=r("instance",t)),r}var r=[],c=0,i=function(t){return function(){var n=c++;return r.push([t,[].slice.call(arguments,0),n,{time:Date.now()}]),i(n)}};n._s=r,this.csa=n}();;
csa('Config', {"CacheDetection.CDNCacheFix":true});
if (window.csa) {
    csa("Config", {
        'Application': 'Retail:Prod:www.amazon.ca',
        'Events.Namespace': 'csa',
        'ObfuscatedMarketplaceId': 'A2EUQ1WTGCTBG2',
        'Events.SushiEndpoint': 'https://unagi.amazon.ca/1/events/com.amazon.csm.csa.prod',
        'CacheDetection.RequestID': "1KMDY2JPGP2X3R80G8WC",
        'CacheDetection.Callback': window.ue && ue.reset,
        'LCP.elementDedup': 1
    });

    csa("Events")("setEntity", {
        page: {requestId: "1KMDY2JPGP2X3R80G8WC", meaningful: "interactive"},
        session: {id: "138-4669640-7712440"}
    });
}
!function(e){var i,r,o="splice",u=e.csa,f={},c={},a=e.csa._s,s=0,l={},g={},h={},n=Object.keys;function t(n,t){return u(n,t)}function v(n,t){var e=c[n]||{};U(e,t),c[n]=e,y(E,0)}function d(n,t,e){var i=!0;t=b(t),e&&e.buffered&&(i=(h[n]||[]).every(function(n){return!1!==t(n)})),i&&(l[n]||(l[n]=[]),l[n].push(t))}function p(n,t){if(t=b(t),n in g)t(g[n]);else{d(n,function(n){return t(n),!1})}}function m(n,t){if(u("Errors")("logError",n),f.DEBUG)throw t||n}function w(){return Math.abs(4294967295*Math.random()|0).toString(36)}function b(n,t){return function(){try{return n.apply(this,arguments)}catch(n){m(n.message||n,n)}}}function y(n,t){return e.setTimeout(b(n),t)}function E(){for(var n=0;n<a.length;){var t=a[n],e=t[0]in c;if(!e&&!r)return void(s=t.length);e?(a[o](s=n,1),D(t)):n++}}function D(n){var arguments,t=c[n[0]],e=(arguments=n[1])[0];if(!t||!t[e])return m("Undefined function: "+t+"/"+e);i=n[3],c[n[2]]=t[e].apply(t,arguments.slice(1))||{},i=0}function S(){r=1,E()}function U(t,e){n(e).forEach(function(n){t[n]=e[n]})}p("$beforeunload",S),v("Config",{instance:function(n){U(f,n)}}),u.plugin=b(function(n){n(t)}),t.config=f,t.register=v,t.on=d,t.removeListener=function(n,t){var e=l[n];e&&e[o](e.indexOf(t),1)},t.once=p,t.emit=function(n,t,e){for(var i=l[n]||[],r=0;r<i.length;)!1===i[r](t)?i[o](r,1):r++;g[n]=t||{},e&&e.buffered&&(h[n]||(h[n]=[]),100<=h[n].length&&h[n].shift(),h[n].push(t||{}))},t.UUID=function(){return[w(),w(),w(),w()].join("-")},t.time=function(n){var t=i?new Date(i.time):new Date;return"ISO"===n?t.toISOString():t.getTime()},t.error=m,t.warn=function(n,t){if(u("Errors")("logWarn",n),f.DEBUG)throw t||n},t.exec=b,t.timeout=y,t.interval=function(n,t){return e.setInterval(b(n),t)},(t.global=e).csa._s.push=function(n){n[0]in c&&(!a.length||r)?D(n):a[o](s++,0,n)},E(),y(function(){y(S,f.SkipMissingPluginsTimeout||5e3)},1)}("undefined"!=typeof window?window:global);csa.plugin(function(o){var r="addEventListener",e="requestAnimationFrame",t=o.exec,i=o.global,f=o.on;o.raf=function(n){if(i[e])return i[e](t(n))},o.on=function(n,e,t,i){return n&&"function"==typeof n[r]?n[r](e,o.exec(t),i):"string"==typeof n?f(n,e,t,i):void 0}});csa.plugin(function(o){var t,n,r={},e="localStorage",c="sessionStorage",a="local",i="session",u=o.exec;function s(e,t){var n;try{r[t]=!!(n=o.global[e]),n=n||{}}catch(e){r[t]=!(n={})}return n}function f(){t=t||s(e,a),n=n||s(c,i)}function l(e){return e&&e[i]?n:t}o.store=u(function(e,t,n){f();var o=l(n);return e?t?void(o[e]=t):o[e]:Object.keys(o)}),o.storageSupport=u(function(){return f(),r}),o.deleteStored=u(function(e,t){f();var n=l(t);if("function"==typeof e)for(var o in n)n.hasOwnProperty(o)&&e(o,n[o])&&delete n[o];else delete n[e]})});csa.plugin(function(o){function r(n){return function(r){o("Metrics",{producerId:"csa",dimensions:{message:r}})("recordMetric",n,1)}}o.register("Errors",{logError:r("jsError"),logWarn:r("jsWarn")})});csa.plugin(function(r){var o,e=r.global,i=r("Events"),f=e.location,d=e.document,a=((e.performance||{}).navigation||{}).type,t=r.on,u=r.emit,g={};function n(a,e){var t=!!o,n=(e=e||{}).keepPageAttributes;t&&(u("$beforePageTransition"),u("$pageTransition")),t&&!n&&i("removeEntity","page"),o=r.UUID(),n?g.id=o:g={schemaId:"<ns>.PageEntity.1",id:o,url:f.href,server:f.hostname,path:f.pathname,referrer:d.referrer,title:d.title},Object.keys(a||{}).forEach(function(e){g[e]=a[e]}),i("setEntity",{page:g}),u("$pageChange",g,{buffered:1}),t&&u("$afterPageTransition")}function l(){u("$load"),u("$ready"),u("$afterload")}function s(){u("$ready"),u("$beforeunload"),u("$unload"),u("$afterunload")}f&&d&&(t(e,"beforeunload",s),t(e,"pagehide",s),"complete"===d.readyState?l():t(e,"load",l),r.register("SPA",{newPage:n}),n({transitionType:{0:"hard",1:"refresh",2:"back-button"}[a]||"unknown"}))});csa.plugin(function(c){var t="Events",e="UNKNOWN",a="id",u="all",n="messageId",i="timestamp",f="producerId",o="application",r="obfuscatedMarketplaceId",s="entities",d="schemaId",l="version",p="attributes",v="<ns>",g=c.config,h=(c.global.location||{}).host,m=g[t+".Namespace"]||"csa_other",I=g.Application||"Other"+(h?":"+h:""),b=c("Transport"),y={},O=function(t,e){Object.keys(t).forEach(e)};function E(n,i,o){O(i,function(t){var e=o===u||(o||{})[t];t in n||(n[t]={version:1,id:i[t][a]||c.UUID()}),U(n[t],i[t],e)})}function U(e,n,i){O(n,function(t){!function(t,e,n){return"string"!=typeof e&&t!==l?c.error("Attribute is not of type string: "+t):!0===n||1===n||(t===a||!!~(n||[]).indexOf(t))}(t,n[t],i)||(e[t]=n[t])})}function N(o,t,r){O(t,function(t){var e=o[t];if(e[d]){var n={},i={};n[a]=e[a],n[f]=e[f]||r,n[d]=e[d],n[l]=e[l]++,n[p]=i,S(n),U(i,e,1),k(i),b("log",n)}})}function S(t){t[i]=function(t){return"number"==typeof t&&(t=new Date(t).toISOString()),t||c.time("ISO")}(t[i]),t[n]=t[n]||c.UUID(),t[o]=I,t[r]=g.ObfuscatedMarketplaceId||e,t[d]=t[d].replace(v,m)}function k(t){delete t[l],delete t[d],delete t[f]}function w(o){var r={};this.log=function(t,e){var n={},i=(e||{}).ent;return t?"string"!=typeof t[d]?c.error("A valid schema id is required for the event"):(S(t),E(n,y,i),E(n,r,i),E(n,t[s]||{},i),O(n,function(t){k(n[t])}),t[f]=o[f],t[s]=n,void b("log",t)):c.error("The event cannot be undefined")},this.setEntity=function(t){E(r,t,u),N(r,t,o[f])}}g["KillSwitch."+t]||c.register(t,{setEntity:function(t){E(y,t,u),N(y,t,"csa")},removeEntity:function(t){delete y[t]},instance:function(t){return new w(t)}})});csa.plugin(function(s){var c,l="Transport",g="post",u="preflight",r="csa.cajun.",i="store",a="deleteStored",f="sendBeacon",t=0,e=s.config[l+".BufferSize"]||2e3,h=s.config[l+".RetryDelay"]||1500,o=[],p=0,d=[],v=s.global,n=s.on,y=s.once,m=v.document,E=s.timeout,R=s.config[l+".FlushInterval"]||5e3,S=0;function b(n){if(864e5<s.time()-+new Date(n.timestamp))return s.warn("Event is too old: "+n);p<e&&(o.push(n),p++,!S&&t&&(S=E(w,R)))}function w(){d.forEach(function(t){var e=[];o.forEach(function(n){t.accepts(n)&&e.push(n)}),e.length&&(t.chunks?t.chunks(e).forEach(function(n){I(t,n)}):I(t,e))}),o=[],S=0}function I(t,e){function o(){s[a](r+n)}var n=s.UUID();s[i](r+n,JSON.stringify(e)),[function(n,t,e){var o=v.navigator||{},r=v.cordova||{};if(!o[f]||!n[g])return 0;n[u]&&r&&"ios"===r.platformId&&!c&&((new Image).src=n[u]().url,c=1);var i=n[g](t);if(!i.type&&o[f](i.url,i.body))return e(),1},function(n,t,e){if(!n[g])return 0;var o=n[g](t),r=o.url,i=o.body,c=o.type,u=new XMLHttpRequest,a=0;function f(n,t,e){u.open("POST",n),e&&u.setRequestHeader("Content-Type",e),u.send(t)}return u.onload=function(){u.status<299?e():s.config[l+".XHRRetries"]&&a<3&&E(function(){f(r,i,c)},++a*h)},f(r,i,c),1}].some(function(n){try{return n(t,e,o)}catch(n){}})}y("$afterload",function(){t=1,function(e){(s[i]()||[]).forEach(function(n){if(!n.indexOf(r))try{var t=s[i](n);s[a](n),JSON.parse(t).forEach(e)}catch(n){s.error(n)}})}(b),n(m,"visibilitychange",w,!1),w()}),y("$afterunload",function(){t=1,w()}),n("$afterPageTransition",function(){p=0}),s.register(l,{log:b,register:function(n){d.push(n)}})});csa.plugin(function(n){var r=n.config["Events.SushiEndpoint"];n("Transport")("register",{accepts:function(n){return n.schemaId},post:function(n){var t=n.map(function(n){return{data:n}});return{url:r,body:JSON.stringify({events:t})}},preflight:function(){var n,t=/\/\/(.*?)\//.exec(r);return t&&t[1]&&(n="https://"+t[1]+"/ping"),{url:n}},chunks:function(n){for(var t=[];500<n.length;)t.push(n.splice(0,500));return t.push(n),t}})});csa.plugin(function(n){var t,a,o,r,e=n.config,i="PageViews",d=e[i+".ImpressionMinimumTime"]||1e3,s="hidden",c="innerHeight",g="innerWidth",l="renderedTo",f=l+"Viewed",m=l+"Meaningful",u=l+"Impressed",p=1,v=2,h=3,w=4,y=5,P="loaded",I=7,T=8,b=n.global,E=n.on,V=n("Events",{producerId:"csa"}),$=b.document,M={},S={},H=y;function K(e){if(!M[I]){var i;if(M[e]=n.time(),e!==h&&e!==P||(t=t||M[e]),t&&H===w)a=a||M[e],(i={})[m]=t-o,i[f]=a-o,R("PageView.4",i),r=r||n.timeout(j,d);if(e!==y&&e!==p&&e!==v||(clearTimeout(r),r=0),e!==p&&e!==v||R("PageRender.3",{transitionType:e===p?"hard":"soft"}),e===I)(i={})[m]=t-o,i[f]=a-o,i[u]=M[e]-o,R("PageImpressed.2",i)}}function R(e,i){S[e]||(i.schemaId="<ns>."+e,V("log",i,{ent:"all"}),S[e]=1)}function W(){0===b[c]&&0===b[g]?(H=T,n("Events")("setEntity",{page:{viewport:"hidden-iframe"}})):H=$[s]?y:w,K(H)}function j(){K(I),r=0}function k(){var e=o?v:p;M={},S={},a=t=0,o=n.time(),K(e),W()}function q(){var e=$.readyState;"interactive"===e&&K(h),"complete"===e&&K(P)}e["KillSwitch."+i]||($&&void 0!==$[s]?(k(),E($,"visibilitychange",W,!1),E($,"readystatechange",q,!1),E("$afterPageTransition",k),E("$timing:loaded",q),n.once("$load",q)):n.warn("Page visibility not supported"))});csa.plugin(function(c){var s=c.config["Interactions.ParentChainLength"]||15,e="click",r="touches",f="timeStamp",o="length",u="pageX",g="pageY",p="pageXOffset",h="pageYOffset",m=250,v=5,d=200,l=.5,t={capture:!0,passive:!0},X=c.global,Y=c.emit,n=c.on,x=X.Math.abs,a=(X.document||{}).documentElement||{},y={x:0,y:0,t:0,sX:0,sY:0},N={x:0,y:0,t:0,sX:0,sY:0};function b(t){if(t.id)return"//*[@id='"+t.id+"']";var e=function(t){var e,n=1;for(e=t.previousSibling;e;e=e.previousSibling)e.nodeName===t.nodeName&&(n+=1);return n}(t),n=t.nodeName;return 1!==e&&(n+="["+e+"]"),t.parentNode&&(n=b(t.parentNode)+"/"+n),n}function I(t,e,n){var a=c("Content",{target:n}),i={schemaId:"<ns>.ContentInteraction.1",interaction:t,interactionData:e,messageId:c.UUID()};if(n){var r=b(n);r&&(i.attribution=r);var o=function(t){for(var e=t,n=e.tagName,a=!1,i=t?t.href:null,r=0;r<s;r++){if(!e||!e.parentElement){a=!0;break}n=(e=e.parentElement).tagName+"/"+n,i=i||e.href}return a||(n=".../"+n),{pc:n,hr:i}}(n);o.pc&&(i.interactionData.parentChain=o.pc),o.hr&&(i.interactionData.href=o.hr)}a("log",i),Y("$content.interaction",i)}function i(t){I(e,{interactionX:""+t.pageX,interactionY:""+t.pageY},t.target)}function C(t){if(t&&t[r]&&1===t[r][o]){var e=t[r][0];N=y={e:t.target,x:e[u],y:e[g],t:t[f],sX:X[p],sY:X[h]}}}function D(t){if(t&&t[r]&&1===t[r][o]&&y&&N){var e=t[r][0],n=t[f],a=n-N.t,i={e:t.target,x:e[u],y:e[g],t:n,sX:X[p],sY:X[h]};N=i,d<=a&&(y=i)}}function E(t){if(t){var e=x(y.x-N.x),n=x(y.y-N.y),a=x(y.sX-N.sX),i=x(y.sY-N.sY),r=t[f]-y.t;if(m<1e3*e/r&&v<e||m<1e3*n/r&&v<n){var o=n<e;o&&a&&e*l<=a||!o&&i&&n*l<=i||I((o?"horizontal":"vertical")+"-swipe",{interactionX:""+y.x,interactionY:""+y.y,endX:""+N.x,endY:""+N.y},y.e)}}}n(a,e,i,t),n(a,"touchstart",C,t),n(a,"touchmove",D,t),n(a,"touchend",E,t)});csa.plugin(function(t){var n,r,i,s="MutationObserver",e="PerformanceObserver",u="observe",o="disconnect",f="scroll",a=t.global,c=a.document,l=c.body||c.documentElement,p=Date.now,d=[],b=[],g=[],m=0,v=0,y=0;function O(e){d.push({t:p(),m:e})}function h(e){b.push({t:p(),m:e}),y=1,n&&n()}function w(){y&&(g.push({t:p(),y:v}),v=a.pageYOffset,y=0)}function E(e){m=e,(r=new a[s](h))[u](l,{childList:!0,subtree:!0}),(i=new a[s](O))[u](l,{attributes:!0,subtree:!0,attributeFilter:["src"],attributeOldValue:!0}),t.on(a,f,w,{passive:!0})}p&&a[s]&&(t.config["VisualReady.CollectAfterPaint"]?a[e]&&~(a[e].supportedEntryTypes||[]).indexOf("paint")?new a[e](function(e){E(((e.getEntries()||[])[0]||{}).startTime||p())})[u]({entryTypes:["paint"],buffered:!0}):t.raf(E):E(0),t.register("SpeedIndexBuffers",{getBuffers:function(e){e&&(w(),e(m,d,b,g),r&&r[o](),i&&i[o](),a.removeEventListener(f,w))},registerListener:function(e){n=e}}))});

</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 12228)</script>
<!-- sp:feature:nav-inline-js -->
<!-- NAVYAAN JS -->
<script type="text/javascript">!function(n){function e(n,e){return{m:n,a:function(n){return[].slice.call(n)}(e)}}document.createElement("header");var r=function(n){function u(n,r,u){n[u]=function(){a._replay.push(r.concat(e(u,arguments)))}}var a={};return a._sourceName=n,a._replay=[],a.getNow=function(n,e){return e},a.when=function(){var n=[e("when",arguments)],r={};return u(r,n,"run"),u(r,n,"declare"),u(r,n,"publish"),u(r,n,"build"),r},u(a,[],"declare"),u(a,[],"build"),u(a,[],"publish"),u(a,[],"importEvent"),r._shims.push(a),a};r._shims=[],n.$Nav||(n.$Nav=r("rcx-nav")),n.$Nav.make||(n.$Nav.make=r)}(window)</script><script type="text/javascript">
$Nav.importEvent('navbarJS-beaconbelt');
$Nav.declare('img.sprite', {
  'png32': 'https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936603_.png',
  'png32-2x': 'https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/nav-sprite-global-2x-hm-dsk-reorg._CB405936603_.png'
});
$Nav.declare('img.timeline', {
  'timeline-icon-2x': 'https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/timeline_sprite_2x._CB443581337_.png'
});
window._navbarSpriteUrl = 'https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936603_.png';
$Nav.declare('img.pixel', 'https://images-na.ssl-images-amazon.com/images/G/15/x-locale/common/transparent-pixel._CB485935025_.gif');
</script>
<img src="https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936603_.png" style="display:none" alt=""/>
<script type="text/javascript">var nav_t_after_preload_sprite = + new Date();</script>
<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/41cyy9szMwL._RC|714xw+8HbKL.js,61ACKXDdUsL.js,41RJ26y-U+L.js,11b3Y4WYB6L.js,21qd6OezMHL.js,11k47yUMOjL.js,41SZNgvX4oL.js,51pktuVkksL.js,31pymwzQBWL.js,01KW1GJCT1L.js,31PkUbXQSXL.js_.js?AUIClients/NavDesktopUberAsset#desktop');
});
</script>
<!-- sp:feature:nav-skeleton -->
<!-- sp:feature:navbar -->

<!--Pilu -->


  <!-- NAVYAAN -->











<!-- navmet initial definition -->



<script type='text/javascript'>
    if(window.navmet===undefined) {
      window.navmet=[];
      if (window.performance && window.performance.timing && window.ue_t0) {
        var t = window.performance.timing;
        var now = + new Date();
        window.navmet.basic = {
          'networkLatency': (t.responseStart - t.fetchStart),
          'navFirstPaint': (now - t.responseStart),
          'NavStart': (now - window.ue_t0)
        };
        window.navmet.push({key:"NavFirstPaintStart",end:+new Date(),begin:window.ue_t0});
      }
    }
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainStart",end:+new Date(),begin:window.ue_t0});
    }
</script>




<script type='text/javascript'>window.navmet.tmp=+new Date();</script>
  <script type='text/javascript'>
    // Nav start should be logged at this place only if request is NOT progressively loaded.
    // For progressive loading case this metric is logged as part of skeleton.
    // Presence of skeleton signals that request is progressively loaded.
    if(!document.getElementById("navbar-skeleton")) {
      window.uet && uet('ns');
    }
    window._navbar = (function (o) {
      o.componentLoaded = o.loading = function(){};
      o.browsepromos = {};
      o.issPromos = [];
      return o;
    }(window._navbar || {}));
    window._navbar.declareOnLoad = function () { window.$Nav && $Nav.declare('page.load'); };
    if (window.addEventListener) {
      window.addEventListener("load", window._navbar.declareOnLoad, false);
    } else if (window.attachEvent) {
      window.attachEvent("onload", window._navbar.declareOnLoad);
    } else if (window.$Nav) {
      $Nav.when('page.domReady').run("OnloadFallbackSetup", function () {
        window._navbar.declareOnLoad();
      });
    }
    window.$Nav && $Nav.declare('logEvent.enabled',
      'false');

    window.$Nav && $Nav.declare('config.lightningDeals', {});
  </script>

    <style mark="aboveNavInjectionCSS" type="text/css">
      div#navSwmHoliday.nav-focus {border: none;margin: 0;}#navbar.nav-pinned-pinata #nav-tools .nav-line-3 { height: 16px;line-height:16px;}div#navSwmHoliday.nav-focus {border-bottom: none;margin-top: 0;}
    </style>
    <script mark="aboveNavInjectionJS" type="text/javascript">
      try {
        window.$Nav && $Nav.when('$').run('defineIsArray', function(jQuery) { if(jQuery.isArray===undefined) { jQuery.isArray=function(param) { if(param.length===undefined) { return false; } return true; }; } }); window.$Nav && window.$Nav.when("$","subnav.initFlyouts","constants","nav.inline").build("subnav.builder",function(a,t,e){var n=a("#navbar");return function(s){var r=a("#nav-subnav");if(0===r.length&&(r=a("<div id='nav-subnav'></div>").appendTo("#navbar")),r.html(""),n.removeClass("nav-subnav"),s.categoryKey&&s.digest){r.attr("data-category",s.categoryKey).attr("data-digest",s.digest).attr("class",s.category.data.categoryStyle),s.style?r.attr("style",s.style):r.attr("style")&&r.removeAttr("style");var i=function(t){if(t&&t.href){var n="nav-a",s=t.text,i=t.dataKey;if(!s&&!t.image){if(!i||0!==i.indexOf(e.ADVANCED_PREFIX))return;s="",n+=" nav-aText"}var d=t.image?"<img src='"+t.image+"'class='nav-categ-image' ></a>":s,l=a("<a href='"+t.href+"' class='"+n+"'></a>"),v=a("<span class='nav-a-content'>"+d+"</span>");if("image"===t.type&&(v.html(""),l.addClass("nav-hasImage"),t.rightText=""),t.bold&&!t.image&&l.addClass("nav-b"),t.floatRight&&l.addClass("nav-right"),t.flyoutFullWidth&&"0"!==t.flyoutFullWidth&&l.attr("data-nav-flyout-full-width","1"),t.src){var g=["nav-image"];t["absolute-right"]&&g.push("nav-image-abs-right"),t["absolute-right"]&&g.push("nav-image-abs-right"),a("<img src='"+t.src+"' class='"+g.join(" ")+"' alt='"+(t.alt||"")+"' />").appendTo(v)}t.rightText&&v.append(t.rightText),v.appendTo(l),i&&(a("<span class='nav-arrow'></span>").appendTo(l),l.attr("data-nav-key",i).addClass("nav-hasArrow")),l.appendTo(r),r.append(document.createTextNode(" "))}};if(s.category&&s.category.data&&(s.category.data.bold=!0,i(s.category.data)),s.subnav&&"linkSequence"===s.subnav.type)for(var d=0;d<s.subnav.data.length;d++)i(s.subnav.data[d]);n.addClass("nav-subnav"),t()}}}); window.$Nav && $Nav.when('$','$F','config','logEvent','panels','phoneHome','dataPanel','flyouts.renderPromo','flyouts.sloppyTrigger','flyouts.accessibility','util.mouseOut','util.onKey','debug.param').build('flyouts.buildSubPanels',function($,$F,config,logEvent,panels,phoneHome,dataPanel,renderPromo,createSloppyTrigger,a11yHandler,mouseOutUtility,onKey,debugParam){var flyoutDebug=debugParam('navFlyoutClick');return function(flyout,event){var linkKeys=[];$('.nav-item',flyout.elem()).each(function(){var $item=$(this);linkKeys.push({link:$item,panelKey:$item.attr('data-nav-panelkey')});});if(linkKeys.length===0){return;} var visible=false;var $parent=$('<div class=\'nav-subcats\'></div>').appendTo(flyout.elem());var panelGroup=flyout.getName()+'SubCats';var hideTimeout=null;var sloppyTrigger=createSloppyTrigger($parent);var showParent=function(){if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} if(visible){return;} var height=$('#nav-flyout-shopAll').height();$parent.css({'height': height});$parent.animate({width:'show'},{duration:200,complete:function(){$parent.css({overflow:'visible'});}});visible=true;};var hideParentNow=function(){$parent.stop().css({overflow:'hidden',display:'none',width:'auto',height:'auto'});panels.hideAll({group:panelGroup});visible=false;if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;}};var hideParent=function(){if(!visible){return;} if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} hideTimeout=setTimeout(hideParentNow,10);};flyout.onHide(function(){sloppyTrigger.disable();hideParentNow();this.elem().hide();});var addPanel=function($link,panelKey){var panel=dataPanel({className:'nav-subcat',dataKey:panelKey,groups:[panelGroup],spinner:false,visible:false});if(!flyoutDebug){var mouseout=mouseOutUtility();mouseout.add(flyout.elem());mouseout.action(function(){panel.hide();});mouseout.enable();} var a11y=a11yHandler({link:$link,onEscape:function(){panel.hide();$link.focus();}});var logPanelInteraction=function(promoID,wlTriggers){var logNow=$F.once().on(function(){var panelEvent=$.extend({},event,{id:promoID});if(config.browsePromos&&!!config.browsePromos[promoID]){panelEvent.bp=1;} logEvent(panelEvent);phoneHome.trigger(wlTriggers);});if(panel.isVisible()&&panel.hasInteracted()){logNow();}else{panel.onInteract(logNow);}};panel.onData(function(data){renderPromo(data.promoID,panel.elem());logPanelInteraction(data.promoID,data.wlTriggers);});panel.onShow(function(){var columnCount=$('.nav-column',panel.elem()).length;panel.elem().addClass('nav-colcount-'+columnCount);showParent();var $subCatLinks=$('.nav-subcat-links > a',panel.elem());var length=$subCatLinks.length;if(length>0){var firstElementLeftPos=$subCatLinks.eq(0).offset().left;for(var i=1;i<length;i++){if(firstElementLeftPos===$subCatLinks.eq(i).offset().left){$subCatLinks.eq(i).addClass('nav_linestart');}} if($('span.nav-title.nav-item',panel.elem()).length===0){var catTitle=$.trim($link.html());catTitle=catTitle.replace(/ref=sa_menu_top/g,'ref=sa_menu');var $subPanelTitle=$('<span class=\'nav-title nav-item\'>'+ catTitle+'</span>');panel.elem().prepend($subPanelTitle);}} $link.addClass('nav-active');});panel.onHide(function(){$link.removeClass('nav-active');hideParent();a11y.disable();sloppyTrigger.disable();});panel.onShow(function(){a11y.elems($('a, area',panel.elem()));});sloppyTrigger.register($link,panel);if(flyoutDebug){$link.click(function(){if(panel.isVisible()){panel.hide();}else{panel.show();}});} var panelKeyHandler=onKey($link,function(){if(this.isEnter()||this.isSpace()){panel.show();}},'keydown',false);$link.focus(function(){panelKeyHandler.bind();}).blur(function(){panelKeyHandler.unbind();});panel.elem().appendTo($parent);};var hideParentAndResetTrigger=function(){hideParent();sloppyTrigger.disable();};for(var i=0;i<linkKeys.length;i++){var item=linkKeys[i];if(item.panelKey){addPanel(item.link,item.panelKey);}else{item.link.mouseover(hideParentAndResetTrigger);}}};});
      } catch ( err ) {
        if ( window.$Nav ) {
          window.$Nav.when('metrics', 'logUeError').run(function(metrics, log) {
            metrics.increment('NavJS:AboveNavInjection:error');
            log(err.toString(), {
              'attribution': 'rcx-nav',
              'logLevel': 'FATAL'
            });
          });
        }
      }
    </script>

  <noscript>
    <style type="text/css"><!--
      #navbar #nav-shop .nav-a:hover {
        color: #ff9900;
        text-decoration: underline;
      }
      #navbar #nav-search .nav-search-facade,
      #navbar #nav-tools .nav-icon,
      #navbar #nav-shop .nav-icon,
      #navbar #nav-subnav .nav-hasArrow .nav-arrow {
        display: none;
      }
      #navbar #nav-search .nav-search-submit,
      #navbar #nav-search .nav-search-scope {
        display: block;
      }
      #nav-search .nav-search-scope {
        padding: 0 5px;
      }
      #navbar #nav-search .nav-search-dropdown {
        position: relative;
        top: 5px;
        height: 23px;
        font-size: 14px;
        opacity: 1;
        filter: alpha(opacity = 100);
      }
    --></style>
 </noscript>
<script type='text/javascript'>window.navmet.push({key:'PreNav',end:+new Date(),begin:window.navmet.tmp});</script>

<a id='nav-top'></a>




<a id="skiplink" tabindex="0" class="skip-link">Skip to main content</a>

<script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<!-- Navyaan Upnav -->
    <div id="nav-upnav" aria-hidden="true" >
      <!-- unw1 failed -->
      
    </div>
<script type='text/javascript'>window.navmet.push({key:'UpNav',end:+new Date(),begin:window.navmet.tmp});</script>


<script type='text/javascript'>window.navmet.main=+new Date();</script>

<header id="navbar-main" class = "nav-opt-sprite nav-flex nav-locale-ca nav-lang-en nav-ssl nav-unrec nav-progressive-attribute">

   
  
  <div id='navbar' cel_widget_id='Navigation-desktop-navbar' data-template="layoutSwapToolBar"
  role='navigation' class="nav-sprite-v1 celwidget nav-bluebeacon nav-a11y-t1 bold-focus-hover layout2 nav-flex layout3 layout3-alt nav-packard-glow hamburger nav-progressive-attribute">
    
    <div id='nav-belt'>
      <div class='nav-left'>
        <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
  <div id="nav-logo" >
    <a href="/ref=nav_logo" id="nav-logo-sprites" class="nav-logo-link nav-progressive-attribute" aria-label="Amazon.ca">
      <span class="nav-sprite nav-logo-base"></span>
      <span id="logo-ext" class="nav-sprite nav-logo-ext nav-progressive-content"></span>
      <span class="nav-logo-locale">.ca</span>
    </a>
  </div>
<script type='text/javascript'>window.navmet.push({key:'Logo',end:+new Date(),begin:window.navmet.tmp});</script>
        
<div id="nav-global-location-slot">
    <span id="nav-global-location-data-modal-action" class="a-declarative nav-progressive-attribute" data-a-modal='{&quot;width&quot;:375, &quot;closeButton&quot;:&quot;false&quot;,&quot;popoverLabel&quot;:&quot;Choose your location&quot;, &quot;ajaxHeaders&quot;:{&quot;anti-csrftoken-a2z&quot;:&quot;gAQCJcG3b1wEWkKF5lYRNfRRJ0wMQhk267kUAn4AAAAMAAAAAGC6rX9yYXcAAAAA&quot;}, &quot;name&quot;:&quot;glow-modal&quot;, &quot;url&quot;:&quot;/gp/glow/get-address-selections.html?deviceType&#x3D;desktop&amp;pageType&#x3D;Detail&amp;storeContext&#x3D;music&amp;actionSource&#x3D;desktop-modal&quot;, &quot;footer&quot;:null,&quot;header&quot;:&quot;Choose your location&quot;}' data-action="a-modal">
        <a id="nav-global-location-popover-link" class="nav-a nav-a-2 a-popover-trigger a-declarative nav-progressive-attribute" tabindex="0">
            <div class="nav-sprite nav-progressive-attribute" id="nav-packard-glow-loc-icon"></div>
            <div id="glow-ingress-block">
                <span class="nav-line-1 nav-progressive-content" id="glow-ingress-line1">
                   Hello
                </span>
                <span class="nav-line-2 nav-progressive-content" id="glow-ingress-line2">
                   Select your address
                </span>
            </div>
        </a>
        </span>
        <input data-addnewaddress="add-new" id="unifiedLocation1ClickAddress" name="dropdown-selection" type="hidden" value="add-new" class="nav-progressive-attribute" />
        <input data-addnewaddress="add-new" id="ubbShipTo" name="dropdown-selection-ubb" type="hidden" value="add-new" class="nav-progressive-attribute"/>
        <input id="glowValidationToken" name="glow-validation-token" type="hidden" value="gAQCJcG3b1wEWkKF5lYRNfRRJ0wMQhk267kUAn4AAAAMAAAAAGC6rX9yYXcAAAAA" class="nav-progressive-attribute"/>
</div>

<div id="nav-global-location-toaster-script-container" class="nav-progressive-content">
</div>

      </div>
          <div class='nav-fill'>
            <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<div id="nav-search">
  <div id="nav-bar-left"></div>
  <form
    id="nav-search-bar-form"
    accept-charset="utf-8"
    action="/s/ref=nb_sb_noss"
    class="nav-searchbar nav-progressive-attribute"
    method="GET"
    name="site-search"
    role="search"
  >

    <div class="nav-left">
      <div id="nav-search-dropdown-card">
        
  <div class="nav-search-scope nav-sprite">
    <div class="nav-search-facade" data-value="search-alias=aps">
      <span id="nav-search-label-id" class="nav-search-label nav-progressive-content">Music</span>
      <i class="nav-icon"></i>
    </div>
    <span id="searchDropdownDescription" class="nav-progressive-attribute" style="display:none">Select the department you want to search in</span>
    <select
      aria-describedby="searchDropdownDescription"
      class="nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown"
      data-nav-digest="WBb1edNlW2EKQJp5s1Z61TiM9Ps="
      data-nav-selected="10"
      id="searchDropdownBox"
      name="url"
      style="display: block;"
      tabindex="0"
      title="Search in"
    >
        <option value="search-alias=aps">All Departments</option>
        <option value="search-alias=audible">Audible Audiobooks</option>
        <option value="search-alias=alexa-skills">Alexa Skills</option>
        <option value="search-alias=amazon-devices">Amazon Devices</option>
        <option value="search-alias=warehouse-deals">Amazon Warehouse Deals</option>
        <option value="search-alias=mobile-apps">Apps & Games</option>
        <option value="search-alias=automotive">Automotive</option>
        <option value="search-alias=baby">Baby</option>
        <option value="search-alias=beauty">Beauty</option>
        <option value="search-alias=stripbooks">Books</option>
        <option selected="selected" current="parent" value="search-alias=popular">Music</option>
        <option value="search-alias=fashion">Clothing, Shoes & Jewelry</option>
        <option value="search-alias=fashion-womens">&#160;&#160;&#160;Women</option>
        <option value="search-alias=fashion-mens">&#160;&#160;&#160;Men</option>
        <option value="search-alias=fashion-girls">&#160;&#160;&#160;Girls</option>
        <option value="search-alias=fashion-boys">&#160;&#160;&#160;Boys</option>
        <option value="search-alias=fashion-baby">&#160;&#160;&#160;Baby</option>
        <option value="search-alias=electronics">Electronics</option>
        <option value="search-alias=gift-cards">Gift Cards</option>
        <option value="search-alias=grocery">Grocery</option>
        <option value="search-alias=handmade">Handmade</option>
        <option value="search-alias=hpc">Health & Personal Care</option>
        <option value="search-alias=kitchen">Home & Kitchen</option>
        <option value="search-alias=industrial">Industrial & Scientific</option>
        <option value="search-alias=digital-text">Kindle Store</option>
        <option value="search-alias=fashion-luggage">Luggage & Travel Gear</option>
        <option value="search-alias=luxury-beauty">Luxury Beauty</option>
        <option value="search-alias=dvd">Movies & TV</option>
        <option value="search-alias=mi">Musical Instruments, Stage & Studio</option>
        <option value="search-alias=office-products">Office Products</option>
        <option value="search-alias=lawngarden">Patio, Lawn & Garden</option>
        <option value="search-alias=pets">Pet Supplies</option>
        <option value="search-alias=instant-video">Prime Video</option>
        <option value="search-alias=smart-home">Smart Home</option>
        <option value="search-alias=software">Software</option>
        <option value="search-alias=sporting">Sports & Outdoors</option>
        <option value="search-alias=specialty-aps-sns">Subscribe & Save</option>
        <option value="search-alias=tools">Tools & Home Improvement</option>
        <option value="search-alias=toys">Toys & Games</option>
        <option value="search-alias=videogames">Video Games</option>
    </select>
  </div>

      </div>
    </div>
    <div class="nav-fill">
      <div class="nav-search-field ">
        <input
          type="text"
          id="twotabsearchtextbox"
          value=""
          name="field-keywords"
          autocomplete="off"
          placeholder=""
          class="nav-input nav-progressive-attribute"
          dir="auto"
          tabindex="0"
          aria-label="Search"
        >
      </div>
      <div id="nav-iss-attach"></div>
    </div>
    <div class="nav-right">
      <div class="nav-search-submit nav-sprite">
        <span id="nav-search-submit-text" class="nav-search-submit-text nav-sprite nav-progressive-attribute" aria-label="Go">
          <input id="nav-search-submit-button" type="submit" class="nav-input nav-progressive-attribute" value="Go" tabindex="0">
        </span>
      </div>
    </div>
  </form>
</div>
<script type='text/javascript'>window.navmet.push({key:'Search',end:+new Date(),begin:window.navmet.tmp});</script>
          </div>
      <div class='nav-right'>
          <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
          <div id='nav-tools' class="layoutToolbarPadding">
              
              
              
              
  <a href="/gp/customer-preferences/select-language/ref=topnav_lang?preferencesReturnUrl=%2F" id="icp-nav-flyout" class="nav-a nav-a-2 icp-link-style-2" aria-label="Choose a language for shopping.">
    <span class="icp-nav-link-inner">
      <span class="nav-line-1">
      </span>
      <span class="nav-line-2">
        <span class="icp-nav-flag icp-nav-flag-ca"></span>
        <span class="nav-icon nav-arrow"></span>
      </span>
    </span>
  </a>

              
  <a href="https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2FRage-Against-Machine%2Fdp%2FB0000028RR%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&" class="nav-a nav-a-2   nav-progressive-attribute" data-nav-ref="nav_ya_signin"  data-nav-role="signin" data-ux-jq-mouseenter="true" id="nav-link-accountList" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-link-accountList" data-csa-c-content-id="nav_ya_signin">
  <div class="nav-line-1-container"><span id="nav-link-accountList-nav-line-1" class="nav-line-1 nav-progressive-content">Hello, Sign in</span></div>
  <span class="nav-line-2 ">Account & Lists<span class="nav-icon nav-arrow"></span>
  </span>
</a>

              
<a href="/gp/css/order-history?ref_=nav_orders_first" class="nav-a nav-a-2   nav-progressive-attribute" id="nav-orders" tabindex="0">
  <span class="nav-line-1">Returns</span>
  <span class="nav-line-2">& Orders</span>
</a>

              
              
  <a href="https://www.amazon.ca/gp/cart/view.html?ref_=nav_cart" aria-label="0 items in cart" class="nav-a nav-a-2 nav-progressive-attribute" id="nav-cart">
    <div id="nav-cart-count-container">
      <span id="nav-cart-count" aria-hidden="true" class="nav-cart-count nav-cart-0 nav-progressive-attribute nav-progressive-content">0</span>
      <span class="nav-cart-icon nav-sprite"></span>
    </div>
    <div id="nav-cart-text-container" class=" nav-progressive-attribute">
      <span aria-hidden="true" class="nav-line-1">
         
      </span>
      <span aria-hidden="true" class="nav-line-2">
        Cart
        <span class="nav-icon nav-arrow"></span>
      </span>
    </div>
  </a>

          </div>
          <script type='text/javascript'>window.navmet.push({key:'Tools',end:+new Date(),begin:window.navmet.tmp});</script>

      </div>
    </div>
    <div id='nav-main' class='nav-sprite'>
      <div class='nav-left'>
        <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
  <a href="/gp/site-directory?ref_=nav_em_js_disabled" id="nav-hamburger-menu" role="button" aria-label="Open Menu" data-csa-c-type="widget" data-csa-c-slot-id="HamburgerMenuDesktop"
  data-csa-c-interaction-events="click" >
    <i class="hm-icon nav-sprite"></i>
    <span class="hm-icon-label">All</span>
  </a>
  
<script type="text/javascript">
  var hmenu = document.getElementById("nav-hamburger-menu");
  hmenu.setAttribute("href", "javascript: void(0)");
  window.navHamburgerMetricLogger = function() {
    if (window.ue && window.ue.count) {
      var metricName = "Nav:Hmenu:IconClickActionPending";
      window.ue.count(metricName, (ue.count(metricName) || 0) + 1);
    }
    window.$Nav && $Nav.declare("navHMenuIconClicked",!0);
    window.$Nav && $Nav.declare("navHMenuIconClickedNotReadyTimeStamp", Date.now());
  };
  hmenu.addEventListener("click", window.navHamburgerMetricLogger);
  window.$Nav && $Nav.declare('hamburgerMenuIconAvailableOnLoad', false);
</script>  
<script type='text/javascript'>window.navmet.push({key:'HamburgerMenuIcon',end:+new Date(),begin:window.navmet.tmp});</script>
        
        
        
        
      </div>
      <div class='nav-fill'>
        
          
 <div id="nav-shop">
 </div>
          <div id='nav-xshop-container'>
            <div id='nav-xshop' class="nav-progressive-content">
              <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<a href="/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers_5e07a0361d744326ae799da4b354adca" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_0" data-csa-c-content-id="nav_cs_bestsellers_5e07a0361d744326ae799da4b354adca">Best Sellers</a>

<a href="/prime?ref_=nav_cs_primelink_nonmember_f0320f44e3fa41efaab67b11e9f921d1" class="nav-a  " data-ux-jq-mouseenter="true" id="nav-link-prime" tabindex="0"  data-csa-c-type="link" data-csa-c-slot-id="nav-link-prime" data-csa-c-content-id="nav_cs_primelink_nonmember_f0320f44e3fa41efaab67b11e9f921d1"><span>Prime</span><span class="nav-icon nav-arrow"></span></a>

<a href="/gp/new-releases/?ref_=nav_cs_newreleases_e9f95b2bb12042889b69364b7114d183" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_2" data-csa-c-content-id="nav_cs_newreleases_e9f95b2bb12042889b69364b7114d183">New Releases</a>

<a href="/gcx/-/gfhz/?ref_=nav_cs_giftfinder_9f0da4e43074433bac570d77fbd4125e" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_3" data-csa-c-content-id="nav_cs_giftfinder_9f0da4e43074433bac570d77fbd4125e">Gift Ideas	</a>

<a href="/gp/goldbox?ref_=nav_cs_gb_cb3d1b8cb90f49beb75e70709c5104da" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_4" data-csa-c-content-id="nav_cs_gb_cb3d1b8cb90f49beb75e70709c5104da">Deals Store</a>

<a href="/gp/help/customer/display.html?ref_=nav_cs_help_80966742f8c54e26897f6ff675864430" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_5" data-csa-c-content-id="nav_cs_help_80966742f8c54e26897f6ff675864430">Customer Service</a>

<a href="/Electronics-Accessories/b/?ie=UTF8&node=667823011&ref_=nav_cs_electronics_c9778bce4052480ab5f93f798f2de848" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_6" data-csa-c-content-id="nav_cs_electronics_c9778bce4052480ab5f93f798f2de848">Electronics</a>

<a href="/gp/browse.html?node=2206275011&ref_=nav_cs_home_e30810812540476da315f95f4c1cba0c" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_7" data-csa-c-content-id="nav_cs_home_e30810812540476da315f95f4c1cba0c">Home</a>

<a href="/books-used-books-textbooks/b/?ie=UTF8&node=916520&ref_=nav_cs_books_cfb4c7d7199e41ea967973a464d2fa4c" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_8" data-csa-c-content-id="nav_cs_books_cfb4c7d7199e41ea967973a464d2fa4c">Books</a>

<a href="/Computers-Accessories/b/?ie=UTF8&node=2404990011&ref_=nav_cs_pc_8ec80b6bbe6340c89729e8a4f68f684d" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_9" data-csa-c-content-id="nav_cs_pc_8ec80b6bbe6340c89729e8a4f68f684d">Computers</a>

<a href="/gp/browse.html?node=9230166011&ref_=nav_cs_gc_521dead25f684fd0b0c54d72ee7ac2c9" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_10" data-csa-c-content-id="nav_cs_gc_521dead25f684fd0b0c54d72ee7ac2c9">Gift Cards</a>

<a href="/b/?node=12218500011&ref_=nav_cs_coupons_5c0b5095bded47dc9dbbe58103090fe1" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_11" data-csa-c-content-id="nav_cs_coupons_5c0b5095bded47dc9dbbe58103090fe1">Coupons</a>

<a href="/Toys-Games/b/?ie=UTF8&node=6205517011&ref_=nav_cs_toys_8e4aa2f3b167434e8cd86cd8296ae135" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_12" data-csa-c-content-id="nav_cs_toys_8e4aa2f3b167434e8cd86cd8296ae135">Toys & Games</a>

<a href="/Health-Personal-Care/b/?ie=UTF8&node=6205177011&ref_=nav_cs_hpc_389588d101974a76b1f2a1aec6148be2" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_13" data-csa-c-content-id="nav_cs_hpc_389588d101974a76b1f2a1aec6148be2">Health & Household</a>

<a href="/gp/browse.html?node=21204935011&ref_=nav_cs_fashion_e530da5716f3463aac61c1c214fede3b" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_14" data-csa-c-content-id="nav_cs_fashion_e530da5716f3463aac61c1c214fede3b">Fashion</a>

<a href="/video-games-hardware-accessories/b/?ie=UTF8&node=3198031&ref_=nav_cs_video_games_96df7f31fc134377b70784ea57f4ff5c" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_15" data-csa-c-content-id="nav_cs_video_games_96df7f31fc134377b70784ea57f4ff5c">Computer & Video Games</a>

<a href="/automotive/b/?ie=UTF8&node=6948389011&ref_=nav_cs_automotive_df4975bd27a649d59f0a0f346158957a" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_16" data-csa-c-content-id="nav_cs_automotive_df4975bd27a649d59f0a0f346158957a">Automotive</a>

<a href="/b/?node=15664730011&ld=AZCASOA-sell&ref_=nav_cs_sell_715b740e3393467491e925d9548385ae" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_17" data-csa-c-content-id="nav_cs_sell_715b740e3393467491e925d9548385ae">Sell</a>

<a href="/grocery/b/?ie=UTF8&node=6967215011&ref_=nav_cs_grocery_96a59c746dd945d6a7d9911411f06a1b" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_18" data-csa-c-content-id="nav_cs_grocery_96a59c746dd945d6a7d9911411f06a1b">Grocery</a>

<a href="/sporting-goods/b/?ie=UTF8&node=2242989011&ref_=nav_cs_sports_8188fcfd7d6e449eab692f6d0371d9ff" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_19" data-csa-c-content-id="nav_cs_sports_8188fcfd7d6e449eab692f6d0371d9ff">Sports & Outdoors</a>

<a href="/Beauty/b/?ie=UTF8&node=6205124011&ref_=nav_cs_beauty_46f9bd5d21484218b9b15a4779dcd14a" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_20" data-csa-c-content-id="nav_cs_beauty_46f9bd5d21484218b9b15a4779dcd14a">Beauty & Personal Care</a>

<a href="/gp/browse.html?node=2972705011&ref_=nav_cs_kindle_books_30c4ac32cf754895b19193fffbb9870c" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_21" data-csa-c-content-id="nav_cs_kindle_books_30c4ac32cf754895b19193fffbb9870c">Kindle Books</a>

<a href="/Home-Improvement/b/?ie=UTF8&node=3006902011&ref_=nav_cs_hi_5ac6320bf57f4c35a6df23915e897e0c" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_22" data-csa-c-content-id="nav_cs_hi_5ac6320bf57f4c35a6df23915e897e0c">Home Improvement</a>

<a href="/pet-supplies-dog-cat-food-bed-toy/b/?ie=UTF8&node=6205514011&ref_=nav_cs_pets_e9098347e3f84d95a0fc0b55abe0df36" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_23" data-csa-c-content-id="nav_cs_pets_e9098347e3f84d95a0fc0b55abe0df36">Pet Supplies</a>

<a href="/gp/browse.html?node=3561346011&ref_=nav_cs_baby_4ca8c0ed74054e3392ac379629958f9c" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_24" data-csa-c-content-id="nav_cs_baby_4ca8c0ed74054e3392ac379629958f9c">Baby</a>

<a href="/gp/browse.html?node=19700946011&ref_=nav_cs_registry_e33c68e88c844208a181299c83810267" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_25" data-csa-c-content-id="nav_cs_registry_e33c68e88c844208a181299c83810267">Registry</a>

<a href="/auto-deliveries/landing?ref_=nav_cs_sns_76c49ee1885e4157b2d4da81c2e27802" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_26" data-csa-c-content-id="nav_cs_sns_76c49ee1885e4157b2d4da81c2e27802">Subscribe & save</a>
<script type='text/javascript'>window.navmet.push({key:'CrossShop',end:+new Date(),begin:window.navmet.tmp});</script>
            </div>
          </div>
        
      </div>
      <div class='nav-right'>
          <script type='text/javascript'>window.navmet.tmp=+new Date();</script><!-- Navyaan SWM -->
<div id="nav-swmslot">
  <div id="navSwmHoliday" style="height: 39px; width: 400px; overflow: hidden; position: relative; ">
    <a aria-label="Prime Video" href="/gp/redirect.html/?ie=UTF8&location=https%3A%2F%2Fwww.primevideo.com%2Fref&source=standards&token=6942A3BE332F639522C604291378FE69DB489AE7&ref_=nav_swm_dvm_crs_swm_ca_ra_swm1_panel_A&pf_rd_p=df1599b5-9f46-4f60-b0be-09c997803cd7&pf_rd_s=nav-sitewide-msg&pf_rd_t=4201&pf_rd_i=navbar-4201&pf_rd_m=A2EUQ1WTGCTBG2&pf_rd_r=1KMDY2JPGP2X3R80G8WC" class="nav-imageHref" target="_blank">
  <img alt="Prime Video" src="https://images-na.ssl-images-amazon.com/images/G/15/digital/video/merch/2018/Magellan/AVD10797_SWMRush/Amazon_GW_DesktopSWM_AVD10797_MagellanRush_400x39_EN_5._CB485944329_.jpg">
</a>
      </div>
  
</div><script type='text/javascript'>window.navmet.push({key:'SWM',end:+new Date(),begin:window.navmet.tmp});</script>
      </div>
    </div>

    <div id='nav-subnav-toaster'></div>

    
    <div id="nav-progressive-subnav">
      <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<div id='nav-subnav'  data-category="music">
  <a href="/music-rock-classical-pop-jazz/b/?ie=UTF8&node=916514&ref_=topnav_storetab_m" class="nav-a nav-b" >
    <span class="nav-a-content">
      Music
      
    </span>
  </a>
  <a href="/Vinyl-Records/b/?ie=UTF8&node=1292212011&ref_=sv_m_1" class="nav-a" >
    <span class="nav-a-content">
      Vinyl Records
      
    </span>
  </a>
  <a href="/Music-Deals-CD/b/?ie=UTF8&node=236416011&ref_=sv_m_2" class="nav-a" >
    <span class="nav-a-content">
      Today's Deals
      
    </span>
  </a>
  <a href="/New-Future-Releases-Music/b/?ie=UTF8&node=1003050&ref_=sv_m_3" class="nav-a" >
    <span class="nav-a-content">
      New Releases
      
    </span>
  </a>
  <a href="/gp/bestsellers/music/?ie=UTF8&ref_=sv_m_4" class="nav-a" >
    <span class="nav-a-content">
      Best Sellers
      
    </span>
  </a>
  <a href="/Canadian-Music/b/?ie=UTF8&node=13779501&ref_=sv_m_5" class="nav-a" >
    <span class="nav-a-content">
      Canadian Artists
      
    </span>
  </a>
  <a href="/Classical-Music/b/?ie=UTF8&node=962464&ref_=sv_m_6" class="nav-a" >
    <span class="nav-a-content">
      Classical
      
    </span>
  </a>
  <a href="/Styles-Music/b/?ie=UTF8&node=962454&ref_=sv_m_7" class="nav-a" >
    <span class="nav-a-content">
      Browse Genres
      
    </span>
  </a>
  <a href="/gp/yourstore/recs/?ie=UTF8&ie=UTF8&nodeID=916514&rGroup=music&ref_=sv_m_8" class="nav-a" >
    <span class="nav-a-content">
      Recommendations
      
    </span>
  </a>
  <a href="/musique-cd-francophone-classique-occasion/b/?ie=UTF8&node=962500&ref_=sv_m_9" class="nav-a" >
    <span class="nav-a-content">
      Musique
      
    </span>
  </a>
<!-- nav-linktree-subnav - 'music' -->
</div>

<script type='text/javascript'>window.navmet.push({key:'Subnav',end:+new Date(),begin:window.navmet.tmp});</script>
    </div>

    
    
    
        <div id='nav-flyout-ewc' aria-hidden='true' tabindex='-1' class='nav-ewc-lazy-align nav-ewc-hide-head'><div class='nav-flyout-body ewc-beacon'><div class='nav-ewc-arrow'></div><div class='nav-ewc-content'></div></div></div><script type='text/javascript'>
(function() {
  var viewportWidth = function() {
    return window.innerWidth ||
      document.documentElement.clientWidth ||
      document.body.clientWidth;
  };

  if (typeof uet === 'function') {  uet('x1', 'ewc', {wb: 1}); }

  window.$Nav && $Nav.declare('config.ewc', (function() {
    var config = {"enablePersistent":true,"viewportWidthForPersistent":1400,"isEWCLogging":1,"isEWCStateExpanded":true,"EWCStateReason":"fixed","isSmallScreenEnabled":true,"isFreshCustomer":false,"errorContent":{"html":"<div class='nav-ewc-error'><span class='nav-title'>Oops!</span><p class='nav-paragraph'>There is a problem retrieving your cart right now</p><a href='/gp/cart/view.html?ref_=nav_err_ewc_timeout' class='nav-action-button'><span class='nav-action-inner'>Your Cart</span></a></div>"},"url":"/cart/ewc/compact?hostPageType=Detail&hostSubPageType=null&hostPageRID=1KMDY2JPGP2X3R80G8WC&prerender=0&storeName=music","cartCount":0,"freshCartCount":0,"almCartCount":0,"isCompactViewEnabled":true,"isCompactEWCRendered":true,"isWiderCompactEWCRendered":true};
    var hasAui = window.P && window.P.AUI_BUILD_DATE;
    var isRTLEnabled = (document.dir === 'rtl');
    config.pinnable = config.pinnable && hasAui;
    config.isMigrationTreatment = true;

    config.flyout = (function() {
      var navbelt = document.getElementById('nav-belt');
      var navCart = document.getElementById('nav-cart');
      var ewcFlyout = document.getElementById('nav-flyout-ewc');
      var persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-full-height-persistent-hover';
      var flyout = {};

      var getDocumentScrollTop = function() {
        return (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
      };

      var isWindow = function(obj) {
        return obj != null && obj === obj.window;
      };

      var getWindow = function(elem) {
        return isWindow(elem) ? elem : elem.nodeType === 9 && elem.defaultView;
      };

      var getOffset = function(elem) {
        if (elem.getClientRects && !elem.getClientRects().length) {
          return {top: 0};
        }

        var rect = elem.getBoundingClientRect
          ? elem.getBoundingClientRect()
          : {top: 0};

        if (rect.width || rect.height) {
          var doc = elem.ownerDocument;
          var win = getWindow(doc);
          return {
            top: rect.top + win.pageYOffset - doc.documentElement.clientTop
          };
        }
        return rect;
      };

      flyout.align = function() {
        var newTop = getOffset(navbelt).top - getDocumentScrollTop();
        ewcFlyout.style.top = (newTop > 0 ? newTop + 'px' : 0);
      };

      flyout.hide = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = '')
          : (ewcFlyout.style.right = '');
      };

      if(typeof config.isCompactEWCRendered === 'undefined') {
        if (
          (config.isSmallScreenEnabled && viewportWidth() < 1400) ||
          (config.isCompactViewEnabled && viewportWidth() >= 1400)
        ) {
          config.isCompactEWCRendered = true;
          config.isEWCStateExpanded = true;
          config.url = config.url.replace("/gp/navcart/sidebar", "/cart/ewc/compact");
        } else {
          config.isCompactEWCRendered = false;
        }
      }

      var viewportQualifyForPersistent = function () {
        return (config.isCompactEWCRendered)
          ? true
          : viewportWidth() >= 1400;
      }

      flyout.hasQualifiedViewportForPersistent = viewportQualifyForPersistent;

      var getEWCRightOffset = function() {
        if (!config.isCompactEWCRendered) {
          return 0;
        }

        var $navbelt = document.getElementById('nav-belt');
        if ($navbelt === undefined || $navbelt === null) {
          return 0;
        }

        var EWCCompactViewWidth = (config.isWiderCompactEWCRendered  && viewportWidth() >= 1280) ? 130 : 100;
        var scrollLeft = (window.pageXOffset !== undefined)
          ? window.pageXOffset
          : (document.documentElement || document.body.parentNode || document.body).scrollLeft;
        var scrollXAxis = Math.abs(scrollLeft);
        var windowWidth = document.documentElement.clientWidth;
        var navbeltWidth = $navbelt.offsetWidth;
        var isPartOfNavbarNotVisible = (navbeltWidth + EWCCompactViewWidth) > windowWidth;

        if (isPartOfNavbarNotVisible) {
          return 0 - (navbeltWidth - scrollXAxis - windowWidth + EWCCompactViewWidth);
        } else {
          return 0;
        }
      }

      flyout.getEWCRightOffsetCssProperty = function () {
        return getEWCRightOffset() + 'px';
      }

      if (config.isCompactEWCRendered) {
        persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-compact-view';
        if (config.isWiderCompactEWCRendered) { persistentClassOnBody += ' nav-ewc-wider-compact-view'; }
      }

      flyout.show = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = flyout.getEWCRightOffsetCssProperty())
          : (ewcFlyout.style.right = flyout.getEWCRightOffsetCssProperty());
      };

      var isIOSDevice = function() {
        return (/iPad|iPhone|iPod/.test(navigator.platform) ||
                (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) &&
                !window.MSStream;
      }

      var checkForPersistent = function() {
        if (!hasAui) {
          return { result: false, reason: 'noAui' };
        }
        if (!config.enablePersistent) {
          return { result: false, reason: 'config' };
        }
        if (!viewportQualifyForPersistent()) {
          return { result: false, reason: 'viewport' };
        }
        if (isIOSDevice()) {
          return { result: false, reason: 'iOS' };
        }
        if (!config.cartCount > 0) {
          return { result: false, reason: 'emptycart' };
        }

        return { result: true };
      };

      flyout.ableToPersist = function() {
        return checkForPersistent().result;
      };

      var persistentClassRegExp = '(?:^|\\s)' + persistentClassOnBody + '(?!\\S)';
      flyout.applyPageLayoutForPersistent = function() {
        if (!document.documentElement.className.match( new RegExp(persistentClassRegExp) )) {
          document.documentElement.className += ' ' + persistentClassOnBody;
        }
      };

      flyout.unapplyPageLayoutForPersistent = function() {
        document.documentElement.className = document.documentElement.className.replace( new RegExp(persistentClassRegExp, 'g'), '');
      };

      flyout.persist = function() {
        flyout.applyPageLayoutForPersistent();
        flyout.show();
        if (config.isCompactEWCRendered) {
          flyout.align();
        }
      };

      flyout.unpersist = function() {
        flyout.unapplyPageLayoutForPersistent();
        flyout.hide();
      };

      var resizeCallback = function() {
        if (flyout.ableToPersist()) {
          flyout.persist();
        }
        else {
          flyout.unpersist();
        }
      };

      flyout.bindEvents = function() {
        if (window.addEventListener) {
          window.addEventListener('resize', resizeCallback, false);
          if (config.isCompactEWCRendered) {
            window.addEventListener('scroll', flyout.align, false);
          }
        }
      };

      flyout.unbindEvents = function() {
        if (window.removeEventListener) {
          window.removeEventListener('resize', resizeCallback, false);
          if (config.isCompactEWCRendered) {
            window.removeEventListener('scroll', flyout.align, false);
          }
        }
      };

      var persistentCheck = checkForPersistent();

      if (persistentCheck.result) {
        flyout.persist();
        if (window.ue && ue.tag) {
          ue.tag('ewc:persist');
        }
      } else {
        if (window.ue && ue.tag) {
          ue.tag('ewc:unpersist');
          if (persistentCheck.reason === 'noAui') {
            ue.tag('ewc:unpersist:noAui');
          }
          if (persistentCheck.reason === 'viewport') {
            ue.tag('ewc:unpersist:viewport');
          }
          if (persistentCheck.reason === 'emptycart') {
            ue.tag('ewc:unpersist:emptycart');
          }
          if (persistentCheck.reason === 'iOS') {
            ue.tag('ewc:unpersist:iOS');
          }
        }
      }

      if (window.ue && ue.tag)  {
        if (flyout.hasQualifiedViewportForPersistent()) {
          ue.tag('ewc:bview');
        }
        else {
          ue.tag('ewc:sview');
        }
      }
      flyout.bindEvents();

      return flyout;
    }());

    return config;
  }()));

  if (typeof uet === 'function') {
    uet('x2', 'ewc', {wb: 1});
    (window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function() {
      uet('bb', 'ewc', {wb: 1});
    });
  }

  if (window.ue && ue.tag) {
    ue.tag('ewc');
    ue.tag('ewc:unrec');
    ue.tag('ewc:cartsize:0');

    if ( window.P && window.P.AUI_BUILD_DATE ) {
      ue.tag('ewc:aui');
    } else {
      ue.tag('ewc:noAui');
    }
  }
}());
</script>
    
  </div>

  
  

</header>


<script type='text/javascript'>window.navmet.push({key:'NavBar',end:+new Date(),begin:window.navmet.main});</script>


<script type="text/javascript">
  if (window.ue_t0) {
    window.navmet.push({key:"NavMainPaintEnd",end:+new Date(),begin:window.ue_t0});
    window.navmet.push({key:"NavFirstPaintEnd",end:+new Date(),begin:window.ue_t0});
  }
</script>


<script type='text/javascript'>
    <!--
    window.$Nav && $Nav.declare('config.fixedBarBeacon',false);
    window.$Nav && $Nav.when("data").run(function(data) { data({"freshTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<style>#nav-flyout-fresh{width:269px;padding:0;}#nav-flyout-fresh .nav-flyout-content{padding:0;}</style><a href='/amazonfresh'><img src='https://images-na.ssl-images-amazon.com/images/G/01/omaha/images/yoda/flyout_72dpi._V270255989_.png' /></a>"}}}},"cartTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_cart_timeout"},"title":"Oops!","paragraph":"There is a problem retrieving your cart right now"}}}},"primeTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<a href='/gp/prime?ref_=nav_prime_btn_fb'><img src='https://images-na.ssl-images-amazon.com/images/G/15/prime/yourprime/yourprime-client-fallback._V316467452_.png' /></a>"}}}},"ewcTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_ewc_timeout"},"title":"Oops!","paragraph":"There is a problem retrieving your cart right now"}}}},"errorWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wish List","url":"/gp/registry/wishlist/?ref_=nav_err_wishlist"},"title":"Oops!","paragraph":"There is a problem retrieving the list right now"}}}},"emptyWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wish List","url":"/gp/registry/wishlist/?ref_=nav_err_empty_wishlist"},"title":"Oops!","paragraph":"Your list is empty"}}}},"yourAccountContent":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Account","url":"/gp/css/homepage.html?ref_=nav_err_youraccount"},"title":"Oops!","paragraph":"There is a problem retrieving the list right now"}}}},"shopAllTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"There is a problem retrieving the list right now"}}}},"kindleTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"There is a problem retrieving the list right now"}}}}}); });
window.$Nav && $Nav.when("util.templates").run("FlyoutErrorTemplate", function(templates) {
      templates.add("flyoutError", "<# if(error.title) { #><span class='nav-title'><#=error.title #></span><# } #><# if(error.paragraph) { #><p class='nav-paragraph'><#=error.paragraph #></p><# } #><# if(error.button) { #><a href='<#=error.button.url #>' class='nav-action-button' ><span class='nav-action-inner'><#=error.button.text #></span></a><# } #>");
    });

    if (typeof uet == 'function') {
    uet('bb', 'iss-init-pc', {wb: 1});
  }
  if (!window.$SearchJS && window.$Nav) {
    window.$SearchJS = $Nav.make('sx');
  }

  var opts = {
    host: "completion.amazon.com/search/complete"
  , marketId: "7"
  , obfuscatedMarketId: "A2EUQ1WTGCTBG2"
  , searchAliases: ["aps","amazon-devices","stripbooks","french-books","audible","dvd","popular","videogames","software","vhs","classical","electronics","kitchen","mobile-apps","watches","sporting","tools","baby","digital-text","financial","beauty","hpc","pets","lawngarden","luggage","toys","office-products","automotive","grocery","mi","jewelry","gift-cards","apparel","shoes","smart-home","black-friday","cyber-monday","warehouse-deals","handmade","handmade-jewelry","handmade-home-and-kitchen","industrial","instant-video","alexa-skills","todays-deals","specialty-aps-sns","fashion","fashion-womens","fashion-womens-clothing","fashion-womens-jewelry","fashion-womens-shoes","fashion-womens-watches","fashion-womens-handbags","fashion-mens","fashion-mens-clothing","fashion-mens-jewelry","fashion-mens-shoes","fashion-mens-watches","fashion-girls","fashion-girls-clothing","fashion-girls-jewelry","fashion-girls-shoes","fashion-girls-watches","fashion-boys","fashion-boys-clothing","fashion-boys-jewelry","fashion-boys-shoes","fashion-boys-watches","fashion-baby","fashion-baby-boys","fashion-baby-girls","fashion-luggage"]
  , filterAliases: []
  , pageType: "Detail"
  , requestId: "1KMDY2JPGP2X3R80G8WC"
  , sessionId: "138-4669640-7712440"
  , language: "en_CA"
  , customerId: ""
  , b2b: 0
  , fresh: 0
  , isJpOrCn: 0
  , isUseAuiIss: 1
};

var issOpts = {
    fallbackFlag: 1
  , isDigitalFeaturesEnabled: 0
  , isWayfindingEnabled: 0
  , dropdown: "select.searchSelect"
  , departmentText: "in {department}"
  , suggestionText: "Search suggestions"
  , recentSearchesTreatment: "C"
  , authorSuggestionText: ": all books"
  , translatedStringsMap: {"sx-recent-searches":"Recent searches","sx-your-recent-search":"Inspired by your recent search"}
  , biaTitleText: ""
  , biaPurchasedText: ""
  , biaViewAllText: ""
  , biaViewAllManageText: ""
  , biaAndText: ""
  , biaManageText: ""
  , biaWeblabTreatment: ""
  , issNavConfig: {}
  , np: 0
  , issCorpus: []
  , cf: 1
  , removeDeepNodeISS: ""
  , trendingTreatment: "C"
  , useAPIV2: ""
  , opfSwitch: ""
  , isISSDesktopRefactorEnabled: "1"
  , useServiceHighlighting: "true"
  , isInternal: 0
  , isAPICachingDisabled: true
  , isBrowseNodeScopingEnabled: false
  , isStorefrontTemplateEnabled: false
  , disableAutocompleteOnFocus: ""
};

  if (opts.isUseAuiIss === 1 && window.$Nav) {
  window.$Nav.when('sx.iss').run('iss-mason-init', function(iss){
    var issInitObj = buildIssInitObject(opts, issOpts, true);

    new iss.IssParentCoordinator(issInitObj);

    $SearchJS.declare('canCreateAutocomplete', issInitObj);
  });
} else if (window.$SearchJS) {
  var iss;

  // BEGIN Deprecated globals
  var issHost = opts.host
    , issMktid = opts.marketId
    , issSearchAliases = opts.searchAliases
    , updateISSCompletion = function() { iss.updateAutoCompletion(); };
  // END deprecated globals


  $SearchJS.when('jQuery', 'search-js-autocomplete-lib').run('autocomplete-init', initializeAutocomplete);
  $SearchJS.when('canCreateAutocomplete').run('createAutocomplete', createAutocomplete);

} // END conditional for window.$SearchJS
  function initializeAutocomplete(jQuery) {
  var issInitObj = buildIssInitObject(opts, issOpts);
  $SearchJS.declare("canCreateAutocomplete", issInitObj);
} // END initializeAutocomplete
  function initSearchCsl(searchCSL, issInitObject) {
  searchCSL.init(
    opts.pageType,
    (window.ue && window.ue.rid) || opts.requestId
  );
  $SearchJS.declare("canCreateAutocomplete", issInitObject);
} // END initSearchCsl
  function createAutocomplete(issObject) {
  iss = new AutoComplete(issObject);

  $SearchJS.publish("search-js-autocomplete", iss);

  logMetrics();
} // END createAutocomplete
  function buildIssInitObject(opts, issOpts, isNewIss) {
    var issInitObj = {
        src: opts.host
      , sessionId: opts.sessionId
      , requestId: opts.requestId
      , mkt: opts.marketId
      , obfMkt: opts.obfuscatedMarketId
      , pageType: opts.pageType
      , language: opts.language
      , customerId: opts.customerId
      , fresh: opts.fresh
      , b2b: opts.b2b
      , aliases: opts.searchAliases
      , fb: issOpts.fallbackFlag
      , isDigitalFeaturesEnabled: issOpts.isDigitalFeaturesEnabled
      , isWayfindingEnabled: issOpts.isWayfindingEnabled
      , issPrimeEligible: issOpts.issPrimeEligible
      , deptText: issOpts.departmentText
      , sugText: issOpts.suggestionText
      , filterAliases: opts.filterAliases
      , biaWidgetUrl: opts.biaWidgetUrl
      , recentSearchesTreatment: issOpts.recentSearchesTreatment
      , authorSuggestionText: issOpts.authorSuggestionText
      , translatedStringsMap: issOpts.translatedStringsMap
      , biaTitleText: ""
      , biaPurchasedText: ""
      , biaViewAllText: ""
      , biaViewAllManageText: ""
      , biaAndText: ""
      , biaManageText: ""
      , biaWeblabTreatment: ""
      , issNavConfig: issOpts.issNavConfig
      , cf: issOpts.cf
      , ime: opts.isJpOrCn
      , mktid: opts.marketId
      , qs: opts.isJpOrCn
      , issCorpus: issOpts.issCorpus
      , deepNodeISS: {
          searchAliasAccessor: function($) {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAlias()) ||
                   $('select.searchSelect').children().attr('data-root-alias');
          },
          searchAliasDisplayNameAccessor: function() {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAliasDisplayName());
          }
        }
      , removeDeepNodeISS: issOpts.removeDeepNodeISS
      , trendingTreatment: issOpts.trendingTreatment
      , useAPIV2: issOpts.useAPIV2
      , opfSwitch: issOpts.opfSwitch
      , isISSDesktopRefactorEnabled: issOpts.isISSDesktopRefactorEnabled
      , useServiceHighlighting: issOpts.useServiceHighlighting
      , isInternal: issOpts.isInternal
      , isAPICachingDisabled: issOpts.isAPICachingDisabled
      , isBrowseNodeScopingEnabled: issOpts.isBrowseNodeScopingEnabled
      , isStorefrontTemplateEnabled: issOpts.isStorefrontTemplateEnabled
      , disableAutocompleteOnFocus: issOpts.disableAutocompleteOnFocus
    };
  
    // If we aren't using the new ISS then we need to add these properties
    
    if (!isNewIss) {
      issInitObj.dd = issOpts.dropdown; // The element with id searchDropdownBox doesn't exist in C.
      issInitObj.imeSpacing = issOpts.imeSpacing;
      issInitObj.isNavInline = 1;
      issInitObj.triggerISSOnClick = 0;
      issInitObj.sc = 1;
      issInitObj.np = issOpts.np;
    }
  
    return issInitObj;
  } // END buildIssInitObject
  function logMetrics() {
  if (typeof uet == 'function' && typeof uex == 'function') {
      uet('be', 'iss-init-pc',
          {
              wb: 1
          });
      uex('ld', 'iss-init-pc',
          {
              wb: 1
          });
  }
} // END logMetrics
  
    
window.$Nav && $Nav.declare('config.navDeviceType','desktop');

window.$Nav && $Nav.declare('config.navDebugHighres',false);

window.$Nav && $Nav.declare('config.pageType','Detail');
window.$Nav && $Nav.declare('config.subPageType','null');

window.$Nav && $Nav.declare('config.dynamicMenuUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdynamic\x2Dmenu.html');

window.$Nav && $Nav.declare('config.dismissNotificationUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdismissnotification.html');

window.$Nav && $Nav.declare('config.enableDynamicMenus',true);

window.$Nav && $Nav.declare('config.isInternal',false);

window.$Nav && $Nav.declare('config.isBackup',false);

window.$Nav && $Nav.declare('config.isRecognized',false);

window.$Nav && $Nav.declare('config.transientFlyoutTrigger','\x23nav\x2Dtransient\x2Dflyout\x2Dtrigger');

window.$Nav && $Nav.declare('config.subnavFlyoutUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fgeneric.html');
window.$Nav && $Nav.declare('config.isSubnavFlyoutMigrationEnabled',true);

window.$Nav && $Nav.declare('config.recordEvUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Frecordevent.html');
window.$Nav && $Nav.declare('config.recordEvInterval',15000);
window.$Nav && $Nav.declare('config.sessionId','138\x2D4669640\x2D7712440');
window.$Nav && $Nav.declare('config.requestId','1KMDY2JPGP2X3R80G8WC');

window.$Nav && $Nav.declare('config.alexaListEnabled',false);

window.$Nav && $Nav.declare('config.readyOnATF',false);

window.$Nav && $Nav.declare('config.dynamicMenuArgs',{"rid":"1KMDY2JPGP2X3R80G8WC","isFullWidthPrime":0,"isPrime":0,"dynamicRequest":1,"weblabs":"","isFreshRegionAndCustomer":"","primeMenuWidth":310});

window.$Nav && $Nav.declare('config.customerName',false);

window.$Nav && $Nav.declare('config.yourAccountPrimeURL',null);

window.$Nav && $Nav.declare('config.yourAccountPrimeHover',true);

window.$Nav && $Nav.declare('config.searchBackState',{});

window.$Nav && $Nav.declare('nav.inline');

(function (i) {
i.onload = function() {window.uet && uet('ne')};
i.src = window._navbarSpriteUrl;
}(new Image()));

window.$Nav && $Nav.declare('config.autoFocus',false);

window.$Nav && $Nav.declare('config.responsiveTouchAgents',["ieTouch"]);

window.$Nav && $Nav.declare('config.responsiveGW',false);

window.$Nav && $Nav.declare('config.pageHideEnabled',false);

window.$Nav && $Nav.declare('config.sslTriggerType','null');
window.$Nav && $Nav.declare('config.sslTriggerRetry',0);

window.$Nav && $Nav.declare('config.doubleCart',false);

window.$Nav && $Nav.declare('config.signInOverride',true);

window.$Nav && $Nav.declare('config.signInTooltip',true);

window.$Nav && $Nav.declare('config.isPrimeMember',false);

window.$Nav && $Nav.declare('config.packardGlowTooltip',false);

window.$Nav && $Nav.declare('config.packardGlowFlyout',false);

window.$Nav && $Nav.declare('config.rightMarginAlignEnabled',true);

window.$Nav && $Nav.declare('config.flyoutAnimation',false);

window.$Nav && $Nav.declare('config.campusActivation','null');

window.$Nav && $Nav.declare('config.primeTooltip',false);

window.$Nav && $Nav.declare('config.primeDay',false);

window.$Nav && $Nav.declare('config.disableBuyItAgain',false);

window.$Nav && $Nav.declare('config.enableCrossShopBiaFlyout',false);

window.$Nav && $Nav.declare('config.pseudoPrimeFirstBrowse',null);

window.$Nav && $Nav.declare('config.sdaYourAccount',false);

window.$Nav && $Nav.declare('config.csYourAccount',false);

window.$Nav && $Nav.declare('config.cartFlyoutDisabled',true);

window.$Nav && $Nav.declare('config.isTabletBrowser',false);

window.$Nav && $Nav.declare('config.HmenuProximityArea',[200,200,200,200]);

window.$Nav && $Nav.declare('config.HMenuIsProximity',true);

window.$Nav && $Nav.declare('config.isPureAjaxALF',false);

window.$Nav && $Nav.declare('config.accountListFlyoutRedesign',false);

window.$Nav && $Nav.declare('config.navfresh',false);

window.$Nav && $Nav.declare('config.isFreshRegion',false);

if (window.ue && ue.tag) { ue.tag('navbar'); };

window.$Nav && $Nav.declare('config.blackbelt',true);

window.$Nav && $Nav.declare('config.beaconbelt',true);

window.$Nav && $Nav.declare('config.accountList',true);

window.$Nav && $Nav.declare('config.iPadTablet',false);

window.$Nav && $Nav.declare('config.searchapiEndpoint',false);

window.$Nav && $Nav.declare('config.timeline',false);

window.$Nav && $Nav.declare('config.timelineAsinPriceEnabled',false);

window.$Nav && $Nav.declare('config.timelineDeleteEnabled',false);



window.$Nav && $Nav.declare('config.extendedFlyout',false);

window.$Nav && $Nav.declare('config.flyoutCloseDelay',600);

window.$Nav && $Nav.declare('config.pssFlag',0);

window.$Nav && $Nav.declare('config.isPrimeTooltipMigrated',false);

window.$Nav && $Nav.declare('config.isTimelineMigrationEnabled',false);

window.$Nav && $Nav.declare('config.hashCustomerAndSessionId','fb64de79b829797a445e6cb81a779324a14ee07e');

window.$Nav && $Nav.declare('config.isExportMode',false);

window.$Nav && $Nav.declare('config.languageCode','en_CA');

window.$Nav && $Nav.declare('config.environmentVFI','AmazonNavigationCards\x2Fdevelopment\x40B6048321973\x2DAL2_x86_64');



window.$Nav && $Nav.declare('config.isHMenuBrowserCacheDisable',false);

window.$Nav && $Nav.declare('config.signInUrlWithRefTag','https\x3A\x2F\x2Fwww.amazon.ca\x2Fap\x2Fsignin\x3Fopenid.pape.max_auth_age\x3D0\x26openid.return_to\x3Dhttps\x253A\x252F\x252Fwww.amazon.ca\x252FRage\x2DAgainst\x2DMachine\x252Fdp\x252FB0000028RR\x252F\x253F_encoding\x253DUTF8\x2526ref_\x253DnavSignInUrlRefTagPlaceHolder\x26openid.identity\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x252Fidentifier_select\x26openid.assoc_handle\x3Dcaflex\x26openid.mode\x3Dcheckid_setup\x26openid.claimed_id\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x252Fidentifier_select\x26openid.ns\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x26');

window.$Nav && $Nav.declare('config.isSmile',false);

window.$Nav && $Nav.declare('config.regionalStores',[]);

window.$Nav && $Nav.declare('config.isALFRedesignPT2',false);

window.$Nav && $Nav.declare('config.isNavALFRegistryGiftList',false);

window.$Nav && $Nav.declare('config.marketplaceId','A2EUQ1WTGCTBG2');

window.$Nav && $Nav.declare('config.exportTransitionState','none');

window.$Nav && $Nav.declare('config.enableAeeXopFlyout',true);

if (window.P && typeof window.P.declare === "function" && typeof window.P.now === "function") {
  window.P.now('packardGlowIngressJsEnabled').execute(function(glowEnabled) {
    if (!glowEnabled) {
      window.P.declare('packardGlowIngressJsEnabled', true);
    }
  });
  window.P.now('packardGlowStoreName').execute(function(storeName) {
    if (!storeName) {
      window.P.declare('packardGlowStoreName','music');
    }
  });
}

window.$Nav && $Nav.declare('configComplete');

    -->
</script>


<a id="skippedLink" tabindex="-1"></a>

<script type='text/javascript'>window.navmet.MainEnd = new Date();</script>
<script type="text/javascript">
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainEnd",end:+new Date(),begin:window.ue_t0});
    }
</script>
<!-- sp:feature:host-atf -->

          <script type="text/javascript">
              if(typeof uet === 'function'){uet('bb', 'atfClientSideWaitTimeDesktop', {wb: 1});};
          </script>
<div id='dp' class='music en_CA'>
         





<script type="text/javascript">

  if(typeof P !== "undefined" && typeof P.when === "function"){
    P.when('cf').execute(function() {
          P.when('navbarJS-jQuery').execute(function(){});
  P.when('finderFitsJS').execute(function(){});
  P.when('twister').execute(function(){});
  P.when('swfjs').execute(function(){});

    });
  }
</script>



<div id="percolate-ui-ilm_div">
<div cel_widget_id='percolate-ui-ilm_csm_instrumentation_wrapper' class='celwidget'>

          
    
    
    
    
    
    
            <div class="celwidget pd_rd_w-JTwNb pf_rd_p-fc7fc660-b5d5-41ec-a923-5f923eac8620 pf_rd_r-1KMDY2JPGP2X3R80G8WC pd_rd_r-7a596642-2f1b-4b87-833a-a407f5ba4dbd pd_rd_wg-jVwgh" cel_widget_id="desktop-dp-atf_26a9428c-6389-4260-805a-6605ef087c94" data-csa-c-content-id="fc7fc660-b5d5-41ec-a923-5f923eac8620" data-csa-c-slot-id="desktop-dp-atf-0" data-csa-c-type="widget"><div id="universal-detail-ilm" style="background-color: ;"> <div class="a-section a-spacing-none uilm-section"><a aria-label="Vinyl Day is around the corner. Shop exclusive deals on June 11" class="a-link-normal" href="/b?node=21229754011&pd_rd_w=JTwNb&pf_rd_p=fc7fc660-b5d5-41ec-a923-5f923eac8620&pf_rd_r=1KMDY2JPGP2X3R80G8WC&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_wg=jVwgh"><img alt="" src="https://images-na.ssl-images-amazon.com/images/G/15/CA-hq/2021/img/Music/XCM_Manual_1328148_1685144_CA_ca_pc_ilm_2x_ca_en_3861898_650x45_1X_en_CA._CB668258854_.jpg" height="45" width="650" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/15/CA-hq/2021/img/Music/XCM_Manual_1328148_1685144_CA_ca_pc_ilm_2x_ca_en_3861898_1300x90_2X_en_CA._CB668258854_.jpg"></a></div></div></div>
</div></div>
<div cel_widget_id='percolate-ui-lpo_csm_instrumentation_wrapper' class='celwidget'>






<div class="celwidget pd_rd_w-7g9Tn pf_rd_p-55ea5ed7-d8ce-4183-b0cf-37e635680f3e pf_rd_r-1KMDY2JPGP2X3R80G8WC pd_rd_r-7a596642-2f1b-4b87-833a-a407f5ba4dbd pd_rd_wg-jVwgh" cel_widget_id="desktop-dp-atf_session-similarities" data-csa-c-content-id="55ea5ed7-d8ce-4183-b0cf-37e635680f3e" data-csa-c-slot-id="desktop-dp-atf-1" data-csa-c-type="widget">












 
 




















        <div id="lpo-session-sims-feature" class="a-section similarities-widget sims-lpo-section">
             <div class="sims-lpo-hue-shield"></div> 
            <fieldset class="forScreenreaders">
                <h2 class="a-spacing-small a-color-base sims-lpo-header">Customers who viewed <span class="sims-lpo-header-title">Rage Against The Machine</span> also viewed</h2>
                <div class="a-row a-spacing-small sims-lpo-row">
                    <ul class="a-unordered-list a-nostyle a-vertical sims-lpo-list">
                        <div class="a-column a-span4 sims-lpo-grid-column">
        <div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px">
            <a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_lpo_15_img_0/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B0000029D9&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;float:left;">
                <img alt="Evil Empire" src="https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL160_.jpg" class="sims-lpo-image">
            </div></a>
            <div class="a-text-left a-fixed-left-grid-col sims-lpo-product-details a-col-right" style="padding-left:0%;float:left;">
                
        <div aria-hidden="true">
            
        <div class="p13n-sc-truncate p13n-sc-line-clamp-5 p13n-sc-truncate-desktop-type2" aria-hidden="true" data-rows="5">
            <a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_lpo_15_t_0/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B0000029D9&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC">Evil Empire</a>
        </div>
    
        </div>
    
                
        <div class="a-icon-row a-spacing-mini">
            <a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B0000029D9/ref=pd_lpo_15_cr_0/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC"><i class="a-icon a-icon-star a-star-5"><span class="a-icon-alt">4.8 out of 5 stars</span></i></a>
            <a class="a-size-small a-link-normal" href="/product-reviews/B0000029D9/ref=pd_lpo_15_cr_0/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC">1,389</a>
        </div>
    
                <div><span class="a-color-price"><span class='p13n-sc-price' >$15.48</span></span> </div>
                <a class="a-link-normal" href="/gp/offer-listing/B0000029D9/ref=pd_lpo_15_t_0/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC">35 used and new</a> from <span class="a-size-base a-color-price"><span class='p13n-sc-price' >$5.75</span></span>
            </div>
        </div></div>
    </div><div class="a-column a-span4 sims-lpo-grid-column">
        <div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px">
            <a class="a-link-normal" href="/Battle-Los-Angeles-Vinyl/dp/B07DV8WT6R/ref=pd_lpo_15_img_1/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B07DV8WT6R&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;float:left;">
                <img alt="The Battle Of Los Angeles (Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/71CgqwZKPCL._AC_UL160_.jpg" class="sims-lpo-image">
            </div></a>
            <div class="a-text-left a-fixed-left-grid-col sims-lpo-product-details a-col-right" style="padding-left:0%;float:left;">
                
        <div aria-hidden="true">
            
        <div class="p13n-sc-truncate p13n-sc-line-clamp-5 p13n-sc-truncate-desktop-type2" aria-hidden="true" data-rows="5">
            <a class="a-link-normal" href="/Battle-Los-Angeles-Vinyl/dp/B07DV8WT6R/ref=pd_lpo_15_t_1/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B07DV8WT6R&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC">The Battle Of Los Angeles (Vinyl)</a>
        </div>
    
        </div>
    
                
        <div class="a-icon-row a-spacing-mini">
            <a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B07DV8WT6R/ref=pd_lpo_15_cr_1/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC"><i class="a-icon a-icon-star a-star-5"><span class="a-icon-alt">4.8 out of 5 stars</span></i></a>
            <a class="a-size-small a-link-normal" href="/product-reviews/B07DV8WT6R/ref=pd_lpo_15_cr_1/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC">1,507</a>
        </div>
    
                <div><span class="a-color-price"><span class='p13n-sc-price' >$32.42</span></span> </div>
                <a class="a-link-normal" href="/gp/offer-listing/B07DV8WT6R/ref=pd_lpo_15_t_1/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC">21 used and new</a> from <span class="a-size-base a-color-price"><span class='p13n-sc-price' >$28.76</span></span>
            </div>
        </div></div>
    </div><div class="a-column a-span4 sims-lpo-grid-column a-span-last">
        <div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px">
            <a class="a-link-normal" href="/Renegades-Vinyl-Rage-Against-Machine/dp/B07DVGQJMY/ref=pd_lpo_15_img_2/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B07DVGQJMY&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;float:left;">
                <img alt="Renegades (Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/61Uqi1x%2BO2L._AC_UL160_.jpg" class="sims-lpo-image">
            </div></a>
            <div class="a-text-left a-fixed-left-grid-col sims-lpo-product-details a-col-right" style="padding-left:0%;float:left;">
                
        <div aria-hidden="true">
            
        <div class="p13n-sc-truncate p13n-sc-line-clamp-5 p13n-sc-truncate-desktop-type2" aria-hidden="true" data-rows="5">
            <a class="a-link-normal" href="/Renegades-Vinyl-Rage-Against-Machine/dp/B07DVGQJMY/ref=pd_lpo_15_t_2/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B07DVGQJMY&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC">Renegades (Vinyl)</a>
        </div>
    
        </div>
    
                
        <div class="a-icon-row a-spacing-mini">
            <a class="a-link-normal" title="4.7 out of 5 stars" href="/product-reviews/B07DVGQJMY/ref=pd_lpo_15_cr_2/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC"><i class="a-icon a-icon-star a-star-4-5"><span class="a-icon-alt">4.7 out of 5 stars</span></i></a>
            <a class="a-size-small a-link-normal" href="/product-reviews/B07DVGQJMY/ref=pd_lpo_15_cr_2/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC">780</a>
        </div>
    
                <div><span class="a-color-price"><span class='p13n-sc-price' >$39.76</span></span> <span class="sims-lpo-price-badge"><i class="a-icon a-icon-prime" role="img" aria-label="Prime"></i></span></div>
                <a class="a-link-normal" href="/gp/offer-listing/B07DVGQJMY/ref=pd_lpo_15_t_2/138-4669640-7712440?ie=UTF8&pd_rd_r=7a596642-2f1b-4b87-833a-a407f5ba4dbd&pd_rd_w=7g9Tn&pd_rd_wg=jVwgh&pf_rd_p=55ea5ed7-d8ce-4183-b0cf-37e635680f3e&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC">9 used and new</a> from <span class="a-size-base a-color-price"><span class='p13n-sc-price' >$35.76</span></span>
            </div>
        </div></div>
    </div>
                    </ul>
                </div>
            </fieldset>
        </div>
        
    







</div>
</div>

<div id="cp-merchandising-widget_div">
</div>


<div id="showing-breadcrumbs_div">
</div>


<div id="rw-preload-landing-image_div">
</div>

<script type="text/javascript"> 

(typeof setCSMReq === 'function') && setCSMReq("x1");

                if(typeof uet === 'function'){uet('bb', 'udpV3atfwait', {wb: 1});};
    if(typeof uet === 'function'){uet('be', 'atfClientSideWaitTimeDesktop', {wb: 1});};
</script>

        <div id="dp-container" class="a-container" role="main">

            
    <script type="text/javascript">
    if(typeof uet === 'function'){uet('af', 'atfClientSideWaitTimeDesktop', {wb: 1});};
  </script>

<script type="a-state" data-a-state="{&quot;key&quot;:&quot;desktop-landing-image-data&quot;}">{"landingImageUrl":"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L.__AC_SX300_SY300_QL70_ML2_.jpg"}</script>

<script type="text/javascript">    if(typeof uet === 'function'){uet('be', 'udpV3atfwait', {wb: 1});};
                if(typeof uex === 'function'){uex('ld', 'udpV3atfwait', {wb: 1});};
</script>
  





    


       
































































































































































































































































         
        


















<style type="text/css">
#leftCol {
width:24.0%;
}
.centerColAlign{
margin-left:25.5%;
}
html[dir="rtl"] .centerColAlign{
margin-right:25.5%;
}
</style>

<style type="text/css">
#rightCol {
width: 270px;
}
.centerColAlign{
margin-right:290px;
}
</style>















<div id="orderInformationGroup" class="celwidget" data-feature-name="orderInformationGroup">


























<script> ue && typeof ue.count === 'function' && ue.count("OIG.csm.common.rendered", 1); </script>


















</div>


















<div id="companyCompliancePolicies_feature_div" class="celwidget" data-feature-name="companyCompliancePolicies">






































</div>






<div id="ppd">

<div id="rightCol" class="rightCol rightCol-bbcxoverride">














<div id="tellAFriendBox_feature_div" class="celwidget" data-feature-name="tellAFriendBox">












<div cel_widget_id="tell-a-friend-desktop" class="celwidget">








<div id="tell-a-friend" data-close="Close" data-title="Share this item via Email" class="a-section a-text-center a-spacing-small">
<div style="font-size:13px; line-height:19px">






<a id="swfMailTo" class="a-link-normal email" title="Share via e-mail" href="mailto:?body=I%20want%20to%20recommend%20this%20product%20at%20Amazon%0A%0ARage%20Against%20The%20Machine%0Aby%20Ergodebooks%20Ships%20from%20USA%0ALearn%20more%3A%20https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_sw_em_r_mt_dp_1KMDY2JPGP2X3R80G8WC&amp;subject=Check%20this%20out%20at%20Amazon">Share</a><span class="a-letter-space"></span>
<a id="swfImageMailTo" class="a-link-normal email" title="Share via e-mail" href="mailto:?body=I%20want%20to%20recommend%20this%20product%20at%20Amazon%0A%0ARage%20Against%20The%20Machine%0Aby%20Ergodebooks%20Ships%20from%20USA%0ALearn%20more%3A%20https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_sw_em_r_mt_dp_1KMDY2JPGP2X3R80G8WC&amp;subject=Check%20this%20out%20at%20Amazon"><i class="a-icon a-icon-share-email" role="img" aria-label="Email"></i></a><span class="a-letter-space"></span>
<script type="text/javascript">(function(f) {var _np=(window.P._namespace("DetailPageTellAFriendTemplates"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.when('A','ready').execute('swfMailTo', function(A){
var $ = A.$;
function collectMetrics( placementId ) {
A.ajax('/gp/aw/social/swf/metrics.html/ref=cm_sw_cl_em_'+ placementId, {
method: 'post',
params: {
id: 'mailtoDp',
result: 'mailto share triggered'
}
});
}
$('#swfMailTo,#swfImage').click( function(){
collectMetrics('dp_1KMDY2JPGP2X3R80G8WC');
});
});
}));</script>






<a id="facebook" data-height="400" class="a-link-normal swf-social-site" target="_blank" rel="noopener" title="Facebook" href="/gp/redirect.html/ref=cm_sw_cl_fa_dp_1KMDY2JPGP2X3R80G8WC?_encoding=UTF8&amp;location=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Fshare%3F_encoding%3DUTF8%26app_id%3D465632727431967%26display%3Dpopup%26href%3Dhttps%253A%252F%252Fwww.amazon.ca%252Fdp%252FB0000028RR%252Fref%253Dcm_sw_r_fa_dp_1KMDY2JPGP2X3R80G8WC%26redirect_uri%3Dhttps%253A%252F%252Fwww.amazon.ca%252Fdp%252FB0000028RR%252Fref%253Dcm_sw_s_fa_dp_1KMDY2JPGP2X3R80G8WC%26hashtag%3D%2523Amazon&amp;token=34268044F154806BE1983183DF821D880F9BB41B"><i class="a-icon a-icon-share-facebook" role="img" aria-label="Facebook"></i></a><span class="a-letter-space"></span>






<a id="twitter" data-height="400" class="a-link-normal swf-social-site" target="_blank" rel="noopener" title="Twitter" href="/gp/redirect.html/ref=cm_sw_cl_tw_dp_1KMDY2JPGP2X3R80G8WC?_encoding=UTF8&amp;location=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Foriginal_referer%3Dhttps%25253A%25252F%25252Fwww.amazon.ca%25252Fgp%25252Fproduct%25252FB0000028RR%25252Fref%25253Dcm_sw_r_tw_dp_1KMDY2JPGP2X3R80G8WC%26text%3DRage%2520Against%2520The%2520Machine%2520Rage%2520Against%2520The%2520Machine%26related%3Damazondeals%252Camazonmp3%26url%3Dhttps%253A%252F%252Fwww.amazon.ca%252Fdp%252FB0000028RR%252Fref%253Dcm_sw_r_tw_dp_1KMDY2JPGP2X3R80G8WC%26via%3Damazon&amp;token=892F190F5547F1FC0A3FA86423CCC9AEE095E23C"><i class="a-icon a-icon-share-twitter" role="img" aria-label="Twitter"></i></a><span class="a-letter-space"></span>






<a id="pinterest" data-height="570" class="a-link-normal swf-social-site" target="_blank" rel="noopener" title="Pinterest" href="/gp/redirect.html/ref=cm_sw_cl_pi_dp_1KMDY2JPGP2X3R80G8WC?_encoding=UTF8&amp;location=https%3A%2F%2Fpinterest.com%2Fpin%2Fcreate%2Fbutton%3Furl%3Dhttps%253A%252F%252Fwww.amazon.ca%252Fdp%252FB0000028RR%252Fref%253Dcm_sw_r_pi_dp_1KMDY2JPGP2X3R80G8WC%26description%3DRage%2520Against%2520The%2520Machine%2520Rage%2520Against%2520The%2520Machine%26media%3Dhttps%253A%252F%252Fm.media-amazon.com%252Fimages%252FI%252F61sbdhhOpkL.jpg&amp;token=EFE66309019FAEE3C076CD35A842B2EAAC6F6242"><i class="a-icon a-icon-share-pinterest" role="img" aria-label="Pinterest"></i></a><span class="a-letter-space"></span>


</div>
</div>
<script type="text/javascript">(function(f) {var _np=(window.P._namespace("DetailPageTellAFriendTemplates"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.when('A', 'jQuery').execute('tellAFriendBox', function(A,$) {
var taf = $('#tell-a-friend');
taf.children("[data-height]").click(function() {
var height = $(this).attr('data-height');
window.open(this.href, '_blank', 'location=yes,width=700,height=' + height);
return false;
});
<!-- https://sim.amazon.com/issues/SHARE-1795 --!>
A.on('a:pageUpdate', function() {
var featureElement = document.querySelectorAll("[id='tellAFriendBox_feature_div']");
if (featureElement.length == 2) {
if (!featureElement[1].hidden) {
featureElement[1].hidden = true;
window.ue.count('tell-a-friend-desktop.duplicated', 1);
} else {
window.ue.count('tell-a-friend-desktop.duplicated', 0);
}
}
});
});
}));</script>




</div>























</div>
















































<div id="desktop_buybox" class="celwidget" data-feature-name="desktop_buybox">












<div id="buybox">

















































<div id="desktop_accordion" class="celwidget" data-feature-name="desktop_accordion">

























    
        
        
        
            
            




<div id="accordionRows_feature_div" data-feature-name="accordionRows" data-template-name="accordionRows" class="a-section a-spacing-none">













<div id="accordionRows" class="celwidget" data-feature-name="accordionRows">






























    
        
        
        
            
            
































































































<script type="text/javascript">
P.when("A", "a-expander", "ready").execute(function(A, expander) {
A.on("a:accordion:buybox-accordion:select", function(data) {
// Change active accordion header price color to red
A.$("#buyBoxAccordion").find(".accordion-header span.header-price").
removeClass("a-color-price").addClass("a-color-secondary");
A.$(data.selectedRow.$row).find(".accordion-header span.header-price").
removeClass("a-color-secondary").addClass("a-color-price");
// Change active accordion header prime logo to opaque
A.$("#buyBoxAccordion").find(".accordion-header i.header-prime-logo").
addClass("opacity-50");
A.$(data.selectedRow.$row).find(".accordion-header i.header-prime-logo").
removeClass("opacity-50");
//initialize accordion expander
expander.initializeExpanders();
});
// Record metrics for clicking usedAccordionRow
A.on("a:accordion:buybox-accordion:usedAccordionRow:select", function(data) {
var ue = window.ue;
if (ue && typeof ue.count === 'function') {
ue.count('dpOffers:buybox:mobile:usedAccordionOpen', (ue.count('dpOffers:buybox:mobile:usedAccordionOpen') || 0) + 1);
}
});
});
</script>




<div id="buyBoxAccordion" data-a-accordion-name="buybox-accordion" class="a-box-group a-accordion a-spacing-large" role="">



























































<div id="newAccordionRow" data-buying-option-index="0" class="a-box a-accordion-active celwidget" data-a-accordion-row-name="newAccordionRow"><div class="a-box-inner a-accordion-row-container">
<div class="a-accordion-row-a11y" role="radio" aria-checked="true" aria-expanded="true"><a data-action="a-accordion" class="a-accordion-row a-declarative accordion-header" href="#" aria-label=""><i class="a-icon a-accordion-radio a-icon-radio-active"></i><h5>





































































<div id="buyNew_cbb">















    
    
        
    



    
    
        
    
    





<div class="a-row">
   
        <div class="a-column a-span6">
        <span class="a-text-bold">Buy new:</span>
        </div>
   
   
        
        
        
              <div class="a-column a-span6 a-text-right a-span-last">
              <span id="newBuyBoxPrice" class="a-size-base a-color-price header-price a-text-normal">$32.21</span>
              </div>
        
   

    
    

    
    



























<div id="abbreviate_shipping_accordion_head" class="a-column a-span12 a-text-left show-on-unselected">
<div class="a-row a-color-secondary">



</div>
</div>


<div id="mfn_shipping_accordion_head" class="a-column a-span12 a-text-left show-on-unselected">
<div class="a-row a-color-secondary">























</div>
</div>









<div id="abbreviate_fasttrack_accordion_head" class="a-column a-span12 a-text-left show-on-unselected">
<div class="a-row a-color-secondary">


<div id="fast-track" class="a-section a-spacing-none">


<input type="hidden" id="ftSelectAsin" value="B0000028RR"/>


<input type="hidden" id="ftSelectMerchant" value="A3C9TTIOE1L9MO"/>







<div id="fast-track-message-abbreviate" class="a-section a-spacing-none">
<div class="a-section a-spacing-none">


    
    $4.73
 delivery: <b>


June 23 - July 12

</b>








</div>
</div>







</div>
</div>
</div>



    







<div id="sfsb_accordion_head" class="a-section show-on-unselected sfsb-header-text">
<div class="a-row">
<div class="a-column a-span12 a-text-left truncate">
<span class="a-size-small">
Ships from:
</span>
<span class="a-size-small">
Ergodebooks Ships from USA
</span>
</div>
</div>
<div class="a-row">
<div class="a-column a-span12 a-text-left truncate">
<span class="a-size-small">
Sold by:
</span>
<span class="a-size-small">
Ergodebooks Ships from USA
</span>
</div>
</div>
</div>

</div>
</div>








</h5></a></div>
<div class="a-accordion-inner accordion-row-content">












  
      
      
      
          
      
  


 <div class="a-section">

    

     <form method="post" id="addToCart" action="/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance" class="a-content">
              <input type='hidden' name='CSRF' value='g23AVDCwHo1VyRYMPo1O0gNzdlaVAYeJgOEY0/VyzvGaAAAADAAAAABguq2AcmF3AAAAABVX8CwXqz4nuL9RKX///w==' />
              <input type="hidden" id="offerListingID" name="offerListingID" value="UNpOMQajhZ4LWcHndMWq3Wt2GAQfpb6sUJyFi55CX7O3SpXld0LRmVxdWHnJdreSFAgR7h9l4ahD0siajR3ODM0BfTqOGgSFsINUUnJbG5dGa2z4%2Bjur6zE%2FAAe%2BDfL0QF%2BUKexz2eEmQNDI7S2aH5VObYOjovmzUklZGxhzfD6oyXyuRKooZHok2VY1z%2BCU">
              <input type="hidden" id="session-id" name="session-id" value="138-4669640-7712440">
              <input type="hidden" id="ASIN" name="ASIN" value="B0000028RR">
              <input type="hidden" id="isMerchantExclusive" name="isMerchantExclusive" value="0">
              <input type="hidden" id="merchantID" name="merchantID" value="A3C9TTIOE1L9MO">
              <input type="hidden" id="isAddon" name="isAddon" value="0">
              <input type="hidden" id="nodeID" name="nodeID" value="">
              <input type="hidden" id="sellingCustomerID" name="sellingCustomerID" value="">
              <input type="hidden" id="qid" name="qid" value="">
              <input type="hidden" id="sr" name="sr" value="">
              <input type="hidden" id="storeID" name="storeID" value="">
              <input type="hidden" id="tagActionCode" name="tagActionCode" value="">
              <input type="hidden" id="viewID" name="viewID" value="glance">
              <input type="hidden" id="rebateId" name="rebateId" value="">
              <input type="hidden" id="ctaDeviceType" name="ctaDeviceType" value="desktop">
              <input type="hidden" id="ctaPageType" name="ctaPageType" value="detail">
              <input type="hidden" id="usePrimeHandler" name="usePrimeHandler" value="0">
         
             

             
             

              



    
            
                
                




            

            
            

            
            

            
            <input type="hidden" id="rsid" name="rsid" value="138-4669640-7712440">
            <input type="hidden" id="sourceCustomerOrgListID" name="sourceCustomerOrgListID" value="">
            <input type="hidden" id="sourceCustomerOrgListItemID" name="sourceCustomerOrgListItemID" value="">
            <input type="hidden" name="wlPopCommand" value="">
            
            

     














<div id="desktop_qualifiedBuyBox" class="celwidget" data-feature-name="desktop_qualifiedBuyBox">



















    
        
        
        
            
                
            
            
<div class="a-section a-spacing-none a-padding-none">



















<div id="booksAdditionalPriceInfoContainer" class="celwidget" data-feature-name="booksAdditionalPriceInfoContainer">
































</div>
























<div id="invitePlatform_feature_div" class="celwidget" data-feature-name="invitePlatform">




































</div>
























<div id="pointsInsideBuyBox_feature_div" class="celwidget" data-feature-name="pointsInsideBuyBox">





















































</div>
























<div id="agsShippingAndIfdInsideBuyBox_feature_div" class="celwidget" data-feature-name="agsShippingAndIfdInsideBuyBox">
























<!-- For LightningDeal use case, agsShippingAndIfdInsideBuyBox is only configured on regular offer, so set defaultPageContext as buyingPrice -->

























</div>
























<div id="shippingMessageInsideBuyBox_feature_div" class="celwidget" data-feature-name="shippingMessageInsideBuyBox">


































<div class="a-section a-spacing-base a-text-left">


































<span id="price-shipping-message" class="a-size-base a-color-base"></span>





</div>



























</div>
























<div id="couponsInBuybox_feature_div" class="celwidget" data-feature-name="couponsInBuybox">
















































</div>
























<div id="deliveryBlockContainer" class="celwidget" data-feature-name="deliveryBlockContainer">





























<div id="deliveryBlock_feature_div" class="celwidget" data-feature-name="deliveryBlock">














<div id="deliveryBlockMessage" class="a-section">

<div id="mir-layout-DELIVERY_BLOCK"><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE">$4.73 delivery: <b> June 23 - July 12 </b>
</div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-UPSELL"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-EXTENDED_DELIVERY_PROMISE_MESSAGE"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-HOLIDAY_DELIVERY_MESSAGE"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-SUPPLEMENTAL_DELIVERY_MESSAGE"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-CORE_FREE_SHIPPING_SUPPLEMENTARY_MESSAGE"></div></div>
</div>




<input type="hidden" id="deliveryBlockSelectAsin" value="B0000028RR"/>


<input type="hidden" id="deliveryBlockSelectMerchant" value="A3C9TTIOE1L9MO"/>

<script type="text/javascript">
P.when("A", "jQuery").execute(function(A, $) {
$("#selectQuantity [name='quantity'], #mobileQuantityDropDown").live("change", function (event) {
if (event.updateDeliveryBlockOnQuantityChange) {
return;
}
event.updateDeliveryBlockOnQuantityChange = 1;
// "#buybox" is included in this list because if there is no accordion row, then it is a single-offer layout
var accordionRow = $(this).closest('[id$="AccordionRow"], #buybox');
var quantity = $(this).val();
var asin = accordionRow.find("#deliveryBlockSelectAsin").val();
var merchantId = accordionRow.find("#deliveryBlockSelectMerchant").val();
if (!asin || !merchantId) {
return;
}
var params = [];
params.push("asin=" + asin);
params.push("quantity=" + quantity);
params.push("merchantId=" + merchantId);
$.ajax({
type: "POST",
url: "/gp/product/features/dp-fast-track/udp-ajax-handler/get-quantity-update-message.html?ie=UTF8",
contentType: 'application/x-www-form-urlencoded;charset=utf-8',
data: params.join('&'),
accordionRow: accordionRow,
dataType: "html",
success: function(objResponse) {
if (objResponse != null && objResponse != "") {
accordionRow.find("#deliveryBlockMessage").replaceWith(objResponse);
}
}
});
return;
});
});
</script>

























</div>
























<div id="cipInsideDeliveryBlock_feature_div" class="celwidget" data-feature-name="cipInsideDeliveryBlock">













<span class="a-declarative" data-action="dpContextualIngressPt" data-dpContextualIngressPt="{}">
<a class="a-link-normal" href="#">
<div class="a-row a-spacing-small">
<div class="a-column a-span12 a-text-left">
<div id="contextualIngressPt">
<div id="contextualIngressPtPin"></div>
<span id="contextualIngressPtLabel" class="cip-a-size-small">
<div id="contextualIngressPtLabel_deliveryShortLine">Select delivery location</div>
</span>
</div>
</div>
</div>
</a>
</span>
























</div>



























</div>
























<div id="deliveryPromiseInsideBuyBox_feature_div" class="celwidget" data-feature-name="deliveryPromiseInsideBuyBox">

































<div class="a-section a-spacing-none a-text-left">



































<div id="fast-track" class="a-section a-spacing-none">


<input type="hidden" id="ftSelectAsin" value="B0000028RR"/>


<input type="hidden" id="ftSelectMerchant" value="A3C9TTIOE1L9MO"/>









<div id="fast-track-message" class="a-section a-spacing-base">



<div class="a-section a-spacing-none">










</div>







<script type="text/javascript">
function fastTrackCountDown(secondsLeft, messageSectionId) {
var sectionId = messageSectionId;
var FT_showAndInCountdown = true;
var FT_DayString = "day";
var FT_DaysString = "";
var FT_HourString = "hour";
var FT_HoursString = "hours";
var FT_MinuteString = "minute";
var FT_MinutesString = "minutes";
var FT_AndString = "and";
var FT_startedWithHour = new Date().getHours();
var FT_givenSeconds, FT_actualSeconds;
var timerId;
function getElementsByClassNameCustom(className) {
var selectedElements = [];
if (document.querySelectorAll) {
var sectionIdElements = document.querySelectorAll("#" + sectionId);
for (index = 0; index < sectionIdElements.length; ++index) {
var elements = sectionIdElements[index].querySelectorAll("." + className);
for(var i = 0; elements && i < elements.length; i++) {
selectedElements.push(elements[i]);
}
}
}
return selectedElements;
}
var FT_CurrentDisplayMin;
var clientServerTimeDrift;
var firstTimeUpdate = true;
var countdownElements = getElementsByClassNameCustom("ftCountdownClass");
if (countdownElements.length < 1 && document.getElementById(sectionId) && document.getElementById("ftCountdown")) {
countdownElements.push(document.getElementById("ftCountdown"));
}
function getTimeRemainingString( days, hours, minutes )
{
hours = (days * 24) + hours;
var hourString   =  ( hours == 1 ? FT_HourString : FT_HoursString );
var minuteString =  ( minutes  == 1 ? FT_MinuteString : FT_MinutesString );
if (hours == 0) {
return minutes + " " + minuteString;
}
if (minutes == 0) {
return hours + " " + hourString;
}
if (FT_showAndInCountdown) {
return hours + " " + hourString + " " + FT_AndString + " " + minutes + " " + minuteString;
} else {
return hours + " " + hourString + " " + minutes + " " + minuteString;
}
}
function hideAllFastTrackComponents() {
if (document.querySelectorAll) {
var fastTrackComponents = document.querySelectorAll("#fast-track");
var index;
var shouldHideSections = false;
if (fastTrackComponents) {
for (index = 0; index < fastTrackComponents.length; ++index) {
if (fastTrackComponents[index].querySelector("#" + sectionId)) {
fastTrackComponents[index].style.display = "none";
} else {
shouldHideSections = true;
}
}
if (shouldHideSections) {
var sectionComponents = document.querySelectorAll("#" + sectionId);
if (sectionComponents) {
for (index = 0; index < sectionComponents.length; ++index) {
sectionComponents[index].style.display = "none";
}
}
}
}
}
}
function FT_displayCountdown(forceUpdate)
{
var FT_remainSeconds = FT_givenSeconds - FT_actualSeconds;
//for components having outer div "fast-track" hide that component else hide the message sectionId.
if (FT_remainSeconds < 1) {
hideAllFastTrackComponents();
}
var FT_secondsPerDay = 24 * 60 * 60;
var FT_daysLong = FT_remainSeconds / FT_secondsPerDay;
var FT_days = Math.floor(FT_daysLong);
var FT_hoursLong = (FT_daysLong - FT_days) * 24;
var FT_hours = Math.floor(FT_hoursLong);
var FT_minsLong = (FT_hoursLong - FT_hours) * 60;
var FT_mins = Math.floor(FT_minsLong);
var FT_secsLong = (FT_minsLong - FT_mins) * 60;
var FT_secs = Math.floor(FT_secsLong);
timerId = setTimeout(FT_getTime, 1000);
var ftCountdown = getTimeRemainingString( FT_days, FT_hours, FT_mins );
if (countdownElements.length) {
if (FT_CurrentDisplayMin != FT_mins || forceUpdate || firstTimeUpdate) {
var i = 0, countdownElement;
while (countdownElement = countdownElements[i++]) {
countdownElement.innerHTML = ftCountdown;
}
FT_CurrentDisplayMin = FT_mins;
firstTimeUpdate = false;
}
}
}
function FT_getCountdown(secondsLeft)
{
var FT_currentTime = new Date();
var FT_currentHours = FT_currentTime.getHours();
var FT_currentMins = FT_currentTime.getMinutes();
var FT_currentSecs = FT_currentTime.getSeconds();
FT_givenSeconds = FT_currentHours * 3600 + FT_currentMins * 60 + FT_currentSecs;
FT_givenSeconds += secondsLeft;
FT_getTime();
}
function FT_getTime()
{
var FT_newCurrentTime = new Date();
var FT_actualHours = FT_newCurrentTime.getHours();
if (FT_startedWithHour > FT_actualHours) {
FT_actualHours += 24;
}
var FT_actualMins = FT_newCurrentTime.getMinutes();
var FT_actualSecs = FT_newCurrentTime.getSeconds();
FT_actualSeconds = FT_actualHours * 3600 + FT_actualMins * 60 + FT_actualSecs;
FT_displayCountdown();
}
FT_getCountdown(secondsLeft);
return {
stopTimer : function() {
clearTimeout(timerId);
}
};
}
</script>

<script type="text/javascript">
P.when("A", "jQuery").execute(function(A, $) {
var pageState = A.state('ftPageState');
if (typeof pageState === 'undefined') {
pageState = {};
}

if(0 > 0)  {
if (pageState["upsell-message"]) {
pageState["upsell-message"].stopTimer();
}
pageState["upsell-message"] = new fastTrackCountDown(0,"upsell-message");
}
if(0 > 0) {
if (pageState["amazon-day-message"]) {
pageState["amazon-day-message"].stopTimer();
}
pageState["amazon-day-message"] = new fastTrackCountDown(0,"amazon-day-message");
}
A.state('ftPageState', pageState);
});
</script>

</div>















</div>



</div>



























</div>
























<div id="promiseBasedBadgeInsideBuyBox_feature_div" class="celwidget" data-feature-name="promiseBasedBadgeInsideBuyBox">

































<div class="a-section a-spacing-none a-text-left">








































































</div>



























</div>
























<div id="addOnMessage_feature_div" class="celwidget" data-feature-name="addOnMessage">



































</div>
























<div id="availabilityInsideBuyBox_feature_div" class="celwidget" data-feature-name="availabilityInsideBuyBox">































<div class="a-section a-spacing-none">



































<div id="availability" class="a-section a-spacing-base">


<span class="a-size-medium a-color-state">


Usually ships within 6 to 10 days.


</span>








</div>





<div class="a-section a-spacing-none">

</div>














<div class="a-section a-spacing-mini">



</div>



</div>
























</div>
























<div id="alternativeProductMessage_feature_div" class="celwidget" data-feature-name="alternativeProductMessage">




































</div>
























<div id="globalStoreBadgePopoverInsideBuybox_feature_div" class="celwidget" data-feature-name="globalStoreBadgePopoverInsideBuybox">




















































</div>
























<div id="quantityRelocate_feature_div" class="celwidget" data-feature-name="quantityRelocate">













































</div>
























<div id="quantityAwarePriceRelocate_feature_div" class="celwidget" data-feature-name="quantityAwarePriceRelocate">








































</div>
























<div id="soldByThirdPartyRelocate_feature_div" class="celwidget" data-feature-name="soldByThirdPartyRelocate">





































































































</div>
























<div id="addToCart_feature_div" class="celwidget" data-feature-name="addToCart">























































<div class="a-button-stack">



<span class="a-declarative" data-action="dp-pre-atc-declarative" data-dp-pre-atc-declarative="{}" id="atc-declarative">
<span id="submit.add-to-cart" class="a-button a-spacing-small a-button-primary a-button-icon"><span class="a-button-inner"><i class="a-icon a-icon-cart"></i><input id="add-to-cart-button" name="submit.add-to-cart" title="Add to Shopping Cart" data-hover="Select &lt;b&gt;__dims__&lt;/b&gt; from the left&lt;br&gt; to add to Shopping Cart" class="a-button-input" type="submit" value="Add to Cart" aria-labelledby="submit.add-to-cart-announce"/><span id="submit.add-to-cart-announce" class="a-button-text" aria-hidden="true">Add to Cart</span></span></span>
</span>

</div>













<div class="dp-cif aok-hidden" data-feature-details='{"name":"atc","isInteractive":false}'></div>
<script type="text/javascript">(function(f) {var _np=(window.P._namespace("DetailPageBuyBoxTemplate"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.now().execute('dp-mark-atc',function(){
if (typeof window.markFeatureRender === 'function') {
window.markFeatureRender('atc',{isInteractive:false});
}
});
}));</script>



























</div>
























<div id="buyNow_feature_div" class="celwidget" data-feature-name="buyNow">































<div class="a-button-stack">

<div id="buyNow" class="a-section a-spacing-base">












<div id="turboState" class="a-section a-spacing-none a-padding-none">
<script type="a-state" data-a-state="{&quot;key&quot;:&quot;turbo-checkout-page-state&quot;}">{"turboWeblab":"RCX_CHECKOUT_TURBO_DESKTOP_NONPRIME_87784","strings":{"TURBO_CHECKOUT_HEADER":"Buy now: Rage Against The Machine","TURBO_LOADING_TEXT":"Loading your order summary"},"inputs":{"a":"B0000028RR","quantity":"1","oid":"","addressId":""},"configurations":{"isSignInEnabled":true,"initiateSelector":"#buy-now-button","prefetchEnabled":true},"buttonID":"buy-now","eligibility":{"isEligible":false},"turboWeblabTreatment":"T2","timeout":"5000"}</script>
</div>

<script type="text/javascript">(function(f) {var _np=(window.P._namespace("TurboClientDetailPage"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.when('cf').execute(function executeTurboAssetsLoadTriggerEvent() {
P.now('turbo-checkout-assets-load-trigger').execute(function(assetsLoadTrigger) {
if (assetsLoadTrigger) {
logTurboCounter("AssetTriggerDedupe");
return;
}
try {
P.declare('turbo-checkout-assets-load-trigger', true);
logTurboCounter('AssetTrigger');
} catch (e) {
logTurboCounter('AssetTriggerException');
}
});
function logTurboCounter(name) {
var counter = 'turboCheckout' + name;
if (window.ue && window.ue.count) {
window.ue.count(counter, 1);
}
}
});
}));</script>



<span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;name&quot;:&quot;turbo&quot;}" id="turbo-checkout-modal"></span>











<span id="submit.buy-now" class="a-button a-button-oneclick a-button-icon onml-buy-now-button"><span class="a-button-inner"><i class="a-icon a-icon-buynow"></i><input id="buy-now-button" name="submit.buy-now" data-hover="__dims__" class="a-button-input" type="submit" aria-labelledby="submit.buy-now-announce"/><span id="submit.buy-now-announce" class="a-button-text" aria-hidden="true">
Buy Now
</span></span></span>
</div>
</div>






























</div>
























<div id="secureTransaction_feature_div" class="celwidget" data-feature-name="secureTransaction">





















<div class="a-section a-spacing-small a-text-left celwidget">
<span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;name&quot;:&quot;secureTransactionsPopover&quot;,&quot;activate&quot;:&quot;onclick&quot;,&quot;position&quot;:&quot;triggerBottom&quot;}">
<a class="a-link-normal a-text-normal" href="#">

<span class="aok-align-center" id="secureTransactionIconWrapper">


<img alt="" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/checkout/truespc/secured-ssl._CB485936932_.png" height="15px"/>
</span>
<span class="a-letter-space"></span>
<span>Secure transaction</span>
</a>
</span>
</div>
<div class="a-popover-preload" id="a-popover-secureTransactionsPopover">
<div cel_widget_id="secureTransaction-celwidget-popover-inner" class="celwidget">
<div class="a-section a-padding-base">

<div class="a-row a-spacing-base">
<span class="a-text-bold">Your transaction is secure</span>
</div>
<div class="a-row a-spacing-micro">
<span>We work hard to protect your security and privacy. Our payment security system encrypts your information during transmission. We don’t share your credit card details with third-party sellers, and we don’t sell your information to others.</span>

<a class="a-link-normal a-nowrap" target="_blank" rel="noopener" href="/gp/help/customer/display.html?nodeId=201909010&amp;ref_=buybox-secureTransaction-learnMore-web">Learn more</a>

</div>
</div>
</div>
</div>

























</div>
























<div id="shipsFromSoldByInsideBuyBox_feature_div" class="celwidget" data-feature-name="shipsFromSoldByInsideBuyBox">































<div class="a-section a-spacing-none">


























<div id="merchant-info" class="a-section a-spacing-base">












Ships from United States and sold by <a href='/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&amp;seller=A3C9TTIOE1L9MO' id='sellerProfileTriggerId'>Ergodebooks Ships from USA</a>.








<span class="">
</span>











</div>




</div>
























</div>
























<div id="originalPackagingMessageInsideBuyBox_feature_div" class="celwidget" data-feature-name="originalPackagingMessageInsideBuyBox">






































</div>
























<div id="tradeInInstantSavings_feature_div" class="celwidget" data-feature-name="tradeInInstantSavings">




































</div>
























<div id="quantityLayoutHigh_feature_div" class="celwidget" data-feature-name="quantityLayoutHigh">





































</div>
























<div id="bbop_feature_div" class="celwidget" data-feature-name="bbop">









































</div>
























<div id="voltageCompliance_feature_div" class="celwidget" data-feature-name="voltageCompliance">





































</div>
























<div id="businessPricing_feature_div" class="celwidget" data-feature-name="businessPricing">



































</div>
























<div id="soldByThirdParty_feature_div" class="celwidget" data-feature-name="soldByThirdParty">












































</div>
























<div id="scheduledDelivery_feature_div" class="celwidget" data-feature-name="scheduledDelivery">



































</div>
























<div id="bbg_feature_div" class="celwidget" data-feature-name="bbg">





































</div>
























<div id="mbb_feature_div" class="celwidget" data-feature-name="mbb">



































</div>
























<div id="desktop_productInsurance_feature_div" class="celwidget" data-feature-name="desktop_productInsurance">




































</div>
























<div id="quantityLayoutLow_feature_div" class="celwidget" data-feature-name="quantityLayoutLow">





































</div>
























<div id="simpleBundleV2_feature_div" class="celwidget" data-feature-name="simpleBundleV2">






































</div>
























<div id="asg_feature_div" class="celwidget" data-feature-name="asg">














































</div>
























<div id="quantityAwarePrice_feature_div" class="celwidget" data-feature-name="quantityAwarePrice">




































</div>
























<div id="addToCart_feature_div" class="celwidget" data-feature-name="addToCart">





































</div>
























<div id="preAddToCartFramework_feature_div" class="celwidget" data-feature-name="preAddToCartFramework">













<script type="a-state" data-a-state="{&quot;key&quot;:&quot;dp-pre-atc-hero&quot;}">{"heroName":""}</script>
<script type="a-state" data-a-state="{&quot;key&quot;:&quot;dp-pre-atc-hero-candidates&quot;}">["addServices"]</script>
























</div>
























<div id="buyNow_feature_div" class="celwidget" data-feature-name="buyNow">





































</div>
























<div id="secureTransaction_feature_div" class="celwidget" data-feature-name="secureTransaction">




































</div>
























<div id="oneClick_feature_div" class="celwidget" data-feature-name="oneClick">





































</div>
























<div id="detailPageGifting_feature_div" class="celwidget" data-feature-name="detailPageGifting">




































</div>
























<div id="makoPreRegistration" class="celwidget" data-feature-name="makoPreRegistration">



























</div>
























<div id="accessoryUpsellAmabot_feature_div" class="celwidget" data-feature-name="accessoryUpsellAmabot">


































</div>
























<div id="accessoryUpsellBtf_feature_div" class="celwidget" data-feature-name="accessoryUpsellBtf">

























 






























</div>
























<div id="unifiedLocation_feature_div" class="celwidget" data-feature-name="unifiedLocation">



































</div>










</div>

        
    




















</div>





    </form>
 </div>

</div>
</div></div>












































<div id="usedAccordionRow" data-buying-option-index="1" class="a-box celwidget" data-a-accordion-row-name="usedAccordionRow"><div class="a-box-inner a-accordion-row-container">
<div class="a-accordion-row-a11y" role="radio" aria-checked="false" aria-expanded="false"><a data-action="a-accordion" class="a-accordion-row a-declarative accordion-header" href="#" aria-label=""><i class="a-icon a-accordion-radio a-icon-radio-inactive"></i><h5>






























































    
    
        
    



    
    
        
    
    





<div class="a-row">
   
        <div class="a-column a-span12">
        <span class="a-text-bold">Save with Used - Very Good</span>
        </div>
   
   
        
              <div class="a-column a-span12 a-text-left">
              <span id="gsbbUsedPrice" class="a-size-base a-color-secondary header-price a-text-normal">$3.21</span>
              </div>
        
        
        
   

    
    

    
    



























<div id="abbreviate_shipping_accordion_head" class="a-column a-span12 a-text-left show-on-unselected">
<div class="a-row a-color-secondary">



</div>
</div>


<div id="mfn_shipping_accordion_head" class="a-column a-span12 a-text-left show-on-unselected">
<div class="a-row a-color-secondary">























</div>
</div>









<div id="abbreviate_fasttrack_accordion_head" class="a-column a-span12 a-text-left show-on-unselected">
<div class="a-row a-color-secondary">


<div id="fast-track" class="a-section a-spacing-none">


<input type="hidden" id="ftSelectAsin" value="B0000028RR"/>


<input type="hidden" id="ftSelectMerchant" value="A35KCY9V16L0JS"/>







<div id="fast-track-message-abbreviate" class="a-section a-spacing-none">
<div class="a-section a-spacing-none">


    
    $3.99
 delivery: <b>


June 14 - 22

</b>








</div>
</div>







</div>
</div>
</div>



    







<div id="sfsb_accordion_head" class="a-section show-on-unselected sfsb-header-text">
<div class="a-row">
<div class="a-column a-span12 a-text-left truncate">
<span class="a-size-small">
Ships from:
</span>
<span class="a-size-small">
Goodwill Store 2024
</span>
</div>
</div>
<div class="a-row">
<div class="a-column a-span12 a-text-left truncate">
<span class="a-size-small">
Sold by:
</span>
<span class="a-size-small">
Goodwill Store 2024
</span>
</div>
</div>
</div>

</div>








</h5></a></div>
<div class="a-accordion-inner accordion-row-content">
















  
      
      
      
          
      
  


 <div class="a-section">

    

     <form method="post" id="addToCart" action="/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance" class="a-content">
              <input type='hidden' name='CSRF' value='g23AVDCwHo1VyRYMPo1O0gNzdlaVAYeJgOEY0/VyzvGaAAAADAAAAABguq2AcmF3AAAAABVX8CwXqz4nuL9RKX///w==' />
              <input type="hidden" id="offerListingID" name="offerListingID" value="Pi7oQOkKPzttZ9Cdwn0236TCyLgNWQ5AoLUqGUsUlKobIf15tSEXOHAAqvoJnrxXwvtdACVeVkZFeY1HuQYZdYEf1%2BlIMVAt%2F3jUgIF7M60WhsLhqYrhzIO9nOgbEtkoGlzXOxu6CwYqhmVzSWwVb2NA9y9ocCiVOI6c7gTcPojkQKNpB6nGLycqs3m5TDhH">
              <input type="hidden" id="session-id" name="session-id" value="138-4669640-7712440">
              <input type="hidden" id="ASIN" name="ASIN" value="B0000028RR">
              <input type="hidden" id="isMerchantExclusive" name="isMerchantExclusive" value="0">
              <input type="hidden" id="merchantID" name="merchantID" value="A35KCY9V16L0JS">
              <input type="hidden" id="isAddon" name="isAddon" value="0">
              <input type="hidden" id="nodeID" name="nodeID" value="">
              <input type="hidden" id="sellingCustomerID" name="sellingCustomerID" value="">
              <input type="hidden" id="qid" name="qid" value="">
              <input type="hidden" id="sr" name="sr" value="">
              <input type="hidden" id="storeID" name="storeID" value="">
              <input type="hidden" id="tagActionCode" name="tagActionCode" value="">
              <input type="hidden" id="viewID" name="viewID" value="glance">
              <input type="hidden" id="rebateId" name="rebateId" value="">
              <input type="hidden" id="ctaDeviceType" name="ctaDeviceType" value="desktop">
              <input type="hidden" id="ctaPageType" name="ctaPageType" value="detail">
              <input type="hidden" id="usePrimeHandler" name="usePrimeHandler" value="0">
         
             

             
             

              



    
            
                
                




            

            
            

            
            

            
            <input type="hidden" id="rsid" name="rsid" value="138-4669640-7712440">
            <input type="hidden" id="sourceCustomerOrgListID" name="sourceCustomerOrgListID" value="">
            <input type="hidden" id="sourceCustomerOrgListItemID" name="sourceCustomerOrgListItemID" value="">
            <input type="hidden" name="wlPopCommand" value="">
            
            

     

<input type="hidden" id="usedMerchantID" name="usedMerchantID" value="A35KCY9V16L0JS"/>
<input type="hidden" id="usedOfferListingID" name="usedOfferListingID" value="Pi7oQOkKPzttZ9Cdwn0236TCyLgNWQ5AoLUqGUsUlKobIf15tSEXOHAAqvoJnrxXwvtdACVeVkZFeY1HuQYZdYEf1%2BlIMVAt%2F3jUgIF7M60WhsLhqYrhzIO9nOgbEtkoGlzXOxu6CwYqhmVzSWwVb2NA9y9ocCiVOI6c7gTcPojkQKNpB6nGLycqs3m5TDhH"/>
<input type="hidden" id="usedSellingCustomerID" name="usedSellingCustomerID" value=""/>















<div id="usedBuyBoxConditionNote_feature_div" class="celwidget" data-feature-name="usedBuyBoxConditionNote">


















<div class="a-row a-spacing-base a-size-base">
<div aria-live="polite" data-a-expander-name="ubb_expander" data-a-expander-collapsed-height="55" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:55px">
<div aria-expanded="false" class="a-expander-content a-expander-partial-collapse-content">
<span>Very Good Condition, Fast Shipping,Hassle-free return policy, means your satisfaction is guaranteed!</span>
</div>
<div class="a-expander-header a-expander-partial-collapse-header"><a href="javascript:void(0)" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;See more&quot;, &quot;collapse_prompt&quot;:&quot;See less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">See more</span></a></div>
</div>
</div>
























</div>



















<div id="shippingMessage_feature_div" class="celwidget" data-feature-name="shippingMessage">


















<div class="a-section">
<div class="a-row">
<div class="a-column a-span12 a-text-left a-spacing-top-micro">


































<span id="price-shipping-message" class="a-size-base a-color-base"></span>





</div>
</div>
</div>


























</div>



















<div id="usedDeliveryBlockContainer" class="celwidget" data-feature-name="usedDeliveryBlockContainer">










































<div id="deliveryBlock_feature_div" data-feature-name="deliveryBlock" data-template-name="deliveryBlock" class="a-section a-spacing-none celwidget">











<div id="deliveryBlockMessage" class="a-section">

<div id="mir-layout-DELIVERY_BLOCK"><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE">$3.99 delivery: <b> June 14 - 22 </b>
</div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-UPSELL"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-EXTENDED_DELIVERY_PROMISE_MESSAGE"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-HOLIDAY_DELIVERY_MESSAGE"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-SUPPLEMENTAL_DELIVERY_MESSAGE"></div><div class="a-spacing-base" id="mir-layout-DELIVERY_BLOCK-slot-CORE_FREE_SHIPPING_SUPPLEMENTARY_MESSAGE"></div></div>
</div>




<input type="hidden" id="deliveryBlockSelectAsin" value="B0000028RR"/>


<input type="hidden" id="deliveryBlockSelectMerchant" value="A35KCY9V16L0JS"/>

<script type="text/javascript">
P.when("A", "jQuery").execute(function(A, $) {
$("#selectQuantity [name='quantity'], #mobileQuantityDropDown").live("change", function (event) {
if (event.updateDeliveryBlockOnQuantityChange) {
return;
}
event.updateDeliveryBlockOnQuantityChange = 1;
// "#buybox" is included in this list because if there is no accordion row, then it is a single-offer layout
var accordionRow = $(this).closest('[id$="AccordionRow"], #buybox');
var quantity = $(this).val();
var asin = accordionRow.find("#deliveryBlockSelectAsin").val();
var merchantId = accordionRow.find("#deliveryBlockSelectMerchant").val();
if (!asin || !merchantId) {
return;
}
var params = [];
params.push("asin=" + asin);
params.push("quantity=" + quantity);
params.push("merchantId=" + merchantId);
$.ajax({
type: "POST",
url: "/gp/product/features/dp-fast-track/udp-ajax-handler/get-quantity-update-message.html?ie=UTF8",
contentType: 'application/x-www-form-urlencoded;charset=utf-8',
data: params.join('&'),
accordionRow: accordionRow,
dataType: "html",
success: function(objResponse) {
if (objResponse != null && objResponse != "") {
accordionRow.find("#deliveryBlockMessage").replaceWith(objResponse);
}
}
});
return;
});
});
</script>
























</div>









































<div id="cipInsideDeliveryBlock_feature_div" data-feature-name="cipInsideDeliveryBlock" data-template-name="cipInsideDeliveryBlock" class="a-section a-spacing-none celwidget">










<span class="a-declarative" data-action="dpContextualIngressPt" data-dpContextualIngressPt="{}">
<a class="a-link-normal" href="#">
<div class="a-row a-spacing-small">
<div class="a-column a-span12 a-text-left">
<div id="contextualIngressPt">
<div id="contextualIngressPtPin"></div>
<span id="contextualIngressPtLabel" class="cip-a-size-small">
<div id="contextualIngressPtLabel_deliveryShortLine">Select delivery location</div>
</span>
</div>
</div>
</div>
</a>
</span>























</div>































</div>



















<div id="dynamicDeliveryMessage_feature_div" class="celwidget" data-feature-name="dynamicDeliveryMessage">






















































</div>



















<div id="dpFastTrack_feature_div" class="celwidget" data-feature-name="dpFastTrack">

































<div class="a-section a-spacing-none a-text-left">



































<div id="fast-track" class="a-section a-spacing-none">


<input type="hidden" id="ftSelectAsin" value="B0000028RR"/>


<input type="hidden" id="ftSelectMerchant" value="A35KCY9V16L0JS"/>









<div id="fast-track-message" class="a-section a-spacing-base">



<div class="a-section a-spacing-none">










</div>







<script type="text/javascript">
function fastTrackCountDown(secondsLeft, messageSectionId) {
var sectionId = messageSectionId;
var FT_showAndInCountdown = true;
var FT_DayString = "day";
var FT_DaysString = "";
var FT_HourString = "hour";
var FT_HoursString = "hours";
var FT_MinuteString = "minute";
var FT_MinutesString = "minutes";
var FT_AndString = "and";
var FT_startedWithHour = new Date().getHours();
var FT_givenSeconds, FT_actualSeconds;
var timerId;
function getElementsByClassNameCustom(className) {
var selectedElements = [];
if (document.querySelectorAll) {
var sectionIdElements = document.querySelectorAll("#" + sectionId);
for (index = 0; index < sectionIdElements.length; ++index) {
var elements = sectionIdElements[index].querySelectorAll("." + className);
for(var i = 0; elements && i < elements.length; i++) {
selectedElements.push(elements[i]);
}
}
}
return selectedElements;
}
var FT_CurrentDisplayMin;
var clientServerTimeDrift;
var firstTimeUpdate = true;
var countdownElements = getElementsByClassNameCustom("ftCountdownClass");
if (countdownElements.length < 1 && document.getElementById(sectionId) && document.getElementById("ftCountdown")) {
countdownElements.push(document.getElementById("ftCountdown"));
}
function getTimeRemainingString( days, hours, minutes )
{
hours = (days * 24) + hours;
var hourString   =  ( hours == 1 ? FT_HourString : FT_HoursString );
var minuteString =  ( minutes  == 1 ? FT_MinuteString : FT_MinutesString );
if (hours == 0) {
return minutes + " " + minuteString;
}
if (minutes == 0) {
return hours + " " + hourString;
}
if (FT_showAndInCountdown) {
return hours + " " + hourString + " " + FT_AndString + " " + minutes + " " + minuteString;
} else {
return hours + " " + hourString + " " + minutes + " " + minuteString;
}
}
function hideAllFastTrackComponents() {
if (document.querySelectorAll) {
var fastTrackComponents = document.querySelectorAll("#fast-track");
var index;
var shouldHideSections = false;
if (fastTrackComponents) {
for (index = 0; index < fastTrackComponents.length; ++index) {
if (fastTrackComponents[index].querySelector("#" + sectionId)) {
fastTrackComponents[index].style.display = "none";
} else {
shouldHideSections = true;
}
}
if (shouldHideSections) {
var sectionComponents = document.querySelectorAll("#" + sectionId);
if (sectionComponents) {
for (index = 0; index < sectionComponents.length; ++index) {
sectionComponents[index].style.display = "none";
}
}
}
}
}
}
function FT_displayCountdown(forceUpdate)
{
var FT_remainSeconds = FT_givenSeconds - FT_actualSeconds;
//for components having outer div "fast-track" hide that component else hide the message sectionId.
if (FT_remainSeconds < 1) {
hideAllFastTrackComponents();
}
var FT_secondsPerDay = 24 * 60 * 60;
var FT_daysLong = FT_remainSeconds / FT_secondsPerDay;
var FT_days = Math.floor(FT_daysLong);
var FT_hoursLong = (FT_daysLong - FT_days) * 24;
var FT_hours = Math.floor(FT_hoursLong);
var FT_minsLong = (FT_hoursLong - FT_hours) * 60;
var FT_mins = Math.floor(FT_minsLong);
var FT_secsLong = (FT_minsLong - FT_mins) * 60;
var FT_secs = Math.floor(FT_secsLong);
timerId = setTimeout(FT_getTime, 1000);
var ftCountdown = getTimeRemainingString( FT_days, FT_hours, FT_mins );
if (countdownElements.length) {
if (FT_CurrentDisplayMin != FT_mins || forceUpdate || firstTimeUpdate) {
var i = 0, countdownElement;
while (countdownElement = countdownElements[i++]) {
countdownElement.innerHTML = ftCountdown;
}
FT_CurrentDisplayMin = FT_mins;
firstTimeUpdate = false;
}
}
}
function FT_getCountdown(secondsLeft)
{
var FT_currentTime = new Date();
var FT_currentHours = FT_currentTime.getHours();
var FT_currentMins = FT_currentTime.getMinutes();
var FT_currentSecs = FT_currentTime.getSeconds();
FT_givenSeconds = FT_currentHours * 3600 + FT_currentMins * 60 + FT_currentSecs;
FT_givenSeconds += secondsLeft;
FT_getTime();
}
function FT_getTime()
{
var FT_newCurrentTime = new Date();
var FT_actualHours = FT_newCurrentTime.getHours();
if (FT_startedWithHour > FT_actualHours) {
FT_actualHours += 24;
}
var FT_actualMins = FT_newCurrentTime.getMinutes();
var FT_actualSecs = FT_newCurrentTime.getSeconds();
FT_actualSeconds = FT_actualHours * 3600 + FT_actualMins * 60 + FT_actualSecs;
FT_displayCountdown();
}
FT_getCountdown(secondsLeft);
return {
stopTimer : function() {
clearTimeout(timerId);
}
};
}
</script>

<script type="text/javascript">
P.when("A", "jQuery").execute(function(A, $) {
var pageState = A.state('ftPageState');
if (typeof pageState === 'undefined') {
pageState = {};
}

if(0 > 0)  {
if (pageState["upsell-message"]) {
pageState["upsell-message"].stopTimer();
}
pageState["upsell-message"] = new fastTrackCountDown(0,"upsell-message");
}
if(0 > 0) {
if (pageState["amazon-day-message"]) {
pageState["amazon-day-message"].stopTimer();
}
pageState["amazon-day-message"] = new fastTrackCountDown(0,"amazon-day-message");
}
A.state('ftPageState', pageState);
});
</script>

</div>















</div>



</div>



























</div>



















<div id="glowContextualIngressPt_feature_div" class="celwidget" data-feature-name="glowContextualIngressPt">




































</div>



















<div id="availability_feature_div" class="celwidget" data-feature-name="availability">































<div class="a-section a-spacing-none">



































<div id="availability" class="a-section a-spacing-base">


<span class="a-size-medium a-color-success">

Only 1 left in stock.



</span>








</div>





<div class="a-section a-spacing-none">

</div>














<div class="a-section a-spacing-mini">



</div>



</div>
























</div>



















<div id="addToCart_feature_div" class="celwidget" data-feature-name="addToCart">





















































<div class="a-button-stack">



<span class="a-declarative" data-action="dp-pre-atc-declarative" data-dp-pre-atc-declarative="{}" id="atc-declarative">
<span id="submit.add-to-cart-ubb" class="a-button a-spacing-small a-button-primary a-button-icon"><span class="a-button-inner"><i class="a-icon a-icon-cart"></i><input id="add-to-cart-button-ubb" name="submit.add-to-cart-ubb" title="Add to Shopping Cart" data-hover="Select &lt;b&gt;__dims__&lt;/b&gt; from the left&lt;br&gt; to add to Shopping Cart" class="a-button-input" type="submit" value="Add to Cart" aria-labelledby="submit.add-to-cart-ubb-announce"/><span id="submit.add-to-cart-ubb-announce" class="a-button-text" aria-hidden="true">Add to Cart</span></span></span>
</span>

</div>





































</div>



















<div id="shipsFromSoldBy_feature_div" class="celwidget" data-feature-name="shipsFromSoldBy">































<div class="a-section a-spacing-none">


























<div id="merchant-info" class="a-section a-spacing-base">












Ships from Canada and sold by <a href='/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&amp;seller=A35KCY9V16L0JS' id='sellerProfileTriggerId'>Goodwill Store 2024</a>.








<span class="">
</span>











</div>




</div>
























</div>







    </form>
 </div>






</div>
</div></div>




















































<!-- unavailableNewRow.jsp is mostly same as "features/buybox/accordion/DesktopRow" template.
Created new file because we need to add additional accordion in case only rental offer is present, more info - https://sim.amazon.com/issues/DPOffersDev-3760
Any change in DesktopRow.jsp should be made to this file as well. -->















































</div>



        
    



















</div>






</div>





<div id="digitalDashHighProminenceAccordion_feature_div" data-feature-name="digitalDashHighProminenceAccordion" data-template-name="digitalDashHighProminenceAccordion" class="a-section a-spacing-none">













<div id="digitalDashHighProminenceAccordion_feature_div" class="celwidget" data-feature-name="digitalDashHighProminenceAccordion">





































</div>






</div>





<div id="marsAccessoryUpsell_feature_div" data-feature-name="marsAccessoryUpsell" data-template-name="marsAccessoryUpsell" class="a-section a-spacing-none">













<div id="marsAccessoryUpsell_feature_div" class="celwidget" data-feature-name="marsAccessoryUpsell">


































</div>






</div>





<div id="accessoryUpsellAccordion_feature_div" data-feature-name="accessoryUpsellAccordion" data-template-name="accessoryUpsellAccordion" class="a-section a-spacing-none">













<div id="accessoryUpsellAccordion_feature_div" class="celwidget" data-feature-name="accessoryUpsellAccordion">

























 






























</div>






</div>





<div id="accessoryUpsellAmabotAccordion_feature_div" data-feature-name="accessoryUpsellAmabotAccordion" data-template-name="accessoryUpsellAmabotAccordion" class="a-section a-spacing-none">













<div id="accessoryUpsellAmabotAccordion_feature_div" class="celwidget" data-feature-name="accessoryUpsellAmabotAccordion">


































</div>






</div>





<div id="addToWishlistAccordion_feature_div" data-feature-name="addToWishlistAccordion" data-template-name="addToWishlistAccordion" class="a-section a-spacing-none">













<div id="addToWishlistAccordion_feature_div" class="celwidget" data-feature-name="addToWishlistAccordion">

























  
      
      
      
          
      
  


 <div class="a-section">

    

     <form method="post" id="addToCart" action="/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance" class="a-content">
              <input type='hidden' name='CSRF' value='g23AVDCwHo1VyRYMPo1O0gNzdlaVAYeJgOEY0/VyzvGaAAAADAAAAABguq2AcmF3AAAAABVX8CwXqz4nuL9RKX///w==' />
              <input type="hidden" id="offerListingID" name="offerListingID" value="UNpOMQajhZ4LWcHndMWq3Wt2GAQfpb6sUJyFi55CX7O3SpXld0LRmVxdWHnJdreSFAgR7h9l4ahD0siajR3ODM0BfTqOGgSFsINUUnJbG5dGa2z4%2Bjur6zE%2FAAe%2BDfL0QF%2BUKexz2eEmQNDI7S2aH5VObYOjovmzUklZGxhzfD6oyXyuRKooZHok2VY1z%2BCU">
              <input type="hidden" id="session-id" name="session-id" value="138-4669640-7712440">
              <input type="hidden" id="ASIN" name="ASIN" value="B0000028RR">
              <input type="hidden" id="isMerchantExclusive" name="isMerchantExclusive" value="0">
              <input type="hidden" id="merchantID" name="merchantID" value="A3C9TTIOE1L9MO">
              <input type="hidden" id="isAddon" name="isAddon" value="0">
              <input type="hidden" id="nodeID" name="nodeID" value="">
              <input type="hidden" id="sellingCustomerID" name="sellingCustomerID" value="">
              <input type="hidden" id="qid" name="qid" value="">
              <input type="hidden" id="sr" name="sr" value="">
              <input type="hidden" id="storeID" name="storeID" value="">
              <input type="hidden" id="tagActionCode" name="tagActionCode" value="">
              <input type="hidden" id="viewID" name="viewID" value="glance">
              <input type="hidden" id="rebateId" name="rebateId" value="">
              <input type="hidden" id="ctaDeviceType" name="ctaDeviceType" value="desktop">
              <input type="hidden" id="ctaPageType" name="ctaPageType" value="detail">
              <input type="hidden" id="usePrimeHandler" name="usePrimeHandler" value="0">
         
             

             
             

              



    
            
                
                




            

            
            

            
            

            
            <input type="hidden" id="rsid" name="rsid" value="138-4669640-7712440">
            <input type="hidden" id="sourceCustomerOrgListID" name="sourceCustomerOrgListID" value="">
            <input type="hidden" id="sourceCustomerOrgListItemID" name="sourceCustomerOrgListItemID" value="">
            <input type="hidden" name="wlPopCommand" value="">
            
            

     
































<hr aria-hidden="true" class="a-spacing-base a-divider-normal"/>








<div id="wishlistButtonStack" class="a-button-stack">












<div id="add-to-wishlist-button-group" data-hover="&lt;!-- If PartialItemStateWeblab is true then, showing different Add-to-wish-list tool-tip message which is consistent with Add-to-Cart tool tip message.  --&gt;



To Add to Wish List, choose from options to the left" class="a-button-group a-declarative a-spacing-none" data-action="a-button-group" role="radiogroup">



<span id="wishListMainButton" class="a-button a-button-groupfirst a-spacing-none a-button-base" role="radio"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fgp%2Faw%2Fd%2FB0000028RR&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caamazon&amp;openid.mode=checkid_setup&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;" name="submit.add-to-registry.wishlist.unrecognized" title="Add to Wish List" data-hover="&lt;!-- If PartialItemStateWeblab is true then, showing different Add-to-wish-list tool-tip message which is consistent with Add-to-Cart tool tip message.  --&gt;



To Add to Wish List, choose from options to the left" class="a-button-text a-text-left" role="button">
Add to Wish List
</a></span></span>



</div>


<div id="atwl-inline-spinner" class="a-section a-hidden">
<div class="a-spinner-wrapper"><span class="a-spinner a-spinner-medium"></span></div>
</div>

<div id="atwl-inline" class="a-section a-spacing-none a-hidden">
<div class="a-row a-text-ellipsis">
<div id="atwl-inline-sucess-msg" class="a-box a-alert-inline a-alert-inline-success"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">
<span class="a-size-base" role="alert">
Added to
</span>
</div></div></div>
<a id="atwl-inline-link" class="a-link-normal" href="/gp/registry/wishlist/">
<span id="atwl-inline-link-text" class="a-size-base" role="alert">
</span>
</a>
</div>
</div>

<div id="atwl-inline-error" class="a-section a-hidden">
<div class="a-box a-alert-inline a-alert-inline-error" aria-live="assertive" role="alert"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">
<span id="atwl-inline-error-msg" class="a-size-base" role="alert">
Unable to add item to Wish List. Please try again.
</span>
</div></div></div>
</div>
<div id="atwl-dd-spinner-holder" class="a-section a-hidden">
<div class="a-row a-dropdown">
<div class="a-section a-popover-wrapper">
<div class="a-section a-text-center a-popover-inner">
<div class="a-box a-popover-loading"><div class="a-box-inner">
</div></div>
</div>
</div>
</div>
</div>
<div id="atwl-dd-error-holder" class="a-section a-hidden">
<div class="a-section a-dropdown">
<div class="a-section a-popover-wrapper">
<div class="a-section a-spacing-base a-padding-base a-text-left a-popover-inner">
<h3 class="a-color-error">

</h3>
<span>

</span>
</div>
</div>
</div>
</div>
<div id="atwl-dd-unavail-holder" class="a-section a-hidden">
<div class="a-section a-dropdown">
<div class="a-section a-popover-wrapper">
<div class="a-section a-spacing-base a-padding-base a-text-left a-popover-inner">
<h3 class="a-color-error">

</h3>
<span>

</span>
</div>
</div>
</div>
</div>
<script type="a-state" data-a-state="{&quot;key&quot;:&quot;atwl&quot;}">{"showInlineLink":false,"hzPopover":true,"wishlistButtonId":"add-to-wishlist-button","dropDownHtml":"","inlineJsFix":true,"wishlistButtonSubmitId":"add-to-wishlist-button-submit","maxAjaxFailureCount":"3","asin":"B0000028RR"}</script>
</div>






<script type="a-state" data-a-state="{&quot;key&quot;:&quot;popoverState&quot;}">{"formId":"addToCart","showWishListDropDown":false,"wishlistPopoverWidth":206,"isAddToWishListDropDownAuiEnabled":true,"showPopover":false}</script>
<div class="aok-hidden" data-amazon-lists-csrf-token="gzRZZBbtVNo0od30hehPta+qN5rrcwwfoqRCTxuE8BkpAAAADAAAAABguq2AcmF3AAAAABVX8CwXqz4nuL9RKX///w=="></div>


<script type="text/javascript">(function(f) {var _np=(window.P._namespace("list-CF-register-js"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
"use strict";
window.P.now('atwl-cf').execute(function (module) {
var isRegistered = (typeof module !== 'undefined');
if (!isRegistered) {
window.P.register('atwl-cf');
}
});
}));</script>















<style type="text/css">
.registry-button-width {
width:100%;
margin-left: ;
margin-right: ;
}
.add-to-baby-button-spacing-bottom {
margin-bottom: 0;
}
</style>

    </form>
 </div>
























</div>






</div>





<div id="addToRegistry_feature_div" data-feature-name="addToRegistry" data-template-name="addToRegistry" class="a-section a-spacing-none">













<div id="addToRegistry_feature_div" class="celwidget" data-feature-name="addToRegistry">


































</div>






</div>





<div id="digitalDashLowProminenceAccordion_feature_div" data-feature-name="digitalDashLowProminenceAccordion" data-template-name="digitalDashLowProminenceAccordion" class="a-section a-spacing-none">













<div id="digitalDashLowProminenceAccordion_feature_div" class="celwidget" data-feature-name="digitalDashLowProminenceAccordion">





































</div>






</div>



        
    




















</div>

































































</div>




















</div>


















<div id="olpLinkWidget_feature_div" class="celwidget" data-feature-name="olpLinkWidget">

















<style>
.olp-touch-link {
position: relative;
text-decoration: inherit !important;
color: inherit !important;
}
.olp-link-widget .arrow-icon {
position: absolute;
top: 36%;
right: 10px;
}
.olp-text-box > .a-color-base {
color: #B12704 !important
}
.olp-text {
float: left;
}
.olp-link-widget {
padding: 10px 0px;
}
.olp-link-widget .a-icon-touch-link {
display: block;
}
.olp-text-box {
text-decoration: none;
padding-right: 10px;
}
html[dir=rtl] .olp-link-widget .a-icon-touch-link {
display: block;
}
html[dir=rtl] .olp-link-widget .arrow-icon {
left: 2%;
right: unset;
}
html[dir=rtl] .olp-text {
float: right !important;
}
html[dir=rtl] .olp-text-box {
padding-left: 10px;
padding-right: 0px;
}
</style>



<div id="all-offers-display" class="a-section">
<div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div>
<form method="get" action="" autocomplete="off" class="aok-hidden all-offers-display-params">
<input type="hidden" name="" value="true" id="all-offers-display-reload-param"/>

<input type="hidden" name="" id="all-offers-display-params" data-asin="B0000028RR" data-m="" data-qid="" data-smid="" data-sourcecustomerorglistid="" data-sourcecustomerorglistitemid="" data-sr=""/>
</form>
</div>
<span class="a-declarative" data-action="close-all-offers-display" data-close-all-offers-display="{}">
<div id="aod-background" class="a-section aok-hidden aod-darken-background">
</div>
</span>






<script type="application/javascript">
P.when("A", "load").execute("aod-assets-loaded", function(A){
function logAssetsNotLoaded() {
if (window.ueLogError) {
var customError = { message: 'Failed to load AOD assets for WDG: music_display_on_website, Device: web' };
var additionalInfo = {
logLevel : 'ERROR',
attribution : 'aod_assets_not_loaded'
};
ueLogError (customError, additionalInfo);
}
if (window.ue && window.ue.count) {
window.ue.count("aod-assets-not-loaded", 1);
}
}
function verifyAssetsLoaded() {
var assetsLoadedPageState = A.state('aod:assetsLoaded');
var logAssetsNotLoadedState = A.state('aod:logAssetsNotLoaded');
if((assetsLoadedPageState == null || !assetsLoadedPageState.isAodAssetsLoaded)
&& (logAssetsNotLoadedState == null || !logAssetsNotLoadedState.isAodAssetsNotLoadedLogged)) {
A.state('aod:logAssetsNotLoaded', {isAodAssetsNotLoadedLogged: true});
logAssetsNotLoaded();
}
}
setTimeout(verifyAssetsLoaded, 50000)
});
</script>













<div class="a-section olp-link-widget">



<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{}">
<a href="/gp/offer-listing/B0000028RR/ref=dp_olp_ALL_mbc?ie=UTF8&amp;condition=ALL" class="a-touch-link a-box olp-touch-link"><div class="a-box-inner"><i class="a-icon a-icon-touch-link"></i>

<div class="olp-text-box">
<span>New &amp; Used (29) from</span><span><br/></span><span class="a-size-base a-color-base">$3.71</span><span>&nbsp;</span><span><span class="a-color-secondary a-size-base">+ $3.49 shipping</span></span>

</div>

<i class="a-icon a-icon-arrow a-icon-small arrow-icon" role="presentation"></i>

</div></a>
</span>




</div>


































</div>




































































<div id="redirection_feature_div" class="celwidget" data-feature-name="redirection">




































</div>


















<div id="tradeInButton_feature_div" class="celwidget" data-feature-name="tradeInButton">














































</div>


















<div id="moreBuyingChoices_feature_div" class="celwidget" data-feature-name="moreBuyingChoices">










































</div>
















































<div id="amsDetailRight_feature_div" class="celwidget" data-feature-name="amsDetailRight">



















<div id="amsDetailRightV2" data-detailPageAsin="B0000028RR">
<script>if (typeof uet === 'function' && typeof ues === 'function') {var scope = 'Detail_ams-detail-right-v2_desktop';var placementId = 'a79ff2fa-21c4-4ca2-b20c-6ea5b8283a5f';ues('wb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); uet('bb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); if (placementId) {ues('wb', 'adplacements:' + placementId, {wb:1});uet('bb', 'adplacements:' + placementId, {wb:1});}}</script><div id="ape_Detail_ams-detail-right-v2_desktop_placement" class="copilot-secure-display celwidget  text/x-dacx-safeframe" cel_widget_id="adplacements:Detail:ams-detail-right-v2:desktop" data-csa-c-type="widget" data-csa-c-slot-id="adplacements:Detail:ams-detail-right-v2:desktop" data-csa-c-content-id="a79ff2fa-21c4-4ca2-b20c-6ea5b8283a5f" data-campaign="13830" style="display: block; margin:auto; line-height:0; margin-top:10px;" data-ad-details='{"slot" :"Detail_ams-detail-right-v2_desktop","pageType": "Detail","subPageType":  "desktop","slotName" :"ams-detail-right-v2","src" : "https://aax-us-east.amazon-adsystem.com/e/xsp/getAd?placementId=a79ff2fa-21c4-4ca2-b20c-6ea5b8283a5f&src=513&slot=ams-detail-right-v2&rid=0101c65f40afa14aedb5e62c5cf36c2f98911d860bd6b244b27ea952d8bb60dc651e&rj=%7B%7D","adServer" :"cs","campaignId" :  "13830","arid" :"85a173aa784d4217b5462d8df80d1a4d","placementId": "a79ff2fa-21c4-4ca2-b20c-6ea5b8283a5f","size" :{"width": "100%","height" : "250px"},"allowedSizes" :[],"allowChangeSize":  true,"allowedDomains" :  ["g-ecx.images-amazon.com"],"aanParams" :   "site%3Damazon.ca%3Bpt%3DDetail%3Bslot%3Dams-detail-right-v2%3Bpid%3DB0000028RR%3Barid%3D85a173aa784d4217b5462d8df80d1a4d","loadAfter" :   "immediate","extraDelay" :  0,"iframeExtraStyle": "","iframeClass":  "","isCardsFlow": false,"adPixels": [],"aaxInstrPixelUrl": "","serverSideFetchAd": "false","enableAdBlockerDetector": false,"disableResizeFunc": true,"minWidthToScale": "","fallbackStaticAdImgUrl": "","fallbackStaticAdClickUrl": "","fallbackStaticAdExtraStyle": "","adFeedbackInfo": {"endPoint": "/gp/aq-feedback/lazyLoad/handler/af-link-handler.html","boolFeedback": true,"slugText": "Sponsored","adFeedbackOnTop":false},"adPlacementMetaData": {"pageUrl": "aHR0cHM6Ly93d3cuYW1hem9uLmNhL2dwL3Byb2R1Y3QvQjAwMDAwMjhSUg==","adElementId": "ape_Detail_ams-detail-right-v2_desktop_placement","pageType": "Detail","slotName": "ams-detail-right-v2"},"adCreativeMetaData": {"adNetwork": "cs"},"advertisementStyle": {"position": "absolute","top": "2px","right": "0px","display": "inline-block","font": "normal 11px Arial","color": "grey"},"feedbackDivStyle": {"position": "relative","height": "14px","top": "2px"},"viewabilityStandards": [{"p": 0, "t": 0, "def": "amzn"}, {"p": 50, "t": 1, "def": "iab"}, {"p": 100, "t": 1, "def": "groupm"}],"ajaxWeblabTriggerId": "","abpStatus": "1","abpAcceptable": "true","disableAdReporterSlot": "false","allowlistedCustomMessageEvents": ["openPsAdPopover", "openATCModal", "setPartner", "sendMetrics", "wrap"],"allowlistedQueryParamKeys": ["sf-overrideVariationId", "sf-overridePredictorId", "sf-forceFailure"],"DAsfUrl":"https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js"}' aria-hidden="true"></div><script>(function(){function a(d,e){if(window.addEventListener){window.addEventListener(d,e,false);}else{if(window.attachEvent){window.attachEvent("on"+d,e);}}}function c(d,e){if(window.removeEventListener){window.removeEventListener(d,e,false);}else{if(window.detachEvent){window.detachEvent("on"+d,e);}}}var b=function(){(function(){(function(l,o){l.sfLogErrors=l.sfLogErrors||false;var q=q||function(v,u){u=u||new Error(v);if(l.ue&&typeof ue.count=="function"){ue.count("adplacements:safeFrameError",1);}if(!l.sfLogErrors){return;}if(l.ueLogError){l.ueLogError(u,{logLevel:"ERROR",attribution:"APE-safeframe",message:v+" "});}else{if(typeof console!=="undefined"&&console.error){console.error(v,u);}}};l.aanParams=l.aanParams||{};l.aanParams["ams-detail-right-v2"]="site=amazon.ca;pt=Detail;slot=ams-detail-right-v2;pid=B0000028RR;arid=85a173aa784d4217b5462d8df80d1a4d";l["ams-detail-right-v2"]={};l["ams-detail-right-v2"].adStartTime=(new Date()).getTime();function d(){return l.innerHeight||o.documentElement.clientHeight;}function g(){return l.innerWidth||o.documentElement.clientWidth;}function e(w,u,v){if(w>0){return(v>w);}else{return(u>0);}}var f=function(){return(Date.now?Date.now():new Date().getTime());};throttle=function(v,x,B){var u,z,C;var A=null;var y=0;if(!B){B={};}var w=function(){y=B.leading===false?0:f();A=null;C=v.apply(u,z);if(!A){u=z=null;}};return function(){var E=f();if(!y&&B.leading===false){y=E;}var D=x-(E-y);u=this;z=arguments;if(D<=0||D>x){if(A){clearTimeout(A);A=null;}y=E;C=v.apply(u,z);if(!A){u=z=null;}}else{if(!A&&B.trailing!==false){A=setTimeout(w,D);}}return C;};};function n(C,A,v,x,u){try{var z=o.getElementById(C).getBoundingClientRect();if(e(z.top,z.bottom,d())&&e(z.left,z.right,g())){if(typeof uet=="function"){uet("bb","adplacements:viewablelatency:"+A,{wb:1});if(v){uet("bb","adplacements:viewablelatency:"+v,{wb:1});}}var w;if(l.csa){var B=o.getElementById(C);if(u=="mobileads"){w=l.csa("Content",{element:B.parentNode});}else{w=l.csa("Content",{element:B});}w("mark","viewablelatency:bodyBegin");if(l.apeViewableLatencyTrackers[x].loaded){w("mark","viewablelatency:loaded");}}if(typeof uex=="function"&&l.ue&&typeof ue.count=="function"){if(l.apeViewableLatencyTrackers[x].loaded){uex("ld","adplacements:viewablelatency:"+A,{wb:1});if(v){uex("ld","adplacements:viewablelatency:"+v,{wb:1});}ue.count("adplacements:htmlviewed:loaded:"+A,1);if(v){ue.count("adplacements:htmlviewed:loaded:"+v,1);}}ue.count("adplacements:htmlviewed:"+A,1);if(v){ue.count("adplacements:htmlviewed:"+v,1);}}l.apeViewableLatencyTrackers[x].viewed=true;if(l.apeViewableLatencyTrackers[x].tracker){c("scroll",l.apeViewableLatencyTrackers[x].tracker);c("resize",l.apeViewableLatencyTrackers[x].tracker);}}}catch(y){l.apeViewableLatencyTrackers[x].valid=false;}}try{l.apeViewableLatencyTrackers=l.apeViewableLatencyTrackers||{};var t="ape_Detail_ams-detail-right-v2_desktop_placement";var s="Detail_ams-detail-right-v2_desktop".replace(/\_/g,":");var i="a79ff2fa-21c4-4ca2-b20c-6ea5b8283a5f";var k="85a173aa784d4217b5462d8df80d1a4d";var h="amazon";l.apeViewableLatencyTrackers[k]=l.apeViewableLatencyTrackers[k]||{};l.apeViewableLatencyTrackers[k].valid=true;n(t,s,i,k,h);if(l.apeViewableLatencyTrackers[k].valid&&!l.apeViewableLatencyTrackers[k].viewed){l.apeViewableLatencyTrackers[k].tracker=throttle(function(){n(t,s,i,k,h);},20);a("scroll",l.apeViewableLatencyTrackers[k].tracker);a("resize",l.apeViewableLatencyTrackers[k].tracker);}}catch(m){if(l.apeViewableLatencyTrackers&&l.apeViewableLatencyTrackers["85a173aa784d4217b5462d8df80d1a4d"]){l.apeViewableLatencyTrackers["85a173aa784d4217b5462d8df80d1a4d"].valid=false;}q("Error initializing viewable latency instrumentation",m);}if(l.csa){var j;var r=o.getElementById(t);if(h=="mobileads"){j=l.csa("Content",{element:r.parentNode});}else{j=l.csa("Content",{element:r});}j("mark","bodyBegin");}try{if(l.DAsf){l.DAsf.loadAds();}else{var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js?csm_attribution=APE-SafeFrame";p.onerror=function(){q("Error loading SafeFrame library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);l.collectSafeframeRTD=Math.random()*100<0;if(l.collectSafeframeRTD){var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/rtd/safeframeRtd-1.50.81044e8.js";p.onerror=function(){q("Error loading SafeFrame RTD library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);}}}catch(m){q("Error appending DAsf library",m);}}(window,document));})();};b();})();</script>
</div>






















</div>


















<div id="attachAccessoryModal_feature_div" class="celwidget" data-feature-name="attachAccessoryModal">
































<input type="hidden" id="attach-weblabsToTriggerOnAddToCart" value="" />
























</div>






























</div>
<div id="leftCenterCol" class="leftCenterCol">

</div>
<div id="leftCol" class="leftCol">














<div id="imageBlock_feature_div" class="celwidget" data-feature-name="imageBlock">

















<script type="text/javascript">(function(f) {var _np=(window.P._namespace("DetailPageShoppableScenes"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
// Intentionally empty version of ImageBlockShoppableSceneView. When weblab is C, this subview will be used.
// Weblab: https://weblab.amazon.com/wl/MIRAI_SCENES_DP_DESKTOP_EXPERIMENT_342971
P.now().register("ImageBlockShoppableSceneView", function() {
function noop() {}
return function ImageBlockShoppableSceneView() {
this.render = noop;
this.update = noop;
};
});
}));</script>

































<div id="imageBlock" aria-hidden="true" class="a-section">
<div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:40px">

<div class="a-text-center a-fixed-left-grid-col a-col-right" style="padding-left:0%;float:left;">
<div id="twister-main-image" class="a-hidden" customfunctionname="(function(id, state){ P.when('A').execute(function(A){ A.trigger('image-block-twister-swatch-hover', id, state); }); });"></div>
<div class="a-row a-grid-vertical-align a-grid-center canvas ie7-width-96">
<div id="main-image-container" class = "a-dynamic-image-container">

<div id="video-outer-container">
<div id="main-video-container">
</div>
<div id="video-canvas-caption" class="a-row">
<div class="a-column a-span12 a-text-center">
<span id="videoCaption" class="a-color-secondary"></span>
</div>
</div>
</div>


<input id="show-immersive-view-on-softlines" type="hidden" value="false"/>




























<!--     Creating a custom overlay for image not available experience -->
<div class="variationUnavailable unavailableExp">
<div class="inner">

<div class="a-box a-alert a-alert-error" aria-live="assertive" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">Image Unavailable</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content">
<span class="a-text-bold">
Image not available for<br/>Colour:
<span class="unvailableVariation"></span>
</span>
</div></div></div>
</div>
</div>

<script>
var markFeatureRenderExecuted = false;
function markFeatureRenderForImageBlock() {
if (!markFeatureRenderExecuted) {
markFeatureRenderExecuted = true;
P.now().execute('dp-mark-imageblock',function(){
var options = {
hasComponents: true,
components: [{
name: 'mainimage'
}]
};
if (typeof window.markFeatureRender === 'function') {
window.markFeatureRender('imageblock',options);
}
});
}
}
</script>

<div class="a-hidden" id="auiImmersiveViewDiv"></div>
<ul class="a-unordered-list a-nostyle a-horizontal list maintain-height">





<li class="image item itemNo0 selected maintain-height"><span class="a-list-item">
<span class="a-declarative" data-action="main-image-click" data-main-image-click="{}" data-ux-click="">
<div id="imgTagWrapperId" class="imgTagWrapper">

<img alt="Rage Against The Machine" src="https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L.__AC_SX300_SY300_QL70_ML2_.jpg" data-old-hires="https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SL1500_.jpg" onload="markFeatureRenderForImageBlock(); this.onload='';setCSMReq('af');if(typeof addlongPoleTag === 'function'){ addlongPoleTag('af','desktop-image-atf-marker');};setCSMReq('cf')" class="a-dynamic-image a-stretch-horizontal" id="landingImage" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX466_.jpg&quot;:[466,466],&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX385_.jpg&quot;:[385,385],&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX342_.jpg&quot;:[342,342],&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX569_.jpg&quot;:[569,569],&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX425_.jpg&quot;:[425,425],&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX522_.jpg&quot;:[522,522],&quot;https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX679_.jpg&quot;:[679,679]}" style="max-width:679px;max-height:679px;"/>

</div>
</span>
</span></li>



<li class="mainImageTemplate template"><span class="a-list-item">
<span class="a-declarative" data-action="main-image-click" data-main-image-click="{}" data-ux-click="">
<div class="imgTagWrapper">
<span class="placeHolder"></span>
</div>
</span>
</span></li>
<li class="swatchHoverExp a-hidden maintain-height"><span class="a-list-item">
<span class="a-declarative" data-action="main-image-click" data-main-image-click="{}">
<div class="imgTagWrapper">
<span class="placeHolder"></span>
</div>
</span>
</span></li>
<li class="itemUnavailable unavailableExp a-hidden"><span class="a-list-item">
<span class="a-size-medium a-color-state a-text-bold">
Sorry, this item is not available in
</span>
</span></li>
<li class="imageUnavailable unavailableExp a-hidden"><span class="a-list-item">
<span class="a-size-medium a-color-state a-text-bold">

</span>
</span></li>
<li id="noFlashContent" class="noFlash a-hidden"><span class="a-list-item">
To view this video, download 
<a class="a-link-normal" target="_blank" rel="noopener noreferrer noopener" href="https://get.adobe.com/flashplayer">
Flash Player
<span class="swSprite s_extLink"></span>
</a>
</span></li>
</ul>

</div>
</div>

<div id="image-canvas-caption" class="a-row">
<div class="a-column a-span12 a-text-center">
<span id="canvasCaption" class="a-color-secondary"></span>
</div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;




<div class="collections-collect-button"></div>



<div id="altImages" class="a-row">




<div id="thumbs-image" class="a-hidden" customfunctionname="(function(id, state, onloadFunction){ P.when('A').execute(function(A){ A.trigger('image-block-twister-swatch-click', id, state, onloadFunction); }); });"></div>

<ul class="a-unordered-list a-nostyle a-button-list a-horizontal">
















<li class="a-spacing-small item"><span class="a-list-item">
<span class="a-declarative" data-action="thumb-action" data-thumb-action="{&quot;thumbnailIndex&quot;:&quot;0&quot;,&quot;variant&quot;:&quot;MAIN&quot;,&quot;index&quot;:0,&quot;type&quot;:&quot;image&quot;}" data-ux-click="">
<span class="a-button a-button-selected a-button-thumbnail a-button-toggle a-button-focus"><span class="a-button-inner"><input class="a-button-input" type="submit"/><span class="a-button-text" aria-hidden="true">



<img alt="" src="https://images-na.ssl-images-amazon.com/images/I/61sbdhhOpkL._AC_SR38,50_.jpg"/>


</span></span></span>
</span>
</span></li>






<li class="a-spacing-small template"><span class="a-list-item">
<span class="a-button a-button-thumbnail a-button-toggle"><span class="a-button-inner"><input class="a-button-input" type="submit"/><span class="a-button-text" aria-hidden="true">
<span class="placeHolder"></span>
</span></span></span>
</span></li>









<li class="a-spacing-small videoCountTemplate aok-hidden"><span class="a-list-item">
<span id="videoCount_template" class="a-size-mini a-color-secondary video-count a-text-bold a-nowrap"> </span>
</span></li>








</ul>


</div>

</div>
</div></div>
</div>


<script type="text/javascript">

maintainHeight = function(){
var mainHolder = document.getElementById("main-image-container");
var imgTagWrapperId = document.getElementById("imgTagWrapperId");
if(mainHolder && typeof mainHolder != 'undefined'){
var ratio = 0.84;
var shouldAutoPlay = false;
var naturalMainImageSize = false;
var videoSizes = [[342, 342], [385, 385], [425, 425], [466, 466], [522, 522], [569, 569], [679, 679]];


var width = mainHolder.offsetWidth;
var containerHeight = width/ratio;
containerHeight = Math.min(containerHeight, 700);
var landingImage = document.getElementById("landingImage");
var aspectRatio;



aspectRatio = 679/679


var imageHeight = containerHeight;
var imageWidth = width;



if(!shouldAutoPlay) {
imageHeight = Math.min(imageHeight, 679);
imageWidth = Math.min(imageWidth, 679);
}



var imageWidthBasedOnHeight = imageHeight * aspectRatio;
var imageHeightBasedOnWidth = imageWidth / aspectRatio;
imageHeight = Math.min(imageHeight, imageHeightBasedOnWidth);
imageWidth = Math.min(imageWidth, imageWidthBasedOnHeight);
if(typeof mainImgMaxHeight !== 'undefined' && mainImgMaxHeight){
containerHeight = Math.min(mainImgMaxHeight, containerHeight);
}
mainHolder.style.height = containerHeight + "px";
if(imgTagWrapperId && typeof imgTagWrapperId !== 'undefined' ){
imgTagWrapperId.style.height = containerHeight + "px";
}
if(landingImage && !naturalMainImageSize) {
landingImage.style.maxHeight = imageHeight + "px";
landingImage.style.maxWidth  = imageWidth + "px";
}
if(shouldAutoPlay){
if(landingImage){
landingImage.style.height = imageHeight + "px";
landingImage.style.width  = imageWidth + "px";
}
}
}
};
maintainHeight();
window.onresize = function(){
maintainHeight();
};

P.when('A').register("ImageBlockATF", function(A){
var data = {
'colorImages': { 'initial': [{"hiRes":"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SL1500_.jpg","thumb":"https://images-na.ssl-images-amazon.com/images/I/61sbdhhOpkL._AC_SR38,50_.jpg","large":"https://images-na.ssl-images-amazon.com/images/I/61sbdhhOpkL._AC_.jpg","main":{"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX342_.jpg":[342,342],"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX385_.jpg":[385,385],"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX425_.jpg":[425,425],"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX466_.jpg":[466,466],"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX522_.jpg":[522,522],"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX569_.jpg":[569,569],"https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_SX679_.jpg":[679,679]},"variant":"MAIN","lowRes":null,"shoppableScene":null}]},
'colorToAsin': {'initial': {}},
'heroImage': {'initial': []},
'heroVideo': {'initial': []},
'holderRatio': 0.84,
'holderMaxHeight': 700,
'useStretchyImageFix': true,
'videoIngressATFSlateThumbURL': '',
'isEnhancedImageBlockSize' : true,
'atfEnhancedHoverOverlay' : true,
'aibExp3Layout' : 1,
'aibRuleName' : 'frank-powered',
'acEnabled' : true,

'airyConfig' :A.$.parseJSON('{"jsUrl":"https://images-na.ssl-images-amazon.com/images/G/01/vap/video/airy2/prod/2.0.1460.0/js/airy.skin._CB485981857_.js","cssUrl":"https://images-na.ssl-images-amazon.com/images/G/01/vap/video/airy2/prod/2.0.1460.0/css/beacon._CB485971591_.css","swfUrl":"https://images-na.ssl-images-amazon.com/images/G/01/vap/video/airy2/prod/2.0.1460.0/flash/AiryBasicRenderer._CB485925577_.swf","foresterMetadataParams":{"marketplaceId":"A2EUQ1WTGCTBG2","method":"Music.ImageBlock","requestId":"1KMDY2JPGP2X3R80G8WC","session":"138-4669640-7712440","client":"Dpx"}}')

};
A.trigger('P.AboveTheFold'); // trigger ATF event.
return data;
});
</script>














<!--Only include showroom templates when the base view adapter is being invoked-->






<div class="a-popover-preload" id="a-popover-immersiveView">
<div id="iv-tab-view-container">
<ul class="iv-tab-views a-declarative">
<li id="ivVideosTabHeading" class="iv-tab-heading">
<a href="#" data-iv-tab-view="ivVideosTab">
VIDEOS
</a>
</li>
<li id="iv360TabHeading" class="iv-tab-heading">
<a href="#" data-iv-tab-view="iv360Tab">
360° VIEW


</a>
</li>
<li id="ivImagesTabHeading" class="iv-tab-heading">
<a href="#" data-iv-tab-view="ivImagesTab">
IMAGES
</a>
</li>

</ul>
<div id="ivVideosTab" class="iv-box iv-box-tab iv-tab-content">
<div class="iv-box-inner">
<div id="ivVideoBlock">
<div id="ivVideoBlockSpinner" class="a-spinner-wrapper"><span class="a-spinner a-spinner-medium"></span></div>
</div>
</div>
</div>
<div id="iv360Tab" class="iv-box iv-box-tab iv-tab-content">
<div class="iv-box-inner">
<div id="ivMain360">
<div id="ivStage360">
<div id="ivLarge360"></div>
</div>
<div id="ivThumbColumn360">
<div id="ivTitle360"></div>
<div id="ivVariationSelection360"></div>
<div id="ivThumbs360">
<div class="ivRow placeholder"></div>
<div class="ivThumb placeholder">
<div class="ivThumbImage"></div>
</div>
</div>
</div>
<div class="ivClearfix"></div>
</div>
</div>
</div>
<div id="ivImagesTab" class="iv-box iv-box-tab iv-tab-content">
<div class="iv-box-inner">
<div id="ivMain">
<div id="ivStage">
<div id="ivLargeImage"></div>
</div>
<div id="ivThumbColumn">
<div id="ivTitle"></div>
<div id="ivVariationSelection"></div>
<div id="ivThumbs">
<div class="ivRow placeholder"></div>
<div class="ivThumb placeholder">
<div class="ivThumbImage"></div>
</div>
</div>
</div>
<div class="ivClearfix"></div>
</div>
</div>
</div>

</div>
</div>




<div class="dp-cif aok-hidden"
data-feature-details='{"name":"imageblock","hasComponents":true,"components":[{"name":"mainimage","events":["click","hover"]},{"name":"thumbnail","events":["click","hover"]}]}'></div>



<script type="text/javascript">(function(f) {var _np=(window.P._namespace("DetailPageImageBlockTemplate"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.now().execute('dp-mark-imageblock',function(){
var options = {
hasComponents: true,
components: [{
name: 'thumbnail'
}]
};
if (typeof window.markFeatureRender === 'function') {
window.markFeatureRender('imageblock',options);
}
});
}));</script>



























</div>





</div>
<div id="centerCol" class="centerColAlign centerColAlign-bbcxoverride">














<div id="title_feature_div" class="celwidget" data-feature-name="title">















<style type="text/css">
.product-title-word-break {
word-break: break-word;
}
</style>

<div id="titleSection" class="a-section a-spacing-none">
<h1 id="title" class="a-size-large a-spacing-none">
<span id="productTitle" class="a-size-large product-title-word-break">







Rage Against The Machine






</span>






</h1>
<div id="expandTitleToggle" class="a-section a-spacing-none expand aok-hidden"></div>

</div>



























</div>


















<div id="qpeTitleTag_feature_div" class="celwidget" data-feature-name="qpeTitleTag">

























</div>


















<div id="bylineInfo_feature_div" class="celwidget" data-feature-name="bylineInfo">
























<div id="bylineInfo" class="a-section a-spacing-micro bylineHidden feature">









<span class="author notFaded" data-width="">






<a class="a-link-normal" href="/s/ref=dp_byline_sr_music_1?ie=UTF8&amp;field-artist=Rage+Against+The+Machine&amp;search-alias=music-ca">Rage Against The Machine</a>






<span class="contribution" spacing="none">
<span class="a-color-secondary">(Artist)</span>
</span>

</span>









<i class="a-icon a-icon-text-separator" role="presentation"></i>

<span class="a-color-secondary">Format: </span><span>Audio CD</span>



</div>



























</div>


















<div id="cmrsSummary_feature_div" class="celwidget" data-feature-name="cmrsSummary">




































</div>


















<div id="averageCustomerReviews_feature_div" class="celwidget" data-feature-name="averageCustomerReviews">












<style type="text/css">
/*
* Fix for UDP-1061. Average customer reviews has a small extra line on hover
* https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40
*/
.noUnderline a:hover {
text-decoration: none;
}
</style>



















<div id="averageCustomerReviews" data-asin="B0000028RR" data-ref="dpx_acr_pop_" >












<span class="a-declarative" data-action="acrStarsLink-click-metrics" data-acrStarsLink-click-metrics="{}">



<span id="acrPopover" class="reviewCountTextLinkedHistogram noUnderline" title="4.7 out of 5 stars">
<span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;url&quot;:&quot;/gp/customer-reviews/widgets/average-customer-review/popover/ref=dpx_acr_pop_?contextId=dpx&amp;asin=B0000028RR&quot;}">
<a href="javascript:void(0)" class="a-popover-trigger a-declarative">

<i class="a-icon a-icon-star a-star-4-5"><span class="a-icon-alt">4.7 out of 5 stars</span></i>

<i class="a-icon a-icon-popover"></i></a>
</span>
<span class="a-letter-space"></span>
</span>



</span>
<span class="a-letter-space"></span>












<span class="a-declarative" data-action="acrLink-click-metrics" data-acrLink-click-metrics="{}">
<a id="acrCustomerReviewLink" class="a-link-normal" href="#customerReviews">
<span id="acrCustomerReviewText" class="a-size-base">3,129 ratings</span>
</a>
</span>
<script type="text/javascript">
P.when('A', 'ready').execute(function(A) {
A.declarative('acrLink-click-metrics', 'click', { "allowLinkDefault" : true }, function(event){
if(window.ue) {
ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1);
}
});
});
</script>





<script type="text/javascript">
P.when('A', 'cf').execute(function(A) {
A.declarative('acrStarsLink-click-metrics', 'click', { "allowLinkDefault" : true },  function(event){
if(window.ue) {
ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1);
}
});
});
</script>







</div>

























</div>


















<div id="acBadge_feature_div" class="celwidget" data-feature-name="acBadge">





















<script type="a-state" data-a-state="{&quot;key&quot;:&quot;acState&quot;}">{"acAsin":"B0000028RR"}</script>























</div>


















<div id="zeitgeistBadge_feature_div" class="celwidget" data-feature-name="zeitgeistBadge">




































</div>
























<hr/>


































<div id="desktop_unifiedPrice" class="celwidget" data-feature-name="desktop_unifiedPrice">




























<div id="unifiedPrice_feature_div" class="celwidget" data-feature-name="unifiedPrice">









































































<div id="price" class="a-section a-spacing-small">
<table class="a-lineitem">




















































<tr id="priceblock_ourprice_row">
<td id="priceblock_ourprice_lbl" class="a-color-secondary a-size-base a-text-right a-nowrap">Price:</td>
<td class="a-span12">





<span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">$32.21</span>











































































<span id="ourprice_shippingmessage">	













































<span id="price-shipping-message" class="a-size-base a-color-base"></span>






</span>



</td>
</tr>






































































































































































</table>



</div>































</div>


















<div id="quantityPricingTableSummary_feature_div" class="celwidget" data-feature-name="quantityPricingTableSummary">



































</div>






















</div>


















<div id="b2bUpsell_feature_div" class="celwidget" data-feature-name="b2bUpsell">




































</div>


















<div id="iconfarmv2_feature_div" class="celwidget" data-feature-name="iconfarmv2">
























































</div>


















<div id="issuancePriceblockAmabot_feature_div" class="celwidget" data-feature-name="issuancePriceblockAmabot">


































</div>


















<div id="pmpux_feature_div" class="celwidget" data-feature-name="pmpux">



































</div>

































<div id="applicablePromotionList_feature_div" class="celwidget" data-feature-name="applicablePromotionList">






































</div>


















<div id="valuePick_feature_div" class="celwidget" data-feature-name="valuePick">



































</div>























<div id="globalStoreBadgePopover_feature_div" class="celwidget" data-feature-name="globalStoreBadgePopover">














































</div>























<div id="addOnItem_feature_div" class="celwidget" data-feature-name="addOnItem">



































</div>


















<div id="andonCord_feature_div" class="celwidget" data-feature-name="andonCord">


































</div>























<div id="MediaMatrix" class="celwidget" data-feature-name="MediaMatrix">















<div id="all-offers-display" class="a-section">
<div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div>
<form method="get" action="" autocomplete="off" class="aok-hidden all-offers-display-params">
<input type="hidden" name="" value="true" id="all-offers-display-reload-param"/>

<input type="hidden" name="" id="all-offers-display-params" data-asin="B0000028RR" data-m="" data-qid="" data-smid="" data-sourcecustomerorglistid="" data-sourcecustomerorglistitemid="" data-sr=""/>
</form>
</div>
<span class="a-declarative" data-action="close-all-offers-display" data-close-all-offers-display="{}">
<div id="aod-background" class="a-section aok-hidden aod-darken-background">
</div>
</span>






<script type="application/javascript">
P.when("A", "load").execute("aod-assets-loaded", function(A){
function logAssetsNotLoaded() {
if (window.ueLogError) {
var customError = { message: 'Failed to load AOD assets for WDG: music_display_on_website, Device: web' };
var additionalInfo = {
logLevel : 'ERROR',
attribution : 'aod_assets_not_loaded'
};
ueLogError (customError, additionalInfo);
}
if (window.ue && window.ue.count) {
window.ue.count("aod-assets-not-loaded", 1);
}
}
function verifyAssetsLoaded() {
var assetsLoadedPageState = A.state('aod:assetsLoaded');
var logAssetsNotLoadedState = A.state('aod:logAssetsNotLoaded');
if((assetsLoadedPageState == null || !assetsLoadedPageState.isAodAssetsLoaded)
&& (logAssetsNotLoadedState == null || !logAssetsNotLoadedState.isAodAssetsNotLoadedLogged)) {
A.state('aod:logAssetsNotLoaded', {isAodAssetsNotLoadedLogged: true});
logAssetsNotLoaded();
}
}
setTimeout(verifyAssetsLoaded, 50000)
});
</script>















<div id="formats" class="a-section a-spacing-large responsive"><script type="a-state" data-a-state="{&quot;key&quot;:&quot;mediamatrix-saf&quot;}">{"hideEdition":false,"editionCount":18}</script>








<a class="a-size-small a-spacing-small a-spacing-top-micro a-link-normal a-link-expander" href="javascript:void(0)">
<i id="formatsIcon" class="a-icon a-icon-arrow" role="presentation"></i>
<span id="showMoreFormatsPrompt" class="tmmShowPrompt" >See all 18 formats and editions</span>
<span id="hideMoreFormatsPrompt" class="tmmHidePrompt">Hide other formats and editions</span>
</a>


















<div id="twister" class="a-section a-spacing-base a-spacing-top-small a-size-mini">




























<table class="a-normal a-spacing-none title">
<tr>
<td class="dp-title-col">

</td>

<td class="a-color-secondary a-text-right dp-price-col">
<div class="a-fixed-right-grid"><div class="a-fixed-right-grid-inner" style="padding-right:50px">
<div class="a-fixed-right-grid-col a-col-left" style="padding-right:2.5%;float:left;">
Amazon Price
</div>
<div class="a-fixed-right-grid-col a-col-right" style="width:50px;margin-right:-50px;float:left;"></div>
</div></div>
</td>

<td class="a-color-secondary a-text-right dp-new-col">
New from
</td>


<td class="a-color-secondary a-text-right dp-used-col">
Used from
</td>


</tr>
</table>





















































<div class="hr unselected-row"></div>
<div class="top-level unselected-row">
<span class="a-declarative" data-action="tmm-see-more-editions-click" data-tmm-see-more-editions-click="{&quot;metabindingPlaceHolder&quot;:1,&quot;metabindingPlaceHolderState&quot;:&quot;0&quot;,&quot;metabindingUrl&quot;:&quot;/Rage-Against-Mach-Machine/dp/B016W63SAY/ref=tmm_acd_title_0?_encoding=UTF8&amp;amp;qid=&amp;amp;sr=&quot;}" id="declarative_1">
<table class="a-normal a-spacing-none">
<tr>
<td class="dp-title-col">
<!-- Do not show expander when DVD_redesign weblab is in treatment -->



<a class="a-link-expander title-expander" style="vertical-align:middle; padding-left:16px">
<span class="a-link-expander metabinding-expander">



<i id="editionsIcon_1" class="a-icon a-icon-arrow tmm-row-icon" role="presentation"></i>


</span>
</a>








<a href="/Rage-Against-Mach-Machine/dp/B016W63SAY/ref=tmm_acd_title_0?_encoding=UTF8&amp;qid=&amp;sr=" class="title-text">
<span class="a-size-small a-color-base">Audio CD, Remixes included, Nov. 11 2014</span>
<span id="tmmSpinnerDiv_1" style="display: none" class="tmmAjaxLoading"></span>


</a>




<span id="tmmErrorDiv_1" class="tmmErrorClass displayNone">
<div class="a-box a-alert-inline a-alert-inline-error" aria-live="assertive" role="alert"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">
<span>"Please retry"</span>
</div></div></div>
</span>
</td>







<td class="a-text-right dp-price-col">
<div class="a-fixed-right-grid"><div class="a-fixed-right-grid-inner" style="padding-right:50px">
<div class="a-fixed-right-grid-col a-col-left" style="padding-right:2.5%;float:left;">






<a class="a-link-normal" href="/Rage-Against-Mach-Machine/dp/B016W63SAY/ref=tmm_acd_title_0?_encoding=UTF8&amp;qid=&amp;sr=">







<span class="a-size-small a-color-price">$11.50 </span>
</a>






</div>
<div class="a-fixed-right-grid-col a-col-right" style="width:50px;margin-right:-50px;float:left;">





<span id="primeSlot" class="badge-slot">
<div style="display:inline-block;">

</div>
</span>





</div>
</div></div>
</td>






<td class="a-text-right dp-new-col">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;new&quot;,&quot;asin&quot;:&quot;B016W63SAY&quot;}">
<a class="a-link-normal" href="/gp/offer-listing/B016W63SAY/ref=tmm_acd_new_olp_0?ie=UTF8&amp;condition=new">
<span>$7.84</span>
</a>
</span>



</td>







<td class="a-text-right dp-used-col">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;used&quot;,&quot;asin&quot;:&quot;B016W63SAY&quot;}">
<a class="a-link-normal" href="/gp/offer-listing/B016W63SAY/ref=tmm_acd_used_olp_0?ie=UTF8&amp;condition=used">
<span>$13.54</span>
</a>
</span>



</td>







</tr>

</table>
</span>
</div>


<div id="metabinding_row_top_1" class="second-level"></div>




<div id="binding_row_landing">


















<span class="a-declarative" data-action="tmm-see-more-editions-click" data-tmm-see-more-editions-click="{&quot;metabindingUrl&quot;:&quot;#&quot;}" id="declarative_binding_landing">
<table class="a-normal a-spacing-none a-size-mini">
<tr>
<td class="dp-title-col">



<span class="a-color-base binding-title">Audio CD, Explicit Lyrics, Nov. 13 1992</span>




</td>

<td class="a-text-right dp-price-col">
<div class="a-fixed-right-grid"><div class="a-fixed-right-grid-inner" style="padding-right:50px">
<div class="a-fixed-right-grid-col a-col-left" style="padding-right:2.5%;float:left;">














<span class="a-color-price">$32.21 </span>







</div>
<div class="a-fixed-right-grid-col a-col-right" style="width:50px;margin-right:-50px;float:left;">





<span id="primeSlot" class="badge-slot">
<div style="display:inline-block;">

</div>
</span>





</div>
</div></div>
</td>






<td class="a-text-right dp-new-col">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;new&quot;,&quot;asin&quot;:&quot;B0000028RR&quot;}">
<a class="a-link-normal" href="/gp/offer-listing/B0000028RR/ref=tmm_acd_new_olp_0?ie=UTF8&amp;condition=new">
<span>$32.21</span>
</a>
</span>



</td>







<td class="a-text-right dp-used-col">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;used&quot;,&quot;asin&quot;:&quot;B0000028RR&quot;}">
<a class="a-link-normal" href="/gp/offer-listing/B0000028RR/ref=tmm_acd_used_olp_0?ie=UTF8&amp;condition=used">
<span>$3.21</span>
</a>
</span>



</td>







</tr>
</table>
</span>






</div>

<div id="metabinding_row_bottom_1" class="second-level"></div>






















































<div class="hr unselected-row"></div>
<div class="top-level unselected-row">
<span class="a-declarative" data-action="tmm-see-more-editions-click" data-tmm-see-more-editions-click="{&quot;metabindingPlaceHolder&quot;:2,&quot;metabindingPlaceHolderState&quot;:&quot;0&quot;,&quot;metabindingUrl&quot;:&quot;/Rage-Against-20thann-Vinyl-Machine/dp/B009A9EYUO/ref=tmm_vnl_title_0?_encoding=UTF8&amp;amp;qid=&amp;amp;sr=&quot;}" id="declarative_2">
<table class="a-normal a-spacing-none">
<tr>
<td class="dp-title-col">
<!-- Do not show expander when DVD_redesign weblab is in treatment -->



<a class="a-link-expander title-expander" style="vertical-align:middle; padding-left:16px">
<span class="a-link-expander metabinding-expander">



<i id="editionsIcon_2" class="a-icon a-icon-arrow tmm-row-icon" role="presentation"></i>


</span>
</a>








<a href="/Rage-Against-20thann-Vinyl-Machine/dp/B009A9EYUO/ref=tmm_vnl_title_0?_encoding=UTF8&amp;qid=&amp;sr=" class="title-text">
<span class="a-size-small a-color-base">LP Record, Explicit Lyrics, Import, Nov. 27 2012</span>
<span id="tmmSpinnerDiv_2" style="display: none" class="tmmAjaxLoading"></span>


</a>




<span id="tmmErrorDiv_2" class="tmmErrorClass displayNone">
<div class="a-box a-alert-inline a-alert-inline-error" aria-live="assertive" role="alert"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">
<span>"Please retry"</span>
</div></div></div>
</span>
</td>







<td class="a-text-right dp-price-col">
<div class="a-fixed-right-grid"><div class="a-fixed-right-grid-inner" style="padding-right:50px">
<div class="a-fixed-right-grid-col a-col-left" style="padding-right:2.5%;float:left;">






<a class="a-link-normal" href="/Rage-Against-20thann-Vinyl-Machine/dp/B009A9EYUO/ref=tmm_vnl_title_0?_encoding=UTF8&amp;qid=&amp;sr=">







<span class="a-size-small a-color-price">$31.72 </span>
</a>






</div>
<div class="a-fixed-right-grid-col a-col-right" style="width:50px;margin-right:-50px;float:left;">





<span id="primeSlot" class="badge-slot">
<div style="display:inline-block;">

</div>
</span>





</div>
</div></div>
</td>






<td class="a-text-right dp-new-col">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;new&quot;,&quot;asin&quot;:&quot;B009A9EYUO&quot;}">
<a class="a-link-normal" href="/gp/offer-listing/B009A9EYUO/ref=tmm_vnl_new_olp_0?ie=UTF8&amp;condition=new">
<span>$31.72</span>
</a>
</span>



</td>







<td class="a-text-right dp-used-col">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;used&quot;,&quot;asin&quot;:&quot;B009A9EYUO&quot;}">
<a class="a-link-normal" href="/gp/offer-listing/B009A9EYUO/ref=tmm_vnl_used_olp_0?ie=UTF8&amp;condition=used">
<span>$32.28</span>
</a>
</span>



</td>







</tr>

</table>
</span>
</div>


<div id="metabinding_row_top_2" class="second-level"></div>

<div id="metabinding_row_bottom_2" class="second-level"></div>




<script type="a-state" data-a-state="{&quot;key&quot;:&quot;mediamatrix-state&quot;}">{"url_2":"/gp/media-matrix/fetch-DPX-expansion-data.html/ref=tmm_vnl_metabinding_expansion_0?ie=UTF8&amp;bindingCount=5&amp;landingAsin=B0000028RR&amp;currencyOfPreference=CAD&amp;websiteDisplayGroup=music_display_on_website&amp;asin=B009A9EYUO&amp;metabinding=vinyl_meta_binding&amp;metabindingIndex=2&amp;productTypeDefinition=ABIS_MUSIC","isAjaxInProgress_1":"0","url_1":"/gp/media-matrix/fetch-DPX-expansion-data.html/ref=tmm_acd_metabinding_expansion_0?ie=UTF8&amp;bindingCount=13&amp;landingAsin=B0000028RR&amp;currencyOfPreference=CAD&amp;websiteDisplayGroup=music_display_on_website&amp;asin=B016W63SAY&amp;metabinding=audio_cd_meta_binding&amp;metabindingIndex=1&amp;productTypeDefinition=ABIS_MUSIC","isAjaxInProgress_2":"0","isAjaxComplete_1":"0","isAjaxComplete_2":"0"}</script>





</div>
<div id="tmmSwatches" class="a-row nonJSFormats">



<!-- This file is a replica of swatches.jsp
The only difference we have introduced here is to use absolute paths
and dynamic includes
-->
<ul class="a-unordered-list a-nostyle a-button-list a-horizontal">















<li class="swatchElement selected"><span class="a-list-item">







<span class="a-button a-button-selected a-spacing-mini a-button-toggle format"><span class="a-button-inner"><a href="javascript:void(0)" class="a-button-text" role="button">




<span>Audio CD</span> <br/>


<span class="a-color-base">
















<span class="a-size-base a-color-price a-color-price">
$32.21
</span>













</span>





<div style="display:inline-block;">

</div>





</a></span></span>










<span class="tmm-olp-links">

</span>




























<!--
Dispaly logic: https://w.amazon.com/bin/view/DBS/Midas/UDP_Migration/ExternalFeatures/Comixology/
-->




<span class="tmm-olp-links">












<span class="olp-used olp-link">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;used&quot;,&quot;asin&quot;:&quot;B0000028RR&quot;}">
<a class="a-size-mini a-link-normal" href="/gp/offer-listing/B0000028RR/ref=tmm_acd_used_olp_0?ie=UTF8&amp;condition=used">

25 Used <span class="olp-from">from</span> $3.21

</a>
</span>



</span>


<span class="olp-new olp-link">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;new&quot;,&quot;asin&quot;:&quot;B0000028RR&quot;}">
<a class="a-size-mini a-link-normal" href="/gp/offer-listing/B0000028RR/ref=tmm_acd_new_olp_0?ie=UTF8&amp;condition=new">

4 New <span class="olp-from">from</span> $32.21

</a>
</span>



</span>











</span>








</span></li>


















<li class="swatchElement unselected"><span class="a-list-item">







<span class="a-button a-spacing-mini a-button-toggle format"><span class="a-button-inner"><a href="/Rage-Against-20thann-Vinyl-Machine/dp/B009A9EYUO/ref=tmm_vnl_swatch_0?_encoding=UTF8&amp;qid=&amp;sr=" class="a-button-text" role="button">




<span>LP Record</span> <br/>


<span class="a-color-secondary">
















<span class="a-size-base a-color-secondary">
$31.72
</span>













</span>





<div style="display:inline-block;">

</div>





</a></span></span>










<span class="tmm-olp-links">

</span>




























<!--
Dispaly logic: https://w.amazon.com/bin/view/DBS/Midas/UDP_Migration/ExternalFeatures/Comixology/
-->




<span class="tmm-olp-links">












<span class="olp-used olp-link">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;used&quot;,&quot;asin&quot;:&quot;B009A9EYUO&quot;}">
<a class="a-size-mini a-link-normal" href="/gp/offer-listing/B009A9EYUO/ref=tmm_vnl_used_olp_0?ie=UTF8&amp;condition=used">

1 Used <span class="olp-from">from</span> $32.28

</a>
</span>



</span>


<span class="olp-new olp-link">













<span class="a-declarative" data-action="show-all-offers-display" data-show-all-offers-display="{&quot;condition&quot;:&quot;new&quot;,&quot;asin&quot;:&quot;B009A9EYUO&quot;}">
<a class="a-size-mini a-link-normal" href="/gp/offer-listing/B009A9EYUO/ref=tmm_vnl_new_olp_0?ie=UTF8&amp;condition=new">

1 New <span class="olp-from">from</span> $31.72

</a>
</span>



</span>











</span>








</span></li>












</ul>




</div></div>





















</div>


















<div id="twisterPlusWWDesktop" class="celwidget" data-feature-name="twisterPlusWWDesktop">






























</div>


















<div id="productOverview_feature_div" class="celwidget" data-feature-name="productOverview">








































</div>


















<div id="promoPriceBlockMessage_feature_div" class="celwidget" data-feature-name="promoPriceBlockMessage">

















































</div>


















<div id="alternativeOfferEligibilityMessaging_feature_div" class="celwidget" data-feature-name="alternativeOfferEligibilityMessaging">















































<div class="a-section">



</div>
























</div>


















<div id="newerVersion_feature_div" class="celwidget" data-feature-name="newerVersion">




































</div>


















<div id="productAlert_feature_div" class="celwidget" data-feature-name="productAlert">

























</div>


















<div id="vendorPoweredCoupon_feature_div" class="celwidget" data-feature-name="vendorPoweredCoupon">



































</div>





</div>
<div id="hqpWrapper" class="centerColAlign centerColAlign-bbcxoverride">














<div id="translationNotice_feature_div" class="celwidget" data-feature-name="translationNotice">



































</div>


















<div id="edpIngress_feature_div" class="celwidget" data-feature-name="edpIngress">




































</div>


















<div id="heroQuickPromo_feature_div" class="celwidget" data-feature-name="heroQuickPromo">













      <div id="hero-quick-promo" class="a-row a-spacing-medium">
        
            <hr class="a-spacing-medium a-divider-normal">
        

















        




































<script>if (typeof uet === 'function' && typeof ues === 'function') {var scope = 'Detail_hero-quick-promo_Desktop';var placementId = '04675163-3598-46ab-a128-ea7d6f6019e4';ues('wb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); uet('bb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); if (placementId) {ues('wb', 'adplacements:' + placementId, {wb:1});uet('bb', 'adplacements:' + placementId, {wb:1});}}</script><div id="ape_Detail_hero-quick-promo_Desktop_placement" class="copilot-secure-display celwidget  text/x-dacx-safeframe" cel_widget_id="adplacements:Detail:hero-quick-promo:Desktop" data-csa-c-type="widget" data-csa-c-slot-id="adplacements:Detail:hero-quick-promo:Desktop" data-csa-c-content-id="04675163-3598-46ab-a128-ea7d6f6019e4" data-campaign="13305" style="max-width: 650px;margin: auto;margin-left:0px;" data-ad-details='{"slot" :"Detail_hero-quick-promo_Desktop","pageType": "Detail","subPageType":  "Desktop","slotName" :"hero-quick-promo","src" : "prefetchEnabled","adServer" :"cs","campaignId" :  "13305","arid" :"c8f4f1df4f47417385fcc2e02a731b10","placementId": "04675163-3598-46ab-a128-ea7d6f6019e4","size" :{"width": "100%","height" : "130px"},"allowedSizes" :[],"allowChangeSize":  true,"allowedDomains" :  [],"aanParams" :   "site%3Damazon.ca%3Bpt%3DDetail%3Bslot%3Dhero-quick-promo%3Bpid%3DB0000028RR%3Barid%3Dc8f4f1df4f47417385fcc2e02a731b10","loadAfter" :   "immediate","extraDelay" :  0,"iframeExtraStyle": "","iframeClass":  "","isCardsFlow": false,"adPixels": [],"aaxImpPixelUrl":  "https://aax-us-east.amazon-adsystem.com/e/xsp/imp?b=QqcPVrECfoN0V05z2nDmglgAAAF52TW6sQEAAAIBAVgLDqQ","aaxInstrPixelUrl": "https://aax-us-east.amazon-adsystem.com/x/px/QqcPVrECfoN0V05z2nDmglgAAAF52TW6sQEAAAIBAVgLDqQ/","htmlContentEncoded": "PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CiAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCI+CiAgICA8dGl0bGU+PC90aXRsZT4KICAgIDxzdHlsZT5AZm9udC1mYWNle2ZvbnQtZmFtaWx5OidBbWF6b24gRW1iZXInO3NyYzp1cmwoaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvQVVJQ2xpZW50cy9BbWF6b25VSUZvbnQtYW1hem9uZW1iZXJfcmctY2M3ZWJhYTA1YTJjZDNiMDJjMDkyOWFjMDQ3NWE0NGFiMzBiN2VmYS5fVjJfLndvZmYyKSBmb3JtYXQoIndvZmYyIiksdXJsKGh0dHBzOi8vbS5tZWRpYS1hbWF6b24uY29tL2ltYWdlcy9HLzAxL0FVSUNsaWVudHMvQW1hem9uVUlGb250LWFtYXpvbmVtYmVyX3JnLThhOWRiNDAyZDg5NjZhZTkzNzE3YzM0OGI5YWIwYmQwODcwM2E3YTcuX1YyXy53b2ZmKSBmb3JtYXQoIndvZmYiKX1AZm9udC1mYWNle2ZvbnQtZmFtaWx5OidBbWF6b24gRW1iZXInO2ZvbnQtc3R5bGU6aXRhbGljO3NyYzp1cmwoaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvQVVJQ2xpZW50cy9BbWF6b25VSUZvbnQtYW1hem9uZW1iZXJfcmdpdC05Y2MxYmI2NGViMjcwMTM1ZjFhZGYzYTQ4ODFjMmVlNWU3YzM3YmU1Ll9WMl8ud29mZjIpIGZvcm1hdCgid29mZjIiKSx1cmwoaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvQVVJQ2xpZW50cy9BbWF6b25VSUZvbnQtYW1hem9uZW1iZXJfcmdpdC1hNGRjOThkNjQ0ZmYyYWVkZDQxZGEzZGE0NjJmMDlmZmNlODZlYWZiLl9WMl8ud29mZikgZm9ybWF0KCJ3b2ZmIil9QGZvbnQtZmFjZXtmb250LWZhbWlseTonQW1hem9uIEVtYmVyJztmb250LXdlaWdodDo3MDA7c3JjOnVybChodHRwczovL20ubWVkaWEtYW1hem9uLmNvbS9pbWFnZXMvRy8wMS9BVUlDbGllbnRzL0FtYXpvblVJRm9udC1hbWF6b25lbWJlcl9iZC00NmI5MWJkYTY4MTYxYzE0ZTU1NGE3Nzk2NDNlZjQ5NTc0MzE5ODdiLl9WMl8ud29mZjIpIGZvcm1hdCgid29mZjIiKSx1cmwoaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvQVVJQ2xpZW50cy9BbWF6b25VSUZvbnQtYW1hem9uZW1iZXJfYmQtYjYwNTI1MmY4N2I4YjNkZjVhZTIwNjU5NmRhYzA5MzhmYzU4ODhiYy5fVjJfLndvZmYpIGZvcm1hdCgid29mZiIpfUBmb250LWZhY2V7Zm9udC1mYW1pbHk6J0FtYXpvbiBFbWJlcic7Zm9udC1zdHlsZTppdGFsaWM7Zm9udC13ZWlnaHQ6NzAwO3NyYzp1cmwoaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvQVVJQ2xpZW50cy9BbWF6b25VSUZvbnQtYW1hem9uZW1iZXJfYmRpdC04MGZmN2FiYTM3ZGQxZmY1YTZiOTAyMzNhMTllM2E3ODBhOTZkYzJmLl9WMl8ud29mZjIpIGZvcm1hdCgid29mZjIiKSx1cmwoaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvQVVJQ2xpZW50cy9BbWF6b25VSUZvbnQtYW1hem9uZW1iZXJfYmRpdC01NzU5OGNlNDI2YTYxMmJlNWExZDE1ZWVlMDgyNTI2NjhmY2E1ZTdhLl9WMl8ud29mZikgZm9ybWF0KCJ3b2ZmIil9CgouZmFkZUluey13ZWJraXQtYW5pbWF0aW9uOmFuaW1hdGVJbiAxcyAxIGZvcndhcmRzO2FuaW1hdGlvbjphbmltYXRlSW4gMXMgMSBmb3J3YXJkc30uZmFkZU91dHstd2Via2l0LWFuaW1hdGlvbjphbmltYXRlT3V0IDFzIDEgZm9yd2FyZHM7YW5pbWF0aW9uOmFuaW1hdGVPdXQgMXMgMSBmb3J3YXJkc30KCiNhZCwjZGl2LWdwdC1hZCxib2R5LGh0bWx7bWFyZ2luOjA7Zm9udC1mYW1pbHk6J0FtYXpvbiBFbWJlcicsYXJpYWwsc2Fucy1zZXJpZjtib3gtc2l6aW5nOmJvcmRlci1ib3g7LW1vei1ib3gtc2l6aW5nOmJvcmRlci1ib3g7LXdlYmtpdC1ib3gtc2l6aW5nOmJvcmRlci1ib3g7Zm9udC1zaXplOjEzcHg7bGluZS1oZWlnaHQ6MThweDt3aWR0aDoxMDAlO2hlaWdodDoxMDAlfQoKLmZsZXgtY29udGFpbmVye2Rpc3BsYXk6LXdlYmtpdC1ib3g7ZGlzcGxheTotbXMtZmxleGJveDtkaXNwbGF5Oi13ZWJraXQtZmxleDtkaXNwbGF5OmZsZXh9LmZsZXgtZGlyZWN0aW9uLXJvd3stbXMtZmxleC1kaXJlY3Rpb246cm93O2ZsZXgtZGlyZWN0aW9uOnJvd30uZmxleC1kaXJlY3Rpb24tY29sdW1uey1tcy1mbGV4LWRpcmVjdGlvbjpjb2x1bW47ZmxleC1kaXJlY3Rpb246Y29sdW1ufS5mbGV4LXdyYXB7LW1zLWZsZXgtd3JhcDp3cmFwO2ZsZXgtd3JhcDp3cmFwfS5mbGV4LW5vd3JhcHstbXMtZmxleC13cmFwOm5vbmU7LW1zLWZsZXgtd3JhcDpub3dyYXA7ZmxleC13cmFwOm5vd3JhcH0uZmxleC1hbGlnbi1zdGFydHstbXMtZmxleC1hbGlnbjpzdGFydDthbGlnbi1pdGVtczpmbGV4LXN0YXJ0fS5mbGV4LWFsaWduLWNlbnRlcnstbXMtZmxleC1hbGlnbjpjZW50ZXI7YWxpZ24taXRlbXM6Y2VudGVyfS5mbGV4LWFsaWduLWJhc2VsaW5ley1tcy1mbGV4LWFsaWduOmJhc2VsaW5lO2FsaWduLWl0ZW1zOmJhc2VsaW5lfS5mbGV4LWFsaWduLWVuZHstbXMtZmxleC1hbGlnbjplbmQ7YWxpZ24taXRlbXM6ZmxleC1lbmR9LmZsZXgtanVzdGlmeS1zdGFydHstbXMtZmxleC1wYWNrOnN0YXJ0O2p1c3RpZnktY29udGVudDpmbGV4LXN0YXJ0fS5mbGV4LWp1c3RpZnktY2VudGVyey1tcy1mbGV4LXBhY2s6Y2VudGVyO2p1c3RpZnktY29udGVudDpjZW50ZXJ9LmZsZXgtanVzdGlmeS1zcGFjZS1iZXR3ZWVuey1tcy1mbGV4LXBhY2s6anVzdGlmeTtqdXN0aWZ5LWNvbnRlbnQ6c3BhY2UtYmV0d2Vlbn0uZmxleC1qdXN0aWZ5LXNwYWNlLWFyb3VuZHstbXMtZmxleC1wYWNrOmp1c3RpZnk7anVzdGlmeS1jb250ZW50OnNwYWNlLWFyb3VuZH0uZmxleC1qdXN0aWZ5LWVuZHstbXMtZmxleC1wYWNrOmVuZDtqdXN0aWZ5LWNvbnRlbnQ6ZmxleC1lbmR9LmZsZXgtZ3Jvdy0xey13ZWJraXQtZmxleC1ncm93OjE7ZmxleC1ncm93OjF9LmZsZXgtZ3Jvdy0wLTE1ey13ZWJraXQtZmxleC1ncm93Oi4xNTtmbGV4LWdyb3c6LjE1fS5mbGV4LXNocmluay0wey13ZWJraXQtZmxleC1zaHJpbms6MDtmbGV4LXNocmluazowfQoKLmltYWdlLXdpdGgtYmFkZ2V7bWFyZ2luLXRvcDoyMHB4fS5idXktYm94e21pbi13aWR0aDoxNDBweH0ucHJvZHVjdC10aXRsZS1zbWFsbHttYXgtaGVpZ2h0OjQwcHghaW1wb3J0YW50fS5pbWFnZS13cmFwcGVye3dpZHRoOjE0MHB4O2hlaWdodDoxMTBweH0uaW1hZ2Utd2l0aC1iYWRnZSAuaW1hZ2Utd3JhcHBlcntoZWlnaHQ6OTBweH0ucHJvZHVjdC1icmFuZC13cmFwcGVye2ZsZXgtc2hyaW5rOjB9QG1lZGlhIG9ubHkgc2NyZWVuIGFuZCAobWF4LXdpZHRoOjM0MHB4KXsuYW5jaG9yZWQtYmFkZ2UsLnhzLWNvbmRlbnNlZD46bm90KC54cy1zaG93KXtkaXNwbGF5Om5vbmUhaW1wb3J0YW50fS5wcm9kdWN0LXRpdGxlLC5wcm9kdWN0LXRpdGxlLXNtYWxse21heC1oZWlnaHQ6ODBweCFpbXBvcnRhbnR9LmltYWdlLXdpdGgtYmFkZ2V7bWFyZ2luLXRvcDowfS5pbWFnZS13aXRoLWJhZGdlIC5pbWFnZS13cmFwcGVyLC5pbWFnZS13cmFwcGVye3dpZHRoOjgwcHg7aGVpZ2h0OjExMHB4fS5idXktYm94e21pbi13aWR0aDphdXRvO3dpZHRoOmF1dG99fUBtZWRpYSBvbmx5IHNjcmVlbiBhbmQgKG1heC13aWR0aDoyNjBweCl7LmJ1eS1ib3h7bWluLXdpZHRoOmF1dG87d2lkdGg6YXV0b30uaW1hZ2Utd2l0aC1iYWRnZSAuaW1hZ2Utd3JhcHBlciwuaW1hZ2Utd3JhcHBlcnt3aWR0aDo2MHB4O2hlaWdodDoxMTBweH19PC9zdHlsZT4KICAgIAo8L2hlYWQ+Cjxib2R5PgoKPHNjcmlwdD4KICAgIHZhciBQZXJmb3JtYW5jZUV2ZW50TWFuYWdlcj1mdW5jdGlvbihlKXt2YXIgdD17fTtmdW5jdGlvbiBuKHIpe2lmKHRbcl0pcmV0dXJuIHRbcl0uZXhwb3J0czt2YXIgbz10W3JdPXtpOnIsbDohMSxleHBvcnRzOnt9fTtyZXR1cm4gZVtyXS5jYWxsKG8uZXhwb3J0cyxvLG8uZXhwb3J0cyxuKSxvLmw9ITAsby5leHBvcnRzfXJldHVybiBuLm09ZSxuLmM9dCxuLmQ9ZnVuY3Rpb24oZSx0LHIpe24ubyhlLHQpfHxPYmplY3QuZGVmaW5lUHJvcGVydHkoZSx0LHtlbnVtZXJhYmxlOiEwLGdldDpyfSl9LG4ucj1mdW5jdGlvbihlKXsidW5kZWZpbmVkIiE9dHlwZW9mIFN5bWJvbCYmU3ltYm9sLnRvU3RyaW5nVGFnJiZPYmplY3QuZGVmaW5lUHJvcGVydHkoZSxTeW1ib2wudG9TdHJpbmdUYWcse3ZhbHVlOiJNb2R1bGUifSksT2JqZWN0LmRlZmluZVByb3BlcnR5KGUsIl9fZXNNb2R1bGUiLHt2YWx1ZTohMH0pfSxuLnQ9ZnVuY3Rpb24oZSx0KXtpZigxJnQmJihlPW4oZSkpLDgmdClyZXR1cm4gZTtpZig0JnQmJiJvYmplY3QiPT10eXBlb2YgZSYmZSYmZS5fX2VzTW9kdWxlKXJldHVybiBlO3ZhciByPU9iamVjdC5jcmVhdGUobnVsbCk7aWYobi5yKHIpLE9iamVjdC5kZWZpbmVQcm9wZXJ0eShyLCJkZWZhdWx0Iix7ZW51bWVyYWJsZTohMCx2YWx1ZTplfSksMiZ0JiYic3RyaW5nIiE9dHlwZW9mIGUpZm9yKHZhciBvIGluIGUpbi5kKHIsbyxmdW5jdGlvbih0KXtyZXR1cm4gZVt0XX0uYmluZChudWxsLG8pKTtyZXR1cm4gcn0sbi5uPWZ1bmN0aW9uKGUpe3ZhciB0PWUmJmUuX19lc01vZHVsZT9mdW5jdGlvbigpe3JldHVybiBlLmRlZmF1bHR9OmZ1bmN0aW9uKCl7cmV0dXJuIGV9O3JldHVybiBuLmQodCwiYSIsdCksdH0sbi5vPWZ1bmN0aW9uKGUsdCl7cmV0dXJuIE9iamVjdC5wcm90b3R5cGUuaGFzT3duUHJvcGVydHkuY2FsbChlLHQpfSxuLnA9IiIsbihuLnM9NSl9KHswOmZ1bmN0aW9uKGUsdCxuKXsidXNlIHN0cmljdCI7T2JqZWN0LmRlZmluZVByb3BlcnR5KHQsIl9fZXNNb2R1bGUiLHt2YWx1ZTohMH0pLHQuZGVmYXVsdD10LlZJU1VBTF9DT01QTEVURU5FU1NfTEFURU5DWT10LkNSRUFUSVZFX0xPQURfTEFURU5DWT10LlVOQ0FVR0hUX0VSUk9SPXZvaWQgMDtjb25zdCByPSJ1bmNhdWdodEVycm9yIjt0LlVOQ0FVR0hUX0VSUk9SPXI7Y29uc3Qgbz0iY3JlYXRpdmVMb2FkTGF0ZW5jeSI7dC5DUkVBVElWRV9MT0FEX0xBVEVOQ1k9bztjb25zdCBpPSJ2aXN1YWxDb21wbGV0ZW5lc3NMYXRlbmN5Ijt0LlZJU1VBTF9DT01QTEVURU5FU1NfTEFURU5DWT1pLHQuZGVmYXVsdD1jbGFzc3tjb25zdHJ1Y3RvcihlKXtpZih0aGlzLmV2ZW50cz17dW5jYXVnaHRFcnJvcjp7fX0sdGhpcy50aW1lcnM9e30sdGhpcy5vbk5ld0Vycm9yPWZ1bmN0aW9uKCl7fSx0aGlzLndpbmRvdz1lJiZlLndpbmRvd3x8InVuZGVmaW5lZCIhPXR5cGVvZiB3aW5kb3cmJndpbmRvdywhdGhpcy53aW5kb3d8fCF0aGlzLndpbmRvdy5kb2N1bWVudCl0aHJvdyBuZXcgRXJyb3IoIldpbmRvdyBhbmQvb3IgZG9jdW1lbnQgaXMgbm90IGRlZmluZWQiKTt0aGlzLnRyYWNrTG9hZExhdGVuY3koKSx0aGlzLnRyYWNrVmlzdWFsQ29tcGxldGVuZXNzTGF0ZW5jeSgpLHRoaXMuYWRkRXJyb3JMaXN0ZW5lcigpfXRyYWNrTG9hZExhdGVuY3koKXt0aGlzLnRpbWVyc1tvXT1uZXcgRGF0ZX10cmFja1Zpc3VhbENvbXBsZXRlbmVzc0xhdGVuY3koKXt0aGlzLnRpbWVyc1tpXT1uZXcgRGF0ZX1hZGRFcnJvckxpc3RlbmVyKCl7Y29uc3QgZT10aGlzLmV2ZW50c1tyXTt0aGlzLmFkZExpc3RlbmVyKHRoaXMud2luZG93LCJlcnJvciIsdD0+e2xldCBuPXQubWVzc2FnZTtpZih0LmVycm9yJiZ0LmVycm9yLnN0YWNrKXtjb25zdCBlPXQubWVzc2FnZSsiIDogIit0LmVycm9yLnN0YWNrO249ZS5sZW5ndGg8NTAwP2U6ZS5zdWJzdHJpbmcoMCw1MDApfXZvaWQgMD09PWVbbl0mJihlW25dPSEwLHRoaXMub25OZXdFcnJvcihuKSl9KX1hZGRMaXN0ZW5lcihlLHQsbil7Y29uc3Qgcj1mdW5jdGlvbihlPXdpbmRvdy5ldmVudCl7cmV0dXJuIG4oZSl9O2lmKGUuYWRkRXZlbnRMaXN0ZW5lcillLmFkZEV2ZW50TGlzdGVuZXIodCxyLCEwKTtlbHNlIGlmKHQ9Im9uIit0LGUuYXR0YWNoRXZlbnQpZS5hdHRhY2hFdmVudCh0LHIpO2Vsc2V7Y29uc3Qgbj1lW3RdO2VbdF09ZnVuY3Rpb24oKXtyLmFwcGx5KHRoaXMsYXJndW1lbnRzKSwiZnVuY3Rpb24iPT10eXBlb2YgbiYmbi5hcHBseSh0aGlzLGFyZ3VtZW50cyl9fX19fSw1OmZ1bmN0aW9uKGUsdCxuKXtlLmV4cG9ydHM9bigwKX19KTs7CiAgICB2YXIgcGVyZm9ybWFuY2VFdmVudE1hbmFnZXIgPSBuZXcgUGVyZm9ybWFuY2VFdmVudE1hbmFnZXIuZGVmYXVsdCgpOwogICAgCjwvc2NyaXB0Pgo8ZGl2IGlkPSJhZCI+PGRpdiByb2xlPSJsaW5rIiBhcmlhLWxhYmVsPSJTcG9uc29yZWQgQWQKSG93IHRvIFBsYXkgdGhlIEhhcm1vbmljYTogQSBDb21wbGV0ZSBHdWlkZSBmb3IgQmVnaW5uZXJzIC0gQ2hyb21hdGljIGFuZCBEaWF0b25pYyBIYXJtb25pY2EKNC4yIG91dCBvZiA1IHN0YXJzLgoxNTEgY3VzdG9tZXIgcmV2aWV3cy4iICBzdHlsZT0id2lkdGg6MTAwJTtoZWlnaHQ6MTAwJSI+PGRpdiBzdHlsZT0ib3ZlcmZsb3c6aGlkZGVuO3dpZHRoOjEwMCU7aGVpZ2h0OjEwMCUiIGNsYXNzPSIiPjxkaXYgY2xhc3M9ImZsZXgtY29udGFpbmVyCiAgICAgICAgICAgICAgICBmbGV4LWRpcmVjdGlvbi1yb3cKICAgICAgICAgICAgICAgICAgICAgICBmbGV4LWp1c3RpZnktZW5kCiAgICAgICAgICAgICAgICAgICAgICAgZmxleC1hbGlnbi1jZW50ZXIiIHN0eWxlPSJwb3NpdGlvbjpyZWxhdGl2ZTtvdmVyZmxvdzpoaWRkZW47dG9wOjA7bGVmdDowO3dpZHRoOjEwMCU7aGVpZ2h0OjEwMCU7YmFja2dyb3VuZC1jb2xvcjojZmZmO2JvcmRlcjoxcHggc29saWQgI2NjYztib3gtc2l6aW5nOmJvcmRlci1ib3g7cGFkZGluZzoxMHB4IDIwcHg7bWF4LXdpZHRoOjUwMHB4Ij48ZGl2IGNsYXNzPSJmbGV4LWNvbnRhaW5lciBmbGV4LWRpcmVjdGlvbi1jb2x1bW4gcHJvZHVjdC1icmFuZC13cmFwcGVyIGZsZXgtYWxpZ24tY2VudGVyIGZsZXgtanVzdGlmeS1jZW50ZXIgIj48ZGl2IGNsYXNzPSJmbGV4LWNvbnRhaW5lciBmbGV4LWRpcmVjdGlvbi1yb3cgZmxleC1ncm93LTEgZmxleC1qdXN0aWZ5LWNlbnRlciIgc3R5bGU9Im92ZXJmbG93OmhpZGRlbiI+PGRpdiBjbGFzcz0iZmxleC1jb250YWluZXIgZmxleC1hbGlnbi1jZW50ZXIgZmxleC1qdXN0aWZ5LWNlbnRlciBpbWFnZS13cmFwcGVyIj48aW1nIGFsdD0iIiBhcmlhLWhpZGRlbj0idHJ1ZSIgc3JjPSJodHRwczovL20ubWVkaWEtYW1hem9uLmNvbS9pbWFnZXMvSS82MXpaK2pia2RRTC5fQUNfU1gxNDBfU1kxMDhfLmpwZyIgc3R5bGU9Im1heC13aWR0aDoxMDAlO21heC1oZWlnaHQ6MTAwJSIvPjwvZGl2PjwvZGl2PjwvZGl2PjxkaXYgc3R5bGU9Im1heC1oZWlnaHQ6MjAwcHg7ZmxleC1kaXJlY3Rpb246Y29sdW1uO3BhZGRpbmc6MCAwIDAgMjBweDtwb3NpdGlvbjpzdGF0aWM7Ym90dG9tOmF1dG87cmlnaHQ6MDtiYWNrZ3JvdW5kOiNmZmY7b3ZlcmZsb3c6aGlkZGVuIiBjbGFzcz0iZmxleC1jb250YWluZXIgZmxleC1qdXN0aWZ5LWNlbnRlciBidXktYm94Ij48ZGl2IGNsYXNzPSJmbGV4LWNvbnRhaW5lciBmbGV4LWRpcmVjdGlvbi1jb2x1bW4geHMtY29uZGVuc2VkICI+PGRpdiBjbGFzcz0ieHMtc2hvdyI+PGRpdiBzdHlsZT0iY29sb3I6IzExMTExMTtmb250LXNpemU6MTRweDtmb250LXdlaWdodDo0MDA7ZmxleC1zaHJpbms6MDtoZWlnaHQ6YXV0bztsaW5lLWhlaWdodDoxOXB4O21heC1oZWlnaHQ6NjBweDttYXJnaW4tYm90dG9tOjA7b3ZlcmZsb3c6aGlkZGVuO3dvcmQtd3JhcDpicmVhay13b3JkIiBjbGFzcz0icHJvZHVjdC10aXRsZSI+PHNwYW4+SG93IHRvIFBsYXkgdGhlIEhhcm1vbmljYTogQSBDb21wbGV0ZSBHdWlkZSBmb3IgQmVnaW5uZXJzIC0gQ2hyb21hdGljIGFuZCBEaWF0b25pYyBIYXJtb25pY2E8L3NwYW4+PC9kaXY+PC9kaXY+PGRpdiBjbGFzcz0iZmxleC1jb250YWluZXIgZmxleC1kaXJlY3Rpb24tcm93IGZsZXgtbm93cmFwIGZsZXgtYWxpZ24tZW5kIGZsZXgtanVzdGlmeS1zcGFjZS1iZXR3ZWVuIGZsZXgtc2hyaW5rLTAgeHMtc2hvdyI+PGRpdiBzdHlsZT0iLW1zLWZsZXg6MCAxIDEwMCU7ZmxleC1ncm93OjA7ZmxleC1zaHJpbms6MTtkaXNwbGF5OmlubGluZS1ibG9jayIgY2xhc3M9IiB4cy1jb25kZW5zZWQiPjxhIGNsYXNzPSJmbGV4LWNvbnRhaW5lciIgYXJpYS1sYWJlbGxlZEJ5PSJhZCIgc3R5bGU9ImJhY2tncm91bmQ6dHJhbnNwYXJlbnQgdXJsKCZxdW90O2h0dHBzOi8vbS5tZWRpYS1hbWF6b24uY29tL2ltYWdlcy9HLzAxL2QxNmcva3B3L3RyYW5zcGFyZW50LTF4MS5wbmcmcXVvdDspIHJlcGVhdCAwIDA7Ym90dG9tOjA7Y3Vyc29yOnBvaW50ZXI7bGVmdDowO3Bvc2l0aW9uOnJlbGF0aXZlO3JpZ2h0OjA7dG9wOjA7ei1pbmRleDoxMDAwO3RleHQtZGVjb3JhdGlvbjpub25lIiBocmVmPSJodHRwczovL2FheC11cy1lYXN0LmFtYXpvbi1hZHN5c3RlbS5jb20veC9jL1FxY1BWckVDZm9OMFYwNXoybkRtZ2xnQUFBRjUyVFc2c1FFQUFBSUJBVmdMRHFRL2h0dHA6Ly93d3cuYW1hem9uLmNhL2dwL3NscmVkaXJlY3QvcGljYXNzb1JlZGlyZWN0Lmh0bWw/aWU9VVRGOCZhbXA7YWRJZD1BMDcyMDQyNTFOMjgzVDE5NjNUUEwmYW1wO3F1YWxpZmllcj0xNjIyODQ2ODQ3JmFtcDtpZD00MTM1ODIwODU5ODk5MjcmYW1wO3dpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYW1wO3VybD0lMkZkcCUyRjE3OTMzNjE4NDMlMkZyZWYlM0RzeW5fc2Rfb25zaXRlX2Rlc2t0b3BfMTQlM0Zwc2MlM0QxJTI2dWhfaXQlM0QwZTZiMWRlY2ZhMTY3NzU3YWViZGFiN2YwY2NjNDlmZV9DVCZhbXA7dWhfaXQ9MGU2YjFkZWNmYTE2Nzc1N2FlYmRhYjdmMGNjYzQ5ZmVfQ1QiIHRhcmdldD0iX3RvcCI+PGRpdiBjbGFzcz0ic3RhclJhdGluZ1dyYXBwZXIiIHN0eWxlPSJmb250LXNpemU6dW5zZXQ7bGluZS1oZWlnaHQ6MTtwYWRkaW5nLWJvdHRvbTo0cHg7cGFkZGluZy10b3A6NHB4IiBhcmlhLWhpZGRlbj0idHJ1ZSI+PGRpdj48ZGl2IHN0eWxlPSJiYWNrZ3JvdW5kLXJlcGVhdDpuby1yZXBlYXQ7YmFja2dyb3VuZC1zaXplOjM0NHB4IDE1cHg7ZGlzcGxheTppbmxpbmUtYmxvY2s7dmVydGljYWwtYWxpZ246bWlkZGxlO2hlaWdodDoxNnB4O3dpZHRoOjgwcHg7YmFja2dyb3VuZC1pbWFnZTp1cmwoJnF1b3Q7aHR0cHM6Ly9pbWFnZXMtbmEuc3NsLWltYWdlcy1hbWF6b24uY29tL2ltYWdlcy9HLzE1L2RhL2NyZWF0aXZlcy9hdWktbWluaS1zcHJpdGUtMjAxNS0wMi5wbmcmcXVvdDspO2JhY2tncm91bmQtcG9zaXRpb246LTE2cHggMHB4Ij48L2Rpdj48c3BhbiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2lkdGg6MC4zODVlbSI+PC9zcGFuPjxzcGFuIGNvbG9yPSJ0ZXJ0aWFyeSIgc3R5bGU9ImZvbnQtc2l6ZToxMnB4O2xpbmUtaGVpZ2h0OjE7Y29sb3I6IzU1NTtkaXNwbGF5OmlubGluZTt2ZXJ0aWNhbC1hbGlnbjptaWRkbGUiIGFyaWEtaGlkZGVuPSJ0cnVlIj4xNTE8L3NwYW4+PC9kaXY+PGRpdj48L2Rpdj48L2Rpdj48L2E+PGRpdiBzdHlsZT0iYWxpZ24tY29udGVudDpmbGV4LXN0YXJ0O2ZsZXgtd3JhcDp3cmFwO2xpbmUtaGVpZ2h0Om5vcm1hbDt3aWR0aDoxMDAlO21hcmdpbi1ib3R0b206MCIgY2xhc3M9IiB4cy1zaG93Ij48ZGl2IGNsYXNzPSJmbGV4LWNvbnRhaW5lciBmbGV4LWRpcmVjdGlvbi1yb3cgZmxleC1hbGlnbi1iYXNlbGluZSBmbGV4LWp1c3RpZnktc3RhcnQgZmxleC13cmFwIHhzLWNvbmRlbnNlZCI+PHNwYW4gc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO21hcmdpbi1yaWdodDo0cHg7bWFyZ2luLWJvdHRvbTotMnB4O3dpZHRoOm1heC1jb250ZW50Ij48c3BhbiBjbGFzcz0iIiBzdHlsZT0iY29sb3I6IzU1NTtsaW5lLWhlaWdodDpub3JtYWw7Zm9udC1zaXplOjhweDt2ZXJ0aWNhbC1hbGlnbjp0b3A7cGFkZGluZy1yaWdodDoxcHgiPiQ8L3NwYW4+PHNwYW4gY2xhc3M9IiIgc3R5bGU9ImZvbnQtc2l6ZToxNHB4O2NvbG9yOiM1NTU7bGluZS1oZWlnaHQ6MSI+MTAuNDQ8L3NwYW4+PC9zcGFuPjwvZGl2PjwvZGl2PjwvZGl2PjwvZGl2PjwvZGl2PjwvZGl2PjxhIGFyaWEtbGFiZWxsZWRCeT0iYWQiIHN0eWxlPSJiYWNrZ3JvdW5kOnRyYW5zcGFyZW50IHVybCgmcXVvdDtodHRwczovL20ubWVkaWEtYW1hem9uLmNvbS9pbWFnZXMvRy8wMS9kMTZnL2twdy90cmFuc3BhcmVudC0xeDEucG5nJnF1b3Q7KSByZXBlYXQgMCAwO2JvdHRvbTowO2N1cnNvcjpwb2ludGVyO2xlZnQ6MDtwb3NpdGlvbjphYnNvbHV0ZTtyaWdodDowO3RvcDowO3otaW5kZXg6NTAwIiBocmVmPSJodHRwczovL2FheC11cy1lYXN0LmFtYXpvbi1hZHN5c3RlbS5jb20veC9jL1FxY1BWckVDZm9OMFYwNXoybkRtZ2xnQUFBRjUyVFc2c1FFQUFBSUJBVmdMRHFRL2h0dHA6Ly93d3cuYW1hem9uLmNhL2dwL3NscmVkaXJlY3QvcGljYXNzb1JlZGlyZWN0Lmh0bWw/aWU9VVRGOCZhbXA7YWRJZD1BMDcyMDQyNTFOMjgzVDE5NjNUUEwmYW1wO3F1YWxpZmllcj0xNjIyODQ2ODQ3JmFtcDtpZD00MTM1ODIwODU5ODk5MjcmYW1wO3dpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYW1wO3VybD0lMkZkcCUyRjE3OTMzNjE4NDMlMkZyZWYlM0RzeW5fc2Rfb25zaXRlX2Rlc2t0b3BfMTQlM0Zwc2MlM0QxJTI2dWhfaXQlM0QwZTZiMWRlY2ZhMTY3NzU3YWViZGFiN2YwY2NjNDlmZV9DVCZhbXA7dWhfaXQ9MGU2YjFkZWNmYTE2Nzc1N2FlYmRhYjdmMGNjYzQ5ZmVfQ1QiIHRhcmdldD0iX3RvcCI+PC9hPjwvZGl2PjwvZGl2PjwvZGl2PjwvZGl2Pgo8c2NyaXB0PnZhciBhcnJheVByb3RvdHlwZUluY2x1ZGVzPWZ1bmN0aW9uKGUpe3ZhciByPXt9O2Z1bmN0aW9uIHQobil7aWYocltuXSlyZXR1cm4gcltuXS5leHBvcnRzO3ZhciBvPXJbbl09e2k6bixsOiExLGV4cG9ydHM6e319O3JldHVybiBlW25dLmNhbGwoby5leHBvcnRzLG8sby5leHBvcnRzLHQpLG8ubD0hMCxvLmV4cG9ydHN9cmV0dXJuIHQubT1lLHQuYz1yLHQuZD1mdW5jdGlvbihlLHIsbil7dC5vKGUscil8fE9iamVjdC5kZWZpbmVQcm9wZXJ0eShlLHIse2VudW1lcmFibGU6ITAsZ2V0Om59KX0sdC5yPWZ1bmN0aW9uKGUpeyJ1bmRlZmluZWQiIT10eXBlb2YgU3ltYm9sJiZTeW1ib2wudG9TdHJpbmdUYWcmJk9iamVjdC5kZWZpbmVQcm9wZXJ0eShlLFN5bWJvbC50b1N0cmluZ1RhZyx7dmFsdWU6Ik1vZHVsZSJ9KSxPYmplY3QuZGVmaW5lUHJvcGVydHkoZSwiX19lc01vZHVsZSIse3ZhbHVlOiEwfSl9LHQudD1mdW5jdGlvbihlLHIpe2lmKDEmciYmKGU9dChlKSksOCZyKXJldHVybiBlO2lmKDQmciYmIm9iamVjdCI9PXR5cGVvZiBlJiZlJiZlLl9fZXNNb2R1bGUpcmV0dXJuIGU7dmFyIG49T2JqZWN0LmNyZWF0ZShudWxsKTtpZih0LnIobiksT2JqZWN0LmRlZmluZVByb3BlcnR5KG4sImRlZmF1bHQiLHtlbnVtZXJhYmxlOiEwLHZhbHVlOmV9KSwyJnImJiJzdHJpbmciIT10eXBlb2YgZSlmb3IodmFyIG8gaW4gZSl0LmQobixvLGZ1bmN0aW9uKHIpe3JldHVybiBlW3JdfS5iaW5kKG51bGwsbykpO3JldHVybiBufSx0Lm49ZnVuY3Rpb24oZSl7dmFyIHI9ZSYmZS5fX2VzTW9kdWxlP2Z1bmN0aW9uKCl7cmV0dXJuIGUuZGVmYXVsdH06ZnVuY3Rpb24oKXtyZXR1cm4gZX07cmV0dXJuIHQuZChyLCJhIixyKSxyfSx0Lm89ZnVuY3Rpb24oZSxyKXtyZXR1cm4gT2JqZWN0LnByb3RvdHlwZS5oYXNPd25Qcm9wZXJ0eS5jYWxsKGUscil9LHQucD0iIix0KHQucz0wKX0oW2Z1bmN0aW9uKGUscix0KXtlLmV4cG9ydHM9dCgxKX0sZnVuY3Rpb24oZSxyLHQpeyJ1c2Ugc3RyaWN0IjtBcnJheS5wcm90b3R5cGUuaW5jbHVkZXN8fChBcnJheS5wcm90b3R5cGUuaW5jbHVkZXM9ZnVuY3Rpb24oZSl7aWYobnVsbD09dGhpcyl0aHJvdyBuZXcgVHlwZUVycm9yKCJBcnJheS5wcm90b3R5cGUuaW5jbHVkZXMgY2FsbGVkIG9uIG51bGwgb3IgdW5kZWZpbmVkIik7dmFyIHI9T2JqZWN0KHRoaXMpLHQ9cGFyc2VJbnQoci5sZW5ndGgsMTApfHwwO2lmKDA9PT10KXJldHVybiExO3ZhciBuLG89cGFyc2VJbnQoYXJndW1lbnRzWzFdLDEwKXx8MDtsZXQgdTtmb3IoMDw9bz91PW86KHU9dCtvLHU8MCYmKHU9MCkpO3U8dDspe2lmKGU9PT0obj1yW3VdKXx8ZSE9ZSYmbiE9bilyZXR1cm4hMDt1Kyt9cmV0dXJuITF9KX1dKTsKCnZhciBvYmplY3RBc3NpZ249ZnVuY3Rpb24oZSl7dmFyIHQ9e307ZnVuY3Rpb24gbihyKXtpZih0W3JdKXJldHVybiB0W3JdLmV4cG9ydHM7dmFyIG89dFtyXT17aTpyLGw6ITEsZXhwb3J0czp7fX07cmV0dXJuIGVbcl0uY2FsbChvLmV4cG9ydHMsbyxvLmV4cG9ydHMsbiksby5sPSEwLG8uZXhwb3J0c31yZXR1cm4gbi5tPWUsbi5jPXQsbi5kPWZ1bmN0aW9uKGUsdCxyKXtuLm8oZSx0KXx8T2JqZWN0LmRlZmluZVByb3BlcnR5KGUsdCx7ZW51bWVyYWJsZTohMCxnZXQ6cn0pfSxuLnI9ZnVuY3Rpb24oZSl7InVuZGVmaW5lZCIhPXR5cGVvZiBTeW1ib2wmJlN5bWJvbC50b1N0cmluZ1RhZyYmT2JqZWN0LmRlZmluZVByb3BlcnR5KGUsU3ltYm9sLnRvU3RyaW5nVGFnLHt2YWx1ZToiTW9kdWxlIn0pLE9iamVjdC5kZWZpbmVQcm9wZXJ0eShlLCJfX2VzTW9kdWxlIix7dmFsdWU6ITB9KX0sbi50PWZ1bmN0aW9uKGUsdCl7aWYoMSZ0JiYoZT1uKGUpKSw4JnQpcmV0dXJuIGU7aWYoNCZ0JiYib2JqZWN0Ij09dHlwZW9mIGUmJmUmJmUuX19lc01vZHVsZSlyZXR1cm4gZTt2YXIgcj1PYmplY3QuY3JlYXRlKG51bGwpO2lmKG4ucihyKSxPYmplY3QuZGVmaW5lUHJvcGVydHkociwiZGVmYXVsdCIse2VudW1lcmFibGU6ITAsdmFsdWU6ZX0pLDImdCYmInN0cmluZyIhPXR5cGVvZiBlKWZvcih2YXIgbyBpbiBlKW4uZChyLG8sZnVuY3Rpb24odCl7cmV0dXJuIGVbdF19LmJpbmQobnVsbCxvKSk7cmV0dXJuIHJ9LG4ubj1mdW5jdGlvbihlKXt2YXIgdD1lJiZlLl9fZXNNb2R1bGU/ZnVuY3Rpb24oKXtyZXR1cm4gZS5kZWZhdWx0fTpmdW5jdGlvbigpe3JldHVybiBlfTtyZXR1cm4gbi5kKHQsImEiLHQpLHR9LG4ubz1mdW5jdGlvbihlLHQpe3JldHVybiBPYmplY3QucHJvdG90eXBlLmhhc093blByb3BlcnR5LmNhbGwoZSx0KX0sbi5wPSIiLG4obi5zPTIpfShbLCxmdW5jdGlvbihlLHQsbil7ZS5leHBvcnRzPW4oMyl9LGZ1bmN0aW9uKGUsdCxuKXsidXNlIHN0cmljdCI7ImZ1bmN0aW9uIiE9dHlwZW9mIE9iamVjdC5hc3NpZ24mJihPYmplY3QuYXNzaWduPWZ1bmN0aW9uKGUpe2lmKG51bGw9PWUpdGhyb3cgbmV3IFR5cGVFcnJvcigiQ2Fubm90IGNvbnZlcnQgdW5kZWZpbmVkIG9yIG51bGwgdG8gb2JqZWN0Iik7Y29uc3QgdD1PYmplY3QoZSk7Zm9yKGxldCBlPTE7ZTxhcmd1bWVudHMubGVuZ3RoO2UrKyl7dmFyIG49YXJndW1lbnRzW2VdO2lmKG51bGwhPW4pZm9yKGNvbnN0IGUgaW4gbilPYmplY3QucHJvdG90eXBlLmhhc093blByb3BlcnR5LmNhbGwobixlKSYmKHRbZV09bltlXSl9cmV0dXJuIHR9KX1dKTs8L3NjcmlwdD4KPHNjcmlwdCBjcm9zc29yaWdpbj0iYW5vbnltb3VzIiBjaGFyc2V0PSJVVEYtOCIgc3JjPSJodHRwczovL20ubWVkaWEtYW1hem9uLmNvbS9pbWFnZXMvSS8zMWtLc2l1a0V2TC5qcyI+PC9zY3JpcHQ+CjxzY3JpcHQ+CiAgICB2YXIgbG9nZ2luZ01hbmFnZXIgPSBuZXcgTG9nZ2luZ0NsaWVudE1hbmFnZXIuZGVmYXVsdCh7InNoYXphbUlkIjoiUzlfREFfY3JlYXRpdmVJZCIsInRlbXBsYXRlTmFtZSI6IkR5bmFtaWMgZUNvbW1lcmNlX1NEX0NJX0NBX0RFU0tUT1AiLCJ0ZW1wbGF0ZU1ham9yVmVyc2lvbiI6IjAiLCJ0ZW1wbGF0ZU1pbm9yVmVyc2lvbiI6IjAiLCJsb2NhbGUiOiJDQSIsImFkU2VydmVyIjoiUzlfREEiLCJhZElkIjoiUzlfREFfYWRJZCIsImNyZWF0aXZlSWQiOiJTOV9EQV9jcmVhdGl2ZUlkIiwiaW1wcmVzc2lvbklkIjoicHc5V3NRSi1nM1JYVG5QYWNPYUNXQSIsImlzRGVidWciOm51bGwsInN0YWdlIjoicHJvZCIsInJlbmRlcklkIjoiZDVlNTY1YTgtYzhlYi00NjdjLWE1NjUtYThjOGViZDY3YzU1IiwicmVxdWlyZWRFbGVtZW50c0ZvclZpc3VhbENvbXBsZXRlbmVzcyI6WyJwcm9kdWN0SW1hZ2UiLCJzdGFyUmF0aW5nIl0sInByZURlZmluZWRVcmxzRm9yVmlzdWFsQ29tcGxldGVuZXNzIjp7ImFkQ2hvaWNlcyI6Imh0dHBzOi8vaW1hZ2VzLW5hLnNzbC1pbWFnZXMtYW1hem9uLmNvbS9pbWFnZXMvRy8xNS9kYS9hZGNob2ljZXMvYWMtdG9wcmlnaHQtc3ByaXRlLnBuZyIsInByaW1lTG9nbyI6Imh0dHBzOi8vaW1hZ2VzLW5hLnNzbC1pbWFnZXMtYW1hem9uLmNvbS9pbWFnZXMvRy8xNS9kYS9jcmVhdGl2ZXMvcHJpbWUtMngtMjAxNzA1MzEucG5nIiwic3RhclJhdGluZyI6Imh0dHBzOi8vaW1hZ2VzLW5hLnNzbC1pbWFnZXMtYW1hem9uLmNvbS9pbWFnZXMvRy8xNS9kYS9jcmVhdGl2ZXMvYXVpLW1pbmktc3ByaXRlLTIwMTUtMDIucG5nIn0sImN1cnJlbnREYXRlIjoiMjAyMS0wNi0wNFQyMjo0NzoyOC4xMDBaIn0sIHBlcmZvcm1hbmNlRXZlbnRNYW5hZ2VyKTsKPC9zY3JpcHQ+Cgo8c2NyaXB0IHNyYz0iaHR0cHM6Ly9pbWFnZXMtbmEuc3NsLWltYWdlcy1hbWF6b24uY29tL2ltYWdlcy9HLzAxL2RhY3gvanMvcmVhY3QtYnVuZGxlLTE2LjQuMC5taW4uX1YxXy5qcyI+PC9zY3JpcHQ+CjxzY3JpcHQgY3Jvc3NvcmlnaW49ImFub255bW91cyIgY2hhcnNldD0iVVRGLTgiIHNyYz0iaHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0kvNzFZcmd1N3I4Y0wuanMiPjwvc2NyaXB0Pgo8c2NyaXB0PgogICAgdmFyICRhZCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhZCcpOwogICAgUmVhY3RET00uaHlkcmF0ZShSZWFjdC5jcmVhdGVFbGVtZW50KExpYnJhcnkuZGVmYXVsdCwgeyJhYXhSZW5kZXJpbmdDb250ZXh0Ijp7ImltcHJlc3Npb25Ub2tlbiI6IiJ9LCJicmFuZEltYWdlUmVjdFVybCI6IiIsImJyYW5kSW1hZ2VTcXVhcmVVcmwiOiIiLCJjbGlja1VybHMiOlsiIl0sImhlaWdodCI6MTMwLCJpbXByZXNzaW9uVXJscyI6WyIiXSwiaXNCbGFja2phY2siOmZhbHNlLCJpc1IyR2F0ZXdheVNsb3QiOmZhbHNlLCJpc0Nhcm91c2VsIjpmYWxzZSwiaXNMYXJnZUJpbGxib2FyZFNsb3QiOmZhbHNlLCJpc01vYmlsZSI6ZmFsc2UsImlzTXVsdGlBc2luQ2FyZCI6ZmFsc2UsImlzTXVsdGlBc2luU3RhY2siOmZhbHNlLCJpc09mZnNpdGUiOmZhbHNlLCJpc1ByZXZpZXciOmZhbHNlLCJpc1RlYXNlRGlzYWJsZWQiOmZhbHNlLCJsb2NhbGUiOiJDQSIsIm1lZGlhQ2VudHJhbFBhdGgiOiJodHRwczovL2ltYWdlcy1uYS5zc2wtaW1hZ2VzLWFtYXpvbi5jb20vaW1hZ2VzL0cvMTUiLCJwcml2YWN5VXJsIjoiaHR0cDovL3d3dy5hbWF6b24uY2EvYWRwcmVmcy9yZWY9ZHJhX2FfcnZfaGRfaG9feHhfTkM1MTNfMTAwP3BuPTEmcGc9ZHJhJnBwPXJ2JTJDb25jJTJDMTc5MzM2MTg0MyUyQ0EyRVVRMVdUR0NUQkcyJTJDMTc5MzM2MTg0MyUyQ2NzZG5UX0tnSlBGUWFaRHFPeG9adFdiS21VayZhZHY9QTJFVVExV1RHQ1RCRzImdWhfaXQ9MGU2YjFkZWNmYTE2Nzc1N2FlYmRhYjdmMGNjYzQ5ZmVfQ1QmbnA9dHJ1ZSIsInByaXZhY3lJbnRlbnQiOiJhbWF6b25tb2JpbGU6Ly9pbnRlbnQ/aW50ZW50PWh0dHAlM0ElMkYlMkZ3d3cuYW1hem9uLmNhJTJGYWRwcmVmcyUyRnJlZiUzRGRyYV9hX3J2X2hkX2hvX3h4X05DNTEzXzEwMCUzRnBuJTNEMSUyNnBnJTNEZHJhJTI2cHAlM0RydiUyNTJDb25jJTI1MkMxNzkzMzYxODQzJTI1MkNBMkVVUTFXVEdDVEJHMiUyNTJDMTc5MzM2MTg0MyUyNTJDY3NkblRfS2dKUEZRYVpEcU94b1p0V2JLbVVrJTI2YWR2JTNEQTJFVVExV1RHQ1RCRzIlMjZ1aF9pdCUzRDBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUJTI2bnAlM0R0cnVlJmludGVudD1jb20uYW1hem9uLm1vYmlsZS5zaG9wcGluZy53ZWIlM0ElMkYlMkZ3d3cuYW1hem9uLmNhJTJGYWRwcmVmcyUyRnJlZiUzRGRyYV9hX3J2X2hkX2hvX3h4X05DNTEzXzEwMCUzRnBuJTNEMSUyNnBnJTNEZHJhJTI2cHAlM0RydiUyNTJDb25jJTI1MkMxNzkzMzYxODQzJTI1MkNBMkVVUTFXVEdDVEJHMiUyNTJDMTc5MzM2MTg0MyUyNTJDY3NkblRfS2dKUEZRYVpEcU94b1p0V2JLbVVrJTI2YWR2JTNEQTJFVVExV1RHQ1RCRzIlMjZ1aF9pdCUzRDBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUJTI2bnAlM0R0cnVlIiwid2lkdGgiOjY1MCwiaXNQREFTdHlsZSI6ZmFsc2UsIm5ld1N0eWxlVHVybk9mZiI6bnVsbCwiaGFzUHJpbWVEYXlEZWFsIjpmYWxzZSwicHJvZHVjdEltYWdlIjp7InVybCI6Imh0dHBzOi8vbS5tZWRpYS1hbWF6b24uY29tL2ltYWdlcy9JLzYxeloramJrZFFMLmpwZyIsImhlaWdodCI6MTM2MCwid2lkdGgiOjg1MH0sInByb2R1Y3RUaXRsZSI6IkhvdyB0byBQbGF5IHRoZSBIYXJtb25pY2E6IEEgQ29tcGxldGUgR3VpZGUgZm9yIEJlZ2lubmVycyAtIENocm9tYXRpYyBhbmQgRGlhdG9uaWMgSGFybW9uaWNhIiwiYWRMaW5rIjoiaHR0cHM6Ly9hYXgtdXMtZWFzdC5hbWF6b24tYWRzeXN0ZW0uY29tL3gvYy9RcWNQVnJFQ2ZvTjBWMDV6Mm5EbWdsZ0FBQUY1MlRXNnNRRUFBQUlCQVZnTERxUS9odHRwOi8vd3d3LmFtYXpvbi5jYS9ncC9zbHJlZGlyZWN0L3BpY2Fzc29SZWRpcmVjdC5odG1sP2llPVVURjgmYWRJZD1BMDcyMDQyNTFOMjgzVDE5NjNUUEwmcXVhbGlmaWVyPTE2MjI4NDY4NDcmaWQ9NDEzNTgyMDg1OTg5OTI3JndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmdXJsPSUyRmRwJTJGMTc5MzM2MTg0MyUyRnJlZiUzRHN5bl9zZF9vbnNpdGVfZGVza3RvcF8xNCUzRnBzYyUzRDElMjZ1aF9pdCUzRDBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUJnVoX2l0PTBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUIiwiY3VzdG9tZXJSZXZpZXdTdW1tYXJ5Ijp7ImFzaW4iOiIxNzkzMzYxODQzIiwicmF0aW5nIjo0LjIsImNvdW50IjoxNTF9LCJwcmljZSI6MTAuNDQsImN1cnJlbmN5U3ltYm9sIjoiJCIsImZvcm1hdHRlZFByaWNlIjoiMTAuNDQiLCJyZWxlYXNlRGF0ZU1lc3NhZ2UiOiIiLCJwcmljZUZvcm1hdHRpbmdGbGFncyI6eyJpc1N5bWJvbFN1cGVyc2NyaXB0Ijp0cnVlLCJzeW1ib2xQb3NpdGlvbiI6InByZWZpeGVkIn0sInByaWNlUGVyVW5pdE1lc3NhZ2UiOiIiLCJ0YXhNZXNzYWdlIjoiIiwiZGV0YWlsc0FuZERlbGl2ZXJ5TWVzc2FnZSI6IiIsImlzRGVhbCI6ZmFsc2UsImlzUHJpbWUiOmZhbHNlLCJpc1Nuc0Rpc2NvdW50IjpmYWxzZSwic25zVGV4dCI6IlN1YnNjcmliZSAmIFNhdmUiLCJkZWFsT2ZmZXIiOjAsInZpb2xhdGVzTWFwIjpmYWxzZSwicHJvZHVjdEluU3RvY2siOnRydWUsImJ1dHRvblRleHQiOiJTaG9wIG5vdyIsImNhc2NhZGluZ0ludGVudCI6ImFtYXpvbm1vYmlsZTovL2ludGVudD9pbnRlbnQ9aHR0cHMlM0ElMkYlMkZhYXgtdXMtZWFzdC5hbWF6b24tYWRzeXN0ZW0uY29tJTJGeCUyRmMlMkZRcWNQVnJFQ2ZvTjBWMDV6Mm5EbWdsZ0FBQUY1MlRXNnNRRUFBQUlCQVZnTERxUSUyRmh0dHAlM0ElMkYlMkZ3d3cuYW1hem9uLmNhJTJGZ3AlMkZzbHJlZGlyZWN0JTJGcGljYXNzb1JlZGlyZWN0Lmh0bWwlM0ZpZSUzRFVURjglMjZhZElkJTNEQTA3MjA0MjUxTjI4M1QxOTYzVFBMJTI2cXVhbGlmaWVyJTNEMTYyMjg0Njg0NyUyNmlkJTNENDEzNTgyMDg1OTg5OTI3JTI2d2lkZ2V0TmFtZSUzRHNkX29uc2l0ZV9kZXNrdG9wJTI2dXJsJTNEJTI1MkZkcCUyNTJGMTc5MzM2MTg0MyUyNTJGcmVmJTI1M0RzeW5fc2Rfb25zaXRlX2Rlc2t0b3BfMTQlMjUzRnBzYyUyNTNEMSUyNTI2dWhfaXQlMjUzRDBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUJTI2dWhfaXQlM0QwZTZiMWRlY2ZhMTY3NzU3YWViZGFiN2YwY2NjNDlmZV9DVCZpbnRlbnQ9Y29tLmFtYXpvbi5tb2JpbGUuc2hvcHBpbmcud2ViJTNBJTJGJTJGYWF4LXVzLWVhc3QuYW1hem9uLWFkc3lzdGVtLmNvbSUyRnglMkZjJTJGUXFjUFZyRUNmb04wVjA1ejJuRG1nbGdBQUFGNTJUVzZzUUVBQUFJQkFWZ0xEcVElMkZodHRwJTNBJTJGJTJGd3d3LmFtYXpvbi5jYSUyRmdwJTJGc2xyZWRpcmVjdCUyRnBpY2Fzc29SZWRpcmVjdC5odG1sJTNGaWUlM0RVVEY4JTI2YWRJZCUzREEwNzIwNDI1MU4yODNUMTk2M1RQTCUyNnF1YWxpZmllciUzRDE2MjI4NDY4NDclMjZpZCUzRDQxMzU4MjA4NTk4OTkyNyUyNndpZGdldE5hbWUlM0RzZF9vbnNpdGVfZGVza3RvcCUyNnVybCUzRCUyNTJGZHAlMjUyRjE3OTMzNjE4NDMlMjUyRnJlZiUyNTNEc3luX3NkX29uc2l0ZV9kZXNrdG9wXzE0JTI1M0Zwc2MlMjUzRDElMjUyNnVoX2l0JTI1M0QwZTZiMWRlY2ZhMTY3NzU3YWViZGFiN2YwY2NjNDlmZV9DVCUyNnVoX2l0JTNEMGU2YjFkZWNmYTE2Nzc1N2FlYmRhYjdmMGNjYzQ5ZmVfQ1QiLCJidXR0b25MaW5rIjoiaHR0cHM6Ly9hYXgtdXMtZWFzdC5hbWF6b24tYWRzeXN0ZW0uY29tL3gvYy9RcWNQVnJFQ2ZvTjBWMDV6Mm5EbWdsZ0FBQUY1MlRXNnNRRUFBQUlCQVZnTERxUS9odHRwOi8vd3d3LmFtYXpvbi5jYS9ncC9zbHJlZGlyZWN0L3BpY2Fzc29SZWRpcmVjdC5odG1sP2llPVVURjgmYWRJZD1BMDcyMDQyNTFOMjgzVDE5NjNUUEwmcXVhbGlmaWVyPTE2MjI4NDY4NDcmaWQ9NDEzNTgyMDg1OTg5OTI3JndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmdXJsPSUyRmRwJTJGMTc5MzM2MTg0MyUyRnJlZiUzRHN5bl9zZF9vbnNpdGVfZGVza3RvcF8xNCUzRnBzYyUzRDElMjZ1aF9pdCUzRDBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUJnVoX2l0PTBlNmIxZGVjZmExNjc3NTdhZWJkYWI3ZjBjY2M0OWZlX0NUIiwicmV2aWV3TGluayI6Imh0dHBzOi8vd3d3LmFtYXpvbi5jYS9wcm9kdWN0LXJldmlld3MvMTc5MzM2MTg0Mz9hYXhpdGs9NTA5MDI4NWNiODc1Y2EzMWMzYTllM2E3MDEwYzZlMGUiLCJidXR0b25Qcm9wcyI6eyJidXR0b25UeXBlIjoicHJpbWFyeSIsInNpemUiOiJyZWd1bGFyIn0sImZvcm1hdCI6InNob3Agbm93Iiwic2xvdE5hbWUiOm51bGx9KSwgJGFkKTsKICAgIGxvZ2dpbmdNYW5hZ2VyLmFkZFZpZXdhYmlsaXR5TGlzdGVuZXIoJGFkKTsKPC9zY3JpcHQ+Cgo8L2JvZHk+CjwvaHRtbD4K","serverSideFetchAd": "true","enableAdBlockerDetector": false,"disableResizeFunc": false,"minWidthToScale": "","fallbackStaticAdImgUrl": "","fallbackStaticAdClickUrl": "","fallbackStaticAdExtraStyle": "","adFeedbackInfo": {"adProgramId": "1027", "endPoint": "/gp/aq-feedback/lazyLoad/handler/af-link-handler.html","boolFeedback": true,"slugText": "Sponsored","adFeedbackOnTop":false},"adPlacementMetaData": {"pageUrl": "aHR0cHM6Ly93d3cuYW1hem9uLmNhL2dwL3Byb2R1Y3QvQjAwMDAwMjhSUj9kcFJlcXVlc3RJZD0xS01EWTJKUEdQMlgzUjgwRzhXQyZXREc9bXVzaWNfZGlzcGxheV9vbl93ZWJzaXRlJiplbnRyaWVzKj0wJipWZXJzaW9uKj0xJg==","adElementId": "ape_Detail_hero-quick-promo_Desktop_placement","pageType": "Detail","slotName": "hero-quick-promo"},"adCreativeMetaData": {"adProgramId": "1027","adCreativeTemplateName": "Dynamic eCommerce_SD_CI_CA_DESKTOP","adImpressionId": "https://aax-us-east.amazon-adsystem.com/e/xsp/imp?b=QqcPVrECfoN0V05z2nDmglgAAAF52TW6sQEAAAIBAVgLDqQ","adId": "200057018299461","adNetwork": "cs"},"advertisementStyle": {"position": "absolute","top": "2px","right": "0px","display": "inline-block","font": "normal 11px Arial","color": "grey"},"feedbackDivStyle": { "position": "relative", "top": "-2px", "height": "20px", "width":"78px"},"viewabilityStandards": [{"p": 0, "t": 0, "def": "amzn"}, {"p": 50, "t": 1, "def": "iab"}, {"p": 100, "t": 1, "def": "groupm"}],"ajaxWeblabTriggerId": "","abpStatus": "1","abpAcceptable": "true","disableAdReporterSlot": "false","allowlistedCustomMessageEvents": ["openPsAdPopover", "openATCModal", "setPartner", "sendMetrics", "wrap"],"allowlistedQueryParamKeys": ["sf-overrideVariationId", "sf-overridePredictorId", "sf-forceFailure"],"DAsfUrl":"https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js"}' aria-hidden="true"></div><script>(function(){function a(d,e){if(window.addEventListener){window.addEventListener(d,e,false);}else{if(window.attachEvent){window.attachEvent("on"+d,e);}}}function c(d,e){if(window.removeEventListener){window.removeEventListener(d,e,false);}else{if(window.detachEvent){window.detachEvent("on"+d,e);}}}var b=function(){(function(){(function(l,o){l.sfLogErrors=l.sfLogErrors||false;var q=q||function(v,u){u=u||new Error(v);if(l.ue&&typeof ue.count=="function"){ue.count("adplacements:safeFrameError",1);}if(!l.sfLogErrors){return;}if(l.ueLogError){l.ueLogError(u,{logLevel:"ERROR",attribution:"APE-safeframe",message:v+" "});}else{if(typeof console!=="undefined"&&console.error){console.error(v,u);}}};l.aanParams=l.aanParams||{};l.aanParams["hero-quick-promo"]="site=amazon.ca;pt=Detail;slot=hero-quick-promo;pid=B0000028RR;arid=c8f4f1df4f47417385fcc2e02a731b10";l["hero-quick-promo"]={};l["hero-quick-promo"].adStartTime=(new Date()).getTime();function d(){return l.innerHeight||o.documentElement.clientHeight;}function g(){return l.innerWidth||o.documentElement.clientWidth;}function e(w,u,v){if(w>0){return(v>w);}else{return(u>0);}}var f=function(){return(Date.now?Date.now():new Date().getTime());};throttle=function(v,x,B){var u,z,C;var A=null;var y=0;if(!B){B={};}var w=function(){y=B.leading===false?0:f();A=null;C=v.apply(u,z);if(!A){u=z=null;}};return function(){var E=f();if(!y&&B.leading===false){y=E;}var D=x-(E-y);u=this;z=arguments;if(D<=0||D>x){if(A){clearTimeout(A);A=null;}y=E;C=v.apply(u,z);if(!A){u=z=null;}}else{if(!A&&B.trailing!==false){A=setTimeout(w,D);}}return C;};};function n(C,A,v,x,u){try{var z=o.getElementById(C).getBoundingClientRect();if(e(z.top,z.bottom,d())&&e(z.left,z.right,g())){if(typeof uet=="function"){uet("bb","adplacements:viewablelatency:"+A,{wb:1});if(v){uet("bb","adplacements:viewablelatency:"+v,{wb:1});}}var w;if(l.csa){var B=o.getElementById(C);if(u=="mobileads"){w=l.csa("Content",{element:B.parentNode});}else{w=l.csa("Content",{element:B});}w("mark","viewablelatency:bodyBegin");if(l.apeViewableLatencyTrackers[x].loaded){w("mark","viewablelatency:loaded");}}if(typeof uex=="function"&&l.ue&&typeof ue.count=="function"){if(l.apeViewableLatencyTrackers[x].loaded){uex("ld","adplacements:viewablelatency:"+A,{wb:1});if(v){uex("ld","adplacements:viewablelatency:"+v,{wb:1});}ue.count("adplacements:htmlviewed:loaded:"+A,1);if(v){ue.count("adplacements:htmlviewed:loaded:"+v,1);}}ue.count("adplacements:htmlviewed:"+A,1);if(v){ue.count("adplacements:htmlviewed:"+v,1);}}l.apeViewableLatencyTrackers[x].viewed=true;if(l.apeViewableLatencyTrackers[x].tracker){c("scroll",l.apeViewableLatencyTrackers[x].tracker);c("resize",l.apeViewableLatencyTrackers[x].tracker);}}}catch(y){l.apeViewableLatencyTrackers[x].valid=false;}}try{l.apeViewableLatencyTrackers=l.apeViewableLatencyTrackers||{};var t="ape_Detail_hero-quick-promo_Desktop_placement";var s="Detail_hero-quick-promo_Desktop".replace(/\_/g,":");var i="04675163-3598-46ab-a128-ea7d6f6019e4";var k="c8f4f1df4f47417385fcc2e02a731b10";var h="amazon";l.apeViewableLatencyTrackers[k]=l.apeViewableLatencyTrackers[k]||{};l.apeViewableLatencyTrackers[k].valid=true;n(t,s,i,k,h);if(l.apeViewableLatencyTrackers[k].valid&&!l.apeViewableLatencyTrackers[k].viewed){l.apeViewableLatencyTrackers[k].tracker=throttle(function(){n(t,s,i,k,h);},20);a("scroll",l.apeViewableLatencyTrackers[k].tracker);a("resize",l.apeViewableLatencyTrackers[k].tracker);}}catch(m){if(l.apeViewableLatencyTrackers&&l.apeViewableLatencyTrackers.c8f4f1df4f47417385fcc2e02a731b10){l.apeViewableLatencyTrackers.c8f4f1df4f47417385fcc2e02a731b10.valid=false;}q("Error initializing viewable latency instrumentation",m);}if(l.csa){var j;var r=o.getElementById(t);if(h=="mobileads"){j=l.csa("Content",{element:r.parentNode});}else{j=l.csa("Content",{element:r});}j("mark","bodyBegin");}try{if(l.DAsf){l.DAsf.loadAds();}else{var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js?csm_attribution=APE-SafeFrame";p.onerror=function(){q("Error loading SafeFrame library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);l.collectSafeframeRTD=Math.random()*100<0;if(l.collectSafeframeRTD){var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/rtd/safeframeRtd-1.50.81044e8.js";p.onerror=function(){q("Error loading SafeFrame RTD library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);}}}catch(m){q("Error appending DAsf library",m);}}(window,document));})();};b();})();</script>








  
      </div>
    <div style="margin-bottom:5px"></div>















</div>





</div>

</div>

<script type="text/javascript">

if(typeof addlongPoleTag === 'function'){
addlongPoleTag('af','desktop-html-atf-marker');
}
if(window.ue) {
ue.count("dp_aib_centerCol_height", document.getElementById('centerCol').clientHeight);
}
</script>
<div id="hover-zoom-end" class="a-section a-spacing-small a-padding-mini"></div>

<script type="text/javascript">
setCSMReq('af');
</script>
<div id="ATFCriticalFeaturesDataContainer">














<div id="imageBlockVariations_feature_div" class="celwidget" data-feature-name="imageBlockVariations">













<script type="text/javascript">
P.when('jQuery').register('ImageBlockBTF', function(jQuery){
if(window.performance && performance.now && window.ue && ue.count){
ue.count('DPIBBTFRegisterTime',window.parseInt(performance.now()));
}
var data = {};
var obj = jQuery.parseJSON('{"dataInJson":null,"alwaysIncludeVideo":true,"autoplayVideo":false,"defaultColor":"initial","mainImageSizes":[["355","355"],["450","450"],["425","550"],["466","606"],["522","679"],["569","741"],["679","879"]],"maxAlts":7,"altsOnLeft":true,"productGroupID":"music_display_on_website","lazyLoadExperienceDisabled":true,"lazyLoadExperienceOnHoverDisabled":false,"useChromelessVideoPlayer":false,"colorToAsin":{},"refactorEnabled":true,"useIV":true,"tabletWeb":false,"views":["ImageBlockMagnifierView","ImageBlockAltImageView","ImageBlockVideoView","ImageBlockTwisterView","ImageBlockImmersiveViewImages","ImageBlockImmersiveViewVideos","ImageBlockImmersiveView360","ImageBlockTabbedImmersiveView","ImageBlockShoppableSceneView"],"enhancedHoverOverlay":false,"landingAsinColor":"initial","colorImages":{},"heroImages":{},"enable360Map":{},"staticImages":{"hoverZoomIcon":null,"shoppableSceneViewProductsButton":"https://images-na.ssl-images-amazon.com/images/G/15/shopbylook/shoppable-images/view_products._CB403825028_.svg","zoomLensBackground":"https://images-na.ssl-images-amazon.com/images/G/15/apparel/rcxgs/tile._CB483369412_.gif","zoomInCur":"https://images-na.ssl-images-amazon.com/images/G/15/detail-page/cursors/zoomIn._CB485921870_.cur","shoppableSceneSideSheetClose":"https://images-na.ssl-images-amazon.com/images/G/15/shopbylook/shoppable-images/close_x_white._CB416326532_.png","shoppableSceneBackToTopArrow":"https://images-na.ssl-images-amazon.com/images/G/15/shopbylook/shoppable-images/back_to_top_arrow._CB403825028_.svg","arrow":"https://images-na.ssl-images-amazon.com/images/G/15/javascripts/lib/popover/images/light/sprite-vertical-popover-arrow._CB485933081_.png","shoppableSceneTag":"https://images-na.ssl-images-amazon.com/images/G/15/shopbylook/shoppable-images/tag_white._CB403828666_.svg","zoomIn":"https://images-na.ssl-images-amazon.com/images/G/15/detail-page/cursors/zoom-in._CB485944647_.bmp","shoppableSceneTabControlArrow":"https://images-na.ssl-images-amazon.com/images/G/15/shopbylook/shoppable-images/next_tab_control._CB416326532_.svg","zoomOut":"https://images-na.ssl-images-amazon.com/images/G/15/detail-page/cursors/zoom-out._CB485943842_.bmp","videoThumbIcon":"https://images-na.ssl-images-amazon.com/images/G/15/Quarterdeck/en_US/images/video._CB485935549_SS40_.gif","spinnerNoLabel":"https://images-na.ssl-images-amazon.com/images/G/15/ui/loadIndicators/loading-large._CB485945341_.gif","zoomOutCur":"https://images-na.ssl-images-amazon.com/images/G/15/detail-page/cursors/zoomOut._CB485921707_.cur","videoSWFPath":null,"grabbing":"https://images-na.ssl-images-amazon.com/images/G/15/HomeCustomProduct/grabbingbox._CB478670482_.cur","icon360":"https://images-na.ssl-images-amazon.com/images/G/15/HomeCustomProduct/360_icon_73x73v2._CB485971326_SS40_.png","grab":"https://images-na.ssl-images-amazon.com/images/G/15/HomeCustomProduct/grabbox._CB478669156_.cur","shoppableSceneTagHighlighted":"https://images-na.ssl-images-amazon.com/images/G/15/shopbylook/shoppable-images/tag_highlighted._CB403828666_.svg","spinner":"https://images-na.ssl-images-amazon.com/images/G/15/ui/loadIndicators/loading-large_labeled._CB485921383_.gif"},"staticStrings":{"shoppableSceneViewProductsButton":"View products","images":"Images","watchMoreVideos":"Click to see more videos","allMedia":"All Media","dragToSpin":"Drag to Spin","videos":"Vídeos","video":"video","shoppableSceneTabsTitle":"Shop similar products","rollOverToZoom":"Roll over image to zoom in","clickToExpand":"Click to open expanded view","playVideo":"Click to play video","shoppableSceneNoSuggestions":"No results available","touchToZoom":"Touch the image to zoom in","multipleVideos":"VIDEOS","singleVideo":"VIDEO","clickSceneTagsToShopProducts":"Click the tags to shop similar products","pleaseSelect":"Please select","close":"Close","clickToZoom":"Click on the image to zoom in"},"useChildVideos":true,"useClickZoom":false,"useHoverZoom":true,"useHoverZoomIpad":false,"visualDimensions":[],"mainImageHeightPartitions":null,"mainImageMaxSizes":null,"heroFocalPoint":null,"showMagnifierOnHover":false,"disableHoverOnAltImages":false,"overrideAltImageClickAction":false,"naturalMainImageSize":null,"imgTagWrapperClasses":null,"prioritizeVideos":false,"usePeekHover":false,"fadeMagnifier":false,"repositionHeroImage":false,"heroVideoVariant":null,"videos":[],"title":"Rage Against The Machine","airyConfigEnabled":false,"airyConfig":null,"vseVideoDataSourceTreatment":"C","mediaAsin":"B0000028RR","parentAsin":"B0000028RR","largeSCLVideoThumbnail":false,"displayVideoBanner":false,"useVSEVideos":false,"useTabbedImmersiveView":true,"dpRequestId":"1KMDY2JPGP2X3R80G8WC","contentWeblab":"","contentWeblabTreatment":"","dp60VideoThumbMap":null}');
data["alwaysIncludeVideo"] = obj.alwaysIncludeVideo ? 1 : 0;
data["autoplayVideo"] = obj.autoplayVideo ? 1 : 0;
data["defaultColor"] = obj.defaultColor;
data["maxAlts"] = obj.maxAlts;
data["altsOnLeft"] = obj.altsOnLeft;
data["newVideoMissing"] = obj.newVideoMissing;
data["lazyLoadExperienceDisabled"] = obj.lazyLoadExperienceDisabled;
data["lazyLoadExperienceOnHoverDisabled"] = obj.lazyLoadExperienceOnHoverDisabled;
data["useChromelessVideoPlayer"] = obj.useChromelessVideoPlayer ? 1 : 0;
data["colorToAsin"] = obj.colorToAsin;
data["ivRepresentativeAsin"] = obj.ivRepresentativeAsin;
data["ivImageSetKeys"] = obj.ivImageSetKeys;
data["useIV"] = obj.useIV ? 1 : 0;
data["tabletWeb"] = obj.tabletWeb ? 1 : 0;
data["views"] = obj.views;
data["enhancedHoverOverlay"] = obj.enhancedHoverOverlay;
data["landingAsinColor"] = obj.landingAsinColor;
data["colorImages"] = obj.colorImages;
data["heroImage"] = obj.heroImages;
data["spin360ColorEnabled"] = obj.enable360Map;
data["staticImages"] = obj.staticImages;
data["staticStrings"] = obj.staticStrings;
data["useChildVideos"] = obj.useChildVideos ? 1 : 0;
data["useClickZoom"] = obj.useClickZoom ? 1 : 0;
data["useHoverZoom"] = obj.useHoverZoom ? 1 : 0;
data["useHoverZoomIpad"] = obj.useHoverZoomIpad ? 1 : 0;
data["visualDimensions"] = obj.visualDimensions;
data["isLargeSCLVideoThumbnail"] = obj.largeSCLVideoThumbnail;
data["mainImageSizes"] = obj.mainImageSizes;
data["displayVideoBanner"] = obj.displayVideoBanner;
data["mainImageHeightPartitions"] = obj.mainImageHeightPartitions;
data["mainImageMaxSizes"] = obj.mainImageMaxSizes;
data["heroFocalPoint"] = obj.heroFocalPoint;
data["showMagnifierOnHover"] = obj.showMagnifierOnHover ? 1 : 0;
data["disableHoverOnAltImages"] = obj.disableHoverOnAltImages ? 1 : 0;
data["overrideAltImageClickAction"] = obj.overrideAltImageClickAction ? 1 : 0;
data["naturalMainImageSize"] = obj.naturalMainImageSize;
data["imgTagWrapperClasses"] = obj.imgTagWrapperClasses;
data["prioritizeVideos"] = obj.prioritizeVideos;
data["usePeekHover"] = obj.usePeekHover;
data["fadeMagnifier"] = obj.fadeMagnifier;
data["repositionHeroImage"] = obj.repositionHeroImage;
data["heroVideoVariant"] = obj.heroVideoVariant;
data["videos"] = obj.videos;
data["productGroupID"] = obj.productGroupID;
data["title"] = obj.title;
data["airyConfigEnabled"] = obj.airyConfigEnabled;
if (obj.airyConfigEnabled) {
data["airyConfig"] = obj.airyConfig;
}
data["isDPXFeatureEnabled"] = true;
data["useTabbedImmersiveView"] = obj.useTabbedImmersiveView;
data["vseVideoDataSourceTreatment"] = obj.vseVideoDataSourceTreatment;
data["contentWeblab"] = obj.contentWeblab;
data["contentWeblabTreatment"] = obj.contentWeblabTreatment;
data["useVSEVideos"] = obj.useVSEVideos;
data["dpRequestId"] = obj.dpRequestId;
data["mediaAsin"] = obj.mediaAsin;
data["parentAsin"] = obj.parentAsin;
data["dp60VideoThumbMap"] = obj.dp60VideoThumbMap;
return data;
});
</script>

























</div>





</div>

<div id="bottomRow">

</div>





<!-- MarkAF -->






<script type="text/javascript">
  P.now('sp.load.js').execute(function(jsObj){
    if(!jsObj){
      P.declare('sp.load.js', {});
    }
  });
  P.now('dpJsAssetsLoadMarker').execute(function(markerObj){
    if(!markerObj){
      P.declare('dpJsAssetsLoadMarker', {});
    }
  });
</script>

    <script type="text/javascript">
    if(typeof uex === 'function'){uex('ld', 'atfClientSideWaitTimeDesktop', {wb: 1});};
  </script>







 









    






    
    
        
        


    



   

    






        





        <script type="a-state" data-a-state="{&quot;key&quot;:&quot;metrics-schema&quot;}">{"widgetSchema":"dp:widget:","dimensionSchema":"dp:dims:"}</script>




        






























 
 
 

 
 

















    

      












        





    
    
    



















      	  	<script type="a-state" data-a-state="{&quot;key&quot;:&quot;dp_injected_meta_assets&quot;}">{"assetNames":["DetailPageMetaAssetFixed","AmazonUICalendar","DetailPageDesktopImageBlockMetaAsset","MusicDetailPageMetaAsset_TURBO_DESKTOP","DetailPageAllOffersDisplayAssets"]}</script>
                    










  



        
        
        
        
  








    




       















<script type='text/javascript'>P.when('cf').execute(function() { ue.count('dp:widget:dpxSize:dpxBTFSize', 79);ue.count('dp:widget:dpxSize:dpxATFSize', 120);});</script>
         
        






































<div cel_widget_id='dpx-btf-bundle_csm_instrumentation_wrapper' class='celwidget'>




  



        
        
        
        
  








    







<div id="bundleV2_feature_div" class="celwidget" data-feature-name="bundleV2">




































</div>
</div>






<hr class="bucketDivider" noshade="noshade" size="1">
  <div class="bucket" id="quickPromoBucketContent">
    <a id="productPromotions" name="productPromotions"></a>
    <h2>Special offers and product promotions</h2>
    
  
    
    <div class="content">
      <ul class="qpUL">
        <li><style type="text/css">
        #a-page div.unified_widget.rcmBody {
            font-size: 12px;
            font-family: arial,helvetica,sans-serif;
            line-height: 1.4 em;
        }
        #a-page div.unified_widget.rcmBody h2 {
            font-size:135%; 
            font-weight:bold;
            margin:0 0 0.35em 0px;
            color:#E47911; 
            padding:0;
        }
        #a-page div.unified_widget.rcmBody .headline {
            color: #E47911;
            font-size: .92em;
            display: block;
            font-weight: bold;
        }
        #a-page div.unified_widget.rcmBody p {
            margin:0 0 0.5em 0;
            line-height:1.4em;
        }
        #a-page div.unified_widget.rcmBody a {
            color: #004B91;
            text-decoration: underline;
        }
        #a-page div.unified_widget.rcmBody a:active {
            color: #FF9933;
        }
        #a-page div.unified_widget.rcmBody a:visited {
            color: #996633;
        }
        #a-page div.unified_widget.rcmBody hr {
            border-top: ridge;
            margin: 0px;
        }
        #a-page div.unified_widget.rcmBody ul {
            list-style-position: inside;
            margin: 1em 0;
            padding: 0 0 0 30px;
            color: #111;
        }
        #a-page div.unified_widget.rcmBody ul li {
            list-style: disc;
        }
        #a-page div.unified_widget.rcmBody div.bannerImage {
            text-align: center;
        }
        #a-page div.unified_widget.rcmBody .carat {
            font-weight: bold;
            font-size: 120%;
            color: #E47911;
            margin-right: 0.2em;
            font-family: verdana,arial,helvetica,sans-serif;
        }
        #a-page div.unified_widget.rcmBody div.prodImage {
            margin: 0 0.5em 0.25em 0;
            float: left;
        }
    </style><div class="unified_widget rcmBody"><a href="https://www.amazon.ca:443/gp/redirect.html/ref=amb_link_SdHPqUhhQzSHUeYZdw6BmA_1?_encoding=UTF8&location=https%3A%2F%2Fwww.amazon.ca%2Fbusiness%2Fregister%2Forg%2Flanding%3Fref_%3Db2b_reg_ca_SOPP_122020&source=standards&token=D880603F94D233AE281B55A7606337299FF8AC03&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=special-product-offers-2&pf_rd_r=1KMDY2JPGP2X3R80G8WC&pf_rd_r=1KMDY2JPGP2X3R80G8WC&pf_rd_t=201&pf_rd_p=78f41973-687b-4d35-9940-62949101f4f5&pf_rd_p=78f41973-687b-4d35-9940-62949101f4f5&pf_rd_i=B0000028RR"><b>Amazon Business Canada</b></a> : Save time and reduce costs for your business with Quantity Discounts and FREE Shipping in Canada. <a href="https://www.amazon.ca:443/gp/redirect.html/ref=amb_link_SdHPqUhhQzSHUeYZdw6BmA_2?_encoding=UTF8&location=https%3A%2F%2Fwww.amazon.ca%2Fbusiness%2Fregister%2Forg%2Flanding%3Fref_%3Db2b_reg_ca_SOPP_122020&source=standards&token=D880603F94D233AE281B55A7606337299FF8AC03&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=special-product-offers-2&pf_rd_r=1KMDY2JPGP2X3R80G8WC&pf_rd_r=1KMDY2JPGP2X3R80G8WC&pf_rd_t=201&pf_rd_p=78f41973-687b-4d35-9940-62949101f4f5&pf_rd_p=78f41973-687b-4d35-9940-62949101f4f5&pf_rd_i=B0000028RR"><b>Register a free business account</b></a><div class="h_rule"></div></div></li><input type="hidden" name="productPromosHidden" id="productPromosHidden" />
      </ul>
      
    </div>
  </div>
    <script type="text/javascript">
      if (typeof showHideElement == 'function') {
        showHideElement('specialOffersHidden', 'specialOffersDiv');
        showHideElement('productPromosHidden', 'heroQuickPromoDiv');
      }
    </script>
<div cel_widget_id='sims-consolidated-1_csm_instrumentation_wrapper' class='celwidget'>


<div class="celwidget pd_rd_w-Zydas pf_rd_p-67279b87-ccd3-46cd-8df4-d8c53edf84d3 pf_rd_r-1KMDY2JPGP2X3R80G8WC pd_rd_r-34c0e605-14a5-40b3-bf38-60ac9a8deafe pd_rd_wg-CqCH6" cel_widget_id="desktop-dp-sims_fbt" data-csa-c-content-id="67279b87-ccd3-46cd-8df4-d8c53edf84d3" data-csa-c-slot-id="desktop-dp-sims-0" data-csa-c-type="widget">





  


 
 













    <div id='sims-fbt' class='similarities-widget bucket'>
        <hr class="a-divider-normal bucketDivider"><h2>Frequently bought together</h2>
        <div id="sims-fbt-container" data-p13n-feature-metadata="{&quot;baseAsin&quot;:&quot;B0000028RR&quot;,&quot;has_diff_avail&quot;:&quot;0&quot;,&quot;has_seller_difference&quot;:&quot;0&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pf_rd_p&quot;:&quot;67279b87-ccd3-46cd-8df4-d8c53edf84d3&quot;,&quot;pd_rd_w&quot;:&quot;Zydas&quot;}" data-p13n-feature-name="pd_bxgy" data-p13n-global="{&quot;customerId&quot;:0,&quot;marketplace&quot;:&quot;CA&quot;,&quot;requestId&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;marketplaceId&quot;:&quot;A2EUQ1WTGCTBG2&quot;,&quot;session&quot;:&quot;138-4669640-7712440&quot;}" class="a-container">
            <div id='sims-fbt-content'>
                <form id="sims-fbt-form" name="BuyXGetYhandleBuy" method="post" action="/gp/item-dispatch/ref=pd_bxgy_button_crt/138-4669640-7712440?ie=UTF8&pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&pd_rd_w=Zydas&pd_rd_wg=CqCH6&pf_rd_p=67279b87-ccd3-46cd-8df4-d8c53edf84d3&pf_rd_r=1KMDY2JPGP2X3R80G8WC&refRID=1KMDY2JPGP2X3R80G8WC" autocomplete="off">
                <input type="hidden" name="session-id" value="138-4669640-7712440"><input type="hidden" name="discoveredAsins.1" value="B0000029D9"><input type="hidden" name="discoveredAsins.2" value="B00002MZ2C"><input type="hidden" name="CSRF" value="gxHW+2wYtMm7PoQoBKFhKJfaxqIwRBFflcmkIfFkaZa8AAAADAAAAABguq2BcmF3AAAAABVX8CwXqz4nuL9RKX///w==">
                <div>
                    <ul class="a-unordered-list a-nostyle a-horizontal a-spacing-base a-spacing-top-base sims-fbt-image-box">
        <li class="a-align-center sims-fbt-image-1"><span class="a-list-item"><div class="a-section"><img alt="Rage Against The Machine" src="https://images-na.ssl-images-amazon.com/images/I/81Hj5Wf1Z7L._AC_UL115_.jpg" class="sims-fbt-image"></div></span></li><li class="a-align-center sims-fbt-plus-2"><span class="a-list-item a-size-large a-color-tertiary">+</span></li><li class="a-align-center sims-fbt-image-2"><span class="a-list-item"><a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_bxgy_img_2/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B0000029D9&pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&pd_rd_w=Zydas&pd_rd_wg=CqCH6&pf_rd_p=67279b87-ccd3-46cd-8df4-d8c53edf84d3&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC"><div class="a-section"><img alt="Evil Empire" src="https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL115_.jpg" class="sims-fbt-image"></div></a></span></li><li class="a-align-center sims-fbt-plus-3"><span class="a-list-item a-size-large a-color-tertiary">+</span></li><li class="a-align-center sims-fbt-image-3"><span class="a-list-item"><a class="a-link-normal" href="/Battle-Angeles-Rage-Against-Machine/dp/B00002MZ2C/ref=pd_bxgy_img_3/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B00002MZ2C&pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&pd_rd_w=Zydas&pd_rd_wg=CqCH6&pf_rd_p=67279b87-ccd3-46cd-8df4-d8c53edf84d3&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC"><div class="a-section"><img alt="The Battle Of Los Angeles" src="https://images-na.ssl-images-amazon.com/images/I/81-vO7ZkqnL._AC_UL115_.jpg" class="sims-fbt-image"></div></a></span></li>
        </ul>
                    <div class='sims-fbt-price-box'>
                        <div class='sims-fbt-total-price'><span class="a-size-base a-color-secondary sims-fbt-total-price-text">Total price: </span><span class="a-size-medium a-color-price sims-fbt-total-price-value"><span class='p13n-sc-price' >$60.86</span></span></div>
                        <div class='sims-fbt-buttons'><div class="a-button-stack a-spacing-mini">
                            <span class="a-button a-button-primary a-button-small sims-fbt-add-to-cart"><span class="a-button-inner"><input name="submit.addToCart" class="a-button-input" type="submit"><span class="a-button-text" aria-hidden="true">Add all three to Cart</span></span></span>
                            
                        </div></div>
                        <script type="a-state" data-a-state="{&quot;key&quot;:&quot;sims-fbt&quot;}">{"currencyConversionRatio":1,"addToCartText":{"1":"Add to Cart","3":"Add all three to Cart","2":"Add both to Cart"},"allOfferListingIDs":["nl0MvZ0zQXIdaTAUSTD61KwPTMyFy0rUEpNqYAWxhoqBPw6XpfsBqCzj0SphQ0XIWndi0fPaHNvATx8ymXvPPHmRxCxpS1120DBp6ADYgyLAcPkvS48zA6vewT7emaMzwTi35JERyFHDVQNaJ8%2FsF70OIEAhQjTJ3V%2FSaXAnh6nZgulPkkcX7F8FD5fMfLbu","tarK6VU0cMfroEipFQX163LPIBaeQJ%2FJ29PzfCsBBmgBs69BE4VSMq3CE2HF3uhF%2FS8VMOwZlxBGsxFzbYVxlCS8EFXjE%2FJRoqleDdSTsCm1DyjTpS9zKrD8YTp42wn%2F","TPjLQ%2BzCqWFrPACmeruGUTJueJzmpzPP7tVu3HJ%2FdAmw6AU3Ppt7X4hi%2FJkeza7Ed2AcLS2ZldkpoI86rjK%2BVM9t6aTzPxpQ0wD2tJ6o0NOxYNtZxaTSKUUkY8NJ0E8a"],"currencySymbol":"\u003cspan class='p13n-sc-price' >$\u003cspan class=\"sims-fbt-price-value\">\u003c/span>\u003c/span>","currencyCode":"CAD","shouldTruncateCents":0,"MAPText":"To see our price, add these items to your cart. \u003ca class=\"a-link-normal sims-fbt-map-details-link\" target=\"AmazonHelp\" rel=\"noopener\" href=\"/gp/help/customer/display.html/ref=pd_bxgy_map/138-4669640-7712440?ie=UTF8&nodeId=201014980&pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&pd_rd_w=Zydas&pd_rd_wg=CqCH6&pf_rd_p=67279b87-ccd3-46cd-8df4-d8c53edf84d3&pf_rd_r=1KMDY2JPGP2X3R80G8WC&pop-up=1&refRID=1KMDY2JPGP2X3R80G8WC\">Why don't we show the price?\u003c/a>","shippingDetails":{"123":"seller","23":"same","13":"seller","12":"seller"},"shouldUseCommaForDecimal":0,"itemDetails":{"TPjLQ%2BzCqWFrPACmeruGUTJueJzmpzPP7tVu3HJ%2FdAmw6AU3Ppt7X4hi%2FJkeza7Ed2AcLS2ZldkpoI86rjK%2BVM9t6aTzPxpQ0wD2tJ6o0NOxYNtZxaTSKUUkY8NJ0E8a":{"asin":"B00002MZ2C","isPreorder":0,"price":13.17,"doesMAPPolicyApply":0},"tarK6VU0cMfroEipFQX163LPIBaeQJ%2FJ29PzfCsBBmgBs69BE4VSMq3CE2HF3uhF%2FS8VMOwZlxBGsxFzbYVxlCS8EFXjE%2FJRoqleDdSTsCm1DyjTpS9zKrD8YTp42wn%2F":{"asin":"B0000029D9","isPreorder":0,"price":15.48,"doesMAPPolicyApply":0},"nl0MvZ0zQXIdaTAUSTD61KwPTMyFy0rUEpNqYAWxhoqBPw6XpfsBqCzj0SphQ0XIWndi0fPaHNvATx8ymXvPPHmRxCxpS1120DBp6ADYgyLAcPkvS48zA6vewT7emaMzwTi35JERyFHDVQNaJ8%2FsF70OIEAhQjTJ3V%2FSaXAnh6nZgulPkkcX7F8FD5fMfLbu":{"asin":"B0000028RR","isPreorder":0,"price":32.21,"doesMAPPolicyApply":0}},"addToWishListText":{"1":"Add to Wish List","3":"Add all three to Wish List","2":"Add both to Wish List"},"preOrderText":null,"fbtStrings":{"showDetails":"Show details","showDetailsLong":"Show availability and shipping details","differentSellers":"These items are shipped from and sold by different sellers.","noDetails":"Choose items to buy together.","hideDetailsLong":"Hide availability and shipping details","hideDetails":"Hide details","differentAvailabilityOne":"One of these items ships sooner than the other."}}</script>
                    </div>
                </div>
                <div class='sims-fbt-details-link'><div class="a-box a-alert-inline a-alert-inline-info"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content"><span class="a-size-mini sims-fbt-shipping-details-text">These items are shipped from and sold by different sellers.</span> <a class="a-size-mini a-link-normal" href="javascript:void(0)">Show details</a></div></div></div></div>
                <div class='sims-fbt-rows'><fieldset class="forScreenreaders"><legend><span>Buy the selected items together</span></legend><ul class="a-unordered-list a-nostyle a-vertical"><li data-p13n-asin-metadata="{&quot;ref&quot;:&quot;pd_bxgy_1_1&quot;,&quot;price&quot;:32.21,&quot;asin&quot;:&quot;B0000028RR&quot;}" class="a-spacing-mini p13n-asin"><span class="a-list-item"><span class="a-declarative" data-action="fbt-checkbox-click" data-fbt-checkbox-click="{&quot;itemNum&quot;:&quot;1&quot;,&quot;offerListingID&quot;:&quot;nl0MvZ0zQXIdaTAUSTD61KwPTMyFy0rUEpNqYAWxhoqBPw6XpfsBqCzj0SphQ0XIWndi0fPaHNvATx8ymXvPPHmRxCxpS1120DBp6ADYgyLAcPkvS48zA6vewT7emaMzwTi35JERyFHDVQNaJ8%2FsF70OIEAhQjTJ3V%2FSaXAnh6nZgulPkkcX7F8FD5fMfLbu&quot;,&quot;asin&quot;:&quot;B0000028RR&quot;}"><div data-a-input-name="offeringID.1" class="a-checkbox sims-fbt-checkbox"><label><input type="checkbox" name="offeringID.1" value="nl0MvZ0zQXIdaTAUSTD61KwPTMyFy0rUEpNqYAWxhoqBPw6XpfsBqCzj0SphQ0XIWndi0fPaHNvATx8ymXvPPHmRxCxpS1120DBp6ADYgyLAcPkvS48zA6vewT7emaMzwTi35JERyFHDVQNaJ8%2FsF70OIEAhQjTJ3V%2FSaXAnh6nZgulPkkcX7F8FD5fMfLbu" checked><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"><div class = 'sims-fbt-checkbox-label'><span class="sims-fbt-this-item a-text-bold">This item:</span><span>Rage Against The Machine</span><span class="a-size-small"> by Rage Against The Machine</span><span class="a-size-small a-color-secondary"> Audio CD</span> <span class="a-color-price"><span class='p13n-sc-price' >$32.21</span></span> <div class="a-row a-spacing-micro a-spacing-top-micro a-size-small a-color-secondary sims-fbt-seller-info"><div class="a-row"><span class="a-size-base a-color-secondary a-text-normal">Ships from and sold by Ergodebooks Ships from USA.</span></div></div></div></span></label></div></span></span></li><li data-p13n-asin-metadata="{&quot;ref&quot;:&quot;pd_bxgy_2_2&quot;,&quot;price&quot;:15.48,&quot;asin&quot;:&quot;B0000029D9&quot;}" class="a-spacing-mini p13n-asin"><span class="a-list-item"><span class="a-declarative" data-action="fbt-checkbox-click" data-fbt-checkbox-click="{&quot;itemNum&quot;:&quot;2&quot;,&quot;offerListingID&quot;:&quot;tarK6VU0cMfroEipFQX163LPIBaeQJ%2FJ29PzfCsBBmgBs69BE4VSMq3CE2HF3uhF%2FS8VMOwZlxBGsxFzbYVxlCS8EFXjE%2FJRoqleDdSTsCm1DyjTpS9zKrD8YTp42wn%2F&quot;,&quot;asin&quot;:&quot;B0000029D9&quot;}"><div data-a-input-name="offeringID.2" class="a-checkbox sims-fbt-checkbox"><label><input type="checkbox" name="offeringID.2" value="tarK6VU0cMfroEipFQX163LPIBaeQJ%2FJ29PzfCsBBmgBs69BE4VSMq3CE2HF3uhF%2FS8VMOwZlxBGsxFzbYVxlCS8EFXjE%2FJRoqleDdSTsCm1DyjTpS9zKrD8YTp42wn%2F" checked><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"><div class = 'sims-fbt-checkbox-label'><a class="a-size-base a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_bxgy_2/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B0000029D9&pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&pd_rd_w=Zydas&pd_rd_wg=CqCH6&pf_rd_p=67279b87-ccd3-46cd-8df4-d8c53edf84d3&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC">Evil Empire</a><span class="a-size-small"> by Rage Against The Machine</span><span class="a-size-small a-color-secondary"> Audio CD</span> <span class="a-color-price"><span class='p13n-sc-price' >$15.48</span></span> <div class="a-row a-spacing-micro a-spacing-top-micro a-size-small a-color-secondary sims-fbt-seller-info"><div class="a-row"><span class="a-size-base a-color-success">In Stock.</span></div><div class="a-row"><span class="a-size-base a-color-secondary a-text-normal">Ships from and sold by Amazon.ca.</span></div></div></div></span></label></div></span></span></li><li data-p13n-asin-metadata="{&quot;ref&quot;:&quot;pd_bxgy_3_3&quot;,&quot;price&quot;:13.17,&quot;asin&quot;:&quot;B00002MZ2C&quot;}" class="a-spacing-mini p13n-asin"><span class="a-list-item"><span class="a-declarative" data-action="fbt-checkbox-click" data-fbt-checkbox-click="{&quot;itemNum&quot;:&quot;3&quot;,&quot;offerListingID&quot;:&quot;TPjLQ%2BzCqWFrPACmeruGUTJueJzmpzPP7tVu3HJ%2FdAmw6AU3Ppt7X4hi%2FJkeza7Ed2AcLS2ZldkpoI86rjK%2BVM9t6aTzPxpQ0wD2tJ6o0NOxYNtZxaTSKUUkY8NJ0E8a&quot;,&quot;asin&quot;:&quot;B00002MZ2C&quot;}"><div data-a-input-name="offeringID.3" class="a-checkbox sims-fbt-checkbox"><label><input type="checkbox" name="offeringID.3" value="TPjLQ%2BzCqWFrPACmeruGUTJueJzmpzPP7tVu3HJ%2FdAmw6AU3Ppt7X4hi%2FJkeza7Ed2AcLS2ZldkpoI86rjK%2BVM9t6aTzPxpQ0wD2tJ6o0NOxYNtZxaTSKUUkY8NJ0E8a" checked><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"><div class = 'sims-fbt-checkbox-label'><a class="a-size-base a-link-normal" href="/Battle-Angeles-Rage-Against-Machine/dp/B00002MZ2C/ref=pd_bxgy_3/138-4669640-7712440?_encoding=UTF8&pd_rd_i=B00002MZ2C&pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&pd_rd_w=Zydas&pd_rd_wg=CqCH6&pf_rd_p=67279b87-ccd3-46cd-8df4-d8c53edf84d3&pf_rd_r=1KMDY2JPGP2X3R80G8WC&psc=1&refRID=1KMDY2JPGP2X3R80G8WC">The Battle Of Los Angeles</a><span class="a-size-small"> by Rage Against The Machine</span><span class="a-size-small a-color-secondary"> Audio CD</span> <span class="a-color-price"><span class='p13n-sc-price' >$13.17</span></span> <div class="a-row a-spacing-micro a-spacing-top-micro a-size-small a-color-secondary sims-fbt-seller-info"><div class="a-row"><span class="a-size-base a-color-success">In Stock.</span></div><div class="a-row"><span class="a-size-base a-color-secondary a-text-normal">Ships from and sold by Amazon.ca.</span></div></div></div></span></label></div></span></span></li></ul></fieldset></div>
                </form>
            </div>
        </div>
    </div>
    







</div>


</div><div cel_widget_id='sims-consolidated-2_csm_instrumentation_wrapper' class='celwidget'>
<div class="celwidget pd_rd_w-PwwXe pf_rd_p-28f5b2d0-fab0-4512-8e55-c157bfb42e19 pf_rd_r-1KMDY2JPGP2X3R80G8WC pd_rd_r-34c0e605-14a5-40b3-bf38-60ac9a8deafe pd_rd_wg-CqCH6 c-f" cel_widget_id="p13n-desktop-carousel_DPSims_1" data-csa-c-content-id="28f5b2d0-fab0-4512-8e55-c157bfb42e19" data-csa-c-slot-id="desktop-dp-sims-1" data-csa-c-type="widget"><script>if(window.uet){window.uet('bb','p13n-desktop-carousel_DPSims_1',{wb: 1})}</script>
<style>.p13n-sc-shoveler li.a-carousel-card-empty{min-height:250px}.p13n-sc-lazy-desktop .a-carousel-viewport{min-height:244px}
._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-2__EWgCb{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-3__g3dy1{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-4__2q2cc{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-5__2l-dX{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-6__28daG{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-7__1k_Mc{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-8__1yvsR{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-9__3Pofd{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-10__mY8_7{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-carousel_style_column__2x05O{margin-right:0!important}._p13n-desktop-carousel_style_grid-row__3daT_{display:grid;grid-template-columns:repeat(auto-fit,50%)}._p13n-desktop-carousel_style_card__3H7qC{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-box-align:center;-ms-flex-align:center;align-items:center;border-bottom:1px solid #d5dbdb;border-color:#d5dbdb;border-style:solid;border-top:1px solid #d5dbdb;border-width:.5px 1px;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-flow:column;flex-flow:column;height:100%;margin-left:-1px;margin-top:-1px}
._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1:before{border-bottom-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1:after{border-top-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-body__3nkHf{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-text__3apKt{color:#fff;line-height:18px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2Z3cK{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-carousel_price_p13n-sc-price__3mJ9Z{word-wrap:normal}
._p13n-desktop-carousel_prime_p13n-prime-badge__GVM4h{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-carousel_delightPricingStyles_p13n-delight-pricing-badge__26S9Q{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-carousel_panelStyle_panel-text__3TtlT{width:220px}._p13n-desktop-carousel_panelStyle_panel-container__3ZNzh{float:left;width:238px}._p13n-desktop-carousel_panelStyle_panel-subsection__19oyW{padding-left:15px;padding-right:18px}._p13n-desktop-carousel_panelStyle_panel-logo-container__ucYMM{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-carousel_panelStyle_panel-button__GP7zd{width:auto}
._p13n-desktop-carousel_price_p13n-sc-price__bCZQt{word-wrap:normal}
._p13n-desktop-carousel_prime_p13n-prime-badge__wRb4G{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-carousel_delightPricingStyles_p13n-delight-pricing-badge__3R9NU{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7:before{border-bottom-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7:after{border-top-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-body__3iDBy{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-text__1i9QT{color:#fff;line-height:18px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2HApm{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-2__YmMc7{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-3__3xIkK{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-4__2oUlo{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-5__1Hi04{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-6__3fNYL{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-7__q6tIz{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-8__3HH-S{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-9__jEGnm{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-10__28Uvv{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-carousel_panelStyle_panel-text__1TvR6{width:220px}._p13n-desktop-carousel_panelStyle_panel-container__3UQaZ{float:left;width:238px}._p13n-desktop-carousel_panelStyle_panel-subsection__33Pdf{padding-left:15px;padding-right:18px}._p13n-desktop-carousel_panelStyle_panel-logo-container__3Gv6z{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-carousel_panelStyle_panel-button__2-jSo{width:auto}</style>
<!--CardsClient--><div id="CardInstanceEuo2lAkKAHg_V3Eda6elyA" data-card-metrics-id="p13n-desktop-carousel_DPSims_1" data-acp-params="tok=CJagDUqyopZzOfW8o8glr1W6F9CWYZxH4vXIwnV2XZ0;ts=1622846848929;rid=1KMDY2JPGP2X3R80G8WC;d1=440;d2=0;tpm=CGHBD;ref=pd_sim" data-acp-path="/acp/p13n-desktop-carousel/bcraszlmxi-y5vwu/" data-acp-tracking="{&quot;pd_rd_w&quot;:&quot;PwwXe&quot;,&quot;pf_rd_p&quot;:&quot;28f5b2d0-fab0-4512-8e55-c157bfb42e19&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;,&quot;ref_&quot;:&quot;pd_sim&quot;}"><hr aria-hidden="true" class="a-divider-normal bucketDivider"/><div class="a-section a-spacing-large bucket"><div><div data-a-carousel-options="{&quot;ajax&quot;:{&quot;id_list&quot;:[&quot;{\&quot;id\&quot;:\&quot;B0000029D9\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00002MZ2C\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&ququot;B00GC04DZK\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0757HTJCZ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01BUX7Z5I\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000028M7\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01BUX7Z6M\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00EBDXU4A\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00005B36H\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07GW4T67C\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00000JCOV\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00000099Y\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01H2ROWCK\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000XB9\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002JOH\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000024JHZ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0012GMUSQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000993\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B007YLEM3Y\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000024JN\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00004T9UF\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00004Z459\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002JR8\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0002S94OS\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B016W63BBU\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0009MAPUY\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000003TAY\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0057GYO9K\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000OSQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000HDRAWQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B083XVFM3F\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B002OFWG7E\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002LQR\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002WPI\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000021XPG\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002MP2\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00C061I3K\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07RWSH4BP\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00006RU5B\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00EBDXT9G\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000001Y7P\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B083PKY8JF\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0142XIGN8\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000025HAN\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B075VW6YBT\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07H5VVD4Z\&quot;}&quot;]},&quot;autoAdjustHeightFreescroll&quot;:true,&quot;first_item_flush_left&quot;:false,&quot;initThreshold&quot;:100,&quot;loadingThresholdPixels&quot;:100,&quot;name&quot;:&quot;p13n-sc-shoveler_w9z1i5ubq0g&quot;,&quot;nextRequestSize&quot;:6,&quot;set_size&quot;:46}" data-faceoutSpecs="{}" data-faceoutkataname="GeneralFaceout" data-individuals="0" data-language="en-CA" data-linkparameters="{&quot;pd_rd_w&quot;:&quot;PwwXe&quot;,&quot;pf_rd_p&quot;:&quot;28f5b2d0-fab0-4512-8e55-c157bfb42e19&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;}" data-marketplaceid="A2EUQ1WTGCTBG2" data-name="p13n-sc-shoveler_w9z1i5ubq0g" data-offset="6" data-reftagprefix="pd_sim" data-a-display-strategy="swap" data-a-transition-strategy="swap" data-a-ajax-strategy="promise" class="a-begin a-carousel-container a-carousel-static a-carousel-display-swap a-carousel-transition-swap p13n-sc-shoveler"><input type="hidden" autoComplete="on" class="a-carousel-firstvisibleitem"/><div class="a-row a-carousel-header-row a-size-large"><div class="a-column a-span8"><h2 class="a-carousel-heading a-inline-block">Customers who bought this item also bought</h2></div><div class="a-column a-span4 a-span-last a-text-right"><span class="a-carousel-pagination a-size-base"><span class="a-carousel-page-count">Page <span class="a-carousel-page-current">1</span> of <span class="a-carousel-page-max">1</span>  </span><span class="a-carousel-restart-container"><span class="a-text-separator"></span><a class="a-carousel-restart" href="#">Start over</a></span><span class="a-carousel-accessibility-page-info a-offscreen" aria-live="polite">Page 1 of 1  </span></span></div></div><div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left"><a class="a-button a-button-image a-carousel-button a-carousel-goto-prevpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-previous"><span class="a-icon-alt">Previous page</span></i></span></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport"><ol class="a-carousel" role="list"><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_sim_1/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Evil Empire" src="https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_sim_1/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Evil Empire</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Rage Against The Machine</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B0000029D9/ref=pd_sim_cr_1/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">1,389</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_sim_1/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$15.48</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Battle-Angeles-Rage-Against-Machine/dp/B00002MZ2C/ref=pd_sim_2/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00002MZ2C&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="The Battle Of Los Angeles" src="https://images-na.ssl-images-amazon.com/images/I/81-vO7ZkqnL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81-vO7ZkqnL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/81-vO7ZkqnL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/81-vO7ZkqnL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Battle-Angeles-Rage-Against-Machine/dp/B00002MZ2C/ref=pd_sim_2/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00002MZ2C&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">The Battle Of Los Angeles</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Rage Against The Machine</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B00002MZ2C/ref=pd_sim_cr_2/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00002MZ2C"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">1,507</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Battle-Angeles-Rage-Against-Machine/dp/B00002MZ2C/ref=pd_sim_2/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00002MZ2C&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$13.17</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Renegades-Rage-Against-Machine/dp/B00GC04DZK/ref=pd_sim_3/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00GC04DZK&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Renegades" src="https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Renegades-Rage-Against-Machine/dp/B00GC04DZK/ref=pd_sim_3/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00GC04DZK&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Renegades</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">RAGE AGAINST THE MACHINE</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.7 out of 5 stars" href="/product-reviews/B00GC04DZK/ref=pd_sim_cr_3/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00GC04DZK"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">780</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Renegades-Rage-Against-Machine/dp/B00GC04DZK/ref=pd_sim_3/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B00GC04DZK&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$11.76</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Master-Puppets-Remastered-Metallica/dp/B0757HTJCZ/ref=pd_sim_4/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0757HTJCZ&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Master Of Puppets Remastered" src="https://images-na.ssl-images-amazon.com/images/I/81hryXAVZjL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81hryXAVZjL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/81hryXAVZjL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/81hryXAVZjL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Master-Puppets-Remastered-Metallica/dp/B0757HTJCZ/ref=pd_sim_4/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0757HTJCZ&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Master Of Puppets Remastered</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Metallica</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.7 out of 5 stars" href="/product-reviews/B0757HTJCZ/ref=pd_sim_cr_4/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0757HTJCZ"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">4,182</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Master-Puppets-Remastered-Metallica/dp/B0757HTJCZ/ref=pd_sim_4/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0757HTJCZ&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$15.00</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Kill-Em-All-Remastered-Cd-Metallica/dp/B01BUX7Z5I/ref=pd_sim_5/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B01BUX7Z5I&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Kill &#x27;Em All-Remastered Cd" src="https://images-na.ssl-images-amazon.com/images/I/71LExQVFRRL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71LExQVFRRL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/71LExQVFRRL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/71LExQVFRRL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Kill-Em-All-Remastered-Cd-Metallica/dp/B01BUX7Z5I/ref=pd_sim_5/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B01BUX7Z5I&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Kill &#x27;Em All-Remastered Cd</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Metallica</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B01BUX7Z5I/ref=pd_sim_cr_5/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B01BUX7Z5I"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">2,973</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Kill-Em-All-Remastered-Cd-Metallica/dp/B01BUX7Z5I/ref=pd_sim_5/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B01BUX7Z5I&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$15.00</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Dirt-Alice-Chains/dp/B0000028M7/ref=pd_sim_6/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000028M7&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Dirt" src="https://images-na.ssl-images-amazon.com/images/I/81g0YcT68pL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81g0YcT68pL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/81g0YcT68pL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/81g0YcT68pL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Dirt-Alice-Chains/dp/B0000028M7/ref=pd_sim_6/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000028M7&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Dirt</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Alice In Chains</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B0000028M7/ref=pd_sim_cr_6/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000028M7"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">2,416</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Dirt-Alice-Chains/dp/B0000028M7/ref=pd_sim_6/138-4669640-7712440?pd_rd_w=PwwXe&amp;pf_rd_p=28f5b2d0-fab0-4512-8e55-c157bfb42e19&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000028M7&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$14.63</span></span></a></div></li></ol></div></div><div class="a-carousel-col a-carousel-right"><a class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-next"><span class="a-icon-alt">Next page</span></i></span></a></div></div></div><span class="a-end aok-hidden"></span></div></div></div></div><script>if(window.uet){window.uet('be','p13n-desktop-carousel_DPSims_1',{wb: 1})}</script>
<script>P.when('mix:@amzn/mix.client-runtime', 'mix:p13n-desktop-carousel__Rxg3G7zq').execute(function (runtime, cardModule) {runtime.registerCardFactory('CardInstanceEuo2lAkKAHg_V3Eda6elyA', cardModule).then(function(){if(window.uex){window.uex('ld','p13n-desktop-carousel_DPSims_1',{wb: 1})}});});
</script>
<script>P.load.js('https://images-na.ssl-images-amazon.com/images/I/11tq73uW3vL.js?xcp');
</script>
</div>


</div><div cel_widget_id='sims-consolidated-3_csm_instrumentation_wrapper' class='celwidget'>
<div class="celwidget pd_rd_w-zLUWs pf_rd_p-431490c2-f123-449b-9c73-90456a348c29 pf_rd_r-1KMDY2JPGP2X3R80G8WC pd_rd_r-34c0e605-14a5-40b3-bf38-60ac9a8deafe pd_rd_wg-CqCH6 c-f" cel_widget_id="p13n-desktop-carousel_DPSims_2" data-csa-c-content-id="431490c2-f123-449b-9c73-90456a348c29" data-csa-c-slot-id="desktop-dp-sims-2" data-csa-c-type="widget"><script>if(window.uet){window.uet('bb','p13n-desktop-carousel_DPSims_2',{wb: 1})}</script>
<style>.p13n-sc-shoveler li.a-carousel-card-empty{min-height:250px}.p13n-sc-lazy-desktop .a-carousel-viewport{min-height:244px}
._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-2__EWgCb{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-3__g3dy1{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-4__2q2cc{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-5__2l-dX{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-6__28daG{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-7__1k_Mc{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-8__1yvsR{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-9__3Pofd{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-10__mY8_7{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-carousel_style_column__2x05O{margin-right:0!important}._p13n-desktop-carousel_style_grid-row__3daT_{display:grid;grid-template-columns:repeat(auto-fit,50%)}._p13n-desktop-carousel_style_card__3H7qC{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-box-align:center;-ms-flex-align:center;align-items:center;border-bottom:1px solid #d5dbdb;border-color:#d5dbdb;border-style:solid;border-top:1px solid #d5dbdb;border-width:.5px 1px;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-flow:column;flex-flow:column;height:100%;margin-left:-1px;margin-top:-1px}
._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1:before{border-bottom-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1:after{border-top-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-body__3nkHf{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-text__3apKt{color:#fff;line-height:18px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2Z3cK{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-carousel_price_p13n-sc-price__3mJ9Z{word-wrap:normal}
._p13n-desktop-carousel_prime_p13n-prime-badge__GVM4h{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-carousel_delightPricingStyles_p13n-delight-pricing-badge__26S9Q{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-carousel_panelStyle_panel-text__3TtlT{width:220px}._p13n-desktop-carousel_panelStyle_panel-container__3ZNzh{float:left;width:238px}._p13n-desktop-carousel_panelStyle_panel-subsection__19oyW{padding-left:15px;padding-right:18px}._p13n-desktop-carousel_panelStyle_panel-logo-container__ucYMM{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-carousel_panelStyle_panel-button__GP7zd{width:auto}
._p13n-desktop-carousel_price_p13n-sc-price__bCZQt{word-wrap:normal}
._p13n-desktop-carousel_prime_p13n-prime-badge__wRb4G{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-carousel_delightPricingStyles_p13n-delight-pricing-badge__3R9NU{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7:before{border-bottom-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7:after{border-top-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-body__3iDBy{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-text__1i9QT{color:#fff;line-height:18px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2HApm{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-2__YmMc7{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-3__3xIkK{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-4__2oUlo{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-5__1Hi04{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-6__3fNYL{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-7__q6tIz{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-8__3HH-S{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-9__jEGnm{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-10__28Uvv{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-carousel_panelStyle_panel-text__1TvR6{width:220px}._p13n-desktop-carousel_panelStyle_panel-container__3UQaZ{float:left;width:238px}._p13n-desktop-carousel_panelStyle_panel-subsection__33Pdf{padding-left:15px;padding-right:18px}._p13n-desktop-carousel_panelStyle_panel-logo-container__3Gv6z{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-carousel_panelStyle_panel-button__2-jSo{width:auto}</style>
<!--CardsClient--><div id="CardInstancecnIdtudeKzd9GxpAt7aU3A" data-card-metrics-id="p13n-desktop-carousel_DPSims_2" data-acp-params="tok=iAZlpcGagVcbZheq7YaDuHqROJLSjds3_eayWhrz5ik;ts=1622846848920;rid=1KMDY2JPGP2X3R80G8WC;d1=440;d2=0;tpm=CGHBD;ref=pd_vtp" data-acp-path="/acp/p13n-desktop-carousel/bcraszlmxi-y5vwu/" data-acp-tracking="{&quot;pd_rd_w&quot;:&quot;zLUWs&quot;,&quot;pf_rd_p&quot;:&quot;431490c2-f123-449b-9c73-90456a348c29&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;,&quot;ref_&quot;:&quot;pd_vtp&quot;}"><hr aria-hidden="true" class="a-divider-normal bucketDivider"/><div class="a-section a-spacing-large bucket"><div><div data-a-carousel-options="{&quot;ajax&quot;:{&quot;id_list&quot;:[&quot;{\&quot;id\&quot;:\&quot;B07DV8WT6R\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000029D9\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07DVGQJMY\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07DV5M3LS\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07YTDF3XL\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000OU2\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00M30T9F2\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000088DC\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B001U7WUW8\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01BUX7Z5I\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07FSVYRXJ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01BUX7Z6M\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B072WJVDB6\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00005B36H\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07GW4T67C\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B003C1AL7G\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B004OKFISQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000028M7\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B075STW6HV\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00IXLQJ8U\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01L2ZS87S\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002WPH\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00F5YTHYQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00000098N\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01LTHKKAM\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00IXHBMLS\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07NYBGBGV\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01I23QZ7I\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B081WVBKK9\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01CJD63BK\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000XB8\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00M30VKWM\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000993\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000089RV6\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07S3D966F\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00O67EPP4\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00Y4FOU9Y\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07T5R6697\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01LTHN0DG\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0007OY3UC\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0714QLYLB\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00JPV5GA4\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000027RL\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00004WP7P\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00EBDXU4A\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01LTHMF1Y\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B005STGJHQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01EN1ZNHQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000DJYPB\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00004WNFZ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000057DOV\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07Z75ZRSL\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B002OHB3IK\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00GMVZGGO\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00025742A\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00IXHBUG0\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01B2M9H76\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000V7J82S\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00WASEEW0\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B076VHQCSL\&quot;}&quot;]},&quot;autoAdjustHeightFreescroll&quot;:true,&quot;first_item_flush_left&quot;:false,&quot;initThreshold&quot;:100,&quot;loadingThresholdPixels&quot;:100,&quot;name&quot;:&quot;p13n-sc-shoveler_bdisintdrew&quot;,&quot;nextRequestSize&quot;:6,&quot;set_size&quot;:60}" data-faceoutSpecs="{}" data-faceoutkataname="GeneralFaceout" data-individuals="0" data-language="en-CA" data-linkparameters="{&quot;pd_rd_w&quot;:&quot;zLUWs&quot;,&quot;pf_rd_p&quot;:&quot;431490c2-f123-449b-9c73-90456a348c29&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;}" data-marketplaceid="A2EUQ1WTGCTBG2" data-name="p13n-sc-shoveler_bdisintdrew" data-offset="6" data-reftagprefix="pd_vtp" data-a-display-strategy="swap" data-a-transition-strategy="swap" data-a-ajax-strategy="promise" class="a-begin a-carousel-container a-carousel-static a-carousel-display-swap a-carousel-transition-swap p13n-sc-shoveler"><input type="hidden" autoComplete="on" class="a-carousel-firstvisibleitem"/><div class="a-row a-carousel-header-row a-size-large"><div class="a-column a-span8"><h2 class="a-carousel-heading a-inline-block">What other items do customers buy after viewing this item?</h2></div><div class="a-column a-span4 a-span-last a-text-right"><span class="a-carousel-pagination a-size-base"><span class="a-carousel-page-count">Page <span class="a-carousel-page-current">1</span> of <span class="a-carousel-page-max">1</span>  </span><span class="a-carousel-restart-container"><span class="a-text-separator"></span><a class="a-carousel-restart" href="#">Start over</a></span><span class="a-carousel-accessibility-page-info a-offscreen" aria-live="polite">Page 1 of 1  </span></span></div></div><div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left"><a class="a-button a-button-image a-carousel-button a-carousel-goto-prevpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-previous"><span class="a-icon-alt">Previous page</span></i></span></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport"><ol class="a-carousel" role="list"><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Battle-Los-Angeles-Vinyl/dp/B07DV8WT6R/ref=pd_vtp_1/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV8WT6R&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="The Battle Of Los Angeles (Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/71CgqwZKPCL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71CgqwZKPCL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/71CgqwZKPCL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/71CgqwZKPCL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Battle-Los-Angeles-Vinyl/dp/B07DV8WT6R/ref=pd_vtp_1/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV8WT6R&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">The Battle Of Los Angeles (Vinyl)</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Rage Against The Machine</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B07DV8WT6R/ref=pd_vtp_cr_1/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV8WT6R"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">1,507</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">LP Record</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Battle-Los-Angeles-Vinyl/dp/B07DV8WT6R/ref=pd_vtp_1/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV8WT6R&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$32.42</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_vtp_2/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Evil Empire" src="https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/71wiTg29ZvL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_vtp_2/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Evil Empire</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Rage Against The Machine</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B0000029D9/ref=pd_vtp_cr_2/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">1,389</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">Audio CD</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Evil-Empire-Rage-Against-Machine/dp/B0000029D9/ref=pd_vtp_2/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B0000029D9&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$15.48</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Renegades-Vinyl-Rage-Against-Machine/dp/B07DVGQJMY/ref=pd_vtp_3/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DVGQJMY&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Renegades (Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/61Uqi1x+O2L._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Renegades-Vinyl-Rage-Against-Machine/dp/B07DVGQJMY/ref=pd_vtp_3/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DVGQJMY&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Renegades (Vinyl)</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Rage Against The Machine</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.7 out of 5 stars" href="/product-reviews/B07DVGQJMY/ref=pd_vtp_cr_3/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DVGQJMY"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">780</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">LP Record</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Renegades-Vinyl-Rage-Against-Machine/dp/B07DVGQJMY/ref=pd_vtp_3/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DVGQJMY&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$39.76</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Live-Grand-Olympic-Auditorium-Vinyl/dp/B07DV5M3LS/ref=pd_vtp_4/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV5M3LS&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Live at the Grand Olympic Auditorium (Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/71+jnhO+PAL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71+jnhO+PAL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/71+jnhO+PAL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/71+jnhO+PAL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Live-Grand-Olympic-Auditorium-Vinyl/dp/B07DV5M3LS/ref=pd_vtp_4/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV5M3LS&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Live at the Grand Olympic Auditorium (Vinyl)</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Rage Against The Machine</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.9 out of 5 stars" href="/product-reviews/B07DV5M3LS/ref=pd_vtp_cr_4/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV5M3LS"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.9 out of 5 stars</span></i> <span class="a-size-small">173</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">LP Record</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Live-Grand-Olympic-Auditorium-Vinyl/dp/B07DV5M3LS/ref=pd_vtp_4/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07DV5M3LS&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$39.51</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Songs-Deaf-Vinyl-Queens-Stone/dp/B07YTDF3XL/ref=pd_vtp_5/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07YTDF3XL&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Songs For The Deaf (2LP Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/61YqbPSJpqL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/61YqbPSJpqL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/61YqbPSJpqL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/61YqbPSJpqL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Songs-Deaf-Vinyl-Queens-Stone/dp/B07YTDF3XL/ref=pd_vtp_5/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07YTDF3XL&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Songs For The Deaf (2LP Vinyl)</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Queens Of The Stone Age</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B07YTDF3XL/ref=pd_vtp_cr_5/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07YTDF3XL"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">2,120</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">LP Record</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Songs-Deaf-Vinyl-Queens-Stone/dp/B07YTDF3XL/ref=pd_vtp_5/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B07YTDF3XL&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$39.82</span></span></a></div></li><li class="a-carousel-card" style="width:160px" role="listitem"><a class="a-link-normal" href="/Unplugged-N-Y-Vinyl-Nirvana/dp/B000000OU2/ref=pd_vtp_6/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B000000OU2&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Unplugged In N.Y. (Vinyl)" src="https://images-na.ssl-images-amazon.com/images/I/81vS+wfdozL._AC_UL160_SR160,160_.jpg" class="a-dynamic-image p13n-sc-dynamic-image" height="160px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81vS+wfdozL._AC_UL160_SR160,160_.jpg&quot;:[160,160],&quot;https://images-na.ssl-images-amazon.com/images/I/81vS+wfdozL._AC_UL320_SR320,320_.jpg&quot;:[320,320],&quot;https://images-na.ssl-images-amazon.com/images/I/81vS+wfdozL._AC_UL480_SR480,480_.jpg&quot;:[480,480]}" style="max-width:160px;max-height:160px"/></div></a><a class="a-link-normal" href="/Unplugged-N-Y-Vinyl-Nirvana/dp/B000000OU2/ref=pd_vtp_6/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B000000OU2&amp;psc=1"><span><div class="p13n-sc-truncate p13n-sc-truncate-desktop-type2 p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">Unplugged In N.Y. (Vinyl)</div></span></a><div class="a-row a-size-small"><span class="a-size-small a-color-base"><div class="_p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6">Nirvana</div></span></div><div class="a-row"><div class="a-icon-row"><a class="a-link-normal" title="4.8 out of 5 stars" href="/product-reviews/B000000OU2/ref=pd_vtp_cr_6/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B000000OU2"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">4,323</span></a></div></div><div class="a-row a-size-small"><span class="a-size-small a-color-secondary a-text-normal">LP Record</span></div><div class="a-row"><a class="a-link-normal a-text-normal" href="/Unplugged-N-Y-Vinyl-Nirvana/dp/B000000OU2/ref=pd_vtp_6/138-4669640-7712440?pd_rd_w=zLUWs&amp;pf_rd_p=431490c2-f123-449b-9c73-90456a348c29&amp;pf_rd_r=1KMDY2JPGP2X3R80G8WC&amp;pd_rd_r=34c0e605-14a5-40b3-bf38-60ac9a8deafe&amp;pd_rd_wg=CqCH6&amp;pd_rd_i=B000000OU2&amp;psc=1"><span class="a-size-base a-color-price"><span class="_p13n-desktop-carousel_price_p13n-sc-price__bCZQt">$34.36</span></span></a></div></li></ol></div></div><div class="a-carousel-col a-carousel-right"><a class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-next"><span class="a-icon-alt">Next page</span></i></span></a></div></div></div><span class="a-end aok-hidden"></span></div></div></div></div><script>if(window.uet){window.uet('be','p13n-desktop-carousel_DPSims_2',{wb: 1})}</script>
<script>P.when('mix:@amzn/mix.client-runtime', 'mix:p13n-desktop-carousel__Rxg3G7zq').execute(function (runtime, cardModule) {runtime.registerCardFactory('CardInstancecnIdtudeKzd9GxpAt7aU3A', cardModule).then(function(){if(window.uex){window.uex('ld','p13n-desktop-carousel_DPSims_2',{wb: 1})}});});
</script>
<script>P.load.js('https://images-na.ssl-images-amazon.com/images/I/11tq73uW3vL.js?xcp');
</script>
</div>


</div><div cel_widget_id='dpx-detail-bullets_csm_instrumentation_wrapper' class='celwidget'>








  



  



        
        
        
        
  








    


















<div id="detailBullets_feature_div" class="celwidget" data-feature-name="detailBullets">












<style type="text/css">
.detail-bullets-wrapper ul.detail-bullet-list {
margin: 0 0 1px 18px;
}
.detail-bullets-wrapper ul li {
margin-bottom: 5.5px;
}
.detail-bullets-wrapper:last-child {
margin-bottom: 4.5px;
}
</style>

<div id="detailBulletsWrapper_feature_div" data-feature-name="detailBullets" data-template-name="detailBullets" class="a-section feature detail-bullets-wrapper bucket">
<hr aria-hidden="true" class="a-divider-normal bucketDivider"/>
<h2>Product details</h2>
<span class="disclaim">





</span>
<div id="detailBullets_feature_div">







<ul class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list">








<li><span class="a-list-item">
<span class="a-text-bold">Is Discontinued By Manufacturer



:


</span>
<span>No</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">Product Dimensions



:


</span>
<span>14.27 x 12.5 x 0.84 cm; 108.86 Grams</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">Manufacturer



:


</span>
<span>Sony Music Canada Entertainment Inc.</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">Manufacturer reference



:


</span>
<span>MFR074645295923#VG</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">Original Release Date



:


</span>
<span>1992</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">Run time



:


</span>
<span>53 minutes</span>
</span></li>

























<li><span class="a-list-item">
<span class="a-text-bold">Label



:


</span>
<span>Sony Music Canada Entertainment Inc.</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">ASIN



:


</span>
<span>B0000028RR</span>
</span></li>









<li><span class="a-list-item">
<span class="a-text-bold">Number of discs



:


</span>
<span>1</span>
</span></li>







</ul>


</div>
<ul class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list">




<li><span class="a-list-item">



<span class="a-text-bold">
Best Sellers Rank:
</span>
#45,205 in Music (<a href='/gp/bestsellers/music/ref=pd_zg_ts_music'>See Top 100 in Music</a>)
<ul class="a-unordered-list a-nostyle a-vertical zg_hrsr">

<li><span class="a-list-item"> #79 in <a href='/gp/bestsellers/music/1033788/ref=pd_zg_hrsr_music'>Rap Rock Music</a></span></li>

<li><span class="a-list-item"> #747 in <a href='/gp/bestsellers/music/1033836/ref=pd_zg_hrsr_music'>Alternative Metal</a></span></li>

<li><span class="a-list-item"> #1,496 in <a href='/gp/bestsellers/music/1033786/ref=pd_zg_hrsr_music'>Pop Rap</a></span></li>

</ul>



</span></li>



</ul>
<ul class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list">

<li><span class="a-list-item">
<span class="a-text-bold">
Customer Reviews:
</span>

<style type="text/css">
/*
* Fix for UDP-1061. Average customer reviews has a small extra line on hover
* https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40
*/
.noUnderline a:hover {
text-decoration: none;
}
</style>



















<div id="detailBullets_averageCustomerReviews" data-asin="B0000028RR" data-ref="dpx_acr_pop_" >












<span class="a-declarative" data-action="acrStarsLink-click-metrics" data-acrStarsLink-click-metrics="{}">



<span id="acrPopover" class="reviewCountTextLinkedHistogram noUnderline" title="4.7 out of 5 stars">
<span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;url&quot;:&quot;/gp/customer-reviews/widgets/average-customer-review/popover/ref=dpx_acr_pop_?contextId=dpx&amp;asin=B0000028RR&quot;}">
<a href="javascript:void(0)" class="a-popover-trigger a-declarative">

<i class="a-icon a-icon-star a-star-4-5"><span class="a-icon-alt">4.7 out of 5 stars</span></i>

<i class="a-icon a-icon-popover"></i></a>
</span>
<span class="a-letter-space"></span>
</span>



</span>
<span class="a-letter-space"></span>












<span class="a-declarative" data-action="acrLink-click-metrics" data-acrLink-click-metrics="{}">
<a id="acrCustomerReviewLink" class="a-link-normal" href="#customerReviews">
<span id="acrCustomerReviewText" class="a-size-base">3,129 ratings</span>
</a>
</span>
<script type="text/javascript">
P.when('A', 'ready').execute(function(A) {
A.declarative('acrLink-click-metrics', 'click', { "allowLinkDefault" : true }, function(event){
if(window.ue) {
ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1);
}
});
});
</script>





<script type="text/javascript">
P.when('A', 'cf').execute(function(A) {
A.declarative('acrStarsLink-click-metrics', 'click', { "allowLinkDefault" : true },  function(event){
if(window.ue) {
ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1);
}
});
});
</script>







</div>



</span></li>

</ul>
<div class="a-row">




</div>
<div class="a-row">





</div>
</div>






















</div></div><div cel_widget_id='dpx-btf-productDocuments_csm_instrumentation_wrapper' class='celwidget'>




  



        
        
        
        
  








    



 
 
 
 
 
<div id="productDocuments_feature_div" class="celwidget" data-feature-name="productDocuments">













<style>
.ask-product-docs-expander-content {
padding-left: 0;
margin-top: 0;
}
</style>




























</div></div><div cel_widget_id='dpx-legal_csm_instrumentation_wrapper' class='celwidget'>




  



        
        
        
        
  








    








<div id="legal_feature_div" class="celwidget" data-feature-name="legal">




































</div></div>


    
    
<style type="text/css"><!--
.listRowEven {
  background-color: #EEF1F6;
  vertical-align: middle;
}

.listRowOdd {
  background-color: #fff;
  vertical-align: middle;
}

td.listen {
  text-align: center;
  width: 66px;
}

.sampleTracksHeader th {
  padding-top: 1.5em;
}

th.discNumber {
  font-weight: bold;
  text-align: left;
}
--></style>





<script language="Javascript1.1" type="text/javascript">
<!--

  var winArgs = 'width=820,height=550,resizable=yes,scrollbars=no';
        var winName = 'krex';

        function krexLink(url){
                var link = '<a href="javascript:amz_js_PopWin(' + "'" + url + "'" + ',winName,winArgs);void(0);">';
                return link;
        }

var browserRadioTest = null;

function browserHasRadio() {
        if(browserRadioTest == null) {
            browserRadioTest = false;
        }
        return browserRadioTest;
}

//-->
</script>







<hr noshade="noshade" size="1" class="bucketDivider" />
<div class="bucket" id="musicTracksFeature">
<noscript><h2 id='NonJSMusicTracksHeader'>Track Listings</h2></noscript>
<h2 style='display:none' id='MusicTracksHeader'>Track Listings</h2>
<div class="content">
<div id='MusicTracksText' style='display:none'>
</div> 
<script language="JavaScript" type="text/javascript">
	document.getElementById('MusicTracksHeader').style.display = 'inline';
	document.getElementById('MusicTracksText').style.display = 'inline';
</script>
<table cellspacing="1" cellpadding="3" border="0"><tbody>



<tr class="listRowEven">
<td>

1. Bombtrack
</td>
</tr>



<tr class="listRowOdd">
<td>

2. Killing In the Name
</td>
</tr>



<tr class="listRowEven">
<td>

3. Take the Power Back
</td>
</tr>



<tr class="listRowOdd">
<td>

4. Settle for Nothing
</td>
</tr>



<tr class="listRowEven">
<td>

5. Bullet In the Head
</td>
</tr>



<tr class="listRowOdd">
<td>

6. Know Your Enemy
</td>
</tr>



<tr class="listRowEven">
<td>

7. Wake Up
</td>
</tr>



<tr class="listRowOdd">
<td>

8. Fistful of Steel
</td>
</tr>



<tr class="listRowEven">
<td>

9. Township Rebellion
</td>
</tr>



<tr class="listRowOdd">
<td>

10. Freedom
</td>
</tr>
</tbody></table>
</div> 
</div> 






































<div cel_widget_id='dpx-product-description_csm_instrumentation_wrapper' class='celwidget'>




  



        
        
        
        
  








    








<div id="biss-product-description-and-details"></div>
<div id="descriptionAndDetails" class="a-section a-spacing-extra-large">
    <div id="productDescription_feature_div" class="celwidget" data-feature-name="productDescription">












<div>


<div data-feature-name="productDescription" data-template-name="productDescription" id="productDescription_feature_div" class="a-row feature">



<div class="a-divider a-divider-section"><div class="a-divider-inner"></div></div>


<h2 class="default">
Product description

</h2>








<div id="productDescription" class="a-section a-spacing-small">














<!-- show up to 2 reviews by default -->





<h3>Product description</h3>








<p>Previously Enjoyed & Fully Guaranteed<br />

</p>










<h3>Amazon.ca</h3>








<p>Not since the days of the Clash and the MC5 has rock seen such political force as in the uncompromising debut from this L.A. quartet. Expanding the hip-hop/metal style of bands such as the Red Hot Chili Peppers, Rage tap the spirits of vintage Black Sabbath and Led Zeppelin, coupled with hardcore punk intensity and Public Enemy-style grooves. "Bombtrack" opens the LP with a shot of adrenaline and singer Zack de la Rocha's infuriated chorus of "Burn, burn, yes, you're gonna burn!" The intensity doesn't let up an inch on the militant "Killing in the Name" (with the inspiring chant, "Fuck you, I won't do what you tell me!"), the ultrafunky "Bullet in the Head," and the engrossing "Fistful of Steel." Tom Morello combines time-honored metal guitar riffs with sounds that suggest a hip-hop scratcher over a rhythm section that simply takes no prisoners. Intelligent and aggressive, this is unimpeachably one of the best hard-rock records ever made. <i>--James Rotondi</i>

</p>








</div>

<style type="text/css">
#productDescription {
color: #333333;
word-wrap: break-word;
font-size: small;
line-height: initial;
margin: 0.5em 0px 0em 25px;
}

#productDescription_feature_div > h2.default {
color: #CC6600;
font-size: medium;
margin: 0 0 0.25em;
}
#productDescription_feature_div > h2.books {
color:#333 !important;
font-size:21px !important;
line-height: 1.3;
padding-bottom: 4px;
font-weight: normal;
margin: 0px;
}
#productDescription_feature_div > h2.softlines {
color:#333 !important;
font-size:21px !important;
line-height: 1.3;
padding-bottom: 4px;
font-weight: bold;
margin: 0px;
}
#productDescription > p, #productDescription > div, #productDescription > table {
margin: 0 0 1em 0;
}
#productDescription p {
margin: 0em 0 1em 1em;
}
#productDescription h3 {
font-weight: normal;
color: #333333;
font-size: 1.23em;
clear: left;
margin: 0.75em 0px 0.375em -15px;
}
#productDescription table {
border-collapse: inherit !important;
margin-bottom: 0;
}
#productDescription table img {
max-width: inherit !important;
}
#productDescription table td {
font-size: small;
vertical-align: inherit !important;
}
#productDescription ul li {
margin: 0 0 0 20px;
}
#productDescription ul li ul {
list-style-type: disc !important;
margin-left: 20px !important;
}
#productDescription ul ul li {
list-style-type: disc !important;
margin-left: 20px !important;
}
#productDescription > ul ul li {
list-style-type: disc !important;
}
#productDescription ul li ul li {
margin: 0 0 0 20px;
}
#productDescription .aplus p {
margin: 0 0 1em 0;
}
#productDescription small {
font-size: smaller;
}
#productDescription.prodDescWidth {
max-width: 1000px
}
</style>
<!-- Used to set table width because AUI is overriding the width attribute of the tables coming in description -->
<script type="text/javascript">
P.when('jQuery').execute(function($){
$("#productDescription table").each(function() {
var width = $(this).attr('width');
if (width) width += 'px';
else width = 'auto';
$(this).css('width', width);
var padding = $(this).attr('cellpadding');
if (padding) padding += 'px';
else padding = '0px';
$(this).css('padding', padding);
});
});
</script>

<style>
#productDescription h3 {
margin: 0.75em 0px 0.375em -1px;
}
</style>







</div>

</div>






















</div>
</div>
</div>




  



        
        
        
        
  








    

















  



        
        
        
        
  








    

















  



        
        
        
        
  








    













<div cel_widget_id='sims-consolidated-4_csm_instrumentation_wrapper' class='celwidget'>
<div class="celwidget pd_rd_w-6twY9 pf_rd_p-4ffa7419-4177-4fe4-99f6-e3e50be57972 pf_rd_r-1KMDY2JPGP2X3R80G8WC pd_rd_r-34c0e605-14a5-40b3-bf38-60ac9a8deafe pd_rd_wg-CqCH6 c-f" cel_widget_id="p13n-desktop-carousel_DPSims_3" data-csa-c-content-id="4ffa7419-4177-4fe4-99f6-e3e50be57972" data-csa-c-slot-id="desktop-dp-sims-3" data-csa-c-type="widget"><script>if(window.uet){window.uet('bb','p13n-desktop-carousel_DPSims_3',{wb: 1})}</script>
<style>.p13n-sc-shoveler li.a-carousel-card-empty{min-height:250px}.p13n-sc-lazy-desktop .a-carousel-viewport{min-height:244px}
._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-2__EWgCb{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-3__g3dy1{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-4__2q2cc{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-5__2l-dX{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-6__28daG{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-7__1k_Mc{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-8__1yvsR{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-9__3Pofd{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-10__mY8_7{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-carousel_style_column__2x05O{margin-right:0!important}._p13n-desktop-carousel_style_grid-row__3daT_{display:grid;grid-template-columns:repeat(auto-fit,50%)}._p13n-desktop-carousel_style_card__3H7qC{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-box-align:center;-ms-flex-align:center;align-items:center;border-bottom:1px solid #d5dbdb;border-color:#d5dbdb;border-style:solid;border-top:1px solid #d5dbdb;border-width:.5px 1px;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-flow:column;flex-flow:column;height:100%;margin-left:-1px;margin-top:-1px}
._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1:before{border-bottom-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__1-yh1:after{border-top-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-body__3nkHf{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-text__3apKt{color:#fff;line-height:18px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2Z3cK{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-carousel_price_p13n-sc-price__3mJ9Z{word-wrap:normal}
._p13n-desktop-carousel_prime_p13n-prime-badge__GVM4h{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-carousel_delightPricingStyles_p13n-delight-pricing-badge__26S9Q{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-carousel_panelStyle_panel-text__3TtlT{width:220px}._p13n-desktop-carousel_panelStyle_panel-container__3ZNzh{float:left;width:238px}._p13n-desktop-carousel_panelStyle_panel-subsection__19oyW{padding-left:15px;padding-right:18px}._p13n-desktop-carousel_panelStyle_panel-logo-container__ucYMM{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-carousel_panelStyle_panel-button__GP7zd{width:auto}
._p13n-desktop-carousel_price_p13n-sc-price__bCZQt{word-wrap:normal}
._p13n-desktop-carousel_prime_p13n-prime-badge__wRb4G{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-carousel_delightPricingStyles_p13n-delight-pricing-badge__3R9NU{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7:before{border-bottom-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-best-seller-badge__3hEN7:after{border-top-color:#c45500!important}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-body__3iDBy{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-text__1i9QT{color:#fff;line-height:18px}._p13n-desktop-carousel_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2HApm{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-2__YmMc7{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-3__3xIkK{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-4__2oUlo{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-5__1Hi04{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-6__3fNYL{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-7__q6tIz{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-8__3HH-S{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-9__jEGnm{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-carousel_truncationStyles_p13n-sc-css-line-clamp-10__28Uvv{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-carousel_panelStyle_panel-text__1TvR6{width:220px}._p13n-desktop-carousel_panelStyle_panel-container__3UQaZ{float:left;width:238px}._p13n-desktop-carousel_panelStyle_panel-subsection__33Pdf{padding-left:15px;padding-right:18px}._p13n-desktop-carousel_panelStyle_panel-logo-container__3Gv6z{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-carousel_panelStyle_panel-button__2-jSo{width:auto}</style>
<!--CardsClient--><div id="CardInstance7Ga60Mbx--KwI9_A8H65gA" data-card-metrics-id="p13n-desktop-carousel_DPSims_3" data-acp-params="tok=iAZlpcGagVcbZheq7YaDuHqROJLSjds3_eayWhrz5ik;ts=1622846848920;rid=1KMDY2JPGP2X3R80G8WC;d1=440;d2=0;tpm=CGHBD;ref=pd_hr_sbs" data-acp-path="/acp/p13n-desktop-carousel/bcraszlmxi-y5vwu/" data-acp-tracking="{&quot;pd_rd_w&quot;:&quot;6twY9&quot;,&quot;pf_rd_p&quot;:&quot;4ffa7419-4177-4fe4-99f6-e3e50be57972&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;,&quot;ref_&quot;:&quot;pd_hr_sbs&quot;}"><hr aria-hidden="true" class="a-divider-normal bucketDivider"/><div class="a-section a-spacing-large bucket p13n-sc-lazy-desktop"><div><div data-a-carousel-options="{&quot;ajax&quot;:{&quot;id_list&quot;:[&quot;{\&quot;id\&quot;:\&quot;B07DV8WT6R\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000088DC\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B075STW6HV\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000024JN\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B009G7ZYUO\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B08GPKFK6Z\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07FSVYRXJ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00M0CVYCY\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01LTHN0DG\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B072WJVDB6\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B003VPC72K\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07DV8WT6S\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000002JNJ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00004WP7P\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0714QLYLB\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00F5YTHYQ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B01BUX7Z6M\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0713M331T\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B079N1S8MK\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00MG4CVJ6\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07NNLRC6V\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00005B36H\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B001FBJUKE\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B07F6NG84L\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000000993\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B0000AZKFJ\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B002PL5GTC\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B00GC04GDO\&quot;}&quot;,&quot;{\&quot;id\&quot;:\&quot;B000024FY4\&quot;}&quot;]},&quot;autoAdjustHeightFreescroll&quot;:true,&quot;first_item_flush_left&quot;:false,&quot;initThreshold&quot;:1500,&quot;loadingThresholdPixels&quot;:100,&quot;name&quot;:&quot;p13n-sc-shoveler_6v7gnnt9j8f&quot;,&quot;nextRequestSize&quot;:6,&quot;set_size&quot;:29}" data-faceoutSpecs="{}" data-faceoutkataname="GeneralFaceout" data-individuals="0" data-language="en-CA" data-linkparameters="{&quot;pd_rd_w&quot;:&quot;6twY9&quot;,&quot;pf_rd_p&quot;:&quot;4ffa7419-4177-4fe4-99f6-e3e50be57972&quot;,&quot;pf_rd_r&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;pd_rd_r&quot;:&quot;34c0e605-14a5-40b3-bf38-60ac9a8deafe&quot;,&quot;pd_rd_wg&quot;:&quot;CqCH6&quot;}" data-marketplaceid="A2EUQ1WTGCTBG2" data-name="p13n-sc-shoveler_6v7gnnt9j8f" data-offset="0" data-reftagprefix="pd_hr_sbs" data-a-display-strategy="swap" data-a-transition-strategy="swap" data-a-ajax-strategy="promise" class="a-begin a-carousel-container a-carousel-static a-carousel-display-swap a-carousel-transition-swap p13n-sc-shoveler"><input type="hidden" autoComplete="on" class="a-carousel-firstvisibleitem"/><div class="a-row a-carousel-header-row a-size-large"><div class="a-column a-span8"><h2 class="a-carousel-heading a-inline-block">Highly rated by customers</h2></div><div class="a-column a-span4 a-span-last a-text-right"><span class="a-carousel-pagination a-size-base"><span class="a-carousel-page-count">Page <span class="a-carousel-page-current">1</span> of <span class="a-carousel-page-max">1</span>  </span><span class="a-carousel-restart-container"><span class="a-text-separator"></span><a class="a-carousel-restart" href="#">Start over</a></span><span class="a-carousel-accessibility-page-info a-offscreen" aria-live="polite">Page 1 of 1  </span></span></div></div><div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left"><a class="a-button a-button-image a-carousel-button a-carousel-goto-prevpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-previous"><span class="a-icon-alt">Previous page</span></i></span></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport"><ol class="a-carousel" role="list"></ol></div></div><div class="a-carousel-col a-carousel-right"><a class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-next"><span class="a-icon-alt">Next page</span></i></span></a></div></div></div><span class="a-end aok-hidden"></span></div></div></div></div><script>if(window.uet){window.uet('be','p13n-desktop-carousel_DPSims_3',{wb: 1})}</script>
<script>P.when('mix:@amzn/mix.client-runtime', 'mix:p13n-desktop-carousel__Rxg3G7zq').execute(function (runtime, cardModule) {runtime.registerCardFactory('CardInstance7Ga60Mbx--KwI9_A8H65gA', cardModule).then(function(){if(window.uex){window.uex('ld','p13n-desktop-carousel_DPSims_3',{wb: 1})}});});
</script>
<script>P.load.js('https://images-na.ssl-images-amazon.com/images/I/11tq73uW3vL.js?xcp');
</script>
</div>


</div><div cel_widget_id='dpx-sponsored-products-detail_csm_instrumentation_wrapper' class='celwidget'>




  



        
        
        
        
  








    



<div id="sponsoredProducts2_feature_div" class="celwidget" data-feature-name="sponsoredProducts2">











<div cel_widget_id='sp_detail2' class='celwidget'> <style> .sp_large_format_widgetTitle_asinImage_spacing {     margin-bottom: 40px; } .sp_large_format_asinImage_productDescription_spacing {     margin-bottom: 30px; } .sp_large_format_carousel {     height: 461px; } .sp_large_format_offerVertical {     min-height: 375px; } .sp_book_carousel_header {     margin-bottom: 10px; } .sp_badge_spacing_above_image {     margin-top: 0px;     margin-bottom: 5px; } .sp_badge_spacing_below_image {     margin-top: 6px;     margin-bottom: 6px; } .sp_invisible_badge {     visibility: hidden; } .sp_prime_wardrobe_badge {     position: relative;     top: 2px; } .sp_softline_brand_line {     margin-top: 16px;     font-size: 16px;     color: #555555;     margin-bottom: 12px;     display: inline-block; } .sp_softline_oneline_title {     white-space: nowrap;     overflow: hidden;     text-overflow: ellipsis; } .sp_softline_large_image_container {     padding-top: 130%;     position: relative;     margin-bottom: 4px; } .sp_softline_large_image_faceout {     position: absolute;     max-width: 100%;     max-height: 100%;     margin: auto;     top: 0;     bottom: 0;     left: 0;     right: 0; } .unified_ad_labeling_title_margin {     margin-bottom: 0; } .sp_desktop_sponsored_label {     line-height: 23px;     font-family: AmazonEmber,"Amazon Ember",Arial,sans-serif;     font-weight: normal;     margin-bottom: 4px !important; } </style> <style> .sp_amazon_certified_text {     font-size: 13px;     color: #C45500; } .sp_works_with_alexa {     font-size: 13px;     color: #111111; } </style>           <style>     .sp-customer-benefit-message {         color:#565959;         font-size:12px;         font-family:'Amazon Ember',Arial,sans-serif;         line-height:15px;     } </style>                                                                              <script type="a-state" data-a-state="{&quot;key&quot;:&quot;SpViewabilityConfigState&quot;}">{"eelEndpoint":"https://unagi-na.amazon.com/1/events/com.amazon.eel.SponsoredProductsEventTracking.prod"}</script>                                                                                                                                             <hr aria-hidden="true" class="a-divider-normal bucketDivider"/>                                                                                      <div id="sp_detail2" data-a-carousel-options="{&quot;initialSeenAsins&quot;:[&quot;B08QCNRKR6&quot;,&quot;B08DS4TXJ2&quot;,&quot;B07KNZKRDV&quot;,&quot;B07H3KDSWZ&quot;,&quot;B01HRJ9NAY&quot;,&quot;B00WJMQTX4&quot;,&quot;B086H1TMSZ&quot;,&quot;B08YXC6JYS&quot;,&quot;B004D8KX7K&quot;],&quot;set_size&quot;:9,&quot;name&quot;:&quot;sp_detail2_carousel&quot;,&quot;auto_adjust_height&quot;:&quot;true&quot;,&quot;circular&quot;:false,&quot;ajax&quot;:{&quot;params&quot;:{&quot;cc&quot;:9,&quot;widgetLocale&quot;:&quot;en_CA&quot;,&quot;wName&quot;:&quot;sp_detail2&quot;,&quot;isMultiPlacementRequest&quot;:true,&quot;doNotShowProductAttributes&quot;:false,&quot;start&quot;:9,&quot;ASIN&quot;:&quot;B0000028RR&quot;,&quot;pRID&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;isPantry&quot;:0,&quot;slateToken&quot;:&quot;AQF52TW6pl0RIQFSRaln24N7Un6UUa17Svt0rq7MLre75xsZVgWxZhCZRAAAAAgGcmV0YWlsCWFtYXpvbi5jYQ==&quot;,&quot;isFresh&quot;:0},&quot;url&quot;:&quot;/gp/nemo/spd/handlers/spd-shov.html&quot;}}" data-p13n-feature-metadata="{&quot;baseAsin&quot;:&quot;B0000028RR&quot;}" data-p13n-feature-name="sp_detail2" data-p13n-global="{&quot;auiDeviceType&quot;:&quot;desktop&quot;,&quot;marketplaceId&quot;:183231706255110,&quot;marketplace&quot;:&quot;CA&quot;,&quot;requestId&quot;:&quot;1KMDY2JPGP2X3R80G8WC&quot;,&quot;session&quot;:&quot;138-4669640-7712440&quot;}" data-a-display-strategy="swap" data-a-transition-strategy="swap" data-a-ajax-strategy="clicksCustomAjax" class="a-begin a-carousel-container a-carousel-static a-carousel-display-swap a-carousel-transition-swap"><input autocomplete="on" type="hidden" class="a-carousel-firstvisibleitem"/>             <div class="a-row a-carousel-header-row a-size-large pa_componentTitleTest unified_ad_labeling_title_margin"><div class="a-column a-span8"><h2 class="a-carousel-heading a-inline-block">Products related to this item<div class="sp_desktop_sponsored_label">          <style>     .sp_detail2_sponsored_label {         color: #555555;         font-size: 11px;     }     .sp_detail2_info_icon {         width: 11px;         vertical-align: text-bottom;         fill: #969696;     }     .sp_info_link {         text-decoration:none !important;     }          #sp_detail2_hide_feedback_string {         display: none;     }          .sp_detail2_sponsored_label:hover {         color: #111111;     }     .sp_detail2_sponsored_label:hover .sp_detail2_info_icon {         fill: #555555;     }      </style>              <a id="sp_detail2_feedbackMessage" class="a-link-normal dynamicSPFL sp_info_link" href="#sp_detail2_feedbackForm">             <div class="sp_detail2_sponsored_label ">         Sponsored                       <svg aria-hidden="true" class="sp_detail2_info_icon" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">                 <path d="M256,9C119,9,8,120.08,8,257S119,505,256,505,504,394,504,257,393,9,256,9Zm0,76.31A47.69,47.69,0,1,1,208.31,133,47.69,47.69,0,0,1,256,85.31Zm38.15,332.38a12.18,12.18,0,0,1-12.21,12H229.67a11.85,11.85,0,0,1-11.82-12V249.92a11.86,11.86,0,0,1,11.82-12h52.27a12.18,12.18,0,0,1,12.21,12Z"></path>             </svg>              </div> <span id="sp_detail2_hide_feedback_string">Hide feedback</span>         </a>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('AmazonClicks').execute(function (AC) {                 if (AC.registerFeedbackEventsWithSponsoredLabel) {                     AC.registerFeedbackEventsWithSponsoredLabel("sp_detail2_carousel", "sp_detail2_feedbackMessage", "sp_detail2_hide_feedback_string", "pa_feedbackForm_container_sp_detail2");                 }             });         }));</script>               </div></h2>             </div><div class="a-column a-span4 a-span-last a-text-right"><span class="a-carousel-pagination a-size-base"><span class="a-carousel-page-count">Page <span class="a-carousel-page-current">1</span> of <span class="a-carousel-page-max">1</span></span><span class="a-carousel-restart-container"><span class="a-text-separator"></span><a class="a-carousel-restart" href="#">Start over</a></span><span class="a-carousel-accessibility-page-info a-offscreen" aria-live="polite">Page 1 of 1</span></span></div></div>             <div class="a-row">             <div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left"><a class="a-button a-button-image a-carousel-button a-carousel-goto-prevpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-previous"><span class="a-icon-alt">Previous page of related Sponsored Products</span></i></span></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport"><ol class="a-carousel" role="list">                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B08QCNRKR6" data-asin="B08QCNRKR6" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_0&quot;,&quot;asin&quot;:&quot;B08QCNRKR6&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200045750680251&amp;adIndex=0" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200045750680251&amp;eventType=2&amp;adIndex=0"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200045750680251&eventType=2&adIndex=0");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B08QCNRKR6"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=sppnjdSQ9%2BNiA%2B47sBD%2By5feyUPquFjZ6eNmtuMJ3TMr8%2B8%2FoYpFqlOnfbMTZOnnVCgeh7XdCiwc%0AoUtJq0rYRoS9TtLNSLlLTUzrlxpGccO%2FpM%2FPAfhFRhkmn%2FdWAkqoYPt4p%2FDE%2Bemi9YXyHSTHUhmt%0AUHjYt7PmRrei5v6h7PUwWFJtH1HD%2BXnjyEz2Oq709wczoVxSnjVsU4oU0eMQNuunE2gC6w6Sf8ap%0AYG9%2FCyCfoyu89J6bySvSLkF5tZXqRNTWi%2FQZ5ZzNQi0rG3QqBiSRv7TUm0sAtR7mfYX0ROUSuSkU%0ABRABHhS4g23VDfCWSs%2BmjfDMUGYZbAyYg7TIFp69Q6aGsjgHqrqwpXpUOsRhNKyYm3iH8lroml5i%0AdrTd9epkPFbSKC7L32F11ElNMo5fyctlq6FIUKf1qwVDAaQYY3HcsmroYScTI8YC4HgpgJDXAdca%0APdNQjdL3DgN%2FCfuByr1cF4mMtgl23Sq4OmTKOTLvuGQkyVcIlSq9OHZpknhlOFStl0wY%2B1JKy%2F3X%0AMi4q323HzEcYAa8VJRcjMq7Rv5I%2BO2JtKir%2FaP7izMtbUO6ey5XF4VKkVLXmGJuKyR2yQuaJBpGK%0AUMBidZcz%2FuXr4Z8DXo%2BQWYAM9zyak%2BWvR82xmJrvOg4%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="LP&amp;No.1 Vinyl Record Storage Box,Portable Record Carrying Case for 30+ Vinyl Albums,Blue (Upgrade)" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_0?ie=UTF8&amp;adId=A038272029B09Y2105JLZ&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08QCNRKR6%2Fref%3Dsspa_dk_detail_0%3Fpsc%3D1%26pd_rd_i%3DB08QCNRKR6p13NParams">                                                      <img alt="LP&amp;No.1 Vinyl Record Storage Box,Portable Record Carrying Case for 30+ Vinyl Albums,Blue (Upgrade)" src="https://m.media-amazon.com/images/I/31-yeJ7jVbL._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/31-yeJ7jVbL._AC_SR160,160_.jpg&quot;:[160,160],&quot;https://m.media-amazon.com/images/I/31-yeJ7jVbL._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/31-yeJ7jVbL._AC_SR480,480_.jpg&quot;:[480,480]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     LP&amp;No.1 Vinyl Record Storage Box,Portable Record Carrying Case for 30+ Vinyl Albums...</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="LP&amp;No.1 Vinyl Record Storage Box,Portable Record Carrying Case for 30+ Vinyl Albums,Blue (Upgrade)" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_0?ie=UTF8&amp;adId=A038272029B09Y2105JLZ&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08QCNRKR6%2Fref%3Dsspa_dk_detail_0%3Fpsc%3D1%26pd_rd_i%3DB08QCNRKR6p13NParams#customerReviews">         <i class="a-icon a-icon-star a-star-4-5"></i>         <span class="a-color-link">361</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="LP&amp;No.1 Vinyl Record Storage Box,Portable Record Carrying Case for 30+ Vinyl Albums,Blue (Upgrade)" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_0?ie=UTF8&amp;adId=A038272029B09Y2105JLZ&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08QCNRKR6%2Fref%3Dsspa_dk_detail_0%3Fpsc%3D1%26pd_rd_i%3DB08QCNRKR6p13NParams">                         <span class="a-size-medium a-color-price">$61.99</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="LP&amp;No.1 Vinyl Record Storage Box,Portable Record Carrying Case for 30+ Vinyl Albums,Blue (Upgrade)" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_0?ie=UTF8&amp;adId=A038272029B09Y2105JLZ&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08QCNRKR6%2Fref%3Dsspa_dk_detail_0%3Fpsc%3D1%26pd_rd_i%3DB08QCNRKR6p13NParams">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B08DS4TXJ2" data-asin="B08DS4TXJ2" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_1&quot;,&quot;asin&quot;:&quot;B08DS4TXJ2&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200030273077641&amp;adIndex=1" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200030273077641&amp;eventType=2&amp;adIndex=1"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200030273077641&eventType=2&adIndex=1");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B08DS4TXJ2"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=PXWEzjzw566yRkNMMFTbvVheUbbTUb6J4RhcRWvQoJK7zwa25Xe2wB3jkLP8dr2USP%2BwbuE8Mn9P%0Aqk8lJ4Z21MX6z6BouQmZ6xJloI%2BndEUnikrGX2cOy%2BNVf9LTo4Mh7U6WK5BRwYW43ov2vmzZ9a%2F4%0AJ%2FWV6g3KNf%2Fi2e4tMdDA6YieGYT0LjpP8tkKXkaTu4Ja52tKVIDqaoFL30PIkoyisD6ny9emr7Tt%0AzkYxsmRauhczvSBMlL%2FPrFh9fwZFh%2BPnaXnq%2BFjMiZp%2B%2BjfQMUXJNF2uUwTU47NnJI6ASU6VguXm%0AmJ3Vie9sMjkXCKM48%2Fo2DqiyfT%2BY5ucPmBkysIAknVVCKfH18114ixIEMkHO605aIoQ%2BC75iNv1t%0A%2B8znM%2BS0EhzVEpz4P0SCVMabg4LhvOBG75Wgtn97MfHii2onjfkfLLhU19AZjaxfqfn0knNUXX78%0A47Il6sjDzn0SLJlLDSzseMCVF6zL2pUa45e5VJJH7BaVODnB3DSimj%2FWTG1%2BXh8dD63liiZaE8iS%0ASUU%2BcBggWuxZLVPc%2BaI2FQlfquhsvaneBWpKaw7HXoG6E4vs7lHXVV8J%2BhCzVVVTtgeCcLXILwDM%0Avb1OioCrZ313eIAc03V1Cqr85fgN8IUq6wrnXOpDr6ZwMuhQlrzh2Q%3D%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="NIUBEE Black Vinyl Record Shelf Wall Mount 6 Pack,Acrylic Album Record Holder Display Your Daily Listening in Office Home" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_1?ie=UTF8&amp;adId=A00520382QPR7RRA4NU1K&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08DS4TXJ2%2Fref%3Dsspa_dk_detail_1%3Fpsc%3D1%26pd_rd_i%3DB08DS4TXJ2p13NParams">                                                      <img alt="NIUBEE Black Vinyl Record Shelf Wall Mount 6 Pack,Acrylic Album Record Holder Display Your Daily Listening in Office Home" src="https://m.media-amazon.com/images/I/41cAyz7J46L._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/41cAyz7J46L._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/41cAyz7J46L._AC_SR160,160_.jpg&quot;:[160,160],&quot;https://m.media-amazon.com/images/I/41cAyz7J46L._AC_SR480,480_.jpg&quot;:[480,480]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     NIUBEE Black Vinyl Record Shelf Wall Mount 6 Pack,Acrylic Album Record Holder Displ...</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="NIUBEE Black Vinyl Record Shelf Wall Mount 6 Pack,Acrylic Album Record Holder Display Your Daily Listening in Office Home" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_1?ie=UTF8&amp;adId=A00520382QPR7RRA4NU1K&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08DS4TXJ2%2Fref%3Dsspa_dk_detail_1%3Fpsc%3D1%26pd_rd_i%3DB08DS4TXJ2p13NParams#customerReviews">         <i class="a-icon a-icon-star a-star-5"></i>         <span class="a-color-link">1,501</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="NIUBEE Black Vinyl Record Shelf Wall Mount 6 Pack,Acrylic Album Record Holder Display Your Daily Listening in Office Home" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_1?ie=UTF8&amp;adId=A00520382QPR7RRA4NU1K&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08DS4TXJ2%2Fref%3Dsspa_dk_detail_1%3Fpsc%3D1%26pd_rd_i%3DB08DS4TXJ2p13NParams">                         <span class="a-size-medium a-color-price">$54.99</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="NIUBEE Black Vinyl Record Shelf Wall Mount 6 Pack,Acrylic Album Record Holder Display Your Daily Listening in Office Home" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_1?ie=UTF8&amp;adId=A00520382QPR7RRA4NU1K&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB08DS4TXJ2%2Fref%3Dsspa_dk_detail_1%3Fpsc%3D1%26pd_rd_i%3DB08DS4TXJ2p13NParams">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B07KNZKRDV" data-asin="B07KNZKRDV" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_2&quot;,&quot;asin&quot;:&quot;B07KNZKRDV&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200013558385381&amp;adIndex=2" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200013558385381&amp;eventType=2&amp;adIndex=2"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200013558385381&eventType=2&adIndex=2");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B07KNZKRDV"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=nP6WyBT1HA8M88pQFtwGKzuD8yFFUeOUORM4QYA21Nz6kwf2oW8KRdzeye6cqDoy5aKqVoRomJXp%0AsMScBNW1lM28hdVnmYm%2BP5snH0cGKuBVMfqZzg5pDxBgUsiwkJ%2B4a7qG%2Ba8vzKCiS3XY6ZV9bEg7%0Ant4pybntocQneHhFklRtswM56ClJMtCmbAA898M1Owieynmt3bghwpIljgQw4a9wctAt3mje2fKV%0AjRUHFvIx6MtUheVhQ8tVBVdChdtWorYreF6sWjVitomkIDtJiFyDW4RlsWhIwZyzu8ZMF1zOzjlk%0AAgHkFS1bEM67SAYYoffwgfMggmO3dH%2Fxe9RJzqPHdvOwZrFd56md8NnfKqmiU0aekWMIMA8y1h6Q%0AGPnWDHw%2FehORibi13auSpaMf1KXrsoiaZfPBzQQ6hkQ9pvhFAPGovsdpWc00BO3yLMJQRzzlajrP%0Alf8idugH3AGZy%2FK2Lg6NHSUQ5uKcppGdM%2BS9%2FIrg1%2BwcimTKLMQIp9ui5E8ymH4NZftKb3xWEYBC%0AiGRdv35TdgN%2BOZK%2FrijCuW%2B%2BVzy7RL%2BsSAs6x3nXjb9i1MfSGMNVgNJH8jnC%2F2Q5cNjO3qa7LYNn%0AD4rO7xHzGRGVG2qoIm5WS%2FqwkAe%2BMtmHyNqykOUf2C%2BuOnih2QgCQw%3D%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="exreizst Vinyl Record Storage Holder - Record Holder Rack Unit - Store and Hold Magazines Albums Display Stand - Solid Pine Wood with Crystal Clear Acrylic, Brown - Large" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_2?ie=UTF8&amp;adId=A0992884395RA7TNU52LW&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07KNZKRDV%2Fref%3Dsspa_dk_detail_2%3Fpsc%3D1%26pd_rd_i%3DB07KNZKRDVp13NParams">                                                      <img alt="exreizst Vinyl Record Storage Holder - Record Holder Rack Unit - Store and Hold Magazines Albums Display Stand - Solid Pine Wood with Crystal Clear Acrylic, Brown - Large" src="https://m.media-amazon.com/images/I/31sRdNbfd5L._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/31sRdNbfd5L._AC_SR480,480_.jpg&quot;:[480,480],&quot;https://m.media-amazon.com/images/I/31sRdNbfd5L._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/31sRdNbfd5L._AC_SR160,160_.jpg&quot;:[160,160]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     exreizst Vinyl Record Storage Holder - Record Holder Rack Unit - Store and Hold Mag...</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="exreizst Vinyl Record Storage Holder - Record Holder Rack Unit - Store and Hold Magazines Albums Display Stand - Solid Pine Wood with Crystal Clear Acrylic, Brown - Large" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_2?ie=UTF8&amp;adId=A0992884395RA7TNU52LW&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07KNZKRDV%2Fref%3Dsspa_dk_detail_2%3Fpsc%3D1%26pd_rd_i%3DB07KNZKRDVp13NParams#customerReviews">         <i class="a-icon a-icon-star a-star-4"></i>         <span class="a-color-link">287</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="exreizst Vinyl Record Storage Holder - Record Holder Rack Unit - Store and Hold Magazines Albums Display Stand - Solid Pine Wood with Crystal Clear Acrylic, Brown - Large" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_2?ie=UTF8&amp;adId=A0992884395RA7TNU52LW&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07KNZKRDV%2Fref%3Dsspa_dk_detail_2%3Fpsc%3D1%26pd_rd_i%3DB07KNZKRDVp13NParams">                         <span class="a-size-medium a-color-price">$31.99</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="exreizst Vinyl Record Storage Holder - Record Holder Rack Unit - Store and Hold Magazines Albums Display Stand - Solid Pine Wood with Crystal Clear Acrylic, Brown - Large" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_2?ie=UTF8&amp;adId=A0992884395RA7TNU52LW&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07KNZKRDV%2Fref%3Dsspa_dk_detail_2%3Fpsc%3D1%26pd_rd_i%3DB07KNZKRDVp13NParams">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B07GBHN6TW" data-asin="B07GBHN6TW" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_3&quot;,&quot;asin&quot;:&quot;B07GBHN6TW&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200053142942531&amp;adIndex=3" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200053142942531&amp;eventType=2&amp;adIndex=3"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200053142942531&eventType=2&adIndex=3");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B07GBHN6TW"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=ibVx6oidA9NBbXMb9Tjk0VbMi7mfMeZQYVrMRU8JQMltBojoU%2F0pQ6U1oWxgtUTxAPI3nidiJpHg%0AK3pKtTkKrDgZiDyW45Cbu28ItLGqkTUUJM4sMbBoR7d0Hf%2BydINYMwX%2FxghIkpU5C7U4mcDsm8nj%0AofYd%2FzFfgvBHCAkMC3rax7lYD0FLSVRXIhljeLBN6kOV5UdzzPJfpnFWcvurCnBdpdN8wGyXO59O%0AWj53VIQzXykqmCrWAHMZtmsmaTfAnhv8tovOrg1P4lcRvcvTD1kN7AwB%2B0a%2BSdN9dqU4vWyD31no%0A6erNXWqwZWa6aDN5mJx1IuxitQw1Ga2WTRT%2FdHNoSDXnqU75z97%2F4v1grzb2Lke62aE3HmBk4bTG%0AsxJai%2Ffove9gD6L%2BH5gND2NuaVYJISPqgujNkhgyj4XVWfWmi3zvzRj2PH%2BZ7yCd73rcMq1fTMpp%0A4jRvgEighZkPH8tjAU7%2BmtSuIVhqC6%2FecfTMc9k0dLMq3xztXpekLr6ZflCGQU%2FfePDcWucuWZGR%0AeXkTR5IDkkZMEAi22Vxbgv4Cqwepc4RhLdvSdfp95kdVbWfqKxhfAuY18YQhSxVG8fmsVs%2Bg2FGW%0APtc%2BXTprrlhOBkz4tQ3L5HU7Ac93dj0u&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="Music from The Last of Us Part 2 (7-Inch) Exclusive Blue Vinyl w/ Black Swirl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_3?ie=UTF8&amp;adId=A02964892VXUK6ACTTVIX&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07GBHN6TW%2Fref%3Dsspa_dk_detail_3%3Fpsc%3D1%26pd_rd_i%3DB07GBHN6TWp13NParams">                                                      <img alt="Music from The Last of Us Part 2 (7-Inch) Exclusive Blue Vinyl w/ Black Swirl" src="https://m.media-amazon.com/images/I/4138ZC92o4L._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/4138ZC92o4L._AC_SR480,480_.jpg&quot;:[480,480],&quot;https://m.media-amazon.com/images/I/4138ZC92o4L._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/4138ZC92o4L._AC_SR160,160_.jpg&quot;:[160,160]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     Music from The Last of Us Part 2 (7-Inch) Exclusive Blue Vinyl w/ Black Swirl</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="Music from The Last of Us Part 2 (7-Inch) Exclusive Blue Vinyl w/ Black Swirl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_3?ie=UTF8&amp;adId=A02964892VXUK6ACTTVIX&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07GBHN6TW%2Fref%3Dsspa_dk_detail_3%3Fpsc%3D1%26pd_rd_i%3DB07GBHN6TWp13NParams#customerReviews">         <i class="a-icon a-icon-star a-star-4-5"></i>         <span class="a-color-link">72</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Music from The Last of Us Part 2 (7-Inch) Exclusive Blue Vinyl w/ Black Swirl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_3?ie=UTF8&amp;adId=A02964892VXUK6ACTTVIX&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07GBHN6TW%2Fref%3Dsspa_dk_detail_3%3Fpsc%3D1%26pd_rd_i%3DB07GBHN6TWp13NParams">                         <span class="a-size-medium a-color-price">$86.27</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Music from The Last of Us Part 2 (7-Inch) Exclusive Blue Vinyl w/ Black Swirl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_3?ie=UTF8&amp;adId=A02964892VXUK6ACTTVIX&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB07GBHN6TW%2Fref%3Dsspa_dk_detail_3%3Fpsc%3D1%26pd_rd_i%3DB07GBHN6TWp13NParams">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B01HRJ9NAY" data-asin="B01HRJ9NAY" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_4&quot;,&quot;asin&quot;:&quot;B01HRJ9NAY&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200058200600151&amp;adIndex=4" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200058200600151&amp;eventType=2&amp;adIndex=4"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200058200600151&eventType=2&adIndex=4");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B01HRJ9NAY"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=dQKM1C8XPpR8dU6Dej%2BX6uXVI0fh091GUKSJndHoE5xdBoxBXxT%2BvlmWoBkJFk3BHqGWvS2NYfYm%0AmeannH2obEdFnE6y1qQ1g%2BxY79faXojwKaDoWbWv3APJrEBHTW9ZvF0k618YKoIz%2BERHfoM9D8Gv%0AclYzKF8j3CjpJu5s%2BKiQs%2B7QdwGzmxRc153MXFuVavgwuAefIqBw2fVho%2FJNHk%2F92q1JL5iCmMe7%0AE6UhMY1U3Z8BhBD1%2FxC5anv0ZJG038YTQQGWrDCy9cR6KGdkakRwbdI%2Flj4oP2aq9nqufg5ooU%2Bx%0AIYbF5yxMiIUvwak8S0exdwfvqJUfci%2ByJOnvhvTvsNl0pt%2B5farGW%2FWbksOASMDDzUYf%2Fx5hCdQq%0AUzV%2B%2BuBAmMblkb5%2BVKlYLgs4Wq4b%2Facu0LZZTpmP8%2BaD8u%2BjuoiJaxuiFAYNoELC9JJ77SgfReCs%0A9hB1iBMP2qfyepD%2FRjMi%2BgjZQ6vf%2FyxaSGlocuaioSsEiAvR2B4Il71ZfK8E6f%2F7cp5NLVPE%2F7UN%0ANU5B0eIHOJmK3OKuJIm3Et0L4t4H2V4sdBQI5ruFzgzNqllc%2BwbBiv5cisUVxtW84FXZn%2F4CukvC%0AENa1cQHL7yX7rWWRcRhrUplaP7SByjlLBPs4L4WS5Do%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="Digital Turntable Stylus Force Gauge 0.01g Neoteck LP Scale Gauge Blue 3-Digit LCD Backlight for Vinyl Players Tonearm Phono Cartridge with 5.00g Calibration Weight" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_4?ie=UTF8&amp;adId=A02452063JV0H0UORIOEG&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB01HRJ9NAY%2Fref%3Dsspa_dk_detail_4%3Fpsc%3D1%26pd_rd_i%3DB01HRJ9NAYp13NParams%26smid%3DA2N4NEZPB53SEZ">                                                      <img alt="Digital Turntable Stylus Force Gauge 0.01g Neoteck LP Scale Gauge Blue 3-Digit LCD Backlight for Vinyl Players Tonearm Phono Cartridge with 5.00g Calibration Weight" src="https://m.media-amazon.com/images/I/41psDE5+joL._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/41psDE5+joL._AC_SR160,160_.jpg&quot;:[160,160],&quot;https://m.media-amazon.com/images/I/41psDE5+joL._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/41psDE5+joL._AC_SR480,480_.jpg&quot;:[480,480]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     Digital Turntable Stylus Force Gauge 0.01g Neoteck LP Scale Gauge Blue 3-Digit LCD ...</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="Digital Turntable Stylus Force Gauge 0.01g Neoteck LP Scale Gauge Blue 3-Digit LCD Backlight for Vinyl Players Tonearm Phono Cartridge with 5.00g Calibration Weight" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_4?ie=UTF8&amp;adId=A02452063JV0H0UORIOEG&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB01HRJ9NAY%2Fref%3Dsspa_dk_detail_4%3Fpsc%3D1%26pd_rd_i%3DB01HRJ9NAYp13NParams%26smid%3DA2N4NEZPB53SEZ#customerReviews">         <i class="a-icon a-icon-star a-star-4-5"></i>         <span class="a-color-link">3,266</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Digital Turntable Stylus Force Gauge 0.01g Neoteck LP Scale Gauge Blue 3-Digit LCD Backlight for Vinyl Players Tonearm Phono Cartridge with 5.00g Calibration Weight" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_4?ie=UTF8&amp;adId=A02452063JV0H0UORIOEG&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB01HRJ9NAY%2Fref%3Dsspa_dk_detail_4%3Fpsc%3D1%26pd_rd_i%3DB01HRJ9NAYp13NParams%26smid%3DA2N4NEZPB53SEZ">                         <span class="a-size-medium a-color-price">$18.99</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Digital Turntable Stylus Force Gauge 0.01g Neoteck LP Scale Gauge Blue 3-Digit LCD Backlight for Vinyl Players Tonearm Phono Cartridge with 5.00g Calibration Weight" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_4?ie=UTF8&amp;adId=A02452063JV0H0UORIOEG&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB01HRJ9NAY%2Fref%3Dsspa_dk_detail_4%3Fpsc%3D1%26pd_rd_i%3DB01HRJ9NAYp13NParams%26smid%3DA2N4NEZPB53SEZ">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B00WJMQTX4" data-asin="B00WJMQTX4" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_5&quot;,&quot;asin&quot;:&quot;B00WJMQTX4&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200002696277331&amp;adIndex=5" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200002696277331&amp;eventType=2&amp;adIndex=5"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200002696277331&eventType=2&adIndex=5");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B00WJMQTX4"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=vHX4c1N8gPzXmUL5UWdjZ5AnbA09GkPY%2FGUcIWpaoYBMCsZ6wxgeHeNaIjKKbJUgfc%2BVxDJi3ZwI%0A6yxFfOmGE%2B5Cf3NaIty9ieTF%2BmPDM5gvGgTD2VFDSbW2%2Bj75cikt6pwZR2cvYFXNg6hdp72WvyI%2B%0A6pUalcKfnO%2BGQ6U7QqDx3Pz5eQverD32fUUVIMAqP12h5Q9JV180u7SUPefWiOWfG17FBZDu6wy0%0AQTltihQEGFWhYSJYOIaCjErXKuhawyN6uEcWwSI3AESx6GzQf3qkPfPUjtitclydZaA6zUm4elKR%0AkmTLbEeQVjCXbilWmeomcxTeLIQjNj8q7GBacQjdhMEiTXrtznLrmBAZorN%2B4gMDw4zSHzOEtN0%2F%0AxJpYhuO40OYhi%2FmT1pLVpBEbnJYGuDR%2FO9fFnjtnCN4CWIaPVkHxQ%2Fr3Q9PZQi6WwOnNJWOArJ3S%0Ah5T3%2FVcrpCm0QPIL4vgLFc8Hg6clb6%2FwPO8diZn4qM96tPuFlzlnRrXbdhHuw%2FpHlzuCP2dSRPn%2F%0ABxfJPY33gPvvJarQ9uPFo9ABWkTWOCBMZJZJVV5kQw7FEJCHsSsHe1D2Vc68vvQFHm2NQrxs%2B6Os%0AJ6P5dQvy7xA%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="New 12pcs 24K Gold Speaker Banana Plug Audio Jack Connector" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_5?ie=UTF8&amp;adId=A09040481ZN0YS4CJEBIO&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB00WJMQTX4%2Fref%3Dsspa_dk_detail_5%3Fpsc%3D1%26pd_rd_i%3DB00WJMQTX4p13NParams">                                                      <img alt="New 12pcs 24K Gold Speaker Banana Plug Audio Jack Connector" src="https://m.media-amazon.com/images/I/51QJWXuRbZL._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/51QJWXuRbZL._AC_SR160,160_.jpg&quot;:[160,160],&quot;https://m.media-amazon.com/images/I/51QJWXuRbZL._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/51QJWXuRbZL._AC_SR480,480_.jpg&quot;:[480,480]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     New 12pcs 24K Gold Speaker Banana Plug Audio Jack Connector</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="New 12pcs 24K Gold Speaker Banana Plug Audio Jack Connector" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_5?ie=UTF8&amp;adId=A09040481ZN0YS4CJEBIO&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB00WJMQTX4%2Fref%3Dsspa_dk_detail_5%3Fpsc%3D1%26pd_rd_i%3DB00WJMQTX4p13NParams#customerReviews">         <i class="a-icon a-icon-star a-star-4-5"></i>         <span class="a-color-link">101</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="New 12pcs 24K Gold Speaker Banana Plug Audio Jack Connector" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_5?ie=UTF8&amp;adId=A09040481ZN0YS4CJEBIO&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB00WJMQTX4%2Fref%3Dsspa_dk_detail_5%3Fpsc%3D1%26pd_rd_i%3DB00WJMQTX4p13NParams">                         <span class="a-size-medium a-color-price">$22.99</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="New 12pcs 24K Gold Speaker Banana Plug Audio Jack Connector" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_5?ie=UTF8&amp;adId=A09040481ZN0YS4CJEBIO&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB00WJMQTX4%2Fref%3Dsspa_dk_detail_5%3Fpsc%3D1%26pd_rd_i%3DB00WJMQTX4p13NParams">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B085XFQHK4" data-asin="B085XFQHK4" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_6&quot;,&quot;asin&quot;:&quot;B085XFQHK4&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200065090034431&amp;adIndex=6" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200065090034431&amp;eventType=2&amp;adIndex=6"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200065090034431&eventType=2&adIndex=6");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B085XFQHK4"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=Cr892di%2FzwEZ1xcYoRy3nh%2BGTWLYoY7D9iDnXzQ6sVRLf1nyYPxGj5bIQ9sfizca%2Bn48jP%2BtCjCu%0A4I9yqCfS7Ifzch15kabXth4cQxgbpKDWLiI0yGYI2clTzSS3hsNOhgpUjPM8ZPGAaCsa3V65ftn4%0AZVN08cFFEHwjvS16RZIF0Kkfq7LzvcZsWpnW3ZOmjazCcoZBEcZJvaT%2Fx5Zx5ASegMaIV5kjXRCT%0AcNrwbAJGfLdPtB%2BlICa0fprltkzmG2sb7zGk14EWTvgkHG8HjyhCyWVshPYG5mGiXM%2BsSh0ev%2B3N%0Aj9LjQjppBpxqA9tqJTl8tpdWcDDAPXAGOcUkC64eOYTXj0JVo90wZl4ws3L2Zgz%2FL0h21lM4WVXR%0AXKihdFVkN968kRnRb%2BPDbEjZUpq%2BwrAV8Tv7DfsRvPC9DDjP03CqGm675IUul%2B4HD1PvOOb7wo6w%0AGn1fMO7%2F6xBb51qJz%2BVQAnv4772%2Bk0hKXe7Xkf1RP0sR7OKL71n%2BX2U9hLG7EsnmY0yfIXJB%2Bxbn%0AdPaMU81lsS%2FzRBHPI9%2FXSq4UmJBcT6f0eBcRM6sl%2BvqVOfxlrzR55SzkxZ9wKs6F7IYMB%2F1pNYyU%0AGTR4owKg6olm0uaBssqy8RdlRbLhgaU1elT0QEzh5As%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="Fall Out Boy - Greatest Hits: Believers Never Die - Volume Two Limited LP Red Vinyl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_6?ie=UTF8&amp;adId=A06364161EZIS3QBTUIQ4&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB085XFQHK4%2Fref%3Dsspa_dk_detail_6%3Fpsc%3D1%26pd_rd_i%3DB085XFQHK4p13NParams%26smid%3DA2NK0A0EZZARO">                                                      <img alt="Fall Out Boy - Greatest Hits: Believers Never Die - Volume Two Limited LP Red Vinyl" src="https://m.media-amazon.com/images/I/41dVcTwEDyL._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/41dVcTwEDyL._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/41dVcTwEDyL._AC_SR160,160_.jpg&quot;:[160,160],&quot;https://m.media-amazon.com/images/I/41dVcTwEDyL._AC_SR480,480_.jpg&quot;:[480,480]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     Fall Out Boy - Greatest Hits: Believers Never Die - Volume Two Limited LP Red Vinyl</div> </a> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Fall Out Boy - Greatest Hits: Believers Never Die - Volume Two Limited LP Red Vinyl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_6?ie=UTF8&amp;adId=A06364161EZIS3QBTUIQ4&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB085XFQHK4%2Fref%3Dsspa_dk_detail_6%3Fpsc%3D1%26pd_rd_i%3DB085XFQHK4p13NParams%26smid%3DA2NK0A0EZZARO">                         <span class="a-size-medium a-color-price">$77.00</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Fall Out Boy - Greatest Hits: Believers Never Die - Volume Two Limited LP Red Vinyl" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_6?ie=UTF8&amp;adId=A06364161EZIS3QBTUIQ4&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB085XFQHK4%2Fref%3Dsspa_dk_detail_6%3Fpsc%3D1%26pd_rd_i%3DB085XFQHK4p13NParams%26smid%3DA2NK0A0EZZARO">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B0833XN43Q" data-asin="B0833XN43Q" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_7&quot;,&quot;asin&quot;:&quot;B0833XN43Q&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200028197208641&amp;adIndex=7" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200028197208641&amp;eventType=2&amp;adIndex=7"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200028197208641&eventType=2&adIndex=7");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B0833XN43Q"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=C%2BMt35wInaetwuUzOZgIMgqOr33xO444ebXD6uiUDGdztF%2Ffb3AaCmS7tyuxPgbBkc9PEzHmr%2F5e%0ATty45Fm1dps%2FjGNuhpzkL6ztwEw3GcTATJaHja5D4%2FTzgK62bF1o%2Ba7ZqrUYY5gVM8gYYg%2FZuvcm%0A5fNvF7sMhx7YFVo8tuC7DtwPDGIJT32omowdgvDqGPN5BEEZ4RvUt%2FFCNoXgls9t9nR9EqgYz9VZ%0AR5%2BmuSMTNTB%2Bmq%2Fihl7mPf1BVcXzH0iAn3CiyHuTvlvEqXdX%2FrANiHheogyXiA8iEOVgk1sk3y8F%0ArhSnFF8CYCc7nKUGQxKgRAUANf8pSYYRLI5QejF1KPw5LjFnzpAXSvUKrqmVy28m4vUmR52260YF%0AXNzozLfQHUY0Me%2BjJSOdDN81tcPHImJoDxOpU5%2F7%2Bts8uvSqT0QpNzRX8whJk1Ar0u8WfxuozSnp%0AX7%2F6qoi%2BbbWz4QwzaXHGIwY2aooTjye4qOezN8D3FEp5qE92Mp%2FpHftCwVvSnP%2F9tS3jQjr7PsV%2B%0AxhjxeeycblnSIjLhCllUeKoJBeu9YQ0MVacsZgIeoBEuBt3NuqFrmiU%3D&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="Mr. Robot: The Complete Series - Blu-ray" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_7?ie=UTF8&amp;adId=A085357111L83SIKNC3TK&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB0833XN43Q%2Fref%3Dsspa_dk_detail_7%3Fpsc%3D1%26pd_rd_i%3DB0833XN43Qp13NParams%26smid%3DALQLN932F0Y46">                                                      <img alt="Mr. Robot: The Complete Series - Blu-ray" src="https://m.media-amazon.com/images/I/41VRNKmo86L._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/41VRNKmo86L._AC_SR480,480_.jpg&quot;:[480,480],&quot;https://m.media-amazon.com/images/I/41VRNKmo86L._AC_SR160,160_.jpg&quot;:[160,160],&quot;https://m.media-amazon.com/images/I/41VRNKmo86L._AC_SR320,320_.jpg&quot;:[320,320]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     Mr. Robot: The Complete Series - Blu-ray</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="Mr. Robot: The Complete Series - Blu-ray" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_7?ie=UTF8&amp;adId=A085357111L83SIKNC3TK&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB0833XN43Q%2Fref%3Dsspa_dk_detail_7%3Fpsc%3D1%26pd_rd_i%3DB0833XN43Qp13NParams%26smid%3DALQLN932F0Y46#customerReviews">         <i class="a-icon a-icon-star a-star-5"></i>         <span class="a-color-link">30</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Mr. Robot: The Complete Series - Blu-ray" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_7?ie=UTF8&amp;adId=A085357111L83SIKNC3TK&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB0833XN43Q%2Fref%3Dsspa_dk_detail_7%3Fpsc%3D1%26pd_rd_i%3DB0833XN43Qp13NParams%26smid%3DALQLN932F0Y46">                         <span class="a-size-medium a-color-price">$81.15</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Mr. Robot: The Complete Series - Blu-ray" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_7?ie=UTF8&amp;adId=A085357111L83SIKNC3TK&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB0833XN43Q%2Fref%3Dsspa_dk_detail_7%3Fpsc%3D1%26pd_rd_i%3DB0833XN43Qp13NParams%26smid%3DALQLN932F0Y46">                           <span style="position: relative; top: 2px;">                 <i class="a-icon a-icon-prime a-icon-small" role="presentation"></i>             </span>                                              </a> </div>      </div>                                                               </li>                                               <li class="a-carousel-card" style=" width:160px; " role="listitem">                                                                                                    <style> .sp_ppu_string {     vertical-align:bottom;     display: inline-block; } </style>                              <div id="sp_detail2_B004D8KX7K" data-asin="B004D8KX7K" data-p13n-asin-metadata="{&quot;ref&quot;:&quot;sspa_dk_detail_8&quot;,&quot;asin&quot;:&quot;B004D8KX7K&quot;}" data-viewpixelurl="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200008290585061&amp;adIndex=8" class="a-section sp_offerVertical p13n-asin sp_ltr_offer">              <noscript>             <img alt="" src="/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;adId=200008290585061&amp;eventType=2&amp;adIndex=8"/>         </noscript>         <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {             P.when('SponsoredProductsViewability').execute(function(SV) {                 SV.loadImagePixel("/gp/sponsored-products/logging/log-action.html?qualifier=1622846847&id=5345304543871616&widgetName=sp_detail2&adId=200008290585061&eventType=2&adIndex=8");             });         }));</script>           <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {     P.when('A', 'SponsoredProductsViewability').execute(function(A, SV) {         SV.registerViewTrackingElement(A.$("#sp_detail2_B004D8KX7K"), "sp_detail2");     }); }));</script> <div class="pa_feedbackForm_container_sp_detail2" style="display:none;">     <div class="sp_adID">         <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;footer&quot;:&quot;\u003cdiv id='sponsored-products-feedback-footer'&gt;&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;name&quot;:&quot;sponsored-products-feedback-modal-sp_detail2&quot;,&quot;width&quot;:&quot;350&quot;,&quot;header&quot;:&quot;Share your feedback&quot;,&quot;url&quot;:&quot;/gp/sponsored-products/lazyLoad/handler/sp-feedback-handler.html?pl=jRBS4EgNcDjw8eJGEJ96AYLcsxtDbsrY%2FOMWzS4KUfjPp%2BGMlsqaJYi3LkMlI8PSlQ9J4qBCUCGG%0AAxdbWsgn2L4bRMjJ%2B4RNp9wXQLV0lBHaJfygNYAUx%2FzC8wthm5A8tIr179UbOWEfM12twixIfo08%0AAjAtc4BTX0%2BnrTez%2Byjy5XZLMaKygsctY6bYWHzRzkFxSKEoiQwgkfBzymO%2F6DdcEEoQRecJy3au%0ABeBZlEjI346zyzM2W1NhWwKVpTVHW0i8DtZ9dSxDEB1TrWAOnT63pcKcbBybsmeOwoJuXtQjwu5J%0AUwZsa4REyzNLeaVLPyU4VmP87rizArCj3Qh%2Fkr7XHc9B64ClgoicB6tr8uLi6HMmwFxwZlrzVda9%0AWxEHLOkAn97CUvIhJ%2F%2FXE9Q3AXYypG7KRREImIqrQGnEbul7xxWrNeaXOs%2BAluHz1EmQBtUnJr9e%0AgikMXEVFW1VVcPrnsCV1Ym2Uurgfzn6C06SPQyYwIP2QLYA55Gml%2FTKYLMBeysU%2BiHTuSE0LPEVF%0AHs8qyqpjg00ZZQ2FybN3bRP0lPVPqKF61f2Nf1shY613&quot;}">             <a href="javascript:void(0)" class="a-popover-trigger a-declarative">Feedback<i class="a-icon a-icon-popover"></i></a>         </span>     </div> </div> <a class="a-link-normal" target="_top" rel="noopener" title="Boss TU3 Chromatic Tuner Pedal" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_8?ie=UTF8&amp;adId=A06311621SSGWK0D4VMWN&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB004D8KX7K%2Fref%3Dsspa_dk_detail_8%3Fpsc%3D1%26pd_rd_i%3DB004D8KX7Kp13NParams%26smid%3DA20GF6ZPCE2SWL">                                                      <img alt="Boss TU3 Chromatic Tuner Pedal" src="https://m.media-amazon.com/images/I/51rTLN1HsXL._AC_SR160,160_.jpg" class="a-dynamic-image" height="160" width="160" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/51rTLN1HsXL._AC_SR320,320_.jpg&quot;:[320,320],&quot;https://m.media-amazon.com/images/I/51rTLN1HsXL._AC_SR480,480_.jpg&quot;:[480,480],&quot;https://m.media-amazon.com/images/I/51rTLN1HsXL._AC_SR160,160_.jpg&quot;:[160,160]}"/>                   <div data-rows="4" aria-hidden="true" class="sponsored-products-truncator-truncate sponsored-products-truncator-line-clamp-4">     Boss TU3 Chromatic Tuner Pedal</div> </a>     <div class="a-row">         <a class="a-link-normal adReviewLink a-text-normal" target="_top" rel="noopener" title="Boss TU3 Chromatic Tuner Pedal" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_8?ie=UTF8&amp;adId=A06311621SSGWK0D4VMWN&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB004D8KX7K%2Fref%3Dsspa_dk_detail_8%3Fpsc%3D1%26pd_rd_i%3DB004D8KX7Kp13NParams%26smid%3DA20GF6ZPCE2SWL#customerReviews">         <i class="a-icon a-icon-star a-star-5"></i>         <span class="a-color-link">90</span>         </a>     </div> <div class="a-row a-color-price">                                                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Boss TU3 Chromatic Tuner Pedal" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_8?ie=UTF8&amp;adId=A06311621SSGWK0D4VMWN&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB004D8KX7K%2Fref%3Dsspa_dk_detail_8%3Fpsc%3D1%26pd_rd_i%3DB004D8KX7Kp13NParams%26smid%3DA20GF6ZPCE2SWL">                         <span class="a-size-medium a-color-price">$139.99</span>                                              </a>                                                           <a class="a-link-normal a-text-normal" target="_top" rel="noopener" title="Boss TU3 Chromatic Tuner Pedal" href="https://www.amazon.ca/gp/slredirect/picassoRedirect.html/ref=sspa_dk_detail_8?ie=UTF8&amp;adId=A06311621SSGWK0D4VMWN&amp;qualifier=1622846847&amp;id=5345304543871616&amp;widgetName=sp_detail2&amp;url=%2Fdp%2FB004D8KX7K%2Fref%3Dsspa_dk_detail_8%3Fpsc%3D1%26pd_rd_i%3DB004D8KX7Kp13NParams%26smid%3DA20GF6ZPCE2SWL">                                                   </a> </div>      </div>                                                               </li>                          </ol></div></div><div class="a-carousel-col a-carousel-right"><a class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage" tabindex="0" href="#"><span class="a-button-inner"><i class="a-icon a-icon-next"><span class="a-icon-alt">Next page of related Sponsored Products</span></i></span></a></div></div></div>             </div>         <span class="a-end aok-hidden"></span></div>           <div style="margin-bottom: 19px"></div> <script type="text/javascript">(function(f) {var _np=(window.P._namespace("FirebirdSpRendering"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {    P.when('A', 'a-carousel-framework', 'AmazonClicks').execute(function (A, CF, AC) {         CF.getCarousel(document.getElementById("sp_detail2"));    });                  P.when('A', 'SPHAT').execute(function(A, SPHAT) {                 var containerSelector = "#sp_detail2 div";                 var elementsAllowedToBeHidden = ['script', 'div.sp_adID', 'div.pa_feedbackForm_container_sp_detail2', 'span.a-declarative', 'span.aok-hidden', 'input[type=hidden]', 'noscript'];                 var csmCounterMetricName = 'sp_detail2.adb';                 var hadImpact = SPHAT.checkForHiddenElements(containerSelector, elementsAllowedToBeHidden, csmCounterMetricName);                 A.state("sp_detail2", { adBlockerHadImpact: hadImpact});             });              P.when('SponsoredProductsViewability').execute(function(SV) {      SV.registerAuiEvents(['ready', 'scroll', 'resize', 'orientationchange']);    }); P.when('sp-dp-carousel-truncation').execute(function (truncator) {     truncator.setUpTruncation("sp_detail2"); }); }));</script></div>






















</div>




</div>
  
  
  
  
  


























 
 
 


















        




































<script>if (typeof uet === 'function' && typeof ues === 'function') {var scope = 'Detail_dp-ads-center-promo_Desktop';var placementId = '1276c434-4276-4aea-9cbd-d503573208e5';ues('wb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); uet('bb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); if (placementId) {ues('wb', 'adplacements:' + placementId, {wb:1});uet('bb', 'adplacements:' + placementId, {wb:1});}}</script><hr size="1" noshade="noshade" class="a-divider-normal"><div id="ape_Detail_dp-ads-center-promo_Desktop_placement" class="copilot-secure-display celwidget  text/x-dacx-safeframe" cel_widget_id="adplacements:Detail:dp-ads-center-promo:Desktop" data-csa-c-type="widget" data-csa-c-slot-id="adplacements:Detail:dp-ads-center-promo:Desktop" data-csa-c-content-id="1276c434-4276-4aea-9cbd-d503573208e5" data-campaign="7818" style="display: block; margin:auto; line-height:0; width:970px;" data-ad-details='{"slot" :"Detail_dp-ads-center-promo_Desktop","pageType": "Detail","subPageType":  "Desktop","slotName" :"dp-ads-center-promo","src" : "https://aax-us-east.amazon-adsystem.com/e/xsp/getAd?placementId=1276c434-4276-4aea-9cbd-d503573208e5&src=513&slot=dp-ads-center-promo&rid=0101c65f40afa14aedb5e62c5cf36c2f98911d860bd6b244b27ea952d8bb60dc651e&rj=%7B%7D","adServer" :"cs","campaignId" :  "7818","arid" :"b0a3408703d3447188c55b9422cdd7c9","placementId": "1276c434-4276-4aea-9cbd-d503573208e5","size" :{"width": "970px","height" : "250px"},"allowedSizes" :[],"allowChangeSize":  true,"allowedDomains" :  ["g-ecx.images-amazon.com"],"aanParams" :   "site%3Damazon.ca%3Bpt%3DDetail%3Bslot%3Ddp-ads-center-promo%3Bpid%3DB0000028RR%3Barid%3Db0a3408703d3447188c55b9422cdd7c9","loadAfter" :   "criticalFeature","extraDelay" :  0,"iframeExtraStyle": "","iframeClass":  "","isCardsFlow": false,"adPixels": [],"aaxInstrPixelUrl": "","serverSideFetchAd": "false","enableAdBlockerDetector": false,"disableResizeFunc": true,"minWidthToScale": "","fallbackStaticAdImgUrl": "","fallbackStaticAdClickUrl": "","fallbackStaticAdExtraStyle": "","adFeedbackInfo": {"endPoint": "/gp/aq-feedback/lazyLoad/handler/af-link-handler.html","boolFeedback": true,"slugText": "Sponsored","adFeedbackOnTop":false},"adPlacementMetaData": {"pageUrl": "aHR0cHM6Ly93d3cuYW1hem9uLmNhL2dwL3Byb2R1Y3QvQjAwMDAwMjhSUj9kcFJlcXVlc3RJZD0xS01EWTJKUEdQMlgzUjgwRzhXQyZXREc9bXVzaWNfZGlzcGxheV9vbl93ZWJzaXRlJiplbnRyaWVzKj0wJipWZXJzaW9uKj0xJg==","adElementId": "ape_Detail_dp-ads-center-promo_Desktop_placement","pageType": "Detail","slotName": "dp-ads-center-promo"},"adCreativeMetaData": {"adNetwork": "cs"},"advertisementStyle": {"position": "absolute","top": "2px","right": "0px","display": "inline-block","font": "normal 11px Arial","color": "grey"},"feedbackDivStyle": {"position": "relative","height": "14px","top": "2px"},"viewabilityStandards": [{"p": 0, "t": 0, "def": "amzn"}, {"p": 30, "t": 1, "def": "iab"}, {"p": 100, "t": 1, "def": "groupm"}],"ajaxWeblabTriggerId": "","abpStatus": "1","abpAcceptable": "true","disableAdReporterSlot": "false","allowlistedCustomMessageEvents": ["openPsAdPopover", "openATCModal", "setPartner", "sendMetrics", "wrap"],"allowlistedQueryParamKeys": ["sf-overrideVariationId", "sf-overridePredictorId", "sf-forceFailure"],"DAsfUrl":"https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js"}' aria-hidden="true"></div><script>(function(){function a(d,e){if(window.addEventListener){window.addEventListener(d,e,false);}else{if(window.attachEvent){window.attachEvent("on"+d,e);}}}function c(d,e){if(window.removeEventListener){window.removeEventListener(d,e,false);}else{if(window.detachEvent){window.detachEvent("on"+d,e);}}}var b=function(){(function(){(function(l,o){l.sfLogErrors=l.sfLogErrors||false;var q=q||function(v,u){u=u||new Error(v);if(l.ue&&typeof ue.count=="function"){ue.count("adplacements:safeFrameError",1);}if(!l.sfLogErrors){return;}if(l.ueLogError){l.ueLogError(u,{logLevel:"ERROR",attribution:"APE-safeframe",message:v+" "});}else{if(typeof console!=="undefined"&&console.error){console.error(v,u);}}};l.aanParams=l.aanParams||{};l.aanParams["dp-ads-center-promo"]="site=amazon.ca;pt=Detail;slot=dp-ads-center-promo;pid=B0000028RR;arid=b0a3408703d3447188c55b9422cdd7c9";l["dp-ads-center-promo"]={};l["dp-ads-center-promo"].adStartTime=(new Date()).getTime();function d(){return l.innerHeight||o.documentElement.clientHeight;}function g(){return l.innerWidth||o.documentElement.clientWidth;}function e(w,u,v){if(w>0){return(v>w);}else{return(u>0);}}var f=function(){return(Date.now?Date.now():new Date().getTime());};throttle=function(v,x,B){var u,z,C;var A=null;var y=0;if(!B){B={};}var w=function(){y=B.leading===false?0:f();A=null;C=v.apply(u,z);if(!A){u=z=null;}};return function(){var E=f();if(!y&&B.leading===false){y=E;}var D=x-(E-y);u=this;z=arguments;if(D<=0||D>x){if(A){clearTimeout(A);A=null;}y=E;C=v.apply(u,z);if(!A){u=z=null;}}else{if(!A&&B.trailing!==false){A=setTimeout(w,D);}}return C;};};function n(C,A,v,x,u){try{var z=o.getElementById(C).getBoundingClientRect();if(e(z.top,z.bottom,d())&&e(z.left,z.right,g())){if(typeof uet=="function"){uet("bb","adplacements:viewablelatency:"+A,{wb:1});if(v){uet("bb","adplacements:viewablelatency:"+v,{wb:1});}}var w;if(l.csa){var B=o.getElementById(C);if(u=="mobileads"){w=l.csa("Content",{element:B.parentNode});}else{w=l.csa("Content",{element:B});}w("mark","viewablelatency:bodyBegin");if(l.apeViewableLatencyTrackers[x].loaded){w("mark","viewablelatency:loaded");}}if(typeof uex=="function"&&l.ue&&typeof ue.count=="function"){if(l.apeViewableLatencyTrackers[x].loaded){uex("ld","adplacements:viewablelatency:"+A,{wb:1});if(v){uex("ld","adplacements:viewablelatency:"+v,{wb:1});}ue.count("adplacements:htmlviewed:loaded:"+A,1);if(v){ue.count("adplacements:htmlviewed:loaded:"+v,1);}}ue.count("adplacements:htmlviewed:"+A,1);if(v){ue.count("adplacements:htmlviewed:"+v,1);}}l.apeViewableLatencyTrackers[x].viewed=true;if(l.apeViewableLatencyTrackers[x].tracker){c("scroll",l.apeViewableLatencyTrackers[x].tracker);c("resize",l.apeViewableLatencyTrackers[x].tracker);}}}catch(y){l.apeViewableLatencyTrackers[x].valid=false;}}try{l.apeViewableLatencyTrackers=l.apeViewableLatencyTrackers||{};var t="ape_Detail_dp-ads-center-promo_Desktop_placement";var s="Detail_dp-ads-center-promo_Desktop".replace(/\_/g,":");var i="1276c434-4276-4aea-9cbd-d503573208e5";var k="b0a3408703d3447188c55b9422cdd7c9";var h="amazon";l.apeViewableLatencyTrackers[k]=l.apeViewableLatencyTrackers[k]||{};l.apeViewableLatencyTrackers[k].valid=true;n(t,s,i,k,h);if(l.apeViewableLatencyTrackers[k].valid&&!l.apeViewableLatencyTrackers[k].viewed){l.apeViewableLatencyTrackers[k].tracker=throttle(function(){n(t,s,i,k,h);},20);a("scroll",l.apeViewableLatencyTrackers[k].tracker);a("resize",l.apeViewableLatencyTrackers[k].tracker);}}catch(m){if(l.apeViewableLatencyTrackers&&l.apeViewableLatencyTrackers.b0a3408703d3447188c55b9422cdd7c9){l.apeViewableLatencyTrackers.b0a3408703d3447188c55b9422cdd7c9.valid=false;}q("Error initializing viewable latency instrumentation",m);}if(l.csa){var j;var r=o.getElementById(t);if(h=="mobileads"){j=l.csa("Content",{element:r.parentNode});}else{j=l.csa("Content",{element:r});}j("mark","bodyBegin");}try{if(l.DAsf){l.DAsf.loadAds();}else{var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js?csm_attribution=APE-SafeFrame";p.onerror=function(){q("Error loading SafeFrame library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);l.collectSafeframeRTD=Math.random()*100<0;if(l.collectSafeframeRTD){var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/rtd/safeframeRtd-1.50.81044e8.js";p.onerror=function(){q("Error loading SafeFrame RTD library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);}}}catch(m){q("Error appending DAsf library",m);}}(window,document));})();};b();})();</script><div style="margin-bottom:10px;"></div>








<a id="customerReviews" aria-label="Top reviews" class="a-link-normal" href="#"></a><hr aria-hidden="true" class="a-spacing-large a-divider-normal"/><span class="cr-widget-PageState">
  <span id="cr-state-object" data-state='{"asin":"B0000028RR","customerId":"0","deviceType":"desktop","contextId":"","reviewCommentsAjaxUrl":"","reviewCommentSubmissionAjaxUrl":"","approvedAuthorAjaxUrl":"","reviewsAjaxUrl":"/hz/reviews-render/ajax/medley-filtered-reviews/get/","medleyReviewsAjaxUrl":"/hz/reviews-render/ajax/medley-reviews/get/","reviewerType":"","formatType":"","filterByKeyword":"","filterByLanguage":"","filterByStar":"","filterByHeight":"","filterByWeight":"","showLanguageFilter":false,"showHeightFilter":false,"languageOfPreference":"en_CA","isCardTreatmentEnabled":false,"lazyWidgetLoaderBufferPixels":"1000","lazyWidgetLoaderDelayBeforeTriggering":"5000","lazyWidgetLoaderUrl":"/hz/reviews-render/ajax/lazy-widgets/stream","lazyWidgetCsrfToken":"gpyP8iV9FCWk30lZZ6e0P%2FY%2BKYH6mWAFKwRdev0AAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU","lazyWidgetDomainWhitelist":["amazon.com","amazon.ca","amazon.com.mx","amazon.com.br","amazon.co.uk","amazon.de","amazon.it","amazon.sa","amazon.com.tr","amazon.es","amazon.fr","amazon.in","amazon.ae","amazon.nl","amazon.se","amazon.pl","amazon.eg","amazon.co.jp","amazon.com.au","amazon.sg","amazon.cn"],"signinUrl":"https://www.amazon.ca/ap/signin?openid.return_to\u003dhttps%3A%2F%2Fwww.amazon.ca%2FRage-Against-Machine%2Fproduct-reviews%2FB0000028RR%3Fie%3DUTF8\u0026openid.identity\u003dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select\u0026openid.claimed_id\u003dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select\u0026openid.assoc_handle\u003dcaflex\u0026openid.mode\u003dcheckid_setup\u0026openid.ns\u003dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0","reftagTriggerUrl":"/hz/reviews-render/ajax/reftag-trigger","mobileImageGalleryUrl":"","productInfoUrl":"","disableScroll":false,"onLoadShowHideElements":"#cm-cr-dp-reviews-loading-wrapper,.cr-reviews-loading"}'></span>
</span>
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01STrEog8JL._RC|015DCfR+jFL.css,01LKsGfpclL.css,21ZGXbZs+2L.css,01cdXa5nSoL.css_.css?AUIClients/DesktopMedleyFilteringMetaAsset" />
<script>
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/414YATFBD+L._RC|01TvTYLyWBL.js,11PLCo6zxLL.js,21m3YqNtM+L.js,21HWbFKuvXL.js_.js?AUIClients/DesktopMedleyFilteringMetaAsset');
</script>
<div id="reviewsMedley" data-hook="reviews-medley-widget" class="a-fixed-left-grid a-spacing-extra-large"><div class="a-fixed-left-grid-inner" style="padding-left:300px"><div class="a-fixed-left-grid-col a-col-left" style="width:300px;margin-left:-300px;float:left;"><div class="a-row"><h2>Customer reviews</h2></div><div class="a-section a-spacing-none a-spacing-top-mini cr-widget-ACR"><div class="a-fixed-left-grid AverageCustomerReviews a-spacing-small"><div class="a-fixed-left-grid-inner" style="padding-left:105px"><div class="a-fixed-left-grid-col a-col-left" style="width:105px;margin-left:-105px;float:left;"><i data-hook="average-star-rating" class="a-icon a-icon-star-medium a-star-medium-4-5 averageStarRating"><span class="a-icon-alt">4.7 out of 5 stars</span></i></div><div class="a-fixed-left-grid-col aok-align-center a-col-right" style="padding-left:0%;float:left;"><div class="a-row"><span class="a-size-base a-nowrap"><span data-hook="rating-out-of-text" class="a-size-medium a-color-base">4.7 out of 5</span></span></div></div></div></div><div data-hook="total-review-count" class="a-row a-spacing-medium averageStarRatingNumerical"><span class="a-size-base a-color-secondary"><!--TODO: Replace this string with arp-x-ratings 5/22/19 (ShopperExp-5143)-->
            3,129 global ratings</span></div></div><span class="cr-widget-Histogram">
      <div class="a-fixed-left-grid a-spacing-none"><div class="a-fixed-left-grid-inner" style="padding-left:280px"><div class="a-fixed-left-grid-col a-col-left" style="width:280px;margin-left:-280px;float:left;"><span class="a-declarative" data-action="reviews:filter-action:push-state" data-reviews:filter-action:push-state="{&quot;scrollToSelector&quot;:&quot;#reviews-filter-info&quot;,&quot;allowLinkDefault&quot;:&quot;1&quot;}"><table id="histogramTable" class="a-normal a-spacing-none" role="presentation">








<table id="histogramTable" class="a-normal a-align-center a-spacing-base">
  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;five_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="86% of reviews have 5 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 5star" title="86% of reviews have 5 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            5 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="86% of reviews have 5 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="86%"><div class="a-meter-bar" style="width: 86%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="86% of reviews have 5 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              86%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;four_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="9% of reviews have 4 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 4star" title="9% of reviews have 4 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_4?ie=UTF8&amp;filterByStar=four_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            4 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="9% of reviews have 4 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_4?ie=UTF8&amp;filterByStar=four_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="9%"><div class="a-meter-bar" style="width: 9%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="9% of reviews have 4 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_4?ie=UTF8&amp;filterByStar=four_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              9%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;three_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="2% of reviews have 3 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 3star" title="2% of reviews have 3 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_3?ie=UTF8&amp;filterByStar=three_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            3 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="2% of reviews have 3 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_3?ie=UTF8&amp;filterByStar=three_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="2%"><div class="a-meter-bar" style="width: 2%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="2% of reviews have 3 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_3?ie=UTF8&amp;filterByStar=three_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              2%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;two_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="1% of reviews have 2 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 2star" title="1% of reviews have 2 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_2?ie=UTF8&amp;filterByStar=two_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            2 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="1% of reviews have 2 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_2?ie=UTF8&amp;filterByStar=two_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="1%"><div class="a-meter-bar" style="width: 1%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="1% of reviews have 2 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_2?ie=UTF8&amp;filterByStar=two_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              1%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;one_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="2% of reviews have 1 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 1star" title="2% of reviews have 1 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_1?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            1 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="2% of reviews have 1 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_1?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="2%"><div class="a-meter-bar" style="width: 2%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="2% of reviews have 1 stars" href="/product-reviews/B0000028RR/ref=acr_dp_hist_1?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              2%
            
          </a>
        </span>
      </td>
    </tr>

  


</table>
</table></span></div></div></div><div aria-live="polite" class="a-row a-expander-container a-spacing-top-small a-expander-inline-container"><a href="javascript:void(0)" data-action="a-expander-toggle" class="a-expander-header a-declarative a-expander-inline-header a-link-expander" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;&quot;, &quot;collapse_prompt&quot;:&quot;&quot;}"><i class="a-icon a-icon-expand"></i><span class="a-expander-prompt">How are ratings calculated?</span></a><div aria-expanded="false" class="a-expander-content a-expander-inline-content a-expander-inner" style="display:none">To calculate the overall star rating and percentage breakdown by star, we don’t use a simple average. Instead, our system considers things like how recent a review is and if the reviewer bought the item on Amazon. It also analyzes reviews to verify trustworthiness.</div></div></span>
    <hr aria-hidden="true" class="a-spacing-large a-spacing-top-large a-divider-normal"/><span class="cr-lazy-widget cr-summarization-attributes" data-widget-name='cr-summarization-attributes'>
</span><span class="cr-lazy-widget cr-age-recommendation" data-widget-name='cr-age-recommendation'>
</span><span class="cr-lazy-widget cr-solicitation" data-widget-name='cr-solicitation'>
</span><hr aria-hidden="true" class="a-spacing-extra-large a-spacing-top-extra-large a-divider-normal"/><div id="cr-ADPlaceholder" class="a-section reviews-display-ad"><script>if (typeof uet === 'function' && typeof ues === 'function') {var scope = 'Detail_customer-reviews-top_Glance';var placementId = '36f440ea-620c-4c90-be8d-cf6a8e2a52b5';ues('wb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); uet('bb', 'adplacements:' + scope.replace(/\_/g, ':'), {wb:1}); if (placementId) {ues('wb', 'adplacements:' + placementId, {wb:1});uet('bb', 'adplacements:' + placementId, {wb:1});}}</script><div id="ape_Detail_customer-reviews-top_Glance_placement" class="copilot-secure-display celwidget  text/x-dacx-safeframe" cel_widget_id="adplacements:Detail:customer-reviews-top:Glance" data-csa-c-type="widget" data-csa-c-slot-id="adplacements:Detail:customer-reviews-top:Glance" data-csa-c-content-id="36f440ea-620c-4c90-be8d-cf6a8e2a52b5" data-campaign="7448" style="width:300px; height:280px;" data-ad-details='{"slot" :"Detail_customer-reviews-top_Glance","pageType": "Detail","subPageType":  "Glance","slotName" :"customer-reviews-top","src" : "http://aax-us-east.amazon-adsystem.com/e/xsp/getAd?placementId=36f440ea-620c-4c90-be8d-cf6a8e2a52b5&src=513&slot=customer-reviews-top&rid=0101c65f40afa14aedb5e62c5cf36c2f98911d860bd6b244b27ea952d8bb60dc651e&rj=%7B%7D","adServer" :"cs","campaignId" :  "7448","arid" :"2891289395f246e3b1f83d3b365f6dcb","placementId": "36f440ea-620c-4c90-be8d-cf6a8e2a52b5","size" :{"width": "300","height" : "250"},"allowedSizes" :[{"width":"305px", "height":"255px"},{"width":"305px", "height":"250px"}],"allowChangeSize":  true,"allowedDomains" :  ["g-ecx.images-amazon.com"],"aanParams" :   "site%3Damazon.ca%3Bpt%3DDetail%3Bslot%3Dcustomer-reviews-top%3Bpid%3DB0000028RR%3Barid%3D2891289395f246e3b1f83d3b365f6dcb%3Bef%3D0.00","loadAfter" :   "criticalFeature","extraDelay" :  0,"iframeExtraStyle": "","iframeClass":  "","isCardsFlow": false,"adPixels": [],"aaxInstrPixelUrl": "","serverSideFetchAd": "false","enableAdBlockerDetector": false,"disableResizeFunc": true,"minWidthToScale": "","fallbackStaticAdImgUrl": "","fallbackStaticAdClickUrl": "","fallbackStaticAdExtraStyle": "","adFeedbackInfo": {"endPoint": "/gp/aq-feedback/lazyLoad/handler/af-link-handler.html","boolFeedback": true,"slugText": "Sponsored","adFeedbackOnTop":false},"adPlacementMetaData": {"pageUrl": "aHR0cDovL2hwLXJldmlld3NtZWRsZXktbmEtMWQuaWFkLmFtYXpvbi5jb206ODA4MC9XRUItSU5GL3ZpZXdzL21lZGxleVJBV1BhZ2VWaWV3LmpzcA==","adElementId": "ape_Detail_customer-reviews-top_Glance_placement","pageType": "Detail","slotName": "customer-reviews-top"},"adCreativeMetaData": {"adNetwork": "cs"},"advertisementStyle": {"position": "absolute","top": "2px","right": "0px","display": "inline-block","font": "normal 11px Arial","color": "grey"},"feedbackDivStyle": {"position":"relative","top": "-2px","height":"17px"},"viewabilityStandards": [{"p": 0, "t": 0, "def": "amzn"}, {"p": 50, "t": 1, "def": "iab"}, {"p": 100, "t": 1, "def": "groupm"}],"ajaxWeblabTriggerId": "","abpStatus": "1","abpAcceptable": "true","disableAdReporterSlot": "false","allowlistedCustomMessageEvents": ["openPsAdPopover", "openATCModal", "setPartner", "sendMetrics", "wrap"],"allowlistedQueryParamKeys": ["sf-overrideVariationId", "sf-overridePredictorId", "sf-forceFailure"],"DAsfUrl":"https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js"}' aria-hidden="true"></div><script>(function(){function a(d,e){if(window.addEventListener){window.addEventListener(d,e,false);}else{if(window.attachEvent){window.attachEvent("on"+d,e);}}}function c(d,e){if(window.removeEventListener){window.removeEventListener(d,e,false);}else{if(window.detachEvent){window.detachEvent("on"+d,e);}}}var b=function(){(function(){(function(l,o){l.sfLogErrors=l.sfLogErrors||false;var q=q||function(v,u){u=u||new Error(v);if(l.ue&&typeof ue.count=="function"){ue.count("adplacements:safeFrameError",1);}if(!l.sfLogErrors){return;}if(l.ueLogError){l.ueLogError(u,{logLevel:"ERROR",attribution:"APE-safeframe",message:v+" "});}else{if(typeof console!=="undefined"&&console.error){console.error(v,u);}}};l.aanParams=l.aanParams||{};l.aanParams["customer-reviews-top"]="site=amazon.ca;pt=Detail;slot=customer-reviews-top;pid=B0000028RR;arid=2891289395f246e3b1f83d3b365f6dcb;ef=0.00";l["customer-reviews-top"]={};l["customer-reviews-top"].adStartTime=(new Date()).getTime();function d(){return l.innerHeight||o.documentElement.clientHeight;}function g(){return l.innerWidth||o.documentElement.clientWidth;}function e(w,u,v){if(w>0){return(v>w);}else{return(u>0);}}var f=function(){return(Date.now?Date.now():new Date().getTime());};throttle=function(v,x,B){var u,z,C;var A=null;var y=0;if(!B){B={};}var w=function(){y=B.leading===false?0:f();A=null;C=v.apply(u,z);if(!A){u=z=null;}};return function(){var E=f();if(!y&&B.leading===false){y=E;}var D=x-(E-y);u=this;z=arguments;if(D<=0||D>x){if(A){clearTimeout(A);A=null;}y=E;C=v.apply(u,z);if(!A){u=z=null;}}else{if(!A&&B.trailing!==false){A=setTimeout(w,D);}}return C;};};function n(C,A,v,x,u){try{var z=o.getElementById(C).getBoundingClientRect();if(e(z.top,z.bottom,d())&&e(z.left,z.right,g())){if(typeof uet=="function"){uet("bb","adplacements:viewablelatency:"+A,{wb:1});if(v){uet("bb","adplacements:viewablelatency:"+v,{wb:1});}}var w;if(l.csa){var B=o.getElementById(C);if(u=="mobileads"){w=l.csa("Content",{element:B.parentNode});}else{w=l.csa("Content",{element:B});}w("mark","viewablelatency:bodyBegin");if(l.apeViewableLatencyTrackers[x].loaded){w("mark","viewablelatency:loaded");}}if(typeof uex=="function"&&l.ue&&typeof ue.count=="function"){if(l.apeViewableLatencyTrackers[x].loaded){uex("ld","adplacements:viewablelatency:"+A,{wb:1});if(v){uex("ld","adplacements:viewablelatency:"+v,{wb:1});}ue.count("adplacements:htmlviewed:loaded:"+A,1);if(v){ue.count("adplacements:htmlviewed:loaded:"+v,1);}}ue.count("adplacements:htmlviewed:"+A,1);if(v){ue.count("adplacements:htmlviewed:"+v,1);}}l.apeViewableLatencyTrackers[x].viewed=true;if(l.apeViewableLatencyTrackers[x].tracker){c("scroll",l.apeViewableLatencyTrackers[x].tracker);c("resize",l.apeViewableLatencyTrackers[x].tracker);}}}catch(y){l.apeViewableLatencyTrackers[x].valid=false;}}try{l.apeViewableLatencyTrackers=l.apeViewableLatencyTrackers||{};var t="ape_Detail_customer-reviews-top_Glance_placement";var s="Detail_customer-reviews-top_Glance".replace(/\_/g,":");var i="36f440ea-620c-4c90-be8d-cf6a8e2a52b5";var k="2891289395f246e3b1f83d3b365f6dcb";var h="amazon";l.apeViewableLatencyTrackers[k]=l.apeViewableLatencyTrackers[k]||{};l.apeViewableLatencyTrackers[k].valid=true;n(t,s,i,k,h);if(l.apeViewableLatencyTrackers[k].valid&&!l.apeViewableLatencyTrackers[k].viewed){l.apeViewableLatencyTrackers[k].tracker=throttle(function(){n(t,s,i,k,h);},20);a("scroll",l.apeViewableLatencyTrackers[k].tracker);a("resize",l.apeViewableLatencyTrackers[k].tracker);}}catch(m){if(l.apeViewableLatencyTrackers&&l.apeViewableLatencyTrackers["2891289395f246e3b1f83d3b365f6dcb"]){l.apeViewableLatencyTrackers["2891289395f246e3b1f83d3b365f6dcb"].valid=false;}q("Error initializing viewable latency instrumentation",m);}if(l.csa){var j;var r=o.getElementById(t);if(h=="mobileads"){j=l.csa("Content",{element:r.parentNode});}else{j=l.csa("Content",{element:r});}j("mark","bodyBegin");}try{if(l.DAsf){l.DAsf.loadAds();}else{var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/desktop/DAsf-1.50.81044e8.js?csm_attribution=APE-SafeFrame";p.onerror=function(){q("Error loading SafeFrame library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);l.collectSafeframeRTD=Math.random()*100<0;if(l.collectSafeframeRTD){var p=o.createElement("script");p.type="text/javascript";p.async=true;p.charset="utf-8";p.src="https://images-na.ssl-images-amazon.com/images/S/apesafeframe/ape/sf/rtd/safeframeRtd-1.50.81044e8.js";p.onerror=function(){q("Error loading SafeFrame RTD library");};p.setAttribute("crossorigin","anonymous");(o.getElementsByTagName("head")[0]||o.getElementsByTagName("body")[0]).appendChild(p);}}}catch(m){q("Error appending DAsf library",m);}}(window,document));})();};b();})();</script></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2.5%;float:left;"><div class="a-row cm_cr_grid_center_container"><div class="a-fixed-right-grid-col cm_cr_grid_center_left" style="float:left;"></div><div class="a-fixed-right-grid-col cm_cr_grid_center_right" style="float:left;"><span class="cr-widget-MedleyCustomerImages" data-hook="cr-widget-MedleyCustomerImages">
      <div class="a-popover-preload" id="a-popover-reviews-image-gallery"><div class="reviewLightboxPopoverContainer" data-hook="customer-images-modal">
      <div class="reviewsLightbox" id="reviews-image-gallery"></div>
    </div>
  </div><div id="reviews-image-gallery-container" data-asin="B0000028RR" data-hook="customer-images-widget" class="a-section a-spacing-medium reviews-customer-images"><div class="a-row"><h3>Reviews with images</h3></div><div class="a-row a-spacing-small a-spacing-top-small"><div class="review-image-tile" data-hook="review-image-tile-gallery">
          <img alt="Customer image" src="https://m.media-amazon.com/images/I/81t+tnmGPdL._CR541,0,972,972_UX175.jpg" class="a-dynamic-image cr-customer-image-thumbnail" width="22.5%" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/81t+tnmGPdL._CR541,0,972,972_UX175.jpg&quot;:[175,175],&quot;https://m.media-amazon.com/images/I/81t+tnmGPdL._CR541,0,972,972_UX64.jpg&quot;:[64,64]}"/></div>
      <div class="review-image-tile" data-hook="review-image-tile-gallery">
          <img alt="Customer image" src="https://m.media-amazon.com/images/I/81u0235jqgL._CR0,541,972,972_UX175.jpg" class="a-dynamic-image cr-customer-image-thumbnail" width="22.5%" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/81u0235jqgL._CR0,541,972,972_UX64.jpg&quot;:[64,64],&quot;https://m.media-amazon.com/images/I/81u0235jqgL._CR0,541,972,972_UX175.jpg&quot;:[175,175]}"/></div>
      <div class="review-image-tile" data-hook="review-image-tile-gallery">
          <img alt="Customer image" src="https://m.media-amazon.com/images/I/8129tFqv8gL._CR0,541,972,972_UX175.jpg" class="a-dynamic-image cr-customer-image-thumbnail" width="22.5%" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/8129tFqv8gL._CR0,541,972,972_UX175.jpg&quot;:[175,175],&quot;https://m.media-amazon.com/images/I/8129tFqv8gL._CR0,541,972,972_UX64.jpg&quot;:[64,64]}"/></div>
      <div class="review-image-tile" data-hook="review-image-tile-gallery">
          <img alt="Customer image" src="https://m.media-amazon.com/images/I/81Fc7tdJABL._CR0,351,1060,1060_UX175.jpg" class="a-dynamic-image cr-customer-image-thumbnail" width="22.5%" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/81Fc7tdJABL._CR0,351,1060,1060_UX175.jpg&quot;:[175,175],&quot;https://m.media-amazon.com/images/I/81Fc7tdJABL._CR0,351,1060,1060_UX64.jpg&quot;:[64,64]}"/></div>
      </div><div class="a-row"><a data-hook="see-all-images-link" class="a-link-normal reviews-image-gallery-link" href="#CustomerImages">See all customer images</a></div><div style="display:none;">
        <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;name&quot;:&quot;reviews-image-gallery&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-popover"></i></a></span></div>

  </div></span>
  <span class="cr-lazy-widget cr-summarization-lighthut" data-widget-name='cr-summarization-lighthut'>
</span><span class="cr-widget-FocalReviews" data-hook="cr-widget-FocalReviews">
      <div class="a-section a-spacing-medium"><div class="card-padding">
    <a id="customer-reviews-content" aria-label="Top reviews" class="a-link-normal celwidget" href="#"></a>

















<div id="cm-cr-dp-review-sort-type" data-reftag="cm_cr_dp_d_fltrs_srt" class="a-section a-spacing-small aok-hidden">
  <span class="a-declarative" data-action="reviews:filter-action:change" data-reviews:filter-action:change="{&quot;filterType&quot;:&quot;sortOrder&quot;}">
    
    <span class="a-dropdown-container"><select name="" autocomplete="off" id="cm-cr-sort-dropdown" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative">

      <option value="helpful" data-a-css-class="cm-cr-sort-order-option" selected>
        Top reviews
      </option>

      <option value="recent" data-a-css-class="cm-cr-sort-order-option">
        Most recent
      </option>

    </select><span tabindex="-1" data-a-class="cm-cr-dp-filter-dropdown" class="a-button a-button-dropdown a-button-small cm-cr-dp-filter-dropdown" aria-hidden="true"><span class="a-button-inner"><span class="a-button-text a-declarative" data-action="a-dropdown-button" aria-hidden="true"><span class="a-dropdown-prompt">Top reviews</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span>
  </span>
</div><div id="cm-cr-local-reviews-title" class="a-section"><h3 data-hook="dp-local-reviews-header" class="a-spacing-medium a-spacing-top-large">










  Top reviews from Canada
</h3></div><div id="cm-cr-dp-review-header" class="a-section a-spacing-small"></div><span class="cr-translate-cta">
        </span>

      <div class="a-row"><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center review-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" aria-live="assertive" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem filtering reviews right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div id="cm-cr-dp-reviews-loading-wrapper" class="a-row a-spacing-medium aok-hidden"><div class="a-spinner-wrapper cr-reviews-loading aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><div class="a-section a-spacing-large reviews-content filterable-reviews-content celwidget"><div id="cm-cr-dp-review-list" data-hook="top-customer-reviews-widget" class="a-section review-views celwidget"><div id="R3JKI83YR3OL0E" data-hook="review" class="a-section review aok-relative"><div id="R3JKI83YR3OL0E-review-card" class="a-row a-spacing-none"><div id="customer_review-R3JKI83YR3OL0E" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFCBX4Q5JOQ2JAMSGQGHUGV7SKSQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/5db1c0c8-24d3-4314-a03e-3811dc69e8c8._CR1,0,148,148_SX48_.jpg"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/5db1c0c8-24d3-4314-a03e-3811dc69e8c8._CR1,0,148,148_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Bricktop</span></div></a></div><div class="a-row"><a class="a-link-normal" title="1.0 out of 5 stars" href="/gp/customer-reviews/R3JKI83YR3OL0E/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-1 review-rating"><span class="a-icon-alt">1.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3JKI83YR3OL0E/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>Awful vinyl pressing, Vlado Meller ruins an amazing album with compression - find the original vinyl or new SACD</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on January 2, 2013</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  PLEASE NOTE - this review is for the 20th Anniversary XX vinyl and digital releases. It is NOT referring to the 2016 brand new SACD release mastered by Steve Hoffman which is magical, or the original 1992 Bob Ludwig mastering which was also splendid. Avoid the 20th anniversary releases at all costs unless you have to have the bonus material.<br /><br />Vlado Meller, a name synonymous with awful sounding records and CD's. The man who ruined the last four Red Hot Chili Peppers CD's with huge amounts of dynamic range compression, and the vinyl of I'm With You, the man who ruined the last Jane's Addiction CD and vinyl, has now turned his destructive sonic signature to the great debut album from Rage Against the Machine. This new vinyl release sounds awful compared to the original. The CD has been raped of dynamics and sounds nowhere near as good as the 1992 Bob Ludwig-mastered CD (and Bob has done his fair share of ruining dynamics recently too, so I'm not saying he's a saint by any means).<br /><br />The original vinyl was an all analogue production, it sounds absolutely stunning. The new vinyl, pressed at United in Nashville who are pretty well known for non fill and off centred sides, sounds like a pale shadow of the former. Utterly disappointing.<br /><br />The original vinyl in Mint condition can run over $75, more if sealed. To date it's the only all analogue vinyl pressing. The EU pressings and the recent Music On Vinyl (MOVLP043) repressing of the original '92 EU/UK using original metals are not all analogue cut, or they would have MASTERDISK stamped on them.<br /><br />Another option is the new 2016 Hybrid SACD, mastered from the original 1/2&#34; 30ips analogue tapes by Steve Hoffman. It is cheaper than the original US vinyl and in my opinion, giving the running times per side of the original vinyl and the eq'ing you can tell was applied, is now the definitive edition of the RATM debut.
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">46 people found this helpful</span></div><div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR3JKI83YR3OL0E%26voteValue%3D1%26csrfT%3Dgo09bB7v1h%252BGiGccmAsMHHVnsA6CrmLYStyPdTQAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R3JKI83YR3OL0E&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=go09bB7v1h%2BGiGccmAsMHHVnsA6CrmLYStyPdTQAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3JKI83YR3OL0E&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=go09bB7v1h%2BGiGccmAsMHHVnsA6CrmLYStyPdTQAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3JKI83YR3OL0E&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R3ATR0O30BOPGV" data-hook="review" class="a-section review aok-relative"><div id="R3ATR0O30BOPGV-review-card" class="a-row a-spacing-none"><div id="customer_review-R3ATR0O30BOPGV" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AEF7UPXXLD67KLXP2VL55EKUCQQQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Rick B</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R3ATR0O30BOPGV/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3ATR0O30BOPGV/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>Only about a week late but it did show up AND it is not warped</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on March 22, 2021</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  I didn't like that it was guaranteed to be here on the 18th and didn't show up until the 22nd.<br />I did like that it was flat, the cover was undamaged, the inner although brutally sticky and scratchy is nice looking and the record itself sounds very nice. One of the greatest albums of that decade and definitely one I was happy to be adding to my collection.
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR3ATR0O30BOPGV%26voteValue%3D1%26csrfT%3DgggNXFBFwbXSN8wY0LbOL4Ll%252FUqnaldpfWAOnrYAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R3ATR0O30BOPGV&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gggNXFBFwbXSN8wY0LbOL4Ll%2FUqnaldpfWAOnrYAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3ATR0O30BOPGV&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gggNXFBFwbXSN8wY0LbOL4Ll%2FUqnaldpfWAOnrYAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3ATR0O30BOPGV&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R3UUPZ4PZEMSYQ" data-hook="review" class="a-section review aok-relative"><div id="R3UUPZ4PZEMSYQ-review-card" class="a-row a-spacing-none"><div id="customer_review-R3UUPZ4PZEMSYQ" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFBTSOTSM4UGUAZOSTFT5UHMRSSA/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/1e647f3d-99bb-466d-b037-60dc602afd9b._CR0,25.0,282,282_SX48_.jpg"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/1e647f3d-99bb-466d-b037-60dc602afd9b._CR0,25.0,282,282_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Leonard McAlary</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R3UUPZ4PZEMSYQ/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3UUPZ4PZEMSYQ/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>High school days🤘🏻🤘🏻</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on January 28, 2020</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  I use to bump this album everyday back in high school i'm so glad i own it now. It's just as heavy as it was the first time i ever heard it if not better Rage forever🤘🏻💯
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR3UUPZ4PZEMSYQ%26voteValue%3D1%26csrfT%3DgvwEo6lQdzC0M5Mt%252BvkHg1U133zj0O420lHc3zgAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R3UUPZ4PZEMSYQ&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gvwEo6lQdzC0M5Mt%2BvkHg1U133zj0O420lHc3zgAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3UUPZ4PZEMSYQ&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gvwEo6lQdzC0M5Mt%2BvkHg1U133zj0O420lHc3zgAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3UUPZ4PZEMSYQ&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R10ZEQRXKE1JHL" data-hook="review" class="a-section review aok-relative"><div id="R10ZEQRXKE1JHL-review-card" class="a-row a-spacing-none"><div id="customer_review-R10ZEQRXKE1JHL" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFNQUFQ76J3Z5XNGOLO5V7H6T67Q/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Ollie Pelich</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R10ZEQRXKE1JHL/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R10ZEQRXKE1JHL/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>Rage Against the Machine PictureDisc 20th Anniversary remastered debut.</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on November 3, 2020</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Rage Against the machine 20th anniversary debut album remastered. Classic award winning photograph of Monks protesting the Vietnam war.
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div><div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR10ZEQRXKE1JHL%26voteValue%3D1%26csrfT%3Dgg7TbbPYlml1mPZOohbkuLgfjhN0eUfS6mabHdgAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R10ZEQRXKE1JHL&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gg7TbbPYlml1mPZOohbkuLgfjhN0eUfS6mabHdgAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R10ZEQRXKE1JHL&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gg7TbbPYlml1mPZOohbkuLgfjhN0eUfS6mabHdgAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R10ZEQRXKE1JHL&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R2GGHJWRT10ZWK" data-hook="review" class="a-section review aok-relative"><div id="R2GGHJWRT10ZWK-review-card" class="a-row a-spacing-none"><div id="customer_review-R2GGHJWRT10ZWK" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AGWKSFMGNUKHTVYXD6KNMIKIZXSA/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Gabe</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R2GGHJWRT10ZWK/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R2GGHJWRT10ZWK/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>Great</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on January 17, 2019</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Great
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div><div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR2GGHJWRT10ZWK%26voteValue%3D1%26csrfT%3DgqGjqdXI8G%252F2FFfH9pAlZUu0mWY%252BTRrmnv6aWf0AAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R2GGHJWRT10ZWK&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gqGjqdXI8G%2F2FFfH9pAlZUu0mWY%2BTRrmnv6aWf0AAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R2GGHJWRT10ZWK&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gqGjqdXI8G%2F2FFfH9pAlZUu0mWY%2BTRrmnv6aWf0AAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R2GGHJWRT10ZWK&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="RMP5MBL5WNWGH" data-hook="review" class="a-section review aok-relative"><div id="RMP5MBL5WNWGH-review-card" class="a-row a-spacing-none"><div id="customer_review-RMP5MBL5WNWGH" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AGJLYAARXFRMXWESRQ2WF727RXOA/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">April Holmes</span></div></a></div><div class="a-row"><a class="a-link-normal" title="2.0 out of 5 stars" href="/gp/customer-reviews/RMP5MBL5WNWGH/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-2 review-rating"><span class="a-icon-alt">2.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/RMP5MBL5WNWGH/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>Damaged and torn</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on March 22, 2021</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Item was not new and very damaged. Tears on each side of the vinyl sleeve and bent corners. The record itself seems to look ok, but not happy at all with a mangled up outer jacket.
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div class="a-popover-preload" id="a-popover-RMP5MBL5WNWGH_gallerySection_main">









<div id="RMP5MBL5WNWGH_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">
    <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
   </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini">
            <i class="a-icon a-icon-star a-star-2"><span class="a-icon-alt">2.0 out of 5 stars</span></i>
            <span class="a-size-base a-text-bold">
                Damaged and torn
            </span>
            <br>
            <span class="a-size-small a-color-secondary">
            
              
                  By April Holmes on March 22, 2021
              
              
            


            </span>
        </div>
        <span class="a-size-base">
            Item was not new and very damaged. Tears on each side of the vinyl sleeve and bent corners. The record itself seems to look ok, but not happy at all with a mangled up outer jacket.
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/8129tFqv8gL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                
                    <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/81t+tnmGPdL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                
                    <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/81u0235jqgL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                
            </div>
        </div>
    </div>
</div>

</div><div id="RMP5MBL5WNWGH_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="RMP5MBL5WNWGH">
       <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;name&quot;:&quot;RMP5MBL5WNWGH_gallerySection_main&quot;}" id="RMP5MBL5WNWGH-0"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" data-hook="review-image-tile" class="review-image-tile a-lazy-loaded" height="88" width="100%" data-src="https://images-na.ssl-images-amazon.com/images/I/8129tFqv8gL._SY88.jpg"/><noscript><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/8129tFqv8gL._SY88.jpg" height="88" width="100%"/></noscript><i class="a-icon a-icon-popover"></i></a></span><span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;name&quot;:&quot;RMP5MBL5WNWGH_gallerySection_main&quot;}" id="RMP5MBL5WNWGH-1"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" data-hook="review-image-tile" class="review-image-tile a-lazy-loaded" height="88" width="100%" data-src="https://images-na.ssl-images-amazon.com/images/I/81t+tnmGPdL._SY88.jpg"/><noscript><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/81t+tnmGPdL._SY88.jpg" height="88" width="100%"/></noscript><i class="a-icon a-icon-popover"></i></a></span><span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;name&quot;:&quot;RMP5MBL5WNWGH_gallerySection_main&quot;}" id="RMP5MBL5WNWGH-2"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" data-hook="review-image-tile" class="review-image-tile a-lazy-loaded" height="88" width="100%" data-src="https://images-na.ssl-images-amazon.com/images/I/81u0235jqgL._SY88.jpg"/><noscript><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/81u0235jqgL._SY88.jpg" height="88" width="100%"/></noscript><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:RMP5MBL5WNWGH_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("RMP5MBL5WNWGH", "[https://images-na.ssl-images-amazon.com/images/I/8129tFqv8gL._SL1600_.jpg, https://images-na.ssl-images-amazon.com/images/I/81t+tnmGPdL._SL1600_.jpg, https://images-na.ssl-images-amazon.com/images/I/81u0235jqgL._SL1600_.jpg]", data);
          });
        });
    </script>
<div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DRMP5MBL5WNWGH%26voteValue%3D1%26csrfT%3Dgsk%252BQkLC6DzBHCu1eKMjj0dZy%252FK4xtMQw9eqSPYAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23RMP5MBL5WNWGH&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gsk%2BQkLC6DzBHCu1eKMjj0dZy%2FK4xtMQw9eqSPYAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=RMP5MBL5WNWGH&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gsk%2BQkLC6DzBHCu1eKMjj0dZy%2FK4xtMQw9eqSPYAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=RMP5MBL5WNWGH&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R2DEYM8388YGRM" data-hook="review" class="a-section review aok-relative"><div id="R2DEYM8388YGRM-review-card" class="a-row a-spacing-none"><div id="customer_review-R2DEYM8388YGRM" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AEKPYGILN4T7BMLUFPMK6QOCSGMA/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Fraser </span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R2DEYM8388YGRM/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R2DEYM8388YGRM/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>Arrived new and undamaged</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on January 11, 2019</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Arrived new and undamaged
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div><div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR2DEYM8388YGRM%26voteValue%3D1%26csrfT%3DgsgGSLqzEcQ4RnBAw1Q2oLhraLLLaB%252BULnWWLiQAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R2DEYM8388YGRM&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gsgGSLqzEcQ4RnBAw1Q2oLhraLLLaB%2BULnWWLiQAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R2DEYM8388YGRM&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gsgGSLqzEcQ4RnBAw1Q2oLhraLLLaB%2BULnWWLiQAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R2DEYM8388YGRM&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R3AEXNC5PGGCOK" data-hook="review" class="a-section review aok-relative"><div id="R3AEXNC5PGGCOK-review-card" class="a-row a-spacing-none"><div id="customer_review-R3AEXNC5PGGCOK" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AEA7RK5AZPQYPT23NDIA2HFGKSMQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">The Hills</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R3AEXNC5PGGCOK/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3AEXNC5PGGCOK/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0000028RR">







  
  
    <span>great press</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Canada on March 29, 2020</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  great press of a picture disc virtually very little surface noise great sound
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="cr-helpful-button aok-float-left">
      <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.ca/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fdp%2FB0000028RR%2Fref%3Dcm_cr_dp_d_vote_lft%3Fie%3DUTF8%26voteInstanceId%3DR3AEXNC5PGGCOK%26voteValue%3D1%26csrfT%3Dgi9hKpe7bHAW%252FoalsyO69BVw2Bsn53fcE5CBRPcAAAABAAAAAGC6rYByYXcAAAAA%252B4kUEk%252F7iMGR3xPcX6iU%23R3AEXNC5PGGCOK&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=caflex&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text" role="button"><div class="cr-helpful-text">
          Helpful</div>
      </a></span></span></div>
  </span><span class="cr-footer-line-height">
        <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gi9hKpe7bHAW%2FoalsyO69BVw2Bsn53fcE5CBRPcAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3AEXNC5PGGCOK&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_report&amp;csrfT=gi9hKpe7bHAW%2FoalsyO69BVw2Bsn53fcE5CBRPcAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3AEXNC5PGGCOK&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div></div></div></div><div id="reviews-medley-footer" data-hook="reviews-medley-footer" class="a-section"><div class="a-row"></div><div class="a-row a-spacing-medium"><hr aria-hidden="true" class="a-spacing-base a-divider-normal"/><a data-hook="see-all-reviews-link-foot" class="a-link-emphasis a-text-bold" href="/Rage-Against-Machine/product-reviews/B0000028RR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&amp;reviewerType=all_reviews">See all reviews</a></div></div></div>
</div></span>
  <span class="cr-widget-DesktopGlobalReviews" data-hook="cr-widget-DesktopGlobalReviews">
      





  <div class="a-divider a-divider-section a-spacing-small"><div class="a-divider-inner"></div></div>



<span class="global-reviews-all">
  <div id="reviews-medley-global-expand-head" data-hook="reviews-medley-global-head" class="a-section global-reviews-header">
    <h3 data-hook="dp-global-reviews-header" class="a-spacing-base">
      
        
          Top reviews from other countries
        
        
      
    </h3>
  
    
      <div class="a-section cr-list-loading reviews-loading aok-hidden"></div>
      <div class="a-row">
        <div class="a-section a-spacing-micro cr-translate-these-reviews-section"><span class="a-declarative" data-action="reviews:ajax-post" data-reviews:ajax-post="{&quot;indicatorSelector&quot;:&quot;.reviews-loading&quot;,&quot;params&quot;:{&quot;isSingleReview&quot;:&quot;false&quot;,&quot;reviews&quot;:&quot;[{\&quot;id\&quot;:\&quot;R2KAYLKAD327EI\&quot;,\&quot;version\&quot;:0,\&quot;locale\&quot;:{\&quot;language\&quot;:\&quot;de\&quot;,\&quot;country\&quot;:\&quot;DE\&quot;},\&quot;marketplaceId\&quot;:\&quot;A1PA6795UKMFR9\&quot;}]&quot;,&quot;csrf&quot;:&quot;ggFL4kNO/y772u88th2u66i1MteZ5ntKzndf91IAAAABAAAAAGC6rYByYXcAAAAA+4kUEk/7iMGR3xPcX6iU&quot;,&quot;selectorPrefix&quot;:&quot;.global-reviews-all&quot;},&quot;url&quot;:&quot;/hz/reviews-render/ajax/reviews/augment/ref=cm_cr_dp_d_trn_a_grs&quot;}"><a class="a-link-normal" href="#customerReviews">Translate all reviews to English</a></span></div>
      </div>
    
  </div>
  
  <div class="a-row a-spacing-large">
    <div class="a-section global-reviews-content celwidget">
      
      <div id="cm-cr-global-review-list" data-hook="global-customer-reviews-widget" class="a-section global-review-views review-views celwidget">
        <div id="R3G47VFPOH5DOZ" data-hook="review" class="a-section review aok-relative cr-desktop-review-page-0"><div id="R3G47VFPOH5DOZ-review-card" class="a-row a-spacing-none"><div id="customer_review_foreign-R3G47VFPOH5DOZ" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><div class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Miss J</span></div></div></div><div class="a-row a-spacing-none"><i data-hook="cmps-review-star-rating" class="a-icon a-icon-star a-star-1 review-rating"><span class="a-icon-alt">1.0 out of 5 stars</span></i><span class="a-letter-space"></span><span data-hook="review-title" class="a-size-base review-title a-color-base review-title-content a-text-bold">







  
  
    <span>Manufacturing error</span>
  
</span></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in the United Kingdom on January 12, 2021</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Bought this record twice from Amazon and both copies skipped on the same part of the record. There is clearly a manufacturing error with this whole batch, so be sure to check your copy if you buy. Brilliant album but I will be going to an actual record store to buy this now
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">2 people found this helpful</span></div></span><span class="cr-footer-line-height">
        <span><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=grNRw7U84oMbu1MKiYkJXGRIE%2BdkfsJbcdkQkSoAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3G47VFPOH5DOZ&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=grNRw7U84oMbu1MKiYkJXGRIE%2BdkfsJbcdkQkSoAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R3G47VFPOH5DOZ&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R1GVICGSOTHCMS" data-hook="review" class="a-section review aok-relative cr-desktop-review-page-0"><div id="R1GVICGSOTHCMS-review-card" class="a-row a-spacing-none"><div id="customer_review_foreign-R1GVICGSOTHCMS" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><div class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">MotherDuck</span></div></div></div><div class="a-row a-spacing-none"><i data-hook="cmps-review-star-rating" class="a-icon a-icon-star a-star-1 review-rating"><span class="a-icon-alt">1.0 out of 5 stars</span></i><span class="a-letter-space"></span><span data-hook="review-title" class="a-size-base review-title a-color-base review-title-content a-text-bold">







  
  
    <span>Jumps and skips</span>
  
</span></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in the United Kingdom on December 10, 2020</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Really disappointed as this was going to be a gift. It jumps all the way through the album, too much to be able to enjoy it and not good enough when it’s a gift. I am returning it and will purchase elsewhere as a replacement is likely to have the same issues, it’s the press as not damaged or scratched.
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div></span><span class="cr-footer-line-height">
        <span><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=gpWiwY2ZXLaqLR%2Fh9uXwse%2F5yPwFYWFNhbYukwwAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R1GVICGSOTHCMS&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=gpWiwY2ZXLaqLR%2Fh9uXwse%2F5yPwFYWFNhbYukwwAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R1GVICGSOTHCMS&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R5AKPO9D3RIO5" data-hook="review" class="a-section review aok-relative cr-desktop-review-page-0"><div id="R5AKPO9D3RIO5-review-card" class="a-row a-spacing-none"><div id="customer_review_foreign-R5AKPO9D3RIO5" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><div class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Amazon Customer</span></div></div></div><div class="a-row a-spacing-none"><i data-hook="cmps-review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i><span class="a-letter-space"></span><span data-hook="review-title" class="a-size-base review-title a-color-base review-title-content a-text-bold">







  
  
    <span>Powerful</span>
  
</span></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in the United Kingdom on November 8, 2020</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  forgot how good this is... excellent vinyl pressing...powerful and even more relevent today than it was almost 20 years ago....fits this format perfectly...bass line and guitar riffs make your teeth vibrate....half expecting the turntable to jump off the cupboard and bash me senseless...
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div></span><span class="cr-footer-line-height">
        <span><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=gqerg7IpZv%2BQATSFFa5s5BfyafB8Z0JZsbqkdVoAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R5AKPO9D3RIO5&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=gqerg7IpZv%2BQATSFFa5s5BfyafB8Z0JZsbqkdVoAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R5AKPO9D3RIO5&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="R2KAYLKAD327EI" data-hook="review" class="a-section review aok-relative cr-desktop-review-page-0"><span class="cr-translated-review-content">
    <span class="cr-single-review-loading aok-hidden">
      <span class="reviews-loading"></span>
    </span>
  </span>
<div id="R2KAYLKAD327EI-review-card" class="a-row a-spacing-none"><div id="customer_review_foreign-R2KAYLKAD327EI" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><div class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/a05b7a85-5ce1-4e39-a810-1762800f3246._CR0,0.0,333,333_SX48_.jpg"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/a05b7a85-5ce1-4e39-a810-1762800f3246._CR0,0.0,333,333_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Mike</span></div></div></div><div class="a-row a-spacing-none"><i data-hook="cmps-review-star-rating" class="a-icon a-icon-star a-star-2 review-rating"><span class="a-icon-alt">2.0 out of 5 stars</span></i><span class="a-letter-space"></span><span data-hook="review-title" class="a-size-base review-title a-color-base review-title-content a-text-bold">







  
    <span class="cr-original-review-content">gravierende Sound-Einbußen durch dieses Re-Mastering</span><span class="cr-translated-review-content aok-hidden"></span>
  
  
</span></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in Germany on December 28, 2015</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
    <span class="cr-original-review-content">
  Lieber Vlado Meller! Wenn ein Album in den Sound City Studios in Analogtechnik aufgenommen und auch noch von Andy Wallace persönlich abgemischt wurde, dann bitte: Finger weg lassen! Denn dieses Gesamtwerk aus dem Jahre 1992 hat Musikgeschichte geschrieben! Ich habe diese Scheibe (Vinyl) aus dem Jahre 1992 mit dem aktuellen Remastering verglichen. High-End Plattenspieler und Audio Kette vorhanden. Und ich muss sagen, dass dieses &#34;neue&#34; Remastering eine Katastrophe ist. Wo ist die offene HiHat? Wo die Transparenz der genial abgemischten Becken? Es klingt alles dumpfer, enger, verschlossener. Die alles &#34;tragenden&#34; Becken sind unter einer Bettdecke verschwunden!<br />Schaut Euch den Film &#34;Sound City&#34; an. Dann wird klar, dass man bei solchen bewusst analog aufgenommenen Kunstwerken eines unbedingt beachten sollte: Finger Weg beim Remastering!
</span><span class="cr-translated-review-content aok-hidden"></span>
  
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div class="a-popover-preload" id="a-popover-R2KAYLKAD327EI_gallerySection_main">









<div id="R2KAYLKAD327EI_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">
    <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
   </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini">
            <i class="a-icon a-icon-star a-star-2"><span class="a-icon-alt">2.0 out of 5 stars</span></i>
            <span class="a-size-base a-text-bold">
                gravierende Sound-Einbußen durch dieses Re-Mastering
            </span>
            <br>
            <span class="a-size-small a-color-secondary">
            
              
              
                Reviewed in Germany on December 28, 2015
              
            


            </span>
        </div>
        <span class="a-size-base">
            Lieber Vlado Meller! Wenn ein Album in den Sound City Studios in Analogtechnik aufgenommen und auch noch von Andy Wallace persönlich abgemischt wurde, dann bitte: Finger weg lassen! Denn dieses Gesamtwerk aus dem Jahre 1992 hat Musikgeschichte geschrieben! Ich habe diese Scheibe (Vinyl) aus dem Jahre 1992 mit dem aktuellen Remastering verglichen. High-End Plattenspieler und Audio Kette vorhanden. Und ich muss sagen, dass dieses &#34;neue&#34; Remastering eine Katastrophe ist. Wo ist die offene HiHat? Wo die Transparenz der genial abgemischten Becken? Es klingt alles dumpfer, enger, verschlossener. Die alles &#34;tragenden&#34; Becken sind unter einer Bettdecke verschwunden!<br />Schaut Euch den Film &#34;Sound City&#34; an. Dann wird klar, dass man bei solchen bewusst analog aufgenommenen Kunstwerken eines unbedingt beachten sollte: Finger Weg beim Remastering!
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71vljYJAwxL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                
            </div>
        </div>
    </div>
</div>

</div><div id="R2KAYLKAD327EI_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="R2KAYLKAD327EI">
       <span class="a-declarative" data-action="a-modal" data-a-modal="{&quot;name&quot;:&quot;R2KAYLKAD327EI_gallerySection_main&quot;}" id="R2KAYLKAD327EI-0"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" data-hook="cmps-review-image-tile" class="linkless-review-image-tile a-lazy-loaded" height="88" width="100%" data-src="https://images-na.ssl-images-amazon.com/images/I/71vljYJAwxL._SY88.jpg"/><noscript><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71vljYJAwxL._SY88.jpg" height="88" width="100%"/></noscript><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:R2KAYLKAD327EI_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("R2KAYLKAD327EI", "[https://images-na.ssl-images-amazon.com/images/I/71vljYJAwxL.jpg]", data);
          });
        });
    </script>
<div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">74 people found this helpful</span></div></span><span class="cr-footer-line-height">
        <span><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=ggc5rUPD8a36R3GOxU6nIu%2BC5Z0zPTovjcvLxFAAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R2KAYLKAD327EI&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=ggc5rUPD8a36R3GOxU6nIu%2BC5Z0zPTovjcvLxFAAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R2KAYLKAD327EI&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  <div class="a-section a-spacing-none a-spacing-top-small cr-translate-this-review-section"><span class="a-declarative" data-action="reviews:ajax-post" data-reviews:ajax-post="{&quot;indicatorSelector&quot;:&quot;#R2KAYLKAD327EI .cr-single-review-loading&quot;,&quot;params&quot;:{&quot;isSingleReview&quot;:&quot;true&quot;,&quot;reviews&quot;:&quot;[{\&quot;id\&quot;:\&quot;R2KAYLKAD327EI\&quot;,\&quot;version\&quot;:0,\&quot;locale\&quot;:{\&quot;language\&quot;:\&quot;de\&quot;,\&quot;country\&quot;:\&quot;DE\&quot;},\&quot;marketplaceId\&quot;:\&quot;A1PA6795UKMFR9\&quot;}]&quot;,&quot;csrf&quot;:&quot;ggFL4kNO/y772u88th2u66i1MteZ5ntKzndf91IAAAABAAAAAGC6rYByYXcAAAAA+4kUEk/7iMGR3xPcX6iU&quot;,&quot;selectorPrefix&quot;:&quot;.cr-widget-FocalReviews&quot;},&quot;url&quot;:&quot;/hz/reviews-render/ajax/reviews/augment/ref=cm_cr_dp_d_trn_s_grs&quot;}"><a data-hook="cr-translate-this-review-link" class="a-size-base a-link-normal" href="#customerReviews">Translate review to English</a></span></div></div></div></div></div><div id="R1RGYK1S6YWRMN" data-hook="review" class="a-section review aok-relative cr-desktop-review-page-0"><div id="R1RGYK1S6YWRMN-review-card" class="a-row a-spacing-none"><div id="customer_review_foreign-R1RGYK1S6YWRMN" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><div class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">@Pinhead_UK</span></div></div></div><div class="a-row a-spacing-none"><i data-hook="cmps-review-star-rating" class="a-icon a-icon-star a-star-2 review-rating"><span class="a-icon-alt">2.0 out of 5 stars</span></i><span class="a-letter-space"></span><span data-hook="review-title" class="a-size-base review-title a-color-base review-title-content a-text-bold">







  
  
    <span>Great Album - Poor Vinyl</span>
  
</span></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in the United Kingdom on March 3, 2021</span><div class="a-row a-spacing-mini review-data review-format-strip"><span data-hook="avp-badge-linkless" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text"><div aria-live="polite" data-a-expander-name="review_text_read_more" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">









  
  
    <span>
  Such a great album but it's compromised by the quality of the pressing. Skipping from the first play and skips just when you don't want it to!!!<br />Ruins the enjoyment of the music! Might be an isolated incident but the option to receive a replacement isn't available which is frustrating.<br />Given it two stars because of the vinyl quality but I don't want this to be a reflection of the album! It's a 5 star album!!!
</span>
  
</div><div class="a-expander-header a-expander-partial-collapse-header"><div class="a-expander-content-fade"></div><a href="javascript:void(0)" data-hook="expand-collapse-read-more-less" aria-label="Toggle full review text" data-action="a-expander-toggle" class="a-declarative" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;Read more&quot;, &quot;collapse_prompt&quot;:&quot;Read less&quot;}"><i class="a-icon a-icon-extender-expand"></i><span class="a-expander-prompt">Read more</span></a></div></div></span></div><div data-hook="review-comments" class="a-row review-comments cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div></span><span class="cr-footer-line-height">
        <span><span class="a-declarative" data-action="cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=gu3qis0Yonjx5tmV2yS7tkT41dVJOhqfB5FYBHAAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R1RGYK1S6YWRMN&amp;sessionId=138-4669640-7712440&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-abuse?ie=UTF8&amp;voteDomain=Reviews&amp;ref=cm_cr_dp_d_freport&amp;csrfT=gu3qis0Yonjx5tmV2yS7tkT41dVJOhqfB5FYBHAAAAABAAAAAGC6rYByYXcAAAAA%2B4kUEk%2F7iMGR3xPcX6iU&amp;entityId=R1RGYK1S6YWRMN&amp;sessionId=138-4669640-7712440">Report abuse</a></span></span></span>
  </div></div></div></div><div id="cr-pagination-footer-0" class="a-section a-spacing-top-extra-large"><hr aria-hidden="true" class="a-spacing-base a-divider-normal"/><a data-hook="see-all-reviews-link-foot" class="a-link-emphasis a-text-bold" href="/Rage-Against-Machine/product-reviews/B0000028RR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&amp;reviewerType=all_reviews">See all reviews</a></div>
      </div>
    </div>
  </div>
</span>
</span>
  </div></div></div></div></div><script type="text/javascript">
var isAUI = typeof P === 'object' && typeof P.when === 'function';
  if(typeof setCSMReq == 'function') {
        setCSMReq('cf');
  }else {
     if(typeof uet == 'function') {
        uet('cf');
     }
     if(isAUI){
     	   P.trigger("cf");
     	}else{
     		amznJQ.completedStage('amznJQ.criticalFeature');
     	}
  }
</script>
 





<script type="text/javascript">



(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('cf').execute(function(){
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/21q6fNgsQrL._RC|21XJFDMQuNL.js,11OyIHCq0lL.js,01GhKb2usNL.js_.js?AUIClients/HardlinesFeatureDetailPageMetaAsset');
});




  if(typeof P !== "undefined" && typeof P.when === "function"){
    P.when('cf').execute(function() {
          P.when('search-js-jq').execute(function(){});
  P.when('amazonShoveler').execute(function(){});
  P.when('simsJS').execute(function(){});
  P.when('cmuAnnotations').execute(function(){});
  P.when('externalJS.tagging').execute(function(){});
  P.when('amzn-ratings-bar').execute(function(){});
  P.when('accessoriesJS').execute(function(){});
  P.when('priceformatterJS').execute(function(){});
  P.when('CustomerPopover').execute(function(){});

    });
  }
</script>

 


 

<script type="text/javascript">
// This will fetch the resource in a low impact way from the experiment server.
// executeOnload will prevent fetching the resource until everything else on the page has loaded.
var cloudfrontImg = new Image();
var shouldExecuteOnload = ("1" == "1");
if (shouldExecuteOnload) {
    if (window.addEventListener) {
        window.addEventListener("load", function() {
            setTimeout(function(){ cloudfrontImg.src = "//cloudfront-labs.amazonaws.com/x.png"; }, 400);}, false);
    } else if (window.attachEvent) {
        window.attachEvent("onload", function() {
            setTimeout(function(){ cloudfrontImg.src = "//cloudfront-labs.amazonaws.com/x.png"; }, 400);});
    }
} else {
    setTimeout(function(){ cloudfrontImg.src = "//cloudfront-labs.amazonaws.com/x.png"; }, 400);
}
</script>
 

 
 


<script type="text/javascript">
var isAUI = typeof P === 'object' && typeof P.when === 'function';
  if(typeof setCSMReq == 'function') {
        setCSMReq('cf');
  }else {
     if(typeof uet == 'function') {
        uet('cf');
     }
     if(isAUI){
     	   P.trigger("cf");
     	}else{
     		amznJQ.completedStage('amznJQ.criticalFeature');
     	}
  }
</script>
<div cel_widget_id='dpx-ajax-block-components_csm_instrumentation_wrapper' class='celwidget'>




  



        
        
        
        
  








    








<div id="ajaxBlockComponents_feature_div" class="celwidget" data-feature-name="ajaxBlockComponents">













<script type="text/javascript">
P.when('A').execute('triggerVideoAjax', function(A){
var obj = A.$.parseJSON('{"dataInJson":null,"colorImages":{},"videos":[],"lazyLoadExperienceDisabled":true,"lazyLoadExperienceOnHoverDisabled":false,"refactorEnabled":false,"mainImageSizes":[["355","355"],["450","450"],["425","550"],["466","606"],["522","679"],["569","741"],["679","879"]]}');
A.trigger('triggerVideoAjax',obj.videos);
});

</script>

























</div>
</div>

            
            
    










  <script type="text/javascript">
    // Only execute if performance object is defined in JS
    if(typeof performance!= "undefined" && typeof performance.getEntries != "undefined") {




        var metaAssetNames = [];
        metaAssetNames.push("DetailPageMetaAssetFixed");
        metaAssetNames.push("DetailPageDesktopImageBlockMetaAsset");
        metaAssetNames.push("MusicDetailPageMetaAsset_TURBO_DESKTOP");
        if(metaAssetNames.length > 0)  {
            for(assetIndex = 0; assetIndex < metaAssetNames.length; assetIndex ++) {
	     var metaAssetName = metaAssetNames[assetIndex];
             var re = new RegExp("\\.css\\?AUIClients/" + metaAssetName); 
             for(i = 0; i < performance.getEntries().length; i++) {	   	
                var dpEntry = performance.getEntries()[i];
		var res = dpEntry.name.match(re);
                if(res && dpEntry.initiatorType  && dpEntry.initiatorType == "link") {
                    var dpmaDuration = dpEntry.duration;
                    ue.count(metaAssetName +".duration", dpmaDuration);
                    if(dpmaDuration < 50) {
                        ue.tag(metaAssetName + "Cached");
                    } else {
                        ue.tag(metaAssetName + "NotCached");
                    }
                    ue.count(metaAssetName + ".startTime", dpEntry.startTime);
                }
	      }
	    }
        }
        else {
                ue.count("DPMANoMetaAsset", 1);
        }

        for(i = 0 ; i < performance.getEntries().length ; i++) {
            var name = performance.getEntries()[i].name ;
            var res = name.match(/\.css\?AUIClients\/AmazonUI/);
	    var initiatorType = performance.getEntries()[i].initiatorType;
            if(res && initiatorType && initiatorType == "link") {
                var duration = performance.getEntries()[i].duration ;
                ue.count("aui.duration", duration);
                ue.count("aui.startTime", performance.getEntries()[i].startTime);
                if(duration < 50) {
                    csmTag = "auiCached";
                }
                else {
                    csmTag = "auiNotCached";
                }

                if(window.ue && ue.tag) {
                    ue.tag(csmTag);
                }
                break;
            }
        }
    }
</script>
















<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('A').execute(function(A){
  if(A.preload){
    A.preload('https://images-na.ssl-images-amazon.com/images/I/61XKxrBtDVL._RC|11Y+5x+kkTL.js,51106gSDnJL.js,11-zXBZR6KL.js,11giXtZCwVL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,01O9dYORveL.js,21NNXfMitSL.js,11rRjDLdAVL.js,51X-X0x2aRL.js,11kWu3cNjYL.js,11g2BPXNlrL.js,11OREnu1epL.js,11KbZymw5ZL.js,21r53SJg7LL.js,0190vxtlzcL.js,51GBHgW1KPL.js,31ask0y-LBL.js,015c-6CIP9L.js,01ezj5Rkz1L.js,11+RxVdhNcL.js,31o2NGTXThL.js,01rpauTep4L.js,01ga2A1fW4L.js_.js?AUIClients/AmazonUI&DCahMwKq#348458-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,418YjvsUB+L.css,21qPwhPKAAL.css,01Vctty9pOL.css,017DsKjNQJL.css,01L-6KXabGL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11bGSgD5pDL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,01ZfXnjPmmL.css,01oDR3IULNL.css,31ZcpBfSgNL.css,01XPHJk60-L.css,01R0k0yxPXL.css,21xVR0NtxzL.css,11gneA3MtJL.css,21fecG8pUzL.css,01RddH8vm-L.css,01CFUgsA-YL.css,21AmhU6t0sL.css,11zGrJZ9D2L.css,11tRp6+0HHL.css,11061HxnEvL.css,11oHt2HYxnL.css,01-fWz3sOQL.css,11ocrgKoE-L.css,11RKoGSb-gL.css,11g1xm90ZvL.css,01QrWuRrZ-L.css,21pIv-yKhaL.css,01Wiow6micL.css,01gAR5pB+IL.css,119dKrtBoVL.css,11Y05DTEL6L.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI&q7tmqwsI#not-trident.322290-T1.322288-T1.265810-T2');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/01j2xsQ1yML.css?AUIClients/DetailPageMetaAssetFixed#desktop');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/31cu23aPw1L.js?AUIClients/AmazonUICalendar');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/11xqfyHx1TL._RC|11B3-fvRFzL.css_.css?AUIClients/AmazonUICalendar#not-trident');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/31Nnd8dHj4L._RC|31Nb5hZQizL.js,316nVZ1c+gL.js,21u1PnPEsML.js,318rs4piGPL.js,11ISJZDdTuL.js,01TQyo0bnIL.js,11bdX9xnYpL.js,01jEqq6I0UL.js,013NxCyC-FL.js,61F4XpPaNeL.js,01X5C8pWB1L.js,01Fy9QPljuL.js,11oGaoYgbdL.js,0193uyIciNL.js,41fW1gpnNZL.js,41jhtQ3H1kL.js,11p0nLfNCcL.js,01s9HEfbt3L.js,11iHZuQapKL.js,015TRQC5i+L.js,01JzE3-DfLL.js,6181fgtPhlL.js,01I+ls4AqQL.js,01XEEGOr+kL.js,01G1DehcNNL.js,01PQKs49DyL.js,11qajewhV-L.js,41p3KVnq7iL.js,51xVq6M-4eL.js,01j5DeZSMzL.js,41BxVWt7n0L.js,312EnPYWpmL.js,11nOzlnr6+L.js,011VhuFIPDL.js,01WkIloYPkL.js_.js?AUIClients/HardlinesDetailPageMetaAssetFixed&Lt6MU0H7#desktop.ca.195406-T1.291749-T1.322857-T1.346364-T1.184660-C');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/61OvCWp7nBL._RC|11bRdV2t20L.css,518KmQy9QVL.css,01g2EoxOu-L.css,218Y6Z0tipL.css,21ByukFKG4L.css,01N8OOpUZPL.css,0121zKjk26L.css,11xRy3bSkOL.css,01QUs5FVXoL.css,11jG57OztzL.css,41vOQb1k0LL.css,01FtAuFRr3L.css,01rgQ3jqo7L.css,21KhX-wTSTL.css,31TJtSmBkXL.css,11X8K4AolpL.css,21PjfsP9YvL.css,21W5fiSj06L.css,31cE7qTuwaL.css,015FNYa5WbL.css,01lHbKl4MxL.css,017KStdmPkL.css,21jUQU6VhYL.css,114FIgEwAuL.css,01TrKJuj6JL.css,2170Ev7c3lL.css,01P0iSwDaIL.css,01n8CeLW9QL.css_.css?AUIClients/HardlinesDetailPageMetaAssetFixed&KyaXAigw#desktop.ca.336056-T1.343686-C.310456-T1.237182-T1.172402-T1.346364-T1.129737-C.94145-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/61jl8YsxhUL._RC|01XginIhPBL.js,01PQKs49DyL.js_.js?AUIClients/DetailPageDesktopImageBlockMetaAsset&EIhgIZq+#169593-T1.299993-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/21TMrbNilEL._RC|21YblE14ZTL.js,21E2aIDj6DL.js,318iw3j-82L.js,31KyLb404wL.js,01g2etah0NL.js,21KJ58XxAlL.js,219O6ZmDMOL.js,31oAl8dJC2L.js,41+DnZtRZiL.js,31TF9TzobmL.js,01WNBm1NhqL.js,41mj+87W1ML.js,21-iZD9aN-L.js,41DJO26De1L.js,71LXbtOXb4L.js,4123BTTtUrL.js,11nOzlnr6+L.js,41p3KVnq7iL.js,41lkyHEebjL.js,21NDIsf0a1L.js,11+dypSOVUL.js,01jqyAujTwL.js,31+0pACITzL.js,61OJ4tEokrL.js,01RQtSMdG+L.js,01OtvpwikQL.js,31qUdoxPE8L.js,61Y3Spju5XL.js,21v7Os12mhL.js,21mWHADpIYL.js,21qOGqjcM7L.js,31UaW8zx0bL.js,01lcH4zcTaL.js,013eoEBTVUL.js,01YivelYW5L.js,016QFWAAdML.js,61vQfS7Z7BL.js,41-0DNnwzEL.js,51tG8ZFBvkL.js,11DbyV7EqEL.js,01IQoRXvpnL.js,01R7uttDWaL.js,01dISN2P6PL.js,01uSBjIDXbL.js,01WVAau8sBL.js,01mrvjIHzmL.js,01yrDq7zy5L.js,01fN1Y8iqzL.js,015o6sfRHyL.js,014kCoIHgIL.js,019W6kk1gjL.js,01hkseOXj6L.js,311A0yCIeJL.js,01iRN5bMQkL.js,51jKqMrt8zL.js,01acYp41-1L.js,01sSKGYWoFL.js,01cqBGb9TKL.js,01PQKs49DyL.js,01fffmaF5CL.js,414R8YyB1uL.js,11Xxd-w8V7L.js,31ByFrWaqrL.js,01q-Ep-UrEL.js,01gsBemrwzL.js,013aNY++XJL.js,11pS0Syz0DL.js,51RL3cCksuL.js,018ZxeiHuPL.js,011VhuFIPDL.js,01LBPfQ0IdL.js,013YkX6C2QL.js,21IQl4blS4L.js,01HPCJZdF6L.js,61BHCbTQZEL.js,218Qx5H6s4L.js,01WEY0XphhL.js_.js?AUIClients/HardlinesDetailPageMetaAssetVariable_TURBO_DESKTOP&RosPbaV2#desktop.ca.323516-T1.336153-T1.291426-T1.314612-T1.292695-C.312885-T1.312887-T1.140997-T1.188581-T1.349527-T1.322640-T1.322857-T1.317356-T1.310834-T1.317281-T1.310975-T1.309439-T1.184219-T1.172346-T1.109378-T1.227612-T1.311239-T1.227610-T4.169593-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/21U6%2B8tKunL._RC|315GMAwkLiL.css,01Qji-D4YPL.css,01rdVnPkgmL.css,01KvCqKMBgL.css,11iwHtffX1L.css,41IYcMQCjlL.css,01vUDet4b1L.css,01HIwjet0ZL.css,21CTcSQ19+L.css,21PiSBLb3dL.css,419+eoM+IGL.css,01n8CeLW9QL.css,21jUQU6VhYL.css,31l-Nc5zsiL.css,31dTK1hHb6L.css,11kmwdXfY5L.css,01bkkYjxP7L.css,31v5j8kQd3L.css,01NW8VTUeVL.css,01zWxM9Vh0L.css,011uHgmxBfL.css,416E7MkrO7L.css,31bbR9oU1FL.css,114HJAY+ShL.css,01wkbZw3FtL.css,21ZjVyQPjML.css,01OhA16ND1L.css,41ig2OsbsxL.css,41xvDKH0l6L.css,01TZ9fpDSSL.css,21ohnckzsnL.css,01iXxkJ+wuL.css,11ikU6MX1JL.css,01ZcdNKBOIL.css,31YeUjpBngL.css,01AT3O0C6cL.css,01eugUpDlVL.css,01adN84djtL.css,01+KRP2j52L.css,01lHBbKIwtL.css,01eviB7YqCL.css,01goIIPoVxL.css_.css?AUIClients/HardlinesDetailPageMetaAssetVariable_TURBO_DESKTOP&m270Ugt7#desktop.ca.323516-T1.113788-C.188581-T1.309439-T1.172346-T1.169593-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/11XQDILn5QL._RC|21TMrbNilEL.js,21YblE14ZTL.js,21E2aIDj6DL.js,318iw3j-82L.js,31KyLb404wL.js,01g2etah0NL.js,31Nb5hZQizL.js,21KJ58XxAlL.js,219O6ZmDMOL.js,31oAl8dJC2L.js,41+DnZtRZiL.js,31TF9TzobmL.js,21u1PnPEsML.js,31JUr01gz+L.js,316nVZ1c+gL.js,01AdYLY9rHL.js,01IOMCsVFCL.js,21-iZD9aN-L.js,41DJO26De1L.js,01TQyo0bnIL.js,11bdX9xnYpL.js,71LXbtOXb4L.js,01WNBm1NhqL.js,41mj+87W1ML.js,01X5C8pWB1L.js,01Fy9QPljuL.js,41lkyHEebjL.js,11oGaoYgbdL.js,01HmcbFsnFL.js,01JzE3-DfLL.js,31sG+M5QN5L.js,11+dypSOVUL.js,01I+ls4AqQL.js,01jqyAujTwL.js,31+0pACITzL.js,01OrQ5AXqsL.js,11DGcrZsUwL.js,01OtvpwikQL.js,31qUdoxPE8L.js,21qOGqjcM7L.js,01S8y9NkxoL.js,01ZF+ovNflL.js,31iuSAu5YqL.js,611uA7Z80VL.js,013eoEBTVUL.js,01YivelYW5L.js,016QFWAAdML.js,51tG8ZFBvkL.js,01R7uttDWaL.js,01dISN2P6PL.js,01uSBjIDXbL.js,01WVAau8sBL.js,01mrvjIHzmL.js,01yrDq7zy5L.js,01fN1Y8iqzL.js,01NKGaW0w5L.js,01rEmdLLpxL.js,019W6kk1gjL.js,01hkseOXj6L.js,01lcH4zcTaL.js,01acYp41-1L.js,311A0yCIeJL.js,01iRN5bMQkL.js,51jKqMrt8zL.js,41p3KVnq7iL.js,01XEEGOr+kL.js,01PQKs49DyL.js,31Nnd8dHj4L.js,01gsBemrwzL.js,11qajewhV-L.js,51xVq6M-4eL.js,01j5DeZSMzL.js,41BxVWt7n0L.js,312EnPYWpmL.js,11nOzlnr6+L.js,013aNY++XJL.js,11pS0Syz0DL.js,51RL3cCksuL.js,018ZxeiHuPL.js,011VhuFIPDL.js,01WkIloYPkL.js,21IQl4blS4L.js,01HPCJZdF6L.js,41-0DNnwzEL.js,61BHCbTQZEL.js,218Qx5H6s4L.js,01WEY0XphhL.js_.js?AUIClients/SoftlinesDetailPageMetaAsset_TURBO_DESKTOP&ziZYDvTx#desktop.ca.292695-C.312885-T1.195406-T1.349527-T1.322640-T1.322857-T1.346364-T1.317356-T1.310834-T1.184660-C.310975-T1.309439-T1.184219-T1.202285-C.109378-T1.227612-T1.311239-T1.227610-T4.169593-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/61OvCWp7nBL._RC|11bRdV2t20L.css,41j52RQ1GmL.css,21U6+8tKunL.css,315GMAwkLiL.css,01Qji-D4YPL.css,218Y6Z0tipL.css,01rdVnPkgmL.css,01KvCqKMBgL.css,11iwHtffX1L.css,41IYcMQCjlL.css,01N8OOpUZPL.css,21UvDaNT8uL.css,21ByukFKG4L.css,01lYrTXt4xL.css,0121zKjk26L.css,21CTcSQ19+L.css,21PiSBLb3dL.css,11jG57OztzL.css,01vUDet4b1L.css,01HIwjet0ZL.css,31l-Nc5zsiL.css,01FtAuFRr3L.css,01QLwk8mu6L.css,11kmwdXfY5L.css,01bkkYjxP7L.css,018mGORJ7tL.css,01NW8VTUeVL.css,01zWxM9Vh0L.css,011uHgmxBfL.css,114HJAY+ShL.css,01wL78bNyyL.css,01MLzcotflL.css,21VgVEzltcL.css,21ZjVyQPjML.css,01OhA16ND1L.css,21ohnckzsnL.css,01iXxkJ+wuL.css,01wkbZw3FtL.css,01AT3O0C6cL.css,31YeUjpBngL.css,21jUQU6VhYL.css,015FNYa5WbL.css,01g2EoxOu-L.css,017KStdmPkL.css,114FIgEwAuL.css,01TrKJuj6JL.css,2170Ev7c3lL.css,01P0iSwDaIL.css,01n8CeLW9QL.css,01eviB7YqCL.css,41xvDKH0l6L.css,01goIIPoVxL.css_.css?AUIClients/SoftlinesDetailPageMetaAsset_TURBO_DESKTOP&4hNxXaHU#desktop.ca.113788-C.336056-T1.343686-C.310456-T1.237182-T1.172402-T1.346364-T1.309439-T1.94145-T1.202285-C.109378-T1.169593-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/21E2aIDj6DL._RC|318iw3j-82L.js,31KyLb404wL.js,01g2etah0NL.js,31Nb5hZQizL.js,21KJ58XxAlL.js,219O6ZmDMOL.js,31oAl8dJC2L.js,41+DnZtRZiL.js,31TF9TzobmL.js,01J0x2Pr7-L.js,21cIMwkijYL.js,31vMFUg376L.js,01TQyo0bnIL.js,11bdX9xnYpL.js,71LXbtOXb4L.js,01WNBm1NhqL.js,41mj+87W1ML.js,01X5C8pWB1L.js,01Fy9QPljuL.js,41lkyHEebjL.js,11oGaoYgbdL.js,01JzE3-DfLL.js,11+dypSOVUL.js,01jqyAujTwL.js,31+0pACITzL.js,01OtvpwikQL.js,31qUdoxPE8L.js,11nOzlnr6+L.js,41p3KVnq7iL.js,11p0nLfNCcL.js,11iHZuQapKL.js,21qOGqjcM7L.js,21TMrbNilEL.js,21YblE14ZTL.js,611uA7Z80VL.js,013eoEBTVUL.js,016QFWAAdML.js,51tG8ZFBvkL.js,019W6kk1gjL.js,01hkseOXj6L.js,311A0yCIeJL.js,01iRN5bMQkL.js,51jKqMrt8zL.js,01PQKs49DyL.js,11qajewhV-L.js,51xVq6M-4eL.js,01j5DeZSMzL.js,41BxVWt7n0L.js,312EnPYWpmL.js,013aNY++XJL.js,11pS0Syz0DL.js,51RL3cCksuL.js,018ZxeiHuPL.js,011VhuFIPDL.js,01WkIloYPkL.js,21IQl4blS4L.js,01HPCJZdF6L.js,41-0DNnwzEL.js,61BHCbTQZEL.js,218Qx5H6s4L.js,01WEY0XphhL.js_.js?AUIClients/MediaDetailPageMetaAsset_TURBO_DESKTOP&A1p236Fn#desktop.ca.320228-T1.292695-C.312885-T1.195406-T1.349527-T1.322640-T1.322857-T1.346364-T1.317356-T1.310834-T1.184660-C.310975-T1.309439-T1.184219-T1.109378-T1.227612-T1.311239-T1.227610-T4.169593-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/61OvCWp7nBL._RC|416-VmOaPAL.css,315GMAwkLiL.css,01Qji-D4YPL.css,218Y6Z0tipL.css,01rdVnPkgmL.css,01KvCqKMBgL.css,11iwHtffX1L.css,41IYcMQCjlL.css,31wOEf+ImDL.css,21IgJUJJ2SL.css,11jG57OztzL.css,01vUDet4b1L.css,01HIwjet0ZL.css,31l-Nc5zsiL.css,01FtAuFRr3L.css,11kmwdXfY5L.css,01bkkYjxP7L.css,01NW8VTUeVL.css,01zWxM9Vh0L.css,011uHgmxBfL.css,01n8CeLW9QL.css,21jUQU6VhYL.css,31TJtSmBkXL.css,21PjfsP9YvL.css,114HJAY+ShL.css,21U6+8tKunL.css,21VgVEzltcL.css,21ZjVyQPjML.css,21ohnckzsnL.css,01iXxkJ+wuL.css,31YeUjpBngL.css,018CevqcjhL.css,017KStdmPkL.css,114FIgEwAuL.css,01TrKJuj6JL.css,2170Ev7c3lL.css,01P0iSwDaIL.css,01eviB7YqCL.css,41xvDKH0l6L.css,01goIIPoVxL.css_.css?AUIClients/MediaDetailPageMetaAsset_TURBO_DESKTOP&CMcbSu5Z#desktop.ca.113788-C.336056-T1.343686-C.261576-T1.310456-T1.237182-T1.346364-T1.309439-T1.94145-T1.109378-T1.169593-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/01xYoNpncfL.js?AUIClients/MorpheusPopularityRankSidesheetAssets&O9eWV6N/#310975-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/61ujJ6QAjKL.js?AUIClients/DetailPageAllOffersDisplayAssets&Cnrj+10S#language-en.341404-T1.355883-T1.310975-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/31Le0m%2BQe-L.css?AUIClients/DetailPageAllOffersDisplayAssets&O9eWV6N/#310975-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/91x4PkvZ3CL.js?AUIClients/GestaltDetailPageDesktopMetaAsset');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/611uA7Z80VL.js?AUIClients/DetailPageSnSAssets&DfKKznkU#109378-T1');
    A.preload('https://images-na.ssl-images-amazon.com/images/I/21VgVEzltcL.css?AUIClients/DetailPageSnSAssets&DfKKznkU#109378-T1');
  }
});
</script>
















<script type="text/javascript">

function prefetchTYPAssets() {
    var imageAssets = new Array();
    var jsCssAssets = new Array();
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/x-locale/common/buy-buttons/review-1-click-order._CB485945728_.gif");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/x-locale/common/buttons/continue-shopping._CB485933269_.gif");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/x-locale/common/buy-buttons/thank-you-elbow._CB485935920_.gif");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/x-locale/communities/social/snwicons_v2._CB478838660_.png");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/checkout/assets/carrot._CB485936890_.gif");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/checkout/thank-you-page/assets/yellow-rounded-corner-sprite._CB485934158_.gif");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/checkout/thank-you-page/assets/white-rounded-corner-sprite._CB485935365_.gif");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936603_.png");
      imageAssets.push("https://images-na.ssl-images-amazon.com/images/G/15/x-locale/common/transparent-pixel._CB485935025_.gif");

    // pre-fetching image assets
    for (var i=0; i<imageAssets.length; i++) {
       new Image().src = imageAssets[i];
    }
    // pre-fetching css and js assets based on different browser types
    var isIE = /*@cc_on!@*/0;
    var isFireFox = /Firefox/.test(navigator.userAgent);
    if (isIE) {
      for (var i=0; i<jsCssAssets.length; i++) {
        new Image().src = jsCssAssets[i];
      }
    }
    else if (isFireFox) {
      for (var i=0; i<jsCssAssets.length; i++) {
        var o =  document.createElement("object");
        o.data = jsCssAssets[i];
        o.width = o.height = 0;
        document.body.appendChild(o);
      }
    }
}

    var onload = function () {
        setTimeout(prefetchTYPAssets, 2000);
    };
    if (window.addEventListener) {
        window.addEventListener("load", onload);
    } else if (window.attachEvent) { /* for <= IE 8 */
        window.attachEvent("onload", onload);
    }
</script>

<input type="hidden" name="1click-tsdelta" id="1click-tsdelta">
<script type="text/javascript">
var ocInitTimestamp = 1622846849;
</script>







            







<!--&&&Portal&Delimiter&&&--><!-- sp:end-feature:host-atf -->
<!-- sp:feature:nav-btf -->
<!-- NAVYAAN BTF START -->









<style type="text/css">



#csr-hcb-wrapper {
  display: none;
}

.bia-item .bia-action-button {
  display: inline-block;
  height: 22px;
  margin-top: 3px;
  padding: 0px;
  overflow: hidden;
  text-align: center;
  vertical-align: middle;
  text-decoration: none;
  color: #111;
  font-family: Arial,sans-serif;
  font-size: 11px;
  font-style: normal;
  font-weight: normal;
  line-height: 19px;
  cursor: pointer;
  outline: 0;
  border: 1px solid;
  -webkit-border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  border-radius: 3px 3px 3px 3px;
  border-radius: 0\9;
  border-color: #bcc1c8 #bababa #adb2bb;
  background: #eff0f3;
  background: -moz-linear-gradient(top, #f7f8fa, #e7e9ec);
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #f7f8fa), color-stop(100%, #e7e9ec));
  background: -webkit-linear-gradient(top, #f7f8fa, #e7e9ec);
  background: -o-linear-gradient(top, #f7f8fa, #e7e9ec);
  background: -ms-linear-gradient(top, #f7f8fa, #e7e9ec);
  background: linear-gradient(top, #f7f8fa, #e7e9ec);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#f7f8fa', endColorstr='#e7e9ec',GradientType=0);
  *zoom: 1;
  -webkit-box-shadow: inset 0 1px 0 0 #fff;
  -moz-box-shadow: inset 0 1px 0 0 #fff;
  box-shadow: inset 0 1px 0 0 #fff;
  box-sizing: border-box;
}

#bia-hcb-widget .a-button-text {
    font-family: Arial,sans-serif !important;
}

#bia_content .a-icon-row {
    display: none;
}

#bia-hcb-widget .a-icon-row {
      display: none;
}

#bia_content {
    width: 266px;
}

.nav-flyout-sidePanel {
    width: 266px !important;
}
.aui-atc-button {
    margin-top: 3px;
    overflow: hidden;
    color: #111;
    font-family: Arial,sans-serif;
    font-size: 11px;
    font-style: normal;
    font-weight: normal;
}
.bia-item .bia-action-button:hover {
  border-color: #aeb4bd #adadad #9fa5af;
  background: #e0e3e8;
  background: -moz-linear-gradient(top, #e7eaf0, #d9dce1);
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #e7eaf0), color-stop(100%, #d9dce1));
  background: -webkit-linear-gradient(top, #e7eaf0, #d9dce1);
  background: -o-linear-gradient(top, #e7eaf0, #d9dce1);
  background: -ms-linear-gradient(top, #e7eaf0, #d9dce1);
  background: linear-gradient(top, #e7eaf0, #d9dce1);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#e7eaf0', endColorstr='#d9dce1',GradientType=0);
  *zoom: 1;
  -webkit-box-shadow: 0 1px 3px rgba(255, 255, 255, 0.6) inset;
  -moz-box-shadow: 0 1px 3px rgba(255, 255, 255, 0.6) inset;
  box-shadow: 0 1px 3px rgba(255, 255, 255, 0.6) inset;
}

.bia-item .bia-action-button:active {
  background-color: #dcdfe3;
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) inset;
  -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) inset;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) inset;
}

.bia-item .bia-action-button-disabled {
  background: #f7f8fa;
  color: #b7b7b7;
  border-color: #e0e0e0;
  box-shadow: none;
  cursor: default;
}

.bia-item .bia-action-button-disabled:hover {
  background: #f7f8fa;
  color: #b7b7b7;
  border-color: #e0e0e0;
  box-shadow: none;
  cursor: default;
}

.bia-action-button-inner {
  border-bottom-color: #111111;
  border-bottom-style: none;
  border-bottom-width: 0px;
  border-image-outset: 0px;
  border-image-repeat: stretch;
  border-image-slice: 100%;
  border-image-width: 1;
  border-left-color: #111111;
  border-left-style: none;
  border-left-width: 0px;
  border-right-color: #111111;
  border-right-style: none;
  border-right-width: 0px;
  border-top-color: #111111;
  border-top-style: none;
  border-top-width: 0px;
  box-sizing: border-box;
  display: block;
  height: 20px;
  line-height: 19px;
  overflow: hidden;
  position: relative;
  padding: 0;
  vertical-align: baseline;
}

.bia-action-inner {
  border: 0;
  display: inline;
  font-size: 11px;
  height: auto;
  line-height: 19px;
  padding: 0px 4px 0px 4px;
  text-align: center;
  width: auto;
  white-space: nowrap;
}

.csr-content {
  font-family: Arial, Verdana, Helvetica, sans-serif;
  width: 220px;
  line-height: 19px;
}

.bia-header {
  font-size: 16px;
  color: #E47911;
  padding-bottom: 10px;
}

.bia-header-widget {
  white-space: nowrap;
  overflow: hidden;
}

.b2b-nav-header {
  white-space: nowrap;
  overflow: hidden;
  margin-bottom: 18px;
}

.bia-space-right {
  padding-right: 18px;
  white-space: normal;
  float: left;
}

.b2b-see-more-link a {
  display: inline;
  float: left;
  margin-top: 3px;
  margin-left: 3px;
}

.hcb-see-more-link a {
  color: #333;
  font-size: 13px;
  text-decoration: none;
  font-family: Arial, Verdana, Helvetica, sans-serif;
}

.bia-hcb-body {
  overflow: hidden;
}

.bia-item {
  width: 220px;
  display: inline-block;
  margin-bottom: 20px;
}

.bia-item-image {
  float: left;
  margin-right: 15px;
  width: 75px;
  height: 75px;
}

.bia-image {
  max-height: 75px;
  max-width: 75px;
  border: 0;
}

.bia-item-data {
  float: left;
  width: 130px;
}

.bia-title {
  line-height: 19px;
  font-size: 13px;
  max-height: 60px;
  overflow: hidden;
}

.bia-link:link {
  text-decoration: none;
  font-family: Arial, Verdana, Helvetica, sans-serif;
}

.bia-link:visited {
  text-decoration: none;
  color: #004B91;
}

.bia-price-nav {
  margin-top: -4px;
  color: #800;
  font-size: 12px;
  vertical-align: bottom;
}

.bia-price-yorr {
    margin-top: -8px;
    color: #800;
    font-size: 12px;
    vertical-align: bottom;
}

.bia-price {
  color: #800;
  font-size: 12px;
  vertical-align: bottom;
}

.bia-vpc-t1{
  color: #008a00;
  font-size: 12px;
  font-weight: bold;
}

.bia-vpc-t2{
  color: #008a00;
  font-size: 12px;
}

.bia-vpc-t3{
  font-size: 12px;
  line-height: 20px;
}

.bia-vpc-t3-badge{
  color: #ffffff;
  background-color: #e47911;
  font-weight: normal;

}

.bia-vpc-t3-badge::before{
  border-bottom: 10px solid #e47911;
}

.bia-vpc-t3-badge:after{
  border-top: 10px solid #e47911;
}

.bia-ppu {
  color: #800;
  font-size: 10px;
}

.bia-prime-badge {
  border: 0;
  vertical-align: middle;
}

.bia-cart-action {
  display: none;
}

.bia-cart-msg {
  display: block;
  font-family: Arial, Verdana, Helvetica, sans-serif;
  line-height: 19px;
}

.bia-cart-icon {
  background-image:
      url("https://images-na.ssl-images-amazon.com/images/G/15/Recommendations/MissionExperience/BIA/bia-atc-confirm-icon.jpg");
  display: inline-block;
  width: 14px;
  height: 13px;
  top: 3px;
  line-height: 19px;
  position: relative;
  vertical-align: top;
}

.bia-cart-success {
  color: #090!important;
  display: inline-block;
  margin: 0;
  font-size: 13px;
  font-style: normal;
  font-weight: bold;
  font-family: Arial, Verdana, Helvetica, sans-serif;
}

.bia-cart-title {
  margin-bottom: 3px;
}

.bia-cart-form {
  margin: 0px;
}

.bia-inline-cart-form {
  margin: 0px;
}

.bia-cart-submit {
  cursor: inherit;
  left: 0;
  top: 0;
  line-height: 19px;
  height: 100%;
  width: 100%;
  padding: 1px 6px 1px 6px;
  position: absolute;
  opacity: 0.01;
  overflow: visible;
  filter: alpha(opacity=1);
  z-index: 20;
}

.bia-link-caret {
  color: #e47911;
}

</style>




<script type="text/javascript">
(function ($Nav) {
"use strict";

if (typeof $Nav === 'undefined' || $Nav === null || typeof $Nav.when !== 'function') {
    return;
}
$Nav.when('$', 'data', 'flyout.yourAccount', 'sidepanel.csYourAccount',
          'config')
    .run("BuyitAgain-YourAccount-SidePanel",
    function ($, data, yaFlyout, csYourAccount, config) {
        if (config.disableBuyItAgain) {
          return;
        }
        var render = function (data) {
            if (data.status) {
                var widgetHtml = data.widgetBegin +
                                 data.faceouts.join('') +
                                 data.widgetEnd;
                navbar.sidePanel({
                    flyoutName: 'yourAccount',
                    data: {html: widgetHtml}
                });
            }
        };

        var renderBuyItAgain = function (biaData) {
            if (csYourAccount) {
                csYourAccount.register(render, biaData);
            } else {
                render(biaData);
            }
        };

        yaFlyout.sidePanel.onData(function() {
            enableInlineAddToCart($);
            enableImpressionLogging($);

            P.when('A','p13n-sc-static-list').execute(function(A, StaticList) {
                var navContainer = A.$("#bia-hcb-widget");
                var navList = navContainer.find('.p13n-sc-static-list');
                A.$(navList).bind('truncateList', function() {
                    var staticList = new StaticList(navList);
                });

                A.$(navList).trigger('truncateList');
            });

            if (window.P) {
                P.when('A', 'a-truncate').execute(function(A, truncate) {
                    var truncateElements = A.$('.a-truncate');
                    A.each(truncateElements, function(element) {
                        truncate.get(element).update();
                    });
                });
            }

        });

    yaFlyout.onRender(function() {
            $.ajax({
                url: '/gp/bia/external/bia-hcb-ajax-handler.html',
                data: 
   {"biaHcbRid":"1KMDY2JPGP2X3R80G8WC"},
                dataType: 'json',
                timeout: 4*1000,
                success: renderBuyItAgain,
                error: function (jqXHR, textStatus, errorThrown) {
                }
            });
        });


    var updateNavCartQty = function(qty) {
        if (typeof window.navbar === 'object' && typeof window.navbar.setCartCount === 'function') {
            window.navbar.setCartCount(qty);
        }
    };

    var addToCart = function(params, callback) {
        $.ajax({
           url: '/gp/bia/external/bia-cart-ajax-handler.html',
           data: params,
           dataType: 'json', 
           timeout: 2000,
           success: function(response) { callback(response); },
           error: function() { callback({ok:0}); }
        });
    };

    var enableInlineAddToCart = function ($) {
        if ($(".bia-inline-cart-form").length === 0) {
            return;
        }

        var inlineAddToCartHandler = function(e) {
            e.preventDefault();

            var $target = $(e.target);
            var $item = $target.parents(".bia-item");
            var $submit = $item.find(".bia-cart-submit");
            var params = $target.attr('data-order');

            $submit.attr("disabled", true);
            $item.find(".bia-action-button").addClass("bia-action-button-disabled");

            addToCart(params, 
                function(response) {
                    if(response && response.ok && response.ok === '1') {
                        $item.find(".bia-faceout").hide();
                        $item.find(".bia-cart-action").show();
                        updateNavCartQty(response.numActiveItemsInCart); 
                        //TODO: add metric
                    } else {
                        $target.unbind("submit", inlineAddToCartHandler);
                        $submit.attr("disabled", false);
                        $submit.click();
                        //TODO: add metric
                    }
                }
            );
        };

        $(".bia-inline-cart-form").bind("submit", inlineAddToCartHandler);
    };

    var enableImpressionLogging = function ($) {

        var registerToLog = function (p13nLogger, callOnVisible) {
            var featureEl = $("#bia-hcb-widget");
            callOnVisible.register(featureEl, function () {
                p13nLogger.logAction({
                                action: 'view', 
                                featureElement: featureEl, 
                                replicateAsinImpressions: true
                              });
            });
        };
        
        AmazonUIPageJS.when('p13n-sc-logger', 'p13n-sc-call-on-visible')
            .execute(function(p13nLogger, callOnVisible) {
                    registerToLog(p13nLogger, callOnVisible);});
    };

    });

})(window.$Nav);
//# sourceURL=bia-hcb-js.mi
</script>


<script type="text/javascript">
  window.$Nav && $Nav.when("data").run(function(data){
    data({
      "accountListContent":{"html":"<div id='nav-al-container'><div id='nav-al-signin'><div id='nav-flyout-ya-signin' class='nav-flyout-content nav-flyout-accessibility'><a href='https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2FRage-Against-Machine%2Fdp%2FB0000028RR%2F%3F_encoding%3DUTF8%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' rel='nofollow' class='nav-action-button' data-nav-role='signin' data-nav-ref='nav_signin'><span class='nav-action-inner'>Sign in</span></a><div id='nav-flyout-ya-newCust' class='nav_pop_new_cust nav-flyout-content nav-flyout-accessibility'>New customer? <a href='https://www.amazon.ca/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2FRage-Against-Machine%2Fdp%2FB0000028RR%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' rel='nofollow' class='nav-a'>Start here.</a></div></div></div><div id='nav-al-wishlist' class='nav-al-column nav-tpl-itemList nav-flyout-content nav-flyout-accessibility'><div class='nav-title' id='nav-al-title'>Your Lists</div><a href='/gp/registry/wishlist?triggerElementID=createList&ref_=nav_ListFlyout_gno_createwl' class='nav-link nav-item'><span class='nav-text'>Create a Wish List</span></a> <a href='/gp/registry/search.html?type=wishlist&ref_=nav_ListFlyout_gno_listpop_find' class='nav-link nav-item'><span class='nav-text'>Find a Wish List</span></a> <a href='/wishlist/universal?ref_=nav_ListFlyout_gno_listpop_uwl' class='nav-link nav-item'><span class='nav-text'>Wish from Any Website</span></a> <a href='/gcx/-/gfhz/?_encoding=UTF8&ref_=nav_wishlist_gf' class='nav-link nav-item'><span class='nav-text'>Find a Gift</span></a> <a href='/baby-reg/homepage?ref_=nav_ListFlyout_gno_listpop_br' class='nav-link nav-item'><span class='nav-text'>Baby Registry</span></a> <a href='/wedding/home?ref_=nav_ListFlyout_wr' class='nav-link nav-item'><span class='nav-text'>Wedding Registry</span></a> <a href='/discover' class='nav-link nav-item'><span class='nav-text'>Discover Your Style</span></a> <a href='/showroom?ref_=nav_ListFlyout_srm_your_desk_wl_ca' class='nav-link nav-item'><span class='nav-text'>Explore Showroom</span></a></div><div id='nav-al-your-account' class='nav-al-column nav-template nav-flyout-content nav-tpl-itemList nav-flyout-accessibility'><div class='nav-title'>Your Account</div><a href='/gp/css/homepage.html?ref_=nav_AccountFlyout_ya' class='nav-link nav-item'><span class='nav-text'>Your Account</span></a> <a id='nav_prefetch_yourorders' href='/gp/css/order-history?ref_=nav_AccountFlyout_orders' class='nav-link nav-item'><span class='nav-text'>Your Orders</span></a> <a href='/gp/yourstore?ref_=nav_AccountFlyout_recs' class='nav-link nav-item'><span class='nav-text'>Your Recommendations</span></a> <a href='/auto-deliveries?ref_=nav_AccountFlyout_sns' class='nav-link nav-item'><span class='nav-text'>Your Subscribe & Save Items</span></a> <a href='/gp/primecentral?ref_=nav_AccountFlyout_prime' class='nav-link nav-item'><span class='nav-text'>Your Prime Membership</span></a> <a href='/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions' class='nav-link nav-item'><span class='nav-text'>Memberships & Subscriptions</span></a> <a href='/dp/B07MJM4F44?plattr=CACBCCNAVACC&ref_=nav_cbcc_ca_account' class='nav-link nav-item'><span class='nav-text'>Your Amazon Credit Card</span></a> <a href='/business/register/org/landing?ref_=nav_AccountFlyout_b2b_reg' class='nav-link nav-item'><span class='nav-text'>Register for a Business Account</span></a> <a href='/hz/mycd/myx?ref_=nav_AccountFlyout_myk' class='nav-link nav-item'><span class='nav-text'>Manage Your Content and Devices</span></a> <a href='https://music.amazon.ca?ref=nav_youraccount_cldplyr' class='nav-link nav-item'><span class='nav-text'>Your Music Library</span></a> <a href='/gp/video/ssoredirect?pvp=/ref%3Dnav_youraccount_apv&ref_=nav_AccountFlyout__apv' class='nav-link nav-item'><span class='nav-text'>Your Prime Video</span></a> <a href='/clouddrive?ref_=nav_AccountFlyout_clddrv' class='nav-link nav-item'><span class='nav-text'>Your Amazon Drive</span></a> <a href='/gp/mas/your-account/myapps?ref_=nav_AccountFlyout_aad' class='nav-link nav-item'><span class='nav-text'>Your Apps & Devices</span></a></div></div>"},
      "signinContent":{"html":"<div id='nav-signin-tooltip'><a href='https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2FRage-Against-Machine%2Fdp%2FB0000028RR%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-action-button' data-nav-role='signin' data-nav-ref='nav_custrec_signin'><span class='nav-action-inner'>Sign in</span></a><div class='nav-signin-tooltip-footer'>New customer? <a href='https://www.amazon.ca/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2FRage-Against-Machine%2Fdp%2FB0000028RR%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-a'>Start here.</a></div></div>"},
      "templates":{"itemList":"<# var hasColumns = (function () {  var checkColumns = function (_items) {    if (!_items) {      return false;    }    for (var i=0; i<_items.length; i++) {      if (_items[i].columnBreak || (_items[i].items && checkColumns(_items[i].items))) {        return true;      }    }    return false;  };  return checkColumns(items);}()); #><# if(hasColumns) { #>  <# if(items[0].image && items[0].image.src) { #>    <div class='nav-column nav-column-first nav-column-image'>  <# } else if (items[0].greeting) { #>    <div class='nav-column nav-column-first nav-column-greeting'>  <# } else { #>    <div class='nav-column nav-column-first'>  <# } #><# } #><# var renderItems = function(items) { #>  <# jQuery.each(items, function (i, item) { #>    <# if(hasColumns && item.columnBreak) { #>      <# if(item.image && item.image.src) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-image'>      <# } else if (item.greeting) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-greeting'>      <# } else { #>        </div><div class='nav-column nav-column-notfirst nav-column-break'>      <# } #>    <# } #>    <# if(item.dividerBefore) { #>      <div class='nav-divider'></div>    <# } #>    <# if(item.text || item.content) { #>      <# if(item.url) { #>        <a href='<#=item.url #>' class='nav-link      <# } else {#>        <span class='      <# } #>      <# if(item.panelKey) { #>        nav-hasPanel      <# } #>      <# if(item.items) { #>        nav-title      <# } #>      <# if(item.decorate == 'carat') { #>        nav-carat      <# } #>      <# if(item.decorate == 'nav-action-button') { #>        nav-action-button      <# } #>      nav-item'      <# if(item.extra) { #>        <#=item.extra #>      <# } #>      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      <# if(item.dataNavRole) { #>        data-nav-role='<#=item.dataNavRole #>'      <# } #>      <# if(item.dataNavRef) { #>        data-nav-ref='<#=item.dataNavRef #>'      <# } #>      <# if(item.panelKey) { #>        data-nav-panelkey='<#=item.panelKey #>'        role='navigation'        aria-label='<#=item.text#>'      <# } #>      <# if(item.subtextKey) { #>        data-nav-subtextkey='<#=item.subtextKey #>'      <# } #>      <# if(item.image && item.image.height > 16) { #>        style='line-height:<#=item.image.height #>px;'      <# } #>      >      <# if(item.decorate == 'carat') { #>        <i class='nav-icon'></i>      <# } #>      <# if(item.image && item.image.src) { #>        <img class='nav-image' src='<#=item.image.src #>' style='height:<#=item.image.height #>px; width:<#=item.image.width #>px;' />      <# } #>      <# if(item.text) { #>        <span class='nav-text<# if(item.classname) { #> <#=item.classname #><# } #>'><#=item.text#><# if(item.badgeText) { #>          <span class='nav-badge'><#=item.badgeText#></span>        <# } #></span>      <# } else if (item.content) { #>        <span class='nav-content'><# jQuery.each(item.content, function (j, cItem) { #><# if(cItem.url && cItem.text) { #><a href='<#=cItem.url #>' class='nav-a'><#=cItem.text #></a><# } else if (cItem.text) { #><#=cItem.text#><# } #><# }); #></span>      <# } #>      <# if(item.subtext) { #>        <span class='nav-subtext'><#=item.subtext #></span>      <# } #>      <# if(item.url) { #>        </a>      <# } else {#>        </span>      <# } #>    <# } #>    <# if(item.image && item.image.src) { #>      <# if(item.url) { #>        <a href='<#=item.url #>'>       <# } #>      <img class='nav-image'      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      src='<#=item.image.src #>' <# if (item.alt) { #> alt='<#= item.alt #>'<# } #>/>      <# if(item.url) { #>        </a>       <# } #>    <# } #>    <# if(item.items) { #>      <div class='nav-panel'> <# renderItems(item.items); #> </div>    <# } #>  <# }); #><# }; #><# renderItems(items); #><# if(hasColumns) { #>  </div><# } #>","subnav":"<# if (obj && obj.type === 'vertical') { #>  <# jQuery.each(obj.rows, function (i, row) { #>    <# if (row.flyoutElement === 'button') { #>      <div class='nav_sv_fo_v_button'        <# if (row.elementStyle) { #>          style='<#= row.elementStyle #>'        <# } #>      >        <a href='<#=row.url #>' class='nav-action-button nav-sprite'>          <#=row.text #>        </a>      </div>    <# } else if (row.flyoutElement === 'list' && row.list) { #>      <# jQuery.each(row.list, function (j, list) { #>        <div class='nav_sv_fo_v_column <#=(j === 0) ? 'nav_sv_fo_v_first' : '' #>'>          <ul class='<#=list.elementClass #>'>          <# jQuery.each(list.linkList, function (k, link) { #>            <# if (k === 0) { link.elementClass += ' nav_sv_fo_v_first'; } #>            <li class='<#=link.elementClass #>'>              <# if (link.url) { #>                <a href='<#=link.url #>' class='nav_a'><#=link.text #></a>              <# } else { #>                <span class='nav_sv_fo_v_span'><#=link.text #></span>              <# } #>            </li>          <# }); #>          </ul>        </div>      <# }); #>    <# } else if (row.flyoutElement === 'link') { #>      <# if (row.topSpacer) { #>        <div class='nav_sv_fo_v_clear'></div>      <# } #>      <div class='<#=row.elementClass #>'>        <a href='<#=row.url #>' class='nav_sv_fo_v_lmargin nav_a'>          <#=row.text #>        </a>      </div>    <# } #>  <# }); #><# } else if (obj) { #>  <div class='nav_sv_fo_scheduled'>    <#= obj #>  </div><# } #>","htmlList":"<# jQuery.each(items, function (i, item) { #>  <div class='nav-item'>    <#=item #>  </div><# }); #>"}
    })
  })
</script>

<script type="text/javascript">
  window.$Nav && $Nav.declare('config.flyoutURL', null);
  window.$Nav && $Nav.declare('btf.lite');
  window.$Nav && $Nav.declare('btf.full');
  window.$Nav && $Nav.declare('btf.exists');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).register('navCF');
</script>


    
    
    















<form style="display: none;">
  <input type="hidden" id="rwol-display-called" value="0">
</form>

    <script type="a-state" data-a-state="{&quot;key&quot;:&quot;rw-dynamic-modal-bootstrap&quot;}">{"origSessionId":"138-4669640-7712440","subPageType":null,"pageType":"Detail","ASIN":"B0000028RR","path":"/Rage-Against-Machine/dp/B0000028RR","isAUI":"1"}</script>
      

      
<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function(){
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/11VbV%2B%2BKhQL.js?AUIClients/RetailWebsiteOverlayAUIAssets');
});
</script>




<!-- NAVYAAN BTF END -->
<!-- sp:feature:host-btf -->


  </div>

  </div>

<!-- htmlEndMarker -->













<!-- sp:end-feature:host-btf -->
<!-- sp:feature:aui-preload -->
<!-- sp:feature:nav-footer -->

  <!-- NAVYAAN FOOTER START -->
  <!-- WITH MOZART -->


        






















<div id="rhf" class="copilot-secure-display" style="clear:both" role="complementary" aria-label="Your recently viewed items and featured recommendations">

    <div class="rhf-frame" style="display:none">
        <br />
        <div id="rhf-container">






    <div class='rhf-loading-outer'>
        <table class='rhf-loading-middle'>
            <tr>
                <td class='rhf-loading-inner'>
                    <img src="https://images-na.ssl-images-amazon.com/images/G/15/personalization/ybh/loading-4x-gray._CB485916907_.gif" />
                </td>
            </tr>
        </table>
    </div>








<div id="rhf-context">
    <script type='application/json'>
        {"rhfHandlerParams":{"disableRhfWeblab":"","search":"","rhfAsins":"","noP13NCache":"","weblabTriggers":"","auiDebug":"","keywords":"","k":"","rviAsins":"","url":"","parentSession":"138-4669640-7712440","rhfState":"","contextMetadataOverride":"","currentSubPageType":null,"field-keywords":"","relatedRequestId":"1KMDY2JPGP2X3R80G8WC","recsAsins":"","rhfHorizonteWeblab":"","excludeASIN":"QjAwMDAwMjhSUg==","auditEnabled":"","customerId":"","testRecsFailure":"","previewCampaigns":"","forceWidgets":"","currentPageType":"Detail","stringDebug":""},"subPageType":null,"requestId":"1KMDY2JPGP2X3R80G8WC","sessionId":"138-4669640-7712440","customerId":"","pageType":"Detail","ybhHandlerParams":{"relatedRequestId":"1KMDY2JPGP2X3R80G8WC","currentPageType":"Detail","parentSession":"138-4669640-7712440"}}
    </script>
</div>

</div><noscript>

<div class="rhf-border">

        <div class="rhf-header">
        Your recently viewed items and featured recommendations
    </div>

<div class="rhf-footer">
    <div class="rvi-container">

<div class="ybh-edit">
    <div class="ybh-edit-arrow"> &#8250; </div>
    <div class="ybh-edit-link"><a href="/gp/yourstore/pym/ref=pd_pyml_rhf">View or edit your browsing history</a></div>
</div>
        <span class="no-rvi-message">After viewing product detail pages, look here to find an easy way to navigate back to pages that interest you.</span>
    </div>
</div>
</div>
</noscript><div id="rhf-error" style="display:none;">

<div class="rhf-border">

        <div class="rhf-header">
        Your recently viewed items and featured recommendations
    </div>

<div class="rhf-footer">
    <div class="rvi-container">

<div class="ybh-edit">
    <div class="ybh-edit-arrow"> &#8250; </div>
    <div class="ybh-edit-link"><a href="/gp/yourstore/pym/ref=pd_pyml_rhf">View or edit your browsing history</a></div>
</div>
        <span class="no-rvi-message">After viewing product detail pages, look here to find an easy way to navigate back to pages that interest you.</span>
    </div>
</div>
</div>
</div>
        <br />
    </div>
</div>

<div class="navLeftFooter nav-sprite-v1" id="navFooter">
  
<a href="#nav-top" id="navBackToTop" aria-label="Back to top">
  <div class="navFooterBackToTop">
  <span class="navFooterBackToTopText">
    Back to top
  </span>
  </div>
</a>

  
<div class="navFooterVerticalColumn navAccessibility" role="presentation">
  <div class="navFooterVerticalRow navAccessibility" style="display: table-row;">
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Get to Know Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://www.amazon.jobs" class="nav_a">Careers</a>
            </li>
            <li >
              <a href="/gp/help/customer/display.html?nodeId=200700220&ref_=footer_corpres" class="nav_a">Amazon and Our Planet</a>
            </li>
            <li >
              <a href="https://www.amazon.ca/ir" class="nav_a">Investor Relations</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazon.ca/pr" class="nav_a">Press Releases</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Make Money with Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://sell.amazon.ca/?ld=AZFSSOA-CA-footer&ref_=footer_soa" class="nav_a">Sell on Amazon</a>
            </li>
            <li >
              <a href="https://associates.amazon.ca" class="nav_a">Amazon Associates</a>
            </li>
            <li >
              <a href="/b/?node=16927192011&ld=AZCAHND-footer&ref_=footer_sell" class="nav_a">Sell on Amazon Handmade</a>
            </li>
            <li >
              <a href="https://advertising.amazon.ca/?ref=footer_advtsing_amzn_ca" class="nav_a">Advertise Your Products</a>
            </li>
            <li >
              <a href="https://kdp.amazon.com?language=en_US" class="nav_a">Independently Publish with Us</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazon.ca/b?ie=UTF8&node=15576834011" class="nav_a">Host an Amazon Hub</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Amazon Payment Products</div>
        <ul>
            <li class="nav_first">
              <a href="/dp/B07MJM4F44?plattr=CACBCCFOOT&ref_=nav_cbcc_ca_footer" class="nav_a">Amazon.ca Rewards Mastercard</a>
            </li>
            <li >
              <a href="/gp/browse.html?node=21371066011&ref_=footer_swp" class="nav_a">Shop with Points</a>
            </li>
            <li >
              <a href="/gp/gc/create?ref_=footer_reload_ca" class="nav_a">Reload Your Balance</a>
            </li>
            <li >
              <a href="/gp/browse.html?node=8438004011&ref_=footer_tfx_ca_en" class="nav_a">Amazon Currency Converter</a>
            </li>
            <li >
              <a href="/gp/browse.html?node=9230166011&ref_=footer_gift_cards_ca_en" class="nav_a">Gift Cards</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/browse.html?node=17321486011&ref_=footer_cash_ca_en" class="nav_a">Amazon Cash</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Let Us Help You</div>
        <ul>
            <li class="nav_first">
              <a href="/gp/help/customer/display.html?nodeId=GDFU3JS5AL6SYHRD&ref_=footer_covid" class="nav_a">COVID-19 and Amazon</a>
            </li>
            <li >
              <a href="/gp/help/customer/display.html?nodeId=915470&ref_=footer_shiprates" class="nav_a">Shipping Rates & Policies</a>
            </li>
            <li >
              <a href="/gp/prime?ref_=footer_prime" class="nav_a">Amazon Prime</a>
            </li>
            <li >
              <a href="/gp/css/returns/homepage.html?ref_=footer_hy_f_4" class="nav_a">Returns Are Easy</a>
            </li>
            <li >
              <a href="/hz/mycd/myx?ref_=footer_myk" class="nav_a">Manage your Content and Devices</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/help/customer/display.html?nodeId=508510&ref_=footer_gw_m_b_he" class="nav_a">Customer Service</a>
            </li>
        </ul>
      </div>
  </div>
</div>
<div class="nav-footer-line"></div>

  <div class="navFooterLine navFooterLinkLine navFooterPadItemLine">
    <span>
      <div class="navFooterLine navFooterLogoLine">
        <a  href="/?ref_=footer_logo">
        <div class="nav-logo-base nav-sprite"></div>
        </a>
      </div>
</span><span class="icp-container-desktop"><div class ="navFooterLine">
<style type="text/css">
  #icp-touch-link-language { display: none; }
</style>


<a href="/gp/customer-preferences/select-language/ref=footer_lang?ie=UTF8&preferencesReturnUrl=%2F" class="icp-button" id="icp-touch-link-language">
  <div class="icp-nav-globe-img-2 icp-button-globe-2"></div><span class="icp-color-base">English</span><span class="nav-arrow icp-up-down-arrow"></span><span class="aok-hidden" style="display:none">Choose a language for shopping.</span>
</a>



<style type="text/css">
#icp-touch-link-country { display: none; }
</style>
<a href="/gp/navigation-country/select-country/ref=footer_icp_cp?ie=UTF8&preferencesReturnUrl=%2F" class="icp-button" id="icp-touch-link-country">
  <span class="icp-flag-3 icp-flag-3-ca"></span><span class="icp-color-base">Canada</span><span class="aok-hidden" style="display:none">Choose a country/region for shopping.</span>
</a>
</div></span>
  </div>
  
  
  <div class="navFooterLine navFooterLinkLine navFooterDescLine"  >
    <table class="navFooterMoreOnAmazon" cellspacing="0">
      <tr>
<td class="navFooterDescItem"><a href=https://music.amazon.ca?ref=dm_aff_amz_ca class="nav_a">Amazon Music<br><span class="navFooterDescText">Stream millions<br>of songs</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://advertising.amazon.ca/?ref=footer_advtsing_amzn_ca class="nav_a">Amazon Advertising<br><span class="navFooterDescText">Find, attract, and<br>engage customers</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/gp/browse.html?node=16055945011&ref_=_ca_footer_drive class="nav_a">Amazon Drive<br><span class="navFooterDescText">Cloud storage<br>from Amazon</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://aws.amazon.com/what-is-cloud-computing/?sc_channel=EL&sc_campaign=CA_amazonfooter class="nav_a">Amazon Web Services<br><span class="navFooterDescText">Scalable Cloud<br>Computing Services</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://www.bookdepository.com/ class="nav_a">Book Depository<br><span class="navFooterDescText">Books With Free<br>Delivery Worldwide</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href=https://www.goodreads.com/ class="nav_a">Goodreads<br><span class="navFooterDescText">Book reviews<br>& recommendations</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://www.imdb.com/ class="nav_a">IMDb<br><span class="navFooterDescText">Movies, TV<br>& Celebrities</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/gp/browse.html?node=16055944011&ref_=_gno_p_foot class="nav_a">Amazon Photos<br><span class="navFooterDescText">Unlimited Photo Storage<br>Free With Prime</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://www.shopbop.com/ca/welcome class="nav_a">Shopbop<br><span class="navFooterDescText">Designer<br>Fashion Brands</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/gp/browse.html?node=8929975011&ref_=footer_warehouse_deals class="nav_a">Warehouse Deals<br><span class="navFooterDescText">Open-Box<br>Discounts</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href=https://www.wholefoodsmarket.com class="nav_a">Whole Foods Market<br><span class="navFooterDescText">We Believe in<br>Real Food</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/gp/browse.html?node=17351028011&ref_=footer_carenew class="nav_a">Amazon Renewed<br><span class="navFooterDescText">Like-new products<br>you can trust</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://blinkforhome.com/?ref=nav_footer_ca class="nav_a">Blink<br><span class="navFooterDescText">Smart Security<br>for Every Home
</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/amazonsecondchance?ref_=footer_asc class="nav_a">Amazon Second Chance<br><span class="navFooterDescText">Pass it on, trade it in,<br>give it a second life</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem">&nbsp;</td>
</tr>

    </table>
  </div>

  
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine navFooterCopyright">
  <ul><li class="nav_first"><a href="/gp/help/customer/display.html?nodeId=918816&ref_=footer_cou" class="nav_a">Conditions of Use</a></li><li ><a href="/gp/help/customer/display.html?nodeId=918814&ref_=footer_privacy" class="nav_a">Privacy Notice</a></li><li class="nav_last"><a href="/gp/help/customer/display.html?nodeId=202146130&ref_=footer_iba" class="nav_a">Interest-Based Ads</a></li></ul><span>© 2008-2021, Amazon.com, Inc. or its affiliates</span>
</div>

  
</div>

<div id="sis_pixel_r2" aria-hidden="true" style="height:1px; position: absolute; left: -1000000px; top: -1000000px;"></div><script>(function(a,b){a.attachEvent?a.attachEvent("onload",b):a.addEventListener&&a.addEventListener("load",b,!1)})(window,function(){setTimeout(function(){var el=document.getElementById("sis_pixel_r2");el&&(el.innerHTML='<iframe id="DAsis" src="//s.amazon-adsystem.com/iu3?d=amazon.ca&slot=navFooter&a2=010113a684d639c7c808b053246d1b48eadd9add02325b325b7e7c6f1fa3199944b9&old_oo=0&ts=1622846847727&s=AXZJxpms2UO-ARJFjoolMmiRQr4m2eR2YeDg8o34yau_&cb=1622846847727" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>')},300)});</script>

  <!-- NAVYAAN FOOTER END -->
<!-- sp:feature:amazon-pay-iframe -->
<!-- sp:end-feature:amazon-pay-iframe -->
<div id='be' style="display:none;visibility:hidden;"><form name='ue_backdetect' action="get"><input type="hidden" name='ue_back' value='1' /></form>


<script type="text/javascript">
window.ue_ibe = (window.ue_ibe || 0) + 1;
if (window.ue_ibe === 1) {
(function(e,c){function h(b,a){f.push([b,a])}function g(b,a){if(b){var c=e.head||e.getElementsByTagName("head")[0]||e.documentElement,d=e.createElement("script");d.async="async";d.src=b;d.setAttribute("crossorigin","anonymous");a&&a.onerror&&(d.onerror=a.onerror);a&&a.onload&&(d.onload=a.onload);c.insertBefore(d,c.firstChild)}}function k(){ue.uels=g;for(var b=0;b<f.length;b++){var a=f[b];g(a[0],a[1])}ue.deffered=1}var f=[];c.ue&&(ue.uels=h,c.ue.attach&&c.ue.attach("load",k))})(document,window);


if (window.ue && window.ue.uels) {
        var cel_widgets = [ { "c":"celwidget" },{ "s":"#nav-swmslot > div", "id_gen":function(elem, index){ return 'nav_sitewide_msg'; } },{ "c":"feature" },{ "id":"detail-ilm_div" } ];

                ue.uels("https://images-na.ssl-images-amazon.com/images/I/31YXrY93hfL.js");
}
var ue_mbl=ue_csm.ue.exec(function(e,a){function m(g){b=g||{};a.AMZNPerformance=b;b.transition=b.transition||{};b.timing=b.timing||{};if(a.csa){var c;b.timing.transitionStart&&(c=b.timing.transitionStart);b.timing.processStart&&(c=b.timing.processStart);c&&(csa("PageTiming")("mark","nativeTransitionStart",c),csa("PageTiming")("mark","transitionStart",c))}e.ue.exec(n,"csm-android-check")()&&b.tags instanceof Array&&(g=-1!=b.tags.indexOf("usesAppStartTime")||b.transition.type?!b.transition.type&&-1<
b.tags.indexOf("usesAppStartTime")?"warm-start":void 0:"view-transition",g&&(b.transition.type=g));"reload"===f._nt&&e.ue_orct||"intrapage-transition"===f._nt?d&&d.timing&&d.timing.navigationStart?b.timing.transitionStart=d.timing.navigationStart:delete b.timing.transitionStart:"undefined"===typeof f._nt&&d&&d.timing&&d.timing.navigationStart&&a.history&&"function"===typeof a.History&&"object"===typeof a.history&&a.history.length&&1!=a.history.length&&(b.timing.transitionStart=d.timing.navigationStart);
g=b.transition;c=f._nt?f._nt:void 0;g.subType=c;a.ue&&a.ue.tag&&a.ue.tag("has-AMZNPerformance");f.isl&&a.uex&&a.uex("at","csm-timing");p()}function q(b){a.ue&&a.ue.count&&a.ue.count("csm-cordova-plugin-failed",1)}function n(){return a.cordova&&a.cordova.platformId&&"android"==a.cordova.platformId}function p(){try{a.P.register("AMZNPerformance",function(){return b})}catch(g){}}function k(){if(!b)return"";ue_mbl.cnt=null;for(var a=b.timing,c=b.transition,a=["mts",l(a.transitionStart),"mps",l(a.processStart),
"mtt",c.type,"mtst",c.subType,"mtlt",c.launchType],c="",d=0;d<a.length;d+=2){var f=a[d],e=a[d+1];"undefined"!==typeof e&&(c+="&"+f+"="+e)}return c}function l(a){if("undefined"!==typeof a&&"undefined"!==typeof h)return a-h}function r(a,c){b&&(h=c,b.timing.transitionStart=a,b.transition.type="view-transition",b.transition.subType="ajax-transition",b.transition.launchType="normal",ue_mbl.cnt=k)}var f=e.ue||{},h=e.ue_t0,d=a.performance,b;if(a.P&&a.P.when&&a.P.register)return 1===a.ue_fnt&&(h=a.aPageStart||
e.ue_t0),a.P.when("CSMPlugin").execute(function(a){a.buildAMZNPerformance&&a.buildAMZNPerformance({successCallback:m,failCallback:q})}),{cnt:k,ajax:r}},"mobile-timing")(ue_csm,ue_csm.window);

(function(d){d._uess=function(){var a="";screen&&screen.width&&screen.height&&(a+="&sw="+screen.width+"&sh="+screen.height);var b=function(a){var b=document.documentElement["client"+a];return"CSS1Compat"===document.compatMode&&b||document.body["client"+a]||b},c=b("Width"),b=b("Height");c&&b&&(a+="&vw="+c+"&vh="+b);return a}})(ue_csm);

(function(a){var b=document.ue_backdetect;b&&b.ue_back&&a.ue&&(a.ue.bfini=b.ue_back.value);a.uet&&a.uet("be");a.onLdEnd&&(window.addEventListener?window.addEventListener("load",a.onLdEnd,!1):window.attachEvent&&window.attachEvent("onload",a.onLdEnd));a.ueh&&a.ueh(0,window,"load",a.onLd,1);a.ue&&a.ue.tag&&(a.ue_furl?(b=a.ue_furl.replace(/\./g,"-"),a.ue.tag(b)):a.ue.tag("nofls"))})(ue_csm);

(function(g,h){function d(a,d){var b={};if(!e||!f)try{var c=h.sessionStorage;c?a&&("undefined"!==typeof d?c.setItem(a,d):b.val=c.getItem(a)):f=1}catch(g){e=1}e&&(b.e=1);return b}var b=g.ue||{},a="",f,e,c,a=d("csmtid");f?a="NA":a.e?a="ET":(a=a.val,a||(a=b.oid||"NI",d("csmtid",a)),c=d(b.oid),c.e||(c.val=c.val||0,d(b.oid,c.val+1)),b.ssw=d);b.tabid=a})(ue_csm,ue_csm.window);

ue_csm.ue.exec(function(e,f){var a=e.ue||{},b=a._wlo,d;if(a.ssw){d=a.ssw("CSM_previousURL").val;var c=f.location,b=b?b:c&&c.href?c.href.split("#")[0]:void 0;c=(b||"")===a.ssw("CSM_previousURL").val;!c&&b&&a.ssw("CSM_previousURL",b);d=c?"reload":d?"intrapage-transition":"first-view"}else d="unknown";a._nt=d},"NavTypeModule")(ue_csm,window);
ue_csm.ue.exec(function(c,a){function g(a){a.run(function(e){d.tag("csm-feature-"+a.name+":"+e);d.isl&&c.uex("at")})}if(a.addEventListener)for(var d=c.ue||{},f=[{name:"touch-enabled",run:function(b){var e=function(){a.removeEventListener("touchstart",c,!0);a.removeEventListener("mousemove",d,!0)},c=function(){b("true");e()},d=function(){b("false");e()};a.addEventListener("touchstart",c,!0);a.addEventListener("mousemove",d,!0)}}],b=0;b<f.length;b++)g(f[b])},"csm-features")(ue_csm,window);


(function(b,c){var a=c.images;a&&a.length&&b.ue.count("totalImages",a.length)})(ue_csm,document);
(function(b){function c(){var d=[];a.log&&a.log.isStub&&a.log.replay(function(a){e(d,a)});a.clog&&a.clog.isStub&&a.clog.replay(function(a){e(d,a)});d.length&&(a._flhs+=1,n(d),p(d))}function g(){a.log&&a.log.isStub&&(a.onflush&&a.onflush.replay&&a.onflush.replay(function(a){a[0]()}),a.onunload&&a.onunload.replay&&a.onunload.replay(function(a){a[0]()}),c())}function e(d,b){var c=b[1],f=b[0],e={};a._lpn[c]=(a._lpn[c]||0)+1;e[c]=f;d.push(e)}function n(b){q&&(a._lpn.csm=(a._lpn.csm||0)+1,b.push({csm:{k:"chk",
f:a._flhs,l:a._lpn,s:"inln"}}))}function p(a){if(h)a=k(a),b.navigator.sendBeacon(l,a);else{a=k(a);var c=new b[f];c.open("POST",l,!0);c.setRequestHeader&&c.setRequestHeader("Content-type","text/plain");c.send(a)}}function k(a){return JSON.stringify({rid:b.ue_id,sid:b.ue_sid,mid:b.ue_mid,mkt:b.ue_mkt,sn:b.ue_sn,reqs:a})}var f="XMLHttpRequest",q=1===b.ue_ddq,a=b.ue,r=b[f]&&"withCredentials"in new b[f],h=b.navigator&&b.navigator.sendBeacon,l="//"+b.ue_furl+"/1/batch/1/OE/",m=b.ue_fci_ft||5E3;a&&(r||h)&&
(a._flhs=a._flhs||0,a._lpn=a._lpn||{},a.attach&&(a.attach("beforeunload",a.exec(g,"fcli-bfu")),a.attach("pagehide",a.exec(g,"fcli-ph"))),m&&b.setTimeout(a.exec(c,"fcli-t"),m),a._ffci=a.exec(c))})(window);


(function(k,c){function l(a,b){return a.filter(function(a){return a.initiatorType==b})}function f(a,c){if(b.t[a]){var g=b.t[a]-b._t0,e=c.filter(function(a){return 0!==a.responseEnd&&m(a)<g}),f=l(e,"script"),h=l(e,"link"),k=l(e,"img"),n=e.map(function(a){return a.name.split("/")[2]}).filter(function(a,b,c){return a&&c.lastIndexOf(a)==b}),q=e.filter(function(a){return a.duration<p}),s=g-Math.max.apply(null,e.map(m))<r|0;"af"==a&&(b._afjs=f.length);return a+":"+[e[d],f[d],h[d],k[d],n[d],q[d],s].join("-")}}
function m(a){return a.responseEnd-(b._t0-c.timing.navigationStart)}function n(){var a=c[h]("resource"),d=f("cf",a),g=f("af",a),a=f("ld",a);delete b._rt;b._ld=b.t.ld-b._t0;b._art&&b._art();return[d,g,a].join("_")}var p=20,r=50,d="length",b=k.ue,h="getEntriesByType";b._rre=m;b._rt=c&&c.timing&&c[h]&&n})(ue_csm,window.performance);


(function(c,d){var b=c.ue,a=d.navigator;b&&b.tag&&a&&(a=a.connection||a.mozConnection||a.webkitConnection)&&a.type&&b.tag("netInfo:"+a.type)})(ue_csm,window);


(function(c,d){function h(a,b){for(var c=[],d=0;d<a.length;d++){var e=a[d],f=b.encode(e);if(e[k]){var g=b.metaSep,e=e[k],l=b.metaPairSep,h=[],m=void 0;for(m in e)e.hasOwnProperty(m)&&h.push(m+"="+e[m]);e=h.join(l);f+=g+e}c.push(f)}return c.join(b.resourceSep)}function s(a){var b=a[k]=a[k]||{};b[t]||(b[t]=c.ue_mid);b[u]||(b[u]=c.ue_sid);b[f]||(b[f]=c.ue_id);b.csm=1;a="//"+c.ue_furl+"/1/"+a[v]+"/1/OP/"+a[w]+"/"+a[x]+"/"+h([a],y);if(n)try{n.call(d[p],a)}catch(g){c.ue.sbf=1,(new Image).src=a}else(new Image).src=
a}function q(){g&&g.isStub&&g.replay(function(a,b,c){a=a[0];b=a[k]=a[k]||{};b[f]=b[f]||c;s(a)});l.impression=s;g=null}if(!(1<c.ueinit)){var k="metadata",x="impressionType",v="foresterChannel",w="programGroup",t="marketplaceId",u="session",f="requestId",p="navigator",l=c.ue||{},n=d[p]&&d[p].sendBeacon,r=function(a,b,c,d){return{encode:d,resourceSep:a,metaSep:b,metaPairSep:c}},y=r("","?","&",function(a){return h(a.impressionData,z)}),z=r("/",":",",",function(a){return a.featureName+":"+h(a.resources,
A)}),A=r(",","@","|",function(a){return a.id}),g=l.impression;n?q():(l.attach("load",q),l.attach("beforeunload",q));try{d.P&&d.P.register&&d.P.register("impression-client",function(){})}catch(B){c.ueLogError(B,{logLevel:"WARN"})}}})(ue_csm,window);



var ue_pty = "Detail";

var ue_spty = "Glance";

var ue_pti = "B0000028RR";


var ue_adb = 4;
var ue_adb_rtla = 1;
ue_csm.ue.exec(function(y,a){function t(){if(d&&f){var a;a:{try{a=d.getItem(g);break a}catch(c){}a=void 0}if(a)return b=a,!0}return!1}function u(){if(a.fetch)fetch(m).then(function(a){if(!a.ok)throw Error(a.statusText);return a.text?a.text():null}).then(function(b){b?(-1<b.indexOf("window.ue_adb_chk = 1")&&(a.ue_adb_chk=1),n()):h()})["catch"](h);else e.uels(m,{onerror:h,onload:n})}function h(){b=k;l();if(f)try{d.setItem(g,b)}catch(a){}}function n(){b=1===a.ue_adb_chk?p:k;l();if(f)try{d.setItem(g,
b)}catch(c){}}function q(){a.ue_adb_rtla&&c&&0<c.ec&&!1===r&&(c.elh=null,ueLogError({m:"Hit Info",fromOnError:1},{logLevel:"INFO",adb:b}),r=!0)}function l(){e.tag(b);e.isl&&a.uex&&uex("at",b);s&&s.updateCsmHit("adb",b);c&&0<c.ec?q():a.ue_adb_rtla&&c&&(c.elh=q)}function v(){return b}if(a.ue_adb){a.ue_fadb=a.ue_fadb||10;var e=a.ue,k="adblk_yes",p="adblk_no",m="https://m.media-amazon.com/images/G/01/csm/showads.v2.js?adtag=csm&act=ads_",b="adblk_unk",d;a:{try{d=a.localStorage;break a}catch(z){}d=void 0}var g=
"csm:adb",c=a.ue_err,s=e.cookie,f=void 0!==a.localStorage,w=Math.random()>1-1/a.ue_fadb,r=!1,x=t();w||!x?u():l();a.ue_isAdb=v;a.ue_isAdb.unk="adblk_unk";a.ue_isAdb.no=p;a.ue_isAdb.yes=k}},"adb")(document,window);




(function(c,l,m){function h(a){if(a)try{if(a.id)return"//*[@id='"+a.id+"']";var b,d=1,e;for(e=a.previousSibling;e;e=e.previousSibling)e.nodeName===a.nodeName&&(d+=1);b=d;var c=a.nodeName;1!==b&&(c+="["+b+"]");a.parentNode&&(c=h(a.parentNode)+"/"+c);return c}catch(f){return"DETACHED"}}function f(a){if(a&&a.getAttribute)return a.getAttribute(k)?a.getAttribute(k):f(a.parentElement)}var k="data-cel-widget",g=!1,d=[];(c.ue||{}).isBF=function(){try{var a=JSON.parse(localStorage["csm-bf"]||"[]"),b=0<=a.indexOf(c.ue_id);
a.unshift(c.ue_id);a=a.slice(0,20);localStorage["csm-bf"]=JSON.stringify(a);return b}catch(d){return!1}}();c.ue_utils={getXPath:h,getFirstAscendingWidget:function(a,b){c.ue_cel&&c.ue_fem?!0===g?b(f(a)):d.push({element:a,callback:b}):b()},notifyWidgetsLabeled:function(){if(!1===g){g=!0;for(var a=f,b=0;b<d.length;b++)if(d[b].hasOwnProperty("callback")&&d[b].hasOwnProperty("element")){var c=d[b].callback,e=d[b].element;"function"===typeof c&&"function"===typeof a&&c(a(e))}d=null}},extractStringValue:function(a){if("string"===
typeof a)return a}}})(ue_csm,window,document);


(function(a){a.ue_cel||(a.ue_cel=function(){function f(a,c){c?c.r=v:c={r:v,c:1};!ue_csm.ue_sclog&&c.clog&&d.clog?d.clog(a,c.ns||q,c):c.glog&&d.glog?d.glog(a,c.ns||q,c):d.log(a,c.ns||q,c)}function m(a,d){"function"===typeof g&&g("log",{schemaId:s+".RdCSI.1",eventType:a,clientData:d},{ent:"all"})}function c(){var a=n.length;if(0<a){for(var c=[],b=0;b<a;b++){var F=n[b].api;F.ready()?(F.on({ts:d.d,ns:q}),e.push(n[b]),f({k:"mso",n:n[b].name,t:d.d()})):c.push(n[b])}n=c}}function h(){if(!h.executed){for(var a=
0;a<e.length;a++)e[a].api.off&&e[a].api.off({ts:d.d,ns:q});A();f({k:"eod",t0:d.t0,t:d.d()},{c:1,il:1});h.executed=1;for(a=0;a<e.length;a++)n.push(e[a]);e=[];b(t);b(x)}}function A(a){f({k:"hrt",t:d.d()},{c:1,il:1,n:a});l=Math.min(w,r*l);y()}function y(){b(x);x=k(function(){A(!0)},l)}function u(){h.executed||A()}var p=a.window,k=p.setTimeout,b=p.clearTimeout,r=1.5,w=p.ue_cel_max_hrt||3E4,s="robotdetection",n=[],e=[],q=a.ue_cel_ns||"cel",t,x,d=a.ue,E=a.uet,B=a.uex,v=d.rid,C=p.csa,g,l=p.ue_cel_hrt_int||
3E3,z=p.requestAnimationFrame||function(a){a()};a.ue_cel_lclia&&C&&(g=C("Events",{producerId:s}));if(d.isBF)f({k:"bft",t:d.d()});else{"function"==typeof E&&E("bb","csmCELLSframework",{wb:1});k(c,0);d.onunload(h);if(d.onflush)d.onflush(u);t=k(h,6E5);y();"function"==typeof B&&B("ld","csmCELLSframework",{wb:1});return{registerModule:function(a,b){n.push({name:a,api:b});f({k:"mrg",n:a,t:d.d()});c()},reset:function(a){f({k:"rst",t0:d.t0,t:d.d()});n=n.concat(e);e=[];for(var r=n.length,g=0;g<r;g++)n[g].api.off(),
n[g].api.reset();v=a||d.rid;c();b(t);t=k(h,6E5);h.executed=0},timeout:function(a,d){return k(function(){z(function(){h.executed||a()})},d)},log:f,csaEventLog:m,off:h}}}())})(ue_csm);
(function(a){a.ue_pdm||!a.ue_cel||a.ue.isBF||(a.ue_pdm=function(){function f(){try{var d=b.screen;if(d){var c={w:d.width,aw:d.availWidth,h:d.height,ah:d.availHeight,cd:d.colorDepth,pd:d.pixelDepth};e&&e.w===c.w&&e.h===c.h&&e.aw===c.aw&&e.ah===c.ah&&e.pd===c.pd&&e.cd===c.cd||(e=c,e.t=s(),e.k="sci",E(e),C&&g&&l("sci",{h:(e.h||"0")+""}))}var k=r.body||{},h=r.documentElement||{},m={w:Math.max(k.scrollWidth||0,k.offsetWidth||0,h.clientWidth||0,h.scrollWidth||0,h.offsetWidth||0),h:Math.max(k.scrollHeight||
0,k.offsetHeight||0,h.clientHeight||0,h.scrollHeight||0,h.offsetHeight||0)};q&&q.w===m.w&&q.h===m.h||(q=m,q.t=s(),q.k="doi",E(q));w=a.ue_cel.timeout(f,n);x+=1}catch(p){b.ueLogError&&ueLogError(p,{attribution:"csm-cel-page-module",logLevel:"WARN"})}}function m(){u("ebl","default",!1)}function c(){u("efo","default",!0)}function h(){u("ebl","app",!1)}function A(){u("efo","app",!0)}function y(){b.setTimeout(function(){r[H]?u("ebl","pageviz",!1):u("efo","pageviz",!0)},0)}function u(a,d,c){t!==c&&(E({k:a,
t:s(),s:d},{ff:!0===c?0:1}),C&&g&&l(a,{t:(s()||"0")+"",s:d}));t=c}function p(){d.attach&&(z&&d.attach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.addEventListener&&(a.addEventListener("appPause",h),a.addEventListener("appResume",A))}),d.attach("blur",m,b),d.attach("focus",c,b))}function k(){d.detach&&(z&&d.detach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.removeEventListener&&(a.removeEventListener("appPause",h),a.removeEventListener("appResume",A))}),d.detach("blur",m,b),d.detach("focus",
c,b))}var b=a.window,r=a.document,w,s,n,e,q,t=null,x=0,d=a.ue,E=a.ue_cel.log,B=a.uet,v=a.uex,C=a.ue_cel_lclia,g=b.csa,l=a.ue_cel.csaEventLog,z=!!d.pageViz,D=z&&d.pageViz.event,H=z&&d.pageViz.propHid,I=b.P&&b.P.when;"function"==typeof B&&B("bb","csmCELLSpdm",{wb:1});return{on:function(a){n=a.timespan||500;s=a.ts;p();a=b.location;E({k:"pmd",o:a.origin,p:a.pathname,t:s()});f();"function"==typeof v&&v("ld","csmCELLSpdm",{wb:1})},off:function(a){clearTimeout(w);k();d.count&&d.count("cel.PDM.TotalExecutions",
x)},ready:function(){return r.body&&a.ue_cel&&a.ue_cel.log},reset:function(){e=q=null}}}(),a.ue_cel&&a.ue_cel.registerModule("page module",a.ue_pdm))})(ue_csm);
(function(a){a.ue_vpm||!a.ue_cel||a.ue.isBF||(a.ue_vpm=function(){function f(){var a=y(),b={w:k.innerWidth,h:k.innerHeight,x:k.pageXOffset,y:k.pageYOffset};c&&c.w==b.w&&c.h==b.h&&c.x==b.x&&c.y==b.y||(b.t=a,b.k="vpi",c=b,r(c,{clog:1}),q&&t&&x("vpi",{t:(c.t||"0")+"",h:(c.h||"0")+"",y:(c.y||"0")+"",w:(c.w||"0")+"",x:(c.x||"0")+""}));h=0;u=y()-a;p+=1}function m(){h||(h=a.ue_cel.timeout(f,A))}var c,h,A,y,u=0,p=0,k=a.window,b=a.ue,r=a.ue_cel.log,w=a.uet,s=a.uex,n=b.attach,e=b.detach,q=a.ue_cel_lclia,t=
k.csa,x=a.ue_cel.csaEventLog;"function"==typeof w&&w("bb","csmCELLSvpm",{wb:1});return{on:function(a){y=a.ts;A=a.timespan||100;f();n&&(n("scroll",m),n("resize",m));"function"==typeof s&&s("ld","csmCELLSvpm",{wb:1})},off:function(a){clearTimeout(h);e&&(e("scroll",m),e("resize",m));b.count&&(b.count("cel.VPI.TotalExecutions",p),b.count("cel.VPI.TotalExecutionTime",u),b.count("cel.VPI.AverageExecutionTime",u/p))},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){c=void 0},getVpi:function(){return c}}}(),
a.ue_cel&&a.ue_cel.registerModule("viewport module",a.ue_vpm))})(ue_csm);
(function(a){if(!a.ue_fem&&a.ue_cel&&a.ue_utils){var f=a.ue||{},m=a.window,c=m.document;!f.isBF&&!a.ue_fem&&c.querySelector&&m.getComputedStyle&&[].forEach&&(a.ue_fem=function(){function h(a,d){return a>d?3>a-d:3>d-a}function A(a,d){var c=m.pageXOffset,b=m.pageYOffset,k;a:{try{if(a){var g=a.getBoundingClientRect(),e,r=0===a.offsetWidth&&0===a.offsetHeight;c:{for(var f=a.parentNode,w=g.left||0,n=g.top||0,p=g.width||0,q=g.height||0;f&&f!==document.body;){var l;d:{try{var s=void 0;if(f)var G=f.getBoundingClientRect(),
s={x:G.left||0,y:G.top||0,w:G.width||0,h:G.height||0};else s=void 0;l=s;break d}catch(v){}l=void 0}var t=window.getComputedStyle(f),u="hidden"===t.overflow,y=u||"hidden"===t.overflowX,z=u||"hidden"===t.overflowY,J=n+q-1<l.y+1||n+1>l.y+l.h-1;if((w+p-1<l.x+1||w+1>l.x+l.w-1)&&y||J&&z){e=!0;break c}f=f.parentNode}e=!1}k={x:g.left+c||0,y:g.top+b||0,w:g.width||0,h:g.height||0,d:(r||e)|0}}else k=void 0;break a}catch(A){}k=void 0}if(k&&!a.cel_b)a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,
x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi",cl:a.className},{clog:1});else{if(c=k)c=a.cel_b,b=k,c=b.d===c.d&&1===b.d?!1:!(h(c.x,b.x)&&h(c.y,b.y)&&h(c.w,b.w)&&h(c.h,b.h)&&c.d===b.d);c&&(a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi"},{clog:1}))}}function y(b,g){var h;h=b.c?c.getElementsByClassName(b.c):b.id?[c.getElementById(b.id)]:c.querySelectorAll(b.s);b.w=[];for(var f=0;f<h.length;f++){var e=h[f];if(e){if(!e.getAttribute(x)){var r=e.getAttribute("cel_widget_id")||
(b.id_gen||v)(e,f)||e.id;e.setAttribute(x,r)}b.w.push(e);k(Q,e,g)}}!1===B&&(E++,E===d.length&&(B=!0,a.ue_utils.notifyWidgetsLabeled()))}function u(a,c){g.contains(a)||C({n:a.getAttribute(x),t:c,k:"ewd"},{clog:1})}function p(a){K.length&&ue_cel.timeout(function(){if(q){for(var c=R(),d=!1;R()-c<e&&!d;){for(d=S;0<d--&&0<K.length;){var b=K.shift();T[b.type](b.elem,b.time)}d=0===K.length}U++;p(a)}},0)}function k(a,c,d){K.push({type:a,elem:c,time:d})}function b(a,c){for(var b=0;b<d.length;b++)for(var e=
d[b].w||[],g=0;g<e.length;g++)k(a,e[g],c)}function r(){M||(M=a.ue_cel.timeout(function(){M=null;var c=t();b(W,c);for(var g=0;g<d.length;g++)k(X,d[g],c);0===d.length&&!1===B&&(B=!0,a.ue_utils.notifyWidgetsLabeled());p(c)},n))}function w(){M||N||(N=a.ue_cel.timeout(function(){N=null;var a=t();b(Q,a);p(a)},n))}function s(){return z&&D&&g&&g.contains&&g.getBoundingClientRect&&t}var n=50,e=4.5,q=!1,t,x="data-cel-widget",d=[],E=0,B=!1,v=function(){},C=a.ue_cel.log,g,l,z,D,H=m.MutationObserver||m.WebKitMutationObserver||
m.MozMutationObserver,I=!!H,F,G,O="DOMAttrModified",L="DOMNodeInserted",J="DOMNodeRemoved",N,M,K=[],U=0,S=null,W="removedWidget",X="updateWidgets",Q="processWidget",T,V=m.performance||{},R=V.now&&function(){return V.now()}||function(){return Date.now()};"function"==typeof uet&&uet("bb","csmCELLSfem",{wb:1});return{on:function(b){function e(){if(s()){T={removedWidget:u,updateWidgets:y,processWidget:A};if(I){var a={attributes:!0,subtree:!0};F=new H(w);G=new H(r);F.observe(g,a);G.observe(g,{childList:!0,
subtree:!0});G.observe(l,a)}else z.call(g,O,w),z.call(g,L,r),z.call(g,J,r),z.call(l,L,w),z.call(l,J,w);r()}}g=c.body;l=c.head;z=g.addEventListener;D=g.removeEventListener;t=b.ts;d=a.cel_widgets||[];S=b.bs||5;f.deffered?e():f.attach&&f.attach("load",e);"function"==typeof uex&&uex("ld","csmCELLSfem",{wb:1});q=!0},off:function(){s()&&(G&&(G.disconnect(),G=null),F&&(F.disconnect(),F=null),D.call(g,O,w),D.call(g,L,r),D.call(g,J,r),D.call(l,L,w),D.call(l,J,w));f.count&&f.count("cel.widgets.batchesProcessed",
U);q=!1},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){d=a.cel_widgets||[]}}}(),a.ue_cel&&a.ue_fem&&a.ue_cel.registerModule("features module",a.ue_fem))}})(ue_csm);
(function(a){!a.ue_mcm&&a.ue_cel&&a.ue_utils&&!a.ue.isBF&&(a.ue_mcm=function(){function f(a,b){var h=a.srcElement||a.target||{},f={k:m,w:(b||{}).ow||(A.body||{}).scrollWidth,h:(b||{}).oh||(A.body||{}).scrollHeight,t:(b||{}).ots||c(),x:a.pageX,y:a.pageY,p:p.getXPath(h),n:h.nodeName};y&&"function"===typeof y.now&&a.timeStamp&&(f.dt=(b||{}).odt||y.now()-a.timeStamp,f.dt=parseFloat(f.dt.toFixed(2)));a.button&&(f.b=a.button);h.href&&(f.r=p.extractStringValue(h.href));h.id&&(f.i=h.id);h.className&&h.className.split&&
(f.c=h.className.split(/\s+/));u(f,{c:1})}var m="mcm",c,h=a.window,A=h.document,y=h.performance,u=a.ue_cel.log,p=a.ue_utils;return{on:function(k){c=k.ts;a.ue_cel_stub&&a.ue_cel_stub.replayModule(m,f);h.addEventListener&&h.addEventListener("mousedown",f,!0)},off:function(a){h.addEventListener&&h.removeEventListener("mousedown",f,!0)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){}}}(),a.ue_cel&&a.ue_cel.registerModule("mouse click module",a.ue_mcm))})(ue_csm);
(function(a){a.ue_mmm||!a.ue_cel||a.ue.isBF||(a.ue_mmm=function(f){function m(a,c){var b={x:a.pageX||a.x||0,y:a.pageY||a.y||0,t:p()};!c&&l&&(b.t-l.t<A||b.x==l.x&&b.y==l.y)||(l=b,v.push(b))}function c(){if(v.length){E=F.now();for(var a=0;a<v.length;a++){var c=v[a],b=a;z=v[g];D=c;var e=void 0;if(!(e=2>b)){e=void 0;a:if(v[b].t-v[b-1].t>h)e=0;else{for(e=g+1;e<b;e++){var f=z,k=D,l=v[e];H=(k.x-f.x)*(f.y-l.y)-(f.x-l.x)*(k.y-f.y);if(H*H/((k.x-f.x)*(k.x-f.x)+(k.y-f.y)*(k.y-f.y))>y){e=0;break a}}e=1}e=!e}(I=
e)?g=b-1:C.pop();C.push(c)}B=F.now()-E;q=Math.min(q,B);t=Math.max(t,B);x=(x*d+B)/(d+1);d+=1;n({k:u,e:C,min:Math.floor(1E3*q),max:Math.floor(1E3*t),avg:Math.floor(1E3*x)},{c:1});v=[];C=[];g=0}}var h=100,A=20,y=25,u="mmm1",p,k,b=a.window,r=b.document,w=b.setInterval,s=a.ue,n=a.ue_cel.log,e,q=1E3,t=0,x=0,d=0,E,B,v=[],C=[],g=0,l,z,D,H,I,F=f&&f.now&&f||Date.now&&Date||{now:function(){return(new Date).getTime()}};return{on:function(a){p=a.ts;k=a.ns;s.attach&&s.attach("mousemove",m,r);e=w(c,3E3)},off:function(a){k&&
(l&&m(l,!0),c());clearInterval(e);s.detach&&s.detach("mousemove",m,r)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){v=[];C=[];g=0;l=null}}}(window.performance),a.ue_cel&&a.ue_cel.registerModule("mouse move module",a.ue_mmm))})(ue_csm);



ue_csm.ue.exec(function(b,c){var e=function(){},f=function(){return{send:function(b,d){if(d&&b){var a;if(c.XDomainRequest)a=new XDomainRequest,a.onerror=e,a.ontimeout=e,a.onprogress=e,a.onload=e,a.timeout=0;else if(c.XMLHttpRequest){if(a=new XMLHttpRequest,!("withCredentials"in a))throw"";}else a=void 0;if(!a)throw"";a.open("POST",b,!0);a.setRequestHeader&&a.setRequestHeader("Content-type","text/plain");a.send(d)}},isSupported:!0}}(),g=function(){return{send:function(c,d){if(c&&d)if(navigator.sendBeacon(c,
d))b.ue_sbuimp&&b.ue&&b.ue.ssw&&b.ue.ssw("eelsts","scs");else throw"";},isSupported:!!navigator.sendBeacon&&!(c.cordova&&c.cordova.platformId&&"ios"==c.cordova.platformId)}}();b.ue._ajx=f;b.ue._sBcn=g},"Transportation-clients")(ue_csm,window);
ue_csm.ue.exec(function(b,k){function A(){for(var a=0;a<arguments.length;a++){var c=arguments[a];try{var h;if(c.isSupported){var b=t.buildPayload(l,e);h=c.send(J,b)}else throw dummyException;return h}catch(d){}}B({m:"All supported clients failed",attribution:"CSMSushiClient_TRANSPORTATION_FAIL",f:"sushi-client.js",logLevel:"ERROR"},k.ue_err_chan||"jserr")}function m(){if(e.length){for(var a=0;a<n.length;a++)n[a]();A(d._sBcn||{},d._ajx||{});e=[];f={};l={};u=v=q=w=0}}function K(){var a=new Date,c=function(a){return 10>
a?"0"+a:a};return Date.prototype.toISOString?a.toISOString():a.getUTCFullYear()+"-"+c(a.getUTCMonth()+1)+"-"+c(a.getUTCDate())+"T"+c(a.getUTCHours())+":"+c(a.getUTCMinutes())+":"+c(a.getUTCSeconds())+"."+String((a.getUTCMilliseconds()/1E3).toFixed(3)).slice(2,5)+"Z"}function x(a){try{return JSON.stringify(a)}catch(c){}return null}function C(a,c,h,g){var p=!1;g=g||{};r++;r==D&&B({m:"Max number of Sushi Logs exceeded",f:"sushi-client.js",logLevel:"ERROR",attribution:"CSMSushiClient_MAX_CALLS"},k.ue_err_chan||
"jserr");var f;if(f=!(r>=D))(f=a&&-1<a.constructor.toString().indexOf("Object")&&c&&-1<c.constructor.toString().indexOf("String")&&h&&-1<h.constructor.toString().indexOf("String"))||L++;f&&(d.count&&d.count("Event:"+h,1),a.producerId=a.producerId||c,a.schemaId=a.schemaId||h,a.timestamp=K(),c=Date.now?Date.now():+new Date,h=Math.random().toString().substring(2,12),a.messageId=b.ue_id+"-"+c+"-"+h,g&&!g.ssd&&(a.sessionId=a.sessionId||b.ue_sid,a.requestId=a.requestId||b.ue_id,a.obfuscatedMarketplaceId=
a.obfuscatedMarketplaceId||b.ue_mid),(c=x(a))?(c=c.length,(e.length==M||q+c>N)&&m(),q+=c,a={data:t.compressEvent(a)},e.push(a),(g||{}).n?0===E?m():u||(u=k.setTimeout(m,E)):v||(v=k.setTimeout(m,O)),p=!0):p=!1);!p&&b.ue_int&&console.error("Invalid JS Nexus API call");return p}function F(){if(!G){for(var a=0;a<y.length;a++)y[a]();for(a=0;a<n.length;a++)n[a]();e.length&&(b.ue_sbuimp&&b.ue&&b.ue.ssw&&(a=x({dct:l,evt:e}),b.ue.ssw("eeldata",a),b.ue.ssw("eelsts","unk")),A(d._sBcn||{}));G=!0}}function H(a){y.push(a)}
function I(a){n.push(a)}var D=1E3,M=499,N=524288,s=function(){},d=b.ue||{},B=d.log||s,P=b.uex||s;(b.uet||s)("bb","ue_sushi_v1",{wb:1});var J=b.ue_surl||"https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.gamma",Q=["messageId","timestamp"],z="#",e=[],f={},l={},q=0,w=0,L=0,r=0,y=[],n=[],G=!1,u,v,E=void 0===b.ue_hpsi?1E3:b.ue_hpsi,O=void 0===b.ue_lpsi?1E4:b.ue_lpsi,t=function(){function a(a){f[a]=z+w++;l[f[a]]=a;return f[a]}function c(b){if(!(b instanceof Function)){if(b instanceof Array){for(var g=
[],d=b.length,e=0;e<d;e++)g[e]=c(b[e]);return g}if(b instanceof Object){g={};for(d in b)b.hasOwnProperty(d)&&(g[f[d]?f[d]:a(d)]=-1===Q.indexOf(d)?c(b[d]):b[d]);return g}return"string"===typeof b&&(b.length>(z+w).length||b.charAt(0)===z)?f[b]?f[b]:a(b):b}}return{compressEvent:c,buildPayload:function(){return x({cs:{dct:l},events:e})}}}();(function(){if(d.event&&d.event.isStub){if(b.ue_sbuimp&&b.ue&&b.ue.ssw){var a=b.ue.ssw("eelsts").val;if(a&&"unk"===a&&(a=b.ue.ssw("eeldata").val)){var c;a:{try{c=
JSON.parse(a);break a}catch(f){}c=null}c&&c.evt instanceof Array&&c.dct instanceof Object&&(e=c.evt,l=c.dct,e&&l&&(m(),b.ue.ssw("eeldata","{}"),b.ue.ssw("eelsts","scs")))}}d.event.replay(function(a){a[3]=a[3]||{};a[3].n=1;C.apply(this,a)});d.onSushiUnload.replay(function(a){H(a[0])});d.onSushiFlush.replay(function(a){I(a[0])})}})();d.attach("beforeunload",F);d.attach("pagehide",F);d._cmps=t;d.event=C;d.event.reset=function(){r=0};d.onSushiUnload=H;d.onSushiFlush=I;try{k.P&&k.P.register&&k.P.register("sushi-client",
s)}catch(R){b.ueLogError(R,{logLevel:"WARN"})}P("ld","ue_sushi_v1",{wb:1})},"Nxs-JS-Client")(ue_csm,window);


ue_csm.ue_unrt = 1500;
(function(d,b,t){function u(a,g){var c=a.srcElement||a.target||{},b={k:v,t:g.t,dt:g.dt,x:a.pageX,y:a.pageY,p:e.getXPath(c),n:c.nodeName};a.button&&(b.b=a.button);c.type&&(b.ty=c.type);c.href&&(b.r=e.extractStringValue(c.href));c.id&&(b.i=c.id);c.className&&c.className.split&&(b.c=c.className.split(/\s+/));h+=1;e.getFirstAscendingWidget(c,function(a){b.wd=a;d.ue.log(b,r)})}function w(a){if(!x(a.srcElement||a.target)){m+=1;n=!0;var g=f=d.ue.d(),c;p&&"function"===typeof p.now&&a.timeStamp&&(c=p.now()-
a.timeStamp,c=parseFloat(c.toFixed(2)));s=b.setTimeout(function(){u(a,{t:g,dt:c})},y)}}function z(a){if(a){var b=a.filter(A);a.length!==b.length&&(q=!0,k=d.ue.d(),n&&q&&(k&&f&&d.ue.log({k:B,t:f,m:Math.abs(k-f)},r),l(),q=!1,k=0))}}function A(a){if(!a)return!1;var b="characterData"===a.type?a.target.parentElement:a.target;if(!b||!b.hasAttributes||!b.attributes)return!1;var c={"class":"gw-clock gw-clock-aria s-item-container-height-auto feed-carousel using-mouse kfs-inner-container".split(" "),id:["dealClock",
"deal_expiry_timer","timer"],role:["timer"]},d=!1;Object.keys(c).forEach(function(a){var e=b.attributes[a]?b.attributes[a].value:"";(c[a]||"").forEach(function(a){-1!==e.indexOf(a)&&(d=!0)})});return d}function x(a){if(!a)return!1;var b=(e.extractStringValue(a.nodeName)||"").toLowerCase(),c=(e.extractStringValue(a.type)||"").toLowerCase(),d=(e.extractStringValue(a.href)||"").toLowerCase();a=(e.extractStringValue(a.id)||"").toLowerCase();var f="checkbox color date datetime-local email file month number password radio range reset search tel text time url week".split(" ");
if(-1!==["select","textarea","html"].indexOf(b)||"input"===b&&-1!==f.indexOf(c)||"a"===b&&-1!==d.indexOf("http")||-1!==["sitbreaderrightpageturner","sitbreaderleftpageturner","sitbreaderpagecontainer"].indexOf(a))return!0}function l(){n=!1;f=0;b.clearTimeout(s)}function C(){b.ue.onunload(function(){ue.count("armored-cxguardrails.unresponsive-clicks.violations",h);ue.count("armored-cxguardrails.unresponsive-clicks.violationRate",h/m*100||0)})}if(b.MutationObserver&&b.addEventListener&&Object.keys&&
d&&d.ue&&d.ue.log&&d.ue_unrt&&d.ue_utils){var y=d.ue_unrt,r="cel",v="unr_mcm",B="res_mcm",p=b.performance,e=d.ue_utils,n=!1,f=0,s=0,q=!1,k=0,h=0,m=0;b.addEventListener&&(b.addEventListener("mousedown",w,!0),b.addEventListener("beforeunload",l,!0),b.addEventListener("visibilitychange",l,!0),b.addEventListener("pagehide",l,!0));b.ue&&b.ue.event&&b.ue.onSushiUnload&&b.ue.onunload&&C();(new MutationObserver(z)).observe(t,{childList:!0,attributes:!0,characterData:!0,subtree:!0})}})(ue_csm,window,document);


ue_csm.ue.exec(function(g,e){if(e.ue_err){var f="";e.ue_err.errorHandlers||(e.ue_err.errorHandlers=[]);e.ue_err.errorHandlers.push({name:"fctx",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel)if(f=g.getElementsByTagName("html")[0].innerHTML){var b=f.indexOf("var ue_t0=ue_t0||+new Date();");if(-1!==b){var b=f.substr(0,b).split(String.fromCharCode(10)),d=Math.max(b.length-10-1,0),b=b.slice(d,b.length-1);a.fcsmln=d+b.length+1;a.cinfo=a.cinfo||{};for(var c=0;c<b.length;c++)a.cinfo[d+c+1+""]=
b[c]}b=f.split(String.fromCharCode(10));a.cinfo=a.cinfo||{};if(!(a.f||void 0===a.l||a.l in a.cinfo))for(c=+a.l-1,d=Math.max(c-5,0),c=Math.min(c+5,b.length-1);d<=c;d++)a.cinfo[d+1+""]=b[d]}}})}},"fatals-context")(document,window);


(function(m,a){function c(k){function f(b){b&&"string"===typeof b&&(b=(b=b.match(/^(?:https?:)?\/\/(.*?)(\/|$)/i))&&1<b.length?b[1]:null,b&&b&&("number"===typeof e[b]?e[b]++:e[b]=1))}function d(b){var e=10,d=+new Date;b&&b.timeRemaining?e=b.timeRemaining():b={timeRemaining:function(){return Math.max(0,e-(+new Date-d))}};for(var c=a.performance.getEntries(),k=e;g<c.length&&k>n;)c[g].name&&f(c[g].name),g++,k=b.timeRemaining();g>=c.length?h(!0):l()}function h(b){if(!b){b=m.scripts;var c;if(b)for(var d=
0;d<b.length;d++)(c=b[d].getAttribute("src"))&&"undefined"!==c&&f(c)}0<Object.keys(e).length&&(p&&ue_csm.ue&&ue_csm.ue.event&&ue_csm.ue.event({domains:e,pageType:a.ue_pty||null,subPageType:a.ue_spty||null,pageTypeId:a.ue_pti||null},"csm","csm.CrossOriginDomains.2"),a.ue_ext=e)}function l(){!0===k?d():a.requestIdleCallback?a.requestIdleCallback(d):a.requestAnimationFrame?a.requestAnimationFrame(d):a.setTimeout(d,100)}function c(){if(a.performance&&a.performance.getEntries){var b=a.performance.getEntries();
!b||0>=b.length?h(!1):l()}else h(!1)}var e=a.ue_ext||{};a.ue_ext||c();return e}function q(){setTimeout(c,r)}var s=a.ue_dserr||!1,p=!0,n=1,r=2E3,g=0;a.ue_err&&s&&(a.ue_err.errorHandlers||(a.ue_err.errorHandlers=[]),a.ue_err.errorHandlers.push({name:"ext",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel){var f=c(!0),d=[],h;for(h in f){var f=h,g=f.match(/amazon(\.com?)?\.\w{2,3}$/i);g&&1<g.length||-1!==f.indexOf("amazon-adsystem.com")||-1!==f.indexOf("amazonpay.com")||-1!==f.indexOf("cloudfront-labs.amazonaws.com")||
d.push(h)}a.ext=d}}}));a.ue&&a.ue.isl?c():a.ue&&ue.attach&&ue.attach("load",q)})(document,window);





var ue_wtc_c = 3;
ue_csm.ue.exec(function(b,e){function l(){for(var a=0;a<f.length;a++)a:for(var d=s.replace(A,f[a])+g[f[a]]+t,c=arguments,b=0;b<c.length;b++)try{c[b].send(d);break a}catch(e){}g={};f=[];n=0;k=p}function u(){B?l(q):l(C,q)}function v(a,m,c){r++;if(r>w)d.count&&1==r-w&&(d.count("WeblabTriggerThresholdReached",1),b.ue_int&&console.error("Number of max call reached. Data will no longer be send"));else{var h=c||{};h&&-1<h.constructor.toString().indexOf(D)&&a&&-1<a.constructor.toString().indexOf(x)&&m&&-1<
m.constructor.toString().indexOf(x)?(h=b.ue_id,c&&c.rid&&(h=c.rid),c=h,a=encodeURIComponent(",wl="+a+"/"+m),2E3>a.length+p?(2E3<k+a.length&&u(),void 0===g[c]&&(g[c]="",f.push(c)),g[c]+=a,k+=a.length,n||(n=e.setTimeout(u,E))):b.ue_int&&console.error("Invalid API call. The input provided is over 2000 chars.")):d.count&&(d.count("WeblabTriggerImproperAPICall",1),b.ue_int&&console.error("Invalid API call. The input provided does not match the API protocol i.e ue.trigger(String, String, Object)."))}}function F(){d.trigger&&
d.trigger.isStub&&d.trigger.replay(function(a){v.apply(this,a)})}function y(){z||(f.length&&l(q),z=!0)}var t=":1234",s="//"+b.ue_furl+"/1/remote-weblab-triggers/1/OE/"+b.ue_mid+":"+b.ue_sid+":PLCHLDR_RID$s:wl-client-id%3DCSMTriger",A="PLCHLDR_RID",E=b.wtt||1E4,p=s.length+t.length,w=b.mwtc||2E3,G=1===e.ue_wtc_c,B=3===e.ue_wtc_c,H=e.XMLHttpRequest&&"withCredentials"in new e.XMLHttpRequest,x="String",D="Object",d=b.ue,g={},f=[],k=p,n,z=!1,r=0,C=function(){return{send:function(a){if(H){var b=new e.XMLHttpRequest;
b.open("GET",a,!0);G&&(b.withCredentials=!0);b.send()}else throw"";}}}(),q=function(){return{send:function(a){(new Image).src=a}}}();e.encodeURIComponent&&(d.attach&&(d.attach("beforeunload",y),d.attach("pagehide",y)),F(),d.trigger=v)},"client-wbl-trg")(ue_csm,window);


(function(k,d,h){function f(a,c,b){a&&a.indexOf&&0===a.indexOf("http")&&0!==a.indexOf("https")&&l(s,c,a,b)}function g(a,c,b){a&&a.indexOf&&(location.href.split("#")[0]!=a&&null!==a&&"undefined"!==typeof a||l(t,c,a,b))}function l(a,c,b,e){m[b]||(e=u&&e?n(e):"N/A",d.ueLogError&&d.ueLogError({message:a+c+" : "+b,logLevel:v,stack:"N/A"},{attribution:e}),m[b]=1,p++)}function e(a,c){if(a&&c)for(var b=0;b<a.length;b++)try{c(a[b])}catch(d){}}function q(){return d.performance&&d.performance.getEntriesByType?
d.performance.getEntriesByType("resource"):[]}function n(a){if(a.id)return"//*[@id='"+a.id+"']";var c;c=1;var b;for(b=a.previousSibling;b;b=b.previousSibling)b.nodeName==a.nodeName&&(c+=1);b=a.nodeName;1!=c&&(b+="["+c+"]");a.parentNode&&(b=n(a.parentNode)+"/"+b);return b}function w(){var a=h.images;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"img",a);g(b,"img",a)})}function x(){var a=h.scripts;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"script",a);g(b,"script",a)})}
function y(){var a=h.styleSheets;a&&a.length&&e(a,function(a){if(a=a.ownerNode){var b=a.getAttribute("href");f(b,"style",a);g(b,"style",a)}})}function z(){if(A){var a=q();e(a,function(a){f(a.name,a.initiatorType)})}}function B(){e(q(),function(a){g(a.name,a.initiatorType)})}function r(){var a;a=d.location&&d.location.protocol?d.location.protocol:void 0;"https:"==a&&(z(),w(),x(),y(),B(),p<C&&setTimeout(r,D))}var s="[CSM] Insecure content detected ",t="[CSM] Ajax request to same page detected ",v="WARN",
m={},p=0,D=k.ue_nsip||1E3,C=5,A=1==k.ue_urt,u=!0;ue_csm.ue_disableNonSecure||(d.performance&&d.performance.setResourceTimingBufferSize&&d.performance.setResourceTimingBufferSize(300),r())})(ue_csm,window,document);


var ue_aa_a = "";
if (ue.trigger && (ue_aa_a === "C" || ue_aa_a === "T1")) {
    ue.trigger("UEDATA_AA_SERVERSIDE_ASSIGNMENT_CLIENTSIDE_TRIGGER_190249", ue_aa_a);
}
(function(f,b){function g(){try{b.PerformanceObserver&&"function"===typeof b.PerformanceObserver&&(a=new b.PerformanceObserver(function(b){c(b.getEntries())}),a.observe(d))}catch(h){k()}}function m(){for(var h=d.entryTypes,a=0;a<h.length;a++)c(b.performance.getEntriesByType(h[a]))}function c(a){if(a&&Array.isArray(a)){for(var c=0,e=0;e<a.length;e++){var d=l.indexOf(a[e].name);if(-1!==d){var g=Math.round(b.performance.timing.navigationStart+a[e].startTime);f.uet(n[d],void 0,void 0,g);c++}}l.length===
c&&k()}}function k(){a&&a.disconnect&&"function"===typeof a.disconnect&&a.disconnect()}if("function"===typeof f.uet&&b.performance&&"object"===typeof b.performance&&b.performance.getEntriesByType&&"function"===typeof b.performance.getEntriesByType&&b.performance.timing&&"object"===typeof b.performance.timing&&"number"===typeof b.performance.timing.navigationStart){var d={entryTypes:["paint"]},l=["first-paint","first-contentful-paint"],n=["fp","fcp"],a;try{m(),g()}catch(p){f.ueLogError(p,{logLevel:"ERROR",
attribution:"performanceMetrics"})}}})(ue_csm,window);


if (window.csa) {
    csa("Events")("setEntity", {
        page:{pageType: "Detail", subPageType: "Glance", pageTypeId: "B0000028RR"}
    });
}
csa.plugin(function(e){var i="transitionStart",n="pageVisible",t="PageTiming",a="visibilitychange",o=e("Events",{producerId:"csa"}),r=(e.global.performance||{}).timing,d=["navigationStart","unloadEventStart","unloadEventEnd","redirectStart","redirectEnd","fetchStart","domainLookupStart","domainLookupEnd","connectStart","connectEnd","secureConnectionStart","requestStart","responseStart","responseEnd","domLoading","domInteractive","domContentLoadedEventStart","domContentLoadedEventEnd","domComplete","loadEventStart","loadEventEnd"],c=e.config,l=e.global.document||{},s=(r||{}).navigationStart,u=s,m={},g=0,v=0,f=c[t+".BatchInterval"]||3e3,p=0,S=!0;if(!c["KillSwitch."+t]){if(!r||null===s||s<=0||void 0===s)return e.error("Invalid navigation timing data: "+s);"boolean"!=typeof l.hidden&&"string"!=typeof l.visibilityState||!l.removeEventListener||((S=L())?(E(n,s),b()):e.on(l,a,function t(){(S=L())&&(u=e.time(),l.removeEventListener(a,t),E(n,u),E(i,u),b())})),e.once("$unload",h),e.once("$load",h),e.on("$beforePageTransition",y),e.on("$pageTransition",function(){u=e.time()}),e.register(t,{mark:E})}function E(t,n){null!=t&&(n=n||e.time(),t===i&&(u=n),m[t]=n,b(),e.emit("$timing:"+t,n))}function h(){!function(){if(p)return;for(var t=0;t<d.length;t++)r[d[t]]&&E(d[t],r[d[t]]);p=1}(),g=1,b(!0)}function b(t){g&&S&&!v&&(v=e.timeout(y,t?0:f))}function y(){0<Object.keys(m).length&&(o("log",{markers:function(t,n){var e={};for(var i in t)t.hasOwnProperty(i)&&(e[i]=Math.max(0,t[i]-n));return e}(m,u),markerTimestamps:function(t){for(var n in t)t.hasOwnProperty(n)&&(t[n]=Math.floor(t[n]));return t}(m),navigationStartTimestamp:u?new Date(u).toISOString():null,schemaId:"<ns>.PageLatency.5"},{ent:{page:["pageType","subPageType","requestId"]}}),m={}),v=0}function L(){return!l.hidden||"visible"===l.visibilityState}});csa.plugin(function(t){var a,f="length",u="parentElement",i="target",r="getEntriesByName",o="_osrc",c="_elt",d="_eid",l=10,h=5,g=10,s=100,m=t.global,n=t.timeout,e=m.Math,v=e.max,p=e.floor,E=e.ceil,y=m.document,x=m.performance||{},w=(x.timing||{}).navigationStart,O=Date.now,S=Object.values,T=t("PageTiming"),b=t("SpeedIndexBuffers"),I=[],N=[],B=[],H=[],L=[],W=.1,_=.1,k=0,C=0,P=!0,R=0,X=0,Y=0,$=0,F=1,V=0,j=[],D=0;function M(){for(var e=O(),n=0;a;){if(0!==a[f]){if(!1!==a.h(a[0])&&a.shift(),n++,!Y&&n%l==0&&O()-e>h)break}else a=a.n}k=0,a&&0<a[f]&&(k=k||t.raf(M))}function q(e,n,t,i){V=p(e),I=n,N=t,L=i;var r=y.createTreeWalker(y.body,NodeFilter.SHOW_TEXT,null,null),o={w:m.innerWidth,h:m.innerHeight,x:m.pageXOffset,y:m.pageYOffset};y.body[c]=e,B.push({w:r,vp:o}),H.push({img:y.images,iter:0}),I.h=z,(I.n=N).h=A,(N.n=B).h=G,(B.n=H).h=J,(H.n=L).h=K,a=I,M()}function z(e){e.m.forEach(function(e){var n=e[i];o in n||(n[o]=e.oldValue)})}function A(n){n.m.forEach(function(e){e[i][c]=n.t-w})}function G(e){for(var n,t=e.vp,i=e.w,r=l;(n=i.nextNode())&&0<r;){r-=1;var o=(n[u]||{}).nodeName;"SCRIPT"!==o&&"STYLE"!==o&&"NOSCRIPT"!==o&&0!==(n.nodeValue||"").trim()[f]&&Z(n[u],Q(n),t)}return!n}function J(e){for(var n,t={w:m.innerWidth,h:m.innerHeight,x:m.pageXOffset,y:m.pageYOffset},i=l;e.iter<e.img[f]&&0<i;){var r=e.img[e.iter];Z(r,U((n=r)[o],n)||U(n.currentSrc,n)||U(n.src,n),t),e.iter+=1,i-=1}return e.img[f]<=e.iter}function K(e){var n=[],i=0,r=0,o=C,t=p(e.y/s),a=E((e.y+m.innerHeight)/s);j.slice(t,a).forEach(function(e){(e.elems||[]).forEach(function(e){e.lt in n||(n[e.lt]={}),e.id in n[e.lt]||(i+=(n[e.lt][e.id]=e).a)})}),S(n).forEach(function(e){S(e).forEach(function(e){var n=1-r/i,t=v(e.lt,o);D+=n*(t-o),o=t,function(e,n){for(;W<=1&&W-.01<=e;)ee("visuallyLoaded"+(100*W).toFixed(0),n),W+=_}((r+=e.a)/i,e.lt)})}),C=e.t-w,L[f]<=1&&(ee("speedIndex",D),ee("visuallyLoaded0",V)),P&&(P=!1,ee("atfSpeedIndex",D))}function Q(e){for(var n=e[u],t=g;n&&0<t;){if(n[c]||0===n[c])return v(n[c],V);n=n.parentElement,t-=1}}function U(e,n){if(e){if(!e.indexOf("data:"))return Q(n);var t=x[r](e)||[];if(0<t[f])return v(E(t[0].responseEnd||0),V)}}function Z(e,n,t){if((n||0===n)&&!e[d]){var i=e.getBoundingClientRect(),r=i.width*i.height,o=i.width/2,a=F++;if(0!=r&&!(o<i.right-t.w||i.right<o)){for(var f={e:e,lt:n,a:r,id:a},u=p((i.top+t.y)/s),c=E((i.top+t.y+i.height)/s),l=u;l<=c;l++)l in j||(j[l]={elems:[],lt:0}),j[l].elems.push(f);e[d]=a}}}function ee(e,n){T("mark",e,w+E(n||0))}function ne(){$||(b("getBuffers",q),$=1)}w&&S&&x[r]&&(b("registerListener",function(e){X&&(clearTimeout(R),R=n(ne,2500))}),t.once("$unload",function(){Y=1,ne()}),t.once("$load",function(){X=1,R=n(ne,2500)}),t.once("$timing:functional",ne))});csa.plugin(function(e){var m=!!e.config["LCP.elementDedup"],t=!1,n=e("PageTiming"),r=e.global.PerformanceObserver,a=e.global.performance;function i(){return a.timing.navigationStart}function o(){t||function(o){var l=new r(function(e){var t=e.getEntries();if(0!==t.length){var n=t[t.length-1];if(m&&""!==n.id&&n.element&&"IMG"===n.element.tagName){for(var r={},a=t[0],i=0;i<t.length;i++)t[i].id in r||(""!==t[i].id&&(r[t[i].id]=!0),a.startTime<t[i].startTime&&(a=t[i]));n=a}l.disconnect(),o({startTime:n.startTime,renderTime:n.renderTime,loadTime:n.loadTime})}});try{l.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}}(function(e){e&&(t=!0,n("mark","largestContentfulPaint",Math.floor(e.startTime+i())),e.renderTime&&n("mark","largestContentfulPaint.render",Math.floor(e.renderTime+i())),e.loadTime&&n("mark","largestContentfulPaint.load",Math.floor(e.loadTime+i())))})}r&&a&&a.timing&&(e.once("$unload",o),e.once("$load",o),e.register("LargestContentfulPaint",{}))});csa.plugin(function(r){var e=r("Metrics",{producerId:"csa"}),n=r.global.PerformanceObserver;n&&(n=new n(function(r){var t=r.getEntries();if(0===t.length||!t[0].processingStart||!t[0].startTime)return;!function(r){r=r||0,n.disconnect(),0<=r?e("recordMetric","firstInputDelay",r):e("recordMetric","firstInputDelay.invalid",1)}(t[0].processingStart-t[0].startTime)}),function(){try{n.observe({type:"first-input",buffered:!0})}catch(r){}}())});csa.plugin(function(d){var e="Metrics",r=d.config,u=r[e+".BatchInterval"]||3e3;function n(e){var r=e.producerId,n=e.logger,t=n||d("Events",{producerId:r}),i={},o=(e||{}).dimensions||{},c=0;if(!r&&!n)return d.error("Either a producer id or custom logger must be defined");function s(){Object.keys(i).length&&(t("log",{schemaId:e.schemaId||"<ns>.Metric.3",metrics:i,dimensions:o},e.logOptions||{ent:{page:["pageType","subPageType","requestId"]}}),i={}),c=0}this.recordMetric=function(e,r){i[e]=r,c=c||d.timeout(s,u)},d.on("$beforeunload",s),d.on("$beforePageTransition",s)}r["KillSwitch."+e]||(new n({producerId:"csa"}).recordMetric("baselineMetricEvent",1),d.register(e,{instance:function(e){return new n(e||{})}}))});csa.plugin(function(c){var e="Timers",r=(c.global.performance||{}).timing,u=(r||{}).navigationStart||c.time(),s=c.config[e+".BatchInterval"]||3e3;function n(e){var r=(e=e||{}).producerId,n=e.logger,o={},t=0,i=n||c("Events",{producerId:r});if(!r&&!n)return c.error("Either a producer id or custom logger must be defined");function a(){0<Object.keys(o).length&&(i("log",{markers:o,schemaId:e.schemaId||"<ns>.Timer.1"},e.logOptions),o={}),clearTimeout(t),t=0}this.mark=function(e,r){o[e]=(void 0===r?c.time():r)-u,t=t||c.timeout(a,s)},c.once("$beforeunload",a),c.once("$beforePageTransition",a)}r&&c.register(e,{instance:function(e){return new n(e||{})}})});csa.plugin(function(t){var e="takeRecords",i="disconnect",n="function",o="removeEventListener",c="click",a=t("Metrics",{producerId:"csa"}),r=t("PageTiming"),u=t.global,f=t.timeout,m=t.on,l=u.PerformanceObserver,s=0,d=!1,v=0,h=u.performance,y=u.document,g=null,p=!1;function T(){d||(d=!0,clearTimeout(g),typeof l[e]===n&&l[e](),typeof l[i]===n&&l[i](),a("recordMetric","documentCumulativeLayoutShift",s),r("mark","cumulativeLayoutShiftLastTimestamp",Math.floor(v+h.timing.navigationStart)))}l&&h&&h.timing&&y&&(l=new l(function(t){g&&clearTimeout(g);t.getEntries().forEach(function(t){t.hadRecentInput||(s+=t.value,v<t.startTime&&(v=t.startTime))}),g=f(T,5e3)}),function(){try{l.observe({type:"layout-shift",buffered:!0}),g=f(T,5e3)}catch(t){}}(),m(y,c,function t(e){p||(p=!0,a("recordMetric","documentCumulativeLayoutShiftToFirstInput",s),y[o](c,t))}),m(y,"visibilitychange",function(){"hidden"===y.visibilityState&&T()}),t.once("$unload",T))});csa.plugin(function(e){var t,n=e.global,r=n.PerformanceObserver,c=e("Metrics",{producerId:"csa"}),o=0,i=0,a=-1,l=n.Math,f=l.max,u=l.ceil;if(r){t=new r(function(e){e.getEntries().forEach(function(e){var t=e.duration;o+=t,i+=t,a=f(t,a)})});try{t.observe({type:"longtask",buffered:!0})}catch(e){}t=new r(function(e){0<e.getEntries().length&&(i=0,a=-1)});try{t.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}e.on("$unload",g),e.on("$beforePageTransition",g)}function g(){c("recordMetric","totalBlockingTime",u(i||0)),c("recordMetric","totalBlockingTimeInclLCP",u(o||0)),c("recordMetric","maxBlockingTime",u(a||0)),i=o=0,a=-1}});csa.plugin(function(r){var e="CacheDetection",o="csa-ctoken-",c=r.store,t=r.deleteStored,n=r.config,a=n[e+".RequestID"],i=n[e+".Callback"],s=n[e+".CDNCacheFix"],u=r.global,d=u.document||{},f=u.Date,l=r("Events"),p=r("Events",{producerId:"csa"});function v(e){try{var c=d.cookie.match(RegExp("(^| )"+e+"=([^;]+)"));return c&&c[2].trim()}catch(e){}}!function(){var e=function(){var e=v("cdn-rid");if(e)return{r:e,s:"cdn"}}()||function(){if(r.store(o+a))return{r:r.UUID().toUpperCase().replace(/-/g,"").slice(0,20),s:"device"}}()||{},c=e.r,n=e.s;if(!!c){var t=v("session-id");!function(e,c,n,t){l("setEntity",{page:{pageSource:"cache",requestId:e,cacheRequestId:a,cacheSource:t},session:{id:n}})}(c,0,t,n),s&&"device"!==n||p("log",{schemaId:"<ns>.CacheImpression.1"},{ent:"all"}),i&&i(c,t,n)}}(),c(o+a,f.now()+36e5),r.once("$load",function(){var n=f.now();t(function(e,c){return 0==e.indexOf(o)&&parseInt(c)<n})})});csa.plugin(function(u){var i,t="Content",e="MutationObserver",n="addedNodes",a="querySelectorAll",s="matches",r="getAttributeNames",o="getAttribute",f="dataset",c="widget",l="producerId",d={ent:{element:1,page:["pageType","subPageType","requestId"]}},h=5,g=u.config[t+".BubbleUp.SearchDepth"]||20,m="csaC",p=m+"Id",y={},v=u.config,b=v[t+".Selectors"]||[],E=v[t+".WhitelistedAttributes"]||{href:1,class:1},I=v[t+".EnableContentEntities"],w=u.global,C=w.document||{},A=C.documentElement,U=w.HTMLElement,k={},L=[],N=function(t,e,n,i){var r=this,o=u("Events",{producerId:t||"csa"});e.type=e.type||c,r.id=e.id,r.l=o,r.e=e,r.el=n,r.rt=i,r.dlo=d,r.log=function(t,e){o("log",t,e||d)},e.id&&o("setEntity",{element:e})},O=N.prototype;function D(t){var e=(t=t||{}).element,n=t.target;return e?function(t,e){var n;n=t instanceof U?B(t)||$(e[l],t,H,u.time()):k[t.id]||_(e[l],0,t,u.time());return n}(e,t):n?S(n):u.error("No element or target argument provided.")}function S(t){var e=function(t){var e=null,n=0;for(;t&&n<g;){if(n++,T(t,p)){e=t;break}t=t.parentElement}return e}(t);return e?B(e):new N("csa",{id:null},null,u.time())}function T(t,e){if(t&&t.dataset)return t.dataset[e]}function j(t,e,n){L.push({n:n,e:t,t:e}),x()}function q(){for(var t=u.time(),e=0;0<L.length;){var n=L.shift();if(y[n.n](n.e,n.t),++e%10==0&&u.time()-t>h)break}i=0,L.length&&x()}function x(){i=i||u.raf(q)}function M(t,e,n){return{n:t,e:e,t:n}}function $(t,e,n,i){var r=u.UUID(),o={id:r},c=S(e);return e[f][p]=r,n(o,e),c.id&&(o.parentId=c.id),_(t,e,o,i)}function _(t,e,n,i){I&&(n.schemaId="<ns>.ContentEntity.2"),n.id=n.id||u.UUID();var r=new N(t,n,e,i);return I&&r.log({schemaId:"<ns>.ContentRender.1",timestamp:i}),u.emit("$content.register",r),k[n.id]=r}function B(t){return k[(t[f]||{})[p]]}function H(t,e){r in e&&(function(n,i){Object.keys(n[f]).forEach(function(t){if(!t.indexOf(m)&&m.length<t.length){var e=function(t){return(t[0]||"").toLowerCase()+t.slice(1)}(t.slice(m.length));i[e]=n[f][t]}})}(e,t),function(e,n){(e[r]()||[]).forEach(function(t){t in E&&(n[t]=e[o](t))})}(e,t))}A&&C[a]&&w[e]&&(b.push({selector:"*[data-csa-c-type]",entity:H}),b.push({selector:".celwidget",entity:function(t,e){H(t,e),t.slotId=t.slotId||e[o]("cel_widget_id")||e.id,t.type=t.type||c}}),y[1]=function(t,e){t.forEach(function(t){t[n]&&t[n].constructor&&"NodeList"===t[n].constructor.name&&Array.prototype.forEach.call(t[n],function(t){L.unshift(M(2,t,e))})})},y[2]=function(o,c){a in o&&s in o&&b.forEach(function(t){for(var e=t.selector,n=o[s](e),i=o[a](e),r=i.length-1;0<=r;r--)L.unshift(M(3,{e:i[r],s:t},c));n&&L.unshift(M(3,{e:o,s:t},c))})},y[3]=function(t,e){var n=t.e;B(n)||$("csa",n,t.s.entity,e)},y[4]=function(){u.register(t,{instance:D})},new w[e](function(t){j(t,u.time(),1)}).observe(A,{childList:!0,subtree:!0}),j(A,u.time(),2),j(null,u.time(),4),u.on("$content.export",function(e){Object.keys(e).forEach(function(t){O[t]=e[t]})}))});csa.plugin(function(n){var i,t="ContentImpressions",e="KillSwitch.",o="IntersectionObserver",r="getAttribute",s="dataset",c="intersectionRatio",a="csaCId",m=1e3,l=n.global,f=n.config,u=f[e+t],g=f[e+t+".ContentViews"],v=((l.performance||{}).timing||{}).navigationStart||n.time(),d={};function h(t){t&&(t.v=1,function(t){t.vt=n.time(),t.el.log({schemaId:"<ns>.ContentView.3",timeToViewed:t.vt-t.el.rt,pageFirstPaintToElementViewed:t.vt-v})}(t))}function I(t){t&&!t.it&&(t.i=n.time()-t.is>m,function(t){t.it=n.time(),t.el.log({schemaId:"<ns>.ContentImpressed.2",timeToImpressed:t.it-t.el.rt,pageFirstPaintToElementImpressed:t.it-v})}(t))}!u&&l[o]&&(i=new l[o](function(t){t.forEach(function(t){var e=function(t){if(t&&t[r])return d[t[s][a]]}(t.target);if(e){var i=t.intersectionRect;t.isIntersecting&&0<i.width&&0<i.height&&(g||e.v||h(e),.5<=t[c]&&!e.is&&(e.is=n.time(),e.timer=n.timeout(function(){I(e)},m))),t[c]<.5&&!e.it&&e.timer&&(l.clearTimeout(e.timer),e.is=0,e.timer=0)}})},{threshold:[0,.5]}),n.on("$content.register",function(t){var e=t.el;e&&(d[t.id]={el:t,v:0,i:0,is:0,vt:0,it:0},i.observe(e))}))});csa.plugin(function(e){e.config["KillSwitch.ContentLatency"]||e.emit("$content.export",{mark:function(t,n){var o=this;o.t||(o.t=e("Timers",{logger:o.l,schemaId:"<ns>.ContentLatency.1",logOptions:o.dlo})),o.t("mark",t,n)}})});csa.plugin(function(d){var t,i="normal",s="reload",n="history",o="new-tab",e="ajax",a=1,r=2,c="lastActive",u="lastInteraction",l="used",f="csa-tabbed-browsing",p="visibilityState",g={"back-memory-cache":1,"tab-switch":1,"history-navigation-page-cache":1},v="<ns>.TabbedBrowsing.2",b="visible",m=d.global,y=d("Events",{producerId:"csa"}),I=m.location||{},h=m.document,T=m.JSON,w=((m.performance||{}).navigation||{}).type,z=d.store,P=d.on,S=d.storageSupport(),k=!1,x={},A={},C={},O={},$=!1,j=!1,q=!1;function B(i){try{return T.parse(z(f,void 0,{session:i})||"{}")||{}}catch(i){d.error('Could not parse storage value for key "'+f+'": '+i)}return{}}function E(i,t){z(f,T.stringify(t||{}),{session:i})}function J(i){var t=A.tid||i.id,n=x[c]||{};n.tid===t&&(n.pid=i.id),O={pid:i.id,tid:t,lastInteraction:A[u]||{},initialized:!0},C={lastActive:n,lastInteraction:x[u]||{},time:d.time()}}function N(i){var t=i===o,n=h.referrer,e=!(n&&n.length)||!~n.indexOf(I.origin||""),a=t&&e,r={type:i,toTabId:O.tid,toPageId:O.pid,transitTime:d.time()-x.time||null};a||function(i,t,n){var e=i===s,a=t?x[c]||{}:A,r=x[u]||{},d=A[u]||{},o=t?r:d;n.fromTabId=a.tid,n.fromPageId=a.pid,e||!o.id||o[l]||(n.interactionId=o.id||null,r.id===o.id&&(r[l]=!0),d.id===o.id&&(d[l]=!0))}(i,t,r),y("log",{navigation:r,schemaId:v},{ent:{page:["pageType","subPageType","requestId"]}})}function D(i){q=function(i){return i&&i in g}(i.transitionType),function(){x=B(!1),A=B(!0);var i=x[u],t=A[u],n=!1,e=!1;i&&t&&i.id===t.id&&i[l]!==t[l]&&(n=!i[l],e=!t[l],t[l]=i[l]=!0,n&&E(!1,x),e&&E(!0,A))}(),J(i),$=!0,function(i){var t,n;t=G(),n=H(),(t||n)&&J(i)}(i)}function F(){k&&!q?N(e):(k=!0,N(w===r||q?n:w===a?A.initialized?s:o:A.initialized?i:o))}function G(){return!(!$||!t)&&(A[u]={id:t.messageId,used:!(x[u]={id:t.messageId,used:!1})},!(t=null))}function H(){var i=!1;if(j=h[p]===b,$){var t=x[c]||{};i=function(i,t,n){var e=!1,a=i[c];return j?a&&a.tid===O.tid&&a[b]&&a.pid===n||(i[c]={visible:!0,pid:n,tid:t},e=!0):a&&a.tid===O.tid&&a[b]&&(e=!(a[b]=!1)),e}(x,A.tid||t.tid||O.tid,A.pid||t.pid||O.pid)}return i}S.local&&S.session&&T&&h&&p in h&&(P("$pageChange",function(i){D(i),F(),E(!1,C),E(!0,O),A=O,x=C},{buffered:1}),P("$content.interaction",function(i){t=i,G()&&(E(!1,x),E(!0,A))}),P(h,"visibilitychange",function(){H()&&E(!1,x)},{capture:!1,passive:!0}))});csa.plugin(function(c){var e=c("Metrics",{producerId:"csa"});c.on(c.global,"pageshow",function(c){c&&c.persisted&&e("recordMetric","bfCache",1)})});
if (window.ue && window.ue.uels) {
    ue.uels("https://c.amazon-adsystem.com/bao-csm/forensics/a9-tq-forensics-incremental.min.js");
}


}
/* ◬ */
</script>

</div>

<noscript>
    <img height="1" width="1" style='display:none;visibility:hidden;' src='//fls-na.amazon.ca/1/batch/1/OP/A2EUQ1WTGCTBG2:138-4669640-7712440:1KMDY2JPGP2X3R80G8WC$uedata=s:%2Frd%2Fuedata%3Fnoscript%26id%3D1KMDY2JPGP2X3R80G8WC:0' alt=""/>
</noscript>

<script>window.ue && ue.count && ue.count('CSMLibrarySize', 53698)</script>
</div></body></html>
<!--       _
       .__(.)< (MEOW)
        \___)   
 ~~~~~~~~~~~~~~~~~~-->
<!-- sp:eh:0LtDFb+vPVj6+WhVYoUWQ1Cxx3XwETZIJQWYi4PN1aX0ISiYWFV72n/juIEPPxslB1x1r9VhNEBtzxvKflaYjtOiGplgckQ0YvQ0cPUN+j+6FqOVntYGxg== -->
"""

soup = BeautifulSoup(html_doc, 'html.parser')
webview.create_window("soup", html=soup.prettify())
webview.start()
