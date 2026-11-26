/*I18N_RUNTIME*/
/* Chinese UI for Claude AppStore apps. When the viewer's language is Chinese, UI text nodes and
   placeholder/title/aria-label attributes whose text is in DICT are swapped for Chinese, including
   UI added later (menus, toasts, dialogs). User content is never touched: anything inside SKIP. */
(()=>{
  let ZH=/^zh/i.test(navigator.language||"");
  try{const o=localStorage.getItem("appstore.lang");if(o==="en")ZH=false;else if(o==="zh")ZH=true}catch{}
  window.__ZH=ZH; window.__t=(en,zh)=>ZH?zh:en;
  if(!ZH)return;
  const DICT=/*I18N_DICT*/{}/*END_I18N_DICT*/;
  const PATTERNS=(/*I18N_PATTERNS*/[]/*END_I18N_PATTERNS*/).map(([re,rep])=>[new RegExp("^"+re+"$"),rep]);
  const SKIP='script,style,textarea,input,code,pre,[contenteditable]:not([contenteditable="false"]),[data-no-i18n]'+(/*I18N_SKIP*/""/*END_I18N_SKIP*/);
  const ATTRS=["placeholder","title","aria-label","data-tip","data-ph","alt"];
  const norm=s=>s.replace(/\s+/g," ").trim();
  function tr(s){
    const k=norm(s); if(!k||!/[A-Za-z]/.test(k)) return null;
    let v=DICT[k];
    if(v==null){for(const [re,rep] of PATTERNS){if(re.test(k)){v=k.replace(re,rep);break}}}
    if(v==null||v===k) return null;
    const lead=s.match(/^\s*/)[0], tail=s.match(/\s*$/)[0];
    return lead+v+tail;
  }
  window.__tr=s=>tr(String(s))??s;
  const skipped=el=>{try{return !!(el&&el.closest&&el.closest(SKIP))}catch{return false}};
  function doText(n){const p=n.parentElement;if(!p||skipped(p))return;const v=tr(n.nodeValue);if(v!=null)n.nodeValue=v}
  function doAttrs(el){if(el.nodeType!==1)return;for(const a of ATTRS){const x=el.getAttribute(a);if(!x)continue;if(a==="data-ph"||a==="alt"){if(skipped(el.parentElement))continue}const v=tr(x);if(v!=null)el.setAttribute(a,v)}}
  function walk(root){
    if(root.nodeType===3){doText(root);return}
    if(root.nodeType!==1&&root.nodeType!==11)return;
    if(root.nodeType===1){doAttrs(root);if(skipped(root))return}
    const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT|NodeFilter.SHOW_ELEMENT,{acceptNode(n){
      if(n.nodeType===1){doAttrs(n);return skipped(n)?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_SKIP}
      return NodeFilter.FILTER_ACCEPT}});
    let n;while((n=w.nextNode()))doText(n);
  }
  const mo=new MutationObserver(ms=>{for(const m of ms){
    if(m.type==="childList")m.addedNodes.forEach(walk);
    else if(m.type==="characterData")doText(m.target);
    else if(m.type==="attributes")doAttrs(m.target);
  }});
  const start=()=>{document.documentElement.lang="zh-CN";const t=tr(document.title||"");if(t)document.title=t;walk(document.body);
    mo.observe(document.body,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:ATTRS})};
  if(document.body)start();else document.addEventListener("DOMContentLoaded",start);
  const _a=window.alert,_c=window.confirm,_p=window.prompt;
  window.alert=m=>_a.call(window,tr(String(m))??m);window.confirm=m=>_c.call(window,tr(String(m))??m);window.prompt=(m,d)=>_p.call(window,tr(String(m))??m,d);
})();
/*END_I18N_RUNTIME*/
