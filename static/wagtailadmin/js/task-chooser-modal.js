(()=>{"use strict";var t,e={8432:function(t,e,r){var a=this&&this.__importDefault||function(t){return t&&t.__esModule?t:{default:t}};e.__esModule=!0;var o=a(r(5311)),n=r(5781),i=function(t,e){(0,o.default)("#tab-new a.task-type-choice, #tab-new a.choose-different-task-type",t.body).on("click",(function(){return t.loadUrl(this.href),!1})),(0,o.default)("form.task-create",t.body).on("submit",(function(){var r=new FormData(this);return o.default.ajax({url:this.action,data:r,processData:!1,contentType:!1,type:"POST",dataType:"text",success:t.loadResponseText,error:function(r,a,n){var i=e.error_message+"<br />"+n+" - "+r.status;(0,o.default)("#tab-new",t.body).append('<div class="help-block help-critical"><strong>'+e.error_label+": </strong>"+i+"</div>")}}),!1}))},u={chooser:function(t,e){function r(e){(0,o.default)("a.task-choice",e).on("click",(function(){return t.loadUrl(this.href),!1})),(0,o.default)(".pagination a",e).on("click",(function(){return s(this.href),!1})),(0,n.initTabs)()}var a,u=(0,o.default)("form.task-search",t.body),l=u.attr("action");function s(t,e){var n={url:t,success:function(t){a=null,(0,o.default)("#search-results").html(t),r((0,o.default)("#search-results"))},error:function(){a=null}};e&&(n.data=e),a=o.default.ajax(n)}function c(){return s(l,u.serialize()),!1}r(t.body),i(t,e),(0,o.default)("form.task-search",t.body).on("submit",c),(0,o.default)("#id_q").on("input",(function(){a&&a.abort(),clearTimeout(o.default.data(this,"timer"));var t=setTimeout(c,50);(0,o.default)(this).data("timer",t)})),(0,o.default)("#id_task_type").on("change",(function(){a&&a.abort(),clearTimeout(o.default.data(this,"timer"));var t=setTimeout(c,50);(0,o.default)(this).data("timer",t)}))},task_chosen:function(t,e){t.respond("taskChosen",e.result),t.close()},reshow_create_tab:function(t,e){(0,o.default)("#tab-new",t.body).html(e.htmlFragment),i(t,e)}};window.TASK_CHOOSER_MODAL_ONLOAD_HANDLERS=u},5311:t=>{t.exports=jQuery}},r={};function a(t){var o=r[t];if(void 0!==o)return o.exports;var n=r[t]={exports:{}};return e[t].call(n.exports,n,n.exports,a),n.exports}a.m=e,t=[],a.O=(e,r,o,n)=>{if(!r){var i=1/0;for(c=0;c<t.length;c++){for(var[r,o,n]=t[c],u=!0,l=0;l<r.length;l++)(!1&n||i>=n)&&Object.keys(a.O).every((t=>a.O[t](r[l])))?r.splice(l--,1):(u=!1,n<i&&(i=n));if(u){t.splice(c--,1);var s=o();void 0!==s&&(e=s)}}return e}n=n||0;for(var c=t.length;c>0&&t[c-1][2]>n;c--)t[c]=t[c-1];t[c]=[r,o,n]},a.n=t=>{var e=t&&t.__esModule?()=>t.default:()=>t;return a.d(e,{a:e}),e},a.d=(t,e)=>{for(var r in e)a.o(e,r)&&!a.o(t,r)&&Object.defineProperty(t,r,{enumerable:!0,get:e[r]})},a.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"==typeof window)return window}}(),a.o=(t,e)=>Object.prototype.hasOwnProperty.call(t,e),a.r=t=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},a.j=342,(()=>{var t={342:0};a.O.j=e=>0===t[e];var e=(e,r)=>{var o,n,[i,u,l]=r,s=0;if(i.some((e=>0!==t[e]))){for(o in u)a.o(u,o)&&(a.m[o]=u[o]);if(l)var c=l(a)}for(e&&e(r);s<i.length;s++)n=i[s],a.o(t,n)&&t[n]&&t[n][0](),t[n]=0;return a.O(c)},r=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];r.forEach(e.bind(null,0)),r.push=e.bind(null,r.push.bind(r))})();var o=a.O(void 0,[2751],(()=>a(8432)));o=a.O(o)})();