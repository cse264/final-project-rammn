(function(){"use strict";var e={8754:function(e,t,n){var r=n(9963),i=n(6252);function o(e,t){const n=(0,i.up)("router-view");return(0,i.wg)(),(0,i.j4)(n)}var a=n(3744);const l={},c=(0,a.Z)(l,[["render",o]]);var u=c,s=n(2119);const d={class:"wrapper d-flex flex-column min-vh-100 bg-light"},f={class:"body flex-grow-1 px-3"};function p(e,t,n,r,o,a){const l=(0,i.up)("AppHeader"),c=(0,i.up)("router-view"),u=(0,i.up)("CContainer"),s=(0,i.up)("AppFooter");return(0,i.wg)(),(0,i.iD)("div",null,[(0,i._)("div",d,[(0,i.Wm)(l),(0,i._)("div",f,[(0,i.Wm)(u,{lg:""},{default:(0,i.w5)((()=>[(0,i.Wm)(c)])),_:1})]),(0,i.Wm)(s)])])}var m=n(8549),b=n(3577);const v=(0,i._)("a",{href:"https://github.com/cse264/final-project-rammn",target:"_blank"},"Boredle",-1),h={class:"ms-1"},g=(0,i._)("div",{class:"ms-auto"},[(0,i._)("span",{class:"me-1",target:"_blank"},"Project for"),(0,i._)("a",{href:"https://www.lehigh.edu/",target:"_blank"},"Lehigh University")],-1);function w(e,t,n,r,o,a){const l=(0,i.up)("CFooter");return(0,i.wg)(),(0,i.j4)(l,null,{default:(0,i.w5)((()=>[(0,i._)("div",null,[v,(0,i._)("span",h,"© "+(0,b.zw)((new Date).getFullYear())+" RAMMN",1)]),g])),_:1})}var C={name:"AppFooter"};const _=(0,a.Z)(C,[["render",w]]);var k=_;const y=(0,i.Uk)("Search"),W=(0,i.Uk)("Login"),j=(0,i.Uk)("Profile"),A=(0,i.Uk)("Dashboard");function S(e,t,n,r,o,a){const l=(0,i.up)("CImage"),c=(0,i.up)("CNavbarBrand"),u=(0,i.up)("CNavLink"),s=(0,i.up)("CNavItem"),d=(0,i.up)("CHeaderNav"),f=(0,i.up)("CContainer"),p=(0,i.up)("CHeaderDivider"),m=(0,i.up)("AppBreadcrumb"),b=(0,i.up)("CHeader");return(0,i.wg)(),(0,i.j4)(b,{position:"sticky",class:"mb-4"},{default:(0,i.w5)((()=>[(0,i.Wm)(f,{fluid:""},{default:(0,i.w5)((()=>[(0,i.Wm)(c,{href:"#"},{default:(0,i.w5)((()=>[(0,i.Wm)(l,{src:r.logo,height:"50"},null,8,["src"])])),_:1}),(0,i.Wm)(d,{class:"d-none d-md-flex me-auto"},{default:(0,i.w5)((()=>[(0,i.Wm)(s,null,{default:(0,i.w5)((()=>[(0,i.Wm)(u,{href:"#/search"},{default:(0,i.w5)((()=>[y])),_:1})])),_:1}),(0,i.Wm)(s,null,{default:(0,i.w5)((()=>[(0,i.Wm)(u,{href:"#/login"},{default:(0,i.w5)((()=>[W])),_:1})])),_:1}),(0,i.Wm)(s,null,{default:(0,i.w5)((()=>[(0,i.Wm)(u,{href:"#/profile"},{default:(0,i.w5)((()=>[j])),_:1})])),_:1}),(0,i.Wm)(s,null,{default:(0,i.w5)((()=>[(0,i.Wm)(u,{href:"#/dashboard"},{default:(0,i.w5)((()=>[A])),_:1})])),_:1})])),_:1})])),_:1}),(0,i.Wm)(p),(0,i.Wm)(f,{fluid:""},{default:(0,i.w5)((()=>[(0,i.Wm)(m)])),_:1})])),_:1})}function U(e,t,n,r,o,a){const l=(0,i.up)("CBreadcrumbItem"),c=(0,i.up)("CBreadcrumb");return(0,i.wg)(),(0,i.j4)(c,{class:"d-md-down-none me-auto mb-0"},{default:(0,i.w5)((()=>[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(r.breadcrumbs,(e=>((0,i.wg)(),(0,i.j4)(l,{key:e,href:e.active?"":e.path,active:e.active},{default:(0,i.w5)((()=>[(0,i.Uk)((0,b.zw)(e.name),1)])),_:2},1032,["href","active"])))),128))])),_:1})}var P=n(2262),B={name:"AppBreadcrumb",setup(){const e=(0,P.iH)(),t=()=>V.currentRoute.value.matched.map((e=>({active:e.path===V.currentRoute.value.fullPath,name:e.name,path:`${V.options.history.base}${e.path}`})));return V.afterEach((()=>{e.value=t()})),(0,i.bv)((()=>{e.value=t()})),{breadcrumbs:e}}};const D=(0,a.Z)(B,[["render",U]]);var L=D,O=n.p+"../static/img/logo.acea44e2.png",E={name:"AppHeader",components:{AppBreadcrumb:L},setup(){return{logo:O}}};const T=(0,a.Z)(E,[["render",S]]);var N=T,x={name:"DefaultLayout",components:{AppFooter:k,AppHeader:N,CContainer:m.KB}};const F=(0,a.Z)(x,[["render",p]]);var I=F;const M=[{path:"/",name:"Home",component:I,redirect:"/search",children:[{path:"/search",name:"Search",component:()=>n.e(17).then(n.bind(n,2017))},{path:"/dashboard",name:"Dashboard",component:()=>n.e(336).then(n.bind(n,3336))},{path:"/login",name:"Login",component:()=>n.e(874).then(n.bind(n,874))},{path:"/profile",name:"Profile",component:()=>n.e(302).then(n.bind(n,9302))}]}],$=(0,s.p7)({history:(0,s.r5)("/"),routes:M,scrollBehavior(){return{top:0}}});var V=$,H=n(3907),Z=(0,H.MT)({state:{sidebarVisible:"",sidebarUnfoldable:!1},mutations:{toggleSidebar(e){e.sidebarVisible=!e.sidebarVisible},toggleUnfoldable(e){e.sidebarUnfoldable=!e.sidebarUnfoldable},updateSidebarVisible(e,t){e.sidebarVisible=t.value}},actions:{},modules:{}}),q=n(3075),z=n(7959),Y=n(7168),G=n(1780),R=n(2037),J=n(3221),K=n(5752),Q=n(6863),X=n(5604),ee=n(3074),te=n(9176),ne=n(5981),re=n(3365),ie=n(4556),oe=n(9101),ae=n(1069),le=n(207),ce=n(4485),ue=n(584),se=n(6399),de=n(7628),fe=n(7224),pe=n(4162),me=n(9692),be=n(5520),ve=n(5724),he=n(5987),ge=n(3958),we=n(7993),Ce=n(8450),_e=n(7271),ke=n(3591),ye=n(7741),We=n(6864),je=n(9885),Ae=n(7272),Se=n(2992),Ue=n(1939),Pe=n(1861),Be=n(6155),De=n(1797),Le=n(8081),Oe=n(4442),Ee=n(7246),Te=n(3918),Ne=n(2814),xe=n(484),Fe=n(452),Ie=n(6667),Me=n(7494),$e=n(8008),Ve=n(1232),He=n(6705),Ze=n(4147),qe=n(4648),ze=n(5307),Ye=n(4165),Ge=n(1902),Re=n(9555),Je=n(7923),Ke=n(185),Qe=n(5365),Xe=n(8231),et=n(5737),tt=n(8332),nt=n(3238),rt=n(3644),it=n(8142),ot=n(7482),at=n(6401),lt=n(2569),ct=n(9974),ut=n(1059),st=n(5850),dt=n(6442),ft=n(9020),pt=n(1678),mt=n(4309),bt=n(3989),vt=n(4321),ht=n(4365),gt=n(5618);const wt=Object.assign({},{cilArrowBottom:ke.t,cilArrowRight:ye.n,cilArrowTop:We.T,cilBan:je.E,cilBasket:Ae.o,cilBell:Se.$,cilCalculator:Ue.o,cilCalendar:Pe.J,cilCloudDownload:Be.j,cilChartPie:De.M,cilCheck:Le.J,cilChevronBottom:Oe.b,cilChevronTop:Ee.V,cilCheckCircle:Te._,cilCode:Ne.I,cilCommentSquare:xe.S,cilCursor:Fe.t,cilDrop:Ie.M,cilDollar:Me.T,cilEnvelopeClosed:$e.W,cilEnvelopeOpen:Ve.m,cilEuro:He.z,cilGlobeAlt:Ze.e,cilGrid:qe.x,cilFile:ze.D,cilJustifyCenter:Ye.h,cilLaptop:Ge.U,cilLayers:Re.H,cilLightbulb:Je.O,cilList:Ke.A,cilLocationPin:Qe.i,cilLockLocked:Xe.U,cilMagnifyingGlass:et.M,cilMediaPlay:tt.B,cilMenu:nt.N,cilMoon:rt.S,cilNotes:it.E,cilOptions:ot.t,cilPencil:at.l,cilPeople:lt.g,cilPuzzle:ct.Q,cilSettings:ut.M,cilShieldAlt:st.t,cilSpeech:dt.B,cilSpeedometer:ft.h,cilStar:pt.m,cilTask:mt.W,cilUser:bt.E,cilUserFemale:vt.Q,cilUserFollow:ht.H,cilXCircle:gt.J},{cifUs:ve.E,cifBr:he.N,cifIn:ge.J,cifFr:we.A,cifEs:Ce.z,cifPl:_e.I},{cibFacebook:z.t,cibTwitter:Y._,cibLinkedin:G.n,cibFlickr:R.r,cibTumblr:J.i,cibXing:K.n,cibGithub:Q.G,cibGoogle:X.N,cibStackoverflow:ee.F,cibYoutube:te.N,cibDribbble:ne.x,cibInstagram:re.d,cibPinterest:ie.p,cibVk:oe.o,cibYahoo:ae.s,cibBehance:le.n,cibReddit:ce.m,cibVimeo:ue.R,cibCcMastercard:se.y,cibCcVisa:de.W,cibCcStripe:fe.I,cibCcPaypal:pe.K,cibCcApplePay:me.D,cibCcAmex:be.I}),Ct=(0,i._)("br",null,null,-1),_t=(0,i._)("br",null,null,-1),kt=(0,i.Uk)(" For more information please visit our official "),yt=(0,i.Uk)(" documentation of CoreUI Components Library for Vue.js "),Wt=(0,i.Uk)(" . ");function jt(e,t,n,r,o,a){const l=(0,i.up)("CLink"),c=(0,i.up)("CCallout");return(0,i.wg)(),(0,i.j4)(c,{color:"info",class:"bg-white"},{default:(0,i.w5)((()=>[(0,i.Uk)((0,b.zw)(n.content?n.content:`A Vue ${n.name} component ${n.plural?"have":"has"} been created as a native Vue.js version\n      of Bootstrap ${n.name}. ${n.name} ${n.plural?"are":"is"} delivered with some new features,\n      variants, and unique design that matches CoreUI Design System requirements.`)+" ",1),Ct,_t,kt,(0,i.Wm)(l,{href:r.url,target:"_blank"},{default:(0,i.w5)((()=>[yt])),_:1},8,["href"]),Wt])),_:1})}var At={vc:{Y:"4.1"}},St={name:"DocsCallout",props:{content:{type:String,default:void 0,required:!1},href:{type:String,default:void 0,required:!1},name:{type:String,default:void 0,required:!1},plural:Boolean},setup(e){const t=`https://coreui.io/vue/docs/${At.vc.Y}/${e.url}`;return{url:t}}};const Ut=(0,a.Z)(St,[["render",jt]]);var Pt=Ut;const Bt={class:"example"},Dt=(0,i.Uk)(" Code ");function Lt(e,t,n,r,o,a){const l=(0,i.up)("CIcon"),c=(0,i.up)("CNavLink"),u=(0,i.up)("CNavItem"),s=(0,i.up)("CNav"),d=(0,i.up)("CTabPane"),f=(0,i.up)("CTabContent");return(0,i.wg)(),(0,i.iD)("div",Bt,[(0,i.Wm)(s,{variant:"tabs"},{default:(0,i.w5)((()=>[(0,i.Wm)(u,null,{default:(0,i.w5)((()=>[(0,i.Wm)(c,{href:"#",active:""},{default:(0,i.w5)((()=>[(0,i.Wm)(l,{icon:"cil-media-play",class:"me-2"})])),_:1})])),_:1}),(0,i.Wm)(u,null,{default:(0,i.w5)((()=>[(0,i.Wm)(c,{href:r.url,target:"_blank"},{default:(0,i.w5)((()=>[(0,i.Wm)(l,{icon:"cil-code",class:"me-2"}),Dt])),_:1},8,["href"])])),_:1})])),_:1}),(0,i.Wm)(f,{class:"rounded-bottom"},{default:(0,i.w5)((()=>[(0,i.Wm)(d,{class:"p-3 preview",visible:""},{default:(0,i.w5)((()=>[(0,i.WI)(e.$slots,"default")])),_:3})])),_:3})])}var Ot={name:"DocsExample",props:{href:{type:String,default:void 0,required:!1}},setup(e){const t=`https://coreui.io/vue/docs/${At.vc.Y}/${e.href}`;return{url:t}}};const Et=(0,a.Z)(Ot,[["render",Lt]]);var Tt=Et;const Nt=(0,r.ri)(u);Nt.use(Z),Nt.use(V),Nt.use(m.ZP),Nt.provide("icons",wt),Nt.component("CIcon",q.Z),Nt.component("DocsCallout",Pt),Nt.component("DocsExample",Tt),Nt.mount("#app")}},t={};function n(r){var i=t[r];if(void 0!==i)return i.exports;var o=t[r]={exports:{}};return e[r](o,o.exports,n),o.exports}n.m=e,function(){var e=[];n.O=function(t,r,i,o){if(!r){var a=1/0;for(s=0;s<e.length;s++){r=e[s][0],i=e[s][1],o=e[s][2];for(var l=!0,c=0;c<r.length;c++)(!1&o||a>=o)&&Object.keys(n.O).every((function(e){return n.O[e](r[c])}))?r.splice(c--,1):(l=!1,o<a&&(a=o));if(l){e.splice(s--,1);var u=i();void 0!==u&&(t=u)}}return t}o=o||0;for(var s=e.length;s>0&&e[s-1][2]>o;s--)e[s]=e[s-1];e[s]=[r,i,o]}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,r){return n.f[r](e,t),t}),[]))}}(),function(){n.u=function(e){return"../static/js/"+e+"."+{17:"1a861b7a",302:"ed88786f",336:"e20dee6c",874:"7d641fee"}[e]+".js"}}(),function(){n.miniCssF=function(e){}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="@coreui/coreui-free-vue-admin-template:";n.l=function(r,i,o,a){if(e[r])e[r].push(i);else{var l,c;if(void 0!==o)for(var u=document.getElementsByTagName("script"),s=0;s<u.length;s++){var d=u[s];if(d.getAttribute("src")==r||d.getAttribute("data-webpack")==t+o){l=d;break}}l||(c=!0,l=document.createElement("script"),l.charset="utf-8",l.timeout=120,n.nc&&l.setAttribute("nonce",n.nc),l.setAttribute("data-webpack",t+o),l.src=r),e[r]=[i];var f=function(t,n){l.onerror=l.onload=null,clearTimeout(p);var i=e[r];if(delete e[r],l.parentNode&&l.parentNode.removeChild(l),i&&i.forEach((function(e){return e(n)})),t)return t(n)},p=setTimeout(f.bind(null,void 0,{type:"timeout",target:l}),12e4);l.onerror=f.bind(null,l.onerror),l.onload=f.bind(null,l.onload),c&&document.head.appendChild(l)}}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p="/"}(),function(){var e={143:0};n.f.j=function(t,r){var i=n.o(e,t)?e[t]:void 0;if(0!==i)if(i)r.push(i[2]);else{var o=new Promise((function(n,r){i=e[t]=[n,r]}));r.push(i[2]=o);var a=n.p+n.u(t),l=new Error,c=function(r){if(n.o(e,t)&&(i=e[t],0!==i&&(e[t]=void 0),i)){var o=r&&("load"===r.type?"missing":r.type),a=r&&r.target&&r.target.src;l.message="Loading chunk "+t+" failed.\n("+o+": "+a+")",l.name="ChunkLoadError",l.type=o,l.request=a,i[1](l)}};n.l(a,c,"chunk-"+t,t)}},n.O.j=function(t){return 0===e[t]};var t=function(t,r){var i,o,a=r[0],l=r[1],c=r[2],u=0;if(a.some((function(t){return 0!==e[t]}))){for(i in l)n.o(l,i)&&(n.m[i]=l[i]);if(c)var s=c(n)}for(t&&t(r);u<a.length;u++)o=a[u],n.o(e,o)&&e[o]&&e[o][0](),e[o]=0;return n.O(s)},r=self["webpackChunk_coreui_coreui_free_vue_admin_template"]=self["webpackChunk_coreui_coreui_free_vue_admin_template"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(8754)}));r=n.O(r)})();
//# sourceMappingURL=app.963600bd.js.map