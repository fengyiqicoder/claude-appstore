/*INSTALL_PROMPT*/
/* When this artifact is open in Claude Desktop but not installed as an app yet, invite the person
   to install it. Shows once per session; the install itself is Claude's own dialog, started from
   the person's click (install.request() needs a click). Silent in browsers, on mobile and inside the
   installed app. */
(async()=>{
  if(!window.claude||!claude.use)return;
  try{if(sessionStorage.getItem("appstore.installAsked"))return}catch{}
  const d=await claude.use("desktop").catch(()=>null);
  if(!d||d.fs||!d.install)return;                       // d.fs exists only inside the installed app
  const st=await d.install.state().catch(()=>"unavailable");
  if(st!=="available")return;
  await new Promise(r=>setTimeout(r,900));
  if(document.querySelector(".aspi"))return;
  const zh=window.__ZH??/^zh/i.test(navigator.language||"");
  const T=(en,c)=>zh?c:en;
  const name=(document.title||"").trim()||T("this app","这个 app");
  const icon=typeof DOCK_SVG==="string"?DOCK_SVG:(typeof ICON_SVG==="object"&&ICON_SVG.store)||"";
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const st2=document.createElement("style");
  st2.textContent=`.aspi{position:fixed;inset:0;z-index:2147483000;display:grid;place-items:center;background:rgba(20,20,19,.42);padding:16px;font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif}
.aspi .b{--bg:#FAF9F5;--fg:#141413;--mu:#6B6A64;--pill:#EDE6DA;--ac:#B9532F;--on:#fff;background:var(--bg);color:var(--fg);border-radius:18px;max-width:380px;width:100%;padding:24px 22px 18px;box-shadow:0 20px 60px rgba(0,0,0,.3);display:flex;flex-direction:column;gap:10px;align-items:center;text-align:center}
@media (prefers-color-scheme:dark){.aspi .b{--bg:#262624;--fg:#FAF9F5;--mu:#A6A39A;--pill:#3A3632;--ac:#E08A6A;--on:#1F1E1D}}
.aspi .ic{width:72px;height:72px}.aspi .ic svg{width:72px;height:72px;display:block}
.aspi h3{margin:2px 0 0;font-size:18px;font-weight:700;line-height:1.25}
.aspi p{margin:0;color:var(--mu)}
.aspi .row{display:flex;flex-direction:column;gap:8px;align-self:stretch;margin-top:6px}
.aspi button{font-family:inherit;font-weight:600;font-size:15px;line-height:1;border:0;border-radius:999px;padding:12px 16px;cursor:pointer}
.aspi .y{background:var(--ac);color:var(--on)}.aspi .n{background:var(--pill);color:var(--fg)}`;
  const m=document.createElement("div");m.className="aspi";m.setAttribute("role","dialog");m.setAttribute("aria-modal","true");m.setAttribute("data-no-i18n","");
  m.innerHTML=`<div class="b"><div class="ic">${icon}</div>
    <h3>${esc(T(`Install ${name} as an app?`,`把「${name}」安装为 app？`))}</h3>
    <p>${esc(T("It gets its own window and Dock icon, opens like any other app, and keeps working on your Claude plan.","装好后有自己的窗口和 Dock 图标，像普通 app 一样打开，继续用你的 Claude 套餐。"))}</p>
    <div class="row"><button class="y">${esc(T("Install","安装"))}</button><button class="n">${esc(T("Not now","以后再说"))}</button></div></div>`;
  const close=()=>{m.remove();st2.remove();try{sessionStorage.setItem("appstore.installAsked","1")}catch{}};
  m.addEventListener("click",async e=>{
    if(e.target===m||e.target.closest(".n"))return close();
    if(e.target.closest(".y")){const r=await d.install.request().catch(()=>"failed");close();
      if(r==="failed"||r==="unavailable"){const n=document.createElement("div");n.textContent=T("Couldn't install. Use Install as app in the artifact's menu.","没装上。可以在工件菜单里选“安装为 app”。");n.style.cssText="position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:#141413;color:#fff;padding:10px 14px;border-radius:10px;z-index:2147483000;font:13px system-ui";document.body.appendChild(n);setTimeout(()=>n.remove(),5000)}}
  });
  document.addEventListener("keydown",function k(e){if(e.key==="Escape"&&m.isConnected){close();document.removeEventListener("keydown",k)}});
  document.head?document.head.appendChild(st2):document.body.appendChild(st2);document.body.appendChild(m);
  m.querySelector(".y").focus();
})();
/*END_INSTALL_PROMPT*/
