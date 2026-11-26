"""Embed data/icons/<id>.svg into apps/<id>/index.html as the installed app's Dock icon.
Usage: python3 data/icons/apply_dock_icons.py id [id ...]   (idempotent)"""
import sys, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
START, END = "/*DOCK_ART*/", "/*END_DOCK_ART*/"
for id_ in sys.argv[1:]:
    f = ROOT / "apps" / id_ / "index.html"; s = f.read_text()
    svg = (ROOT / "data/icons" / f"{id_}.svg").read_text()
    fn = (START + "\nconst DOCK_SVG=" + json.dumps(svg).replace("</", "<\\/") + ";\n"
          "function dockIconArt(){return new Promise(res=>{const img=new Image();img.onload=()=>{try{const c=document.createElement(\"canvas\");c.width=c.height=512;const x=c.getContext(\"2d\");"
          "x.shadowColor=\"rgba(0,0,0,.3)\";x.shadowBlur=20;x.shadowOffsetY=8;x.drawImage(img,50,44,412,412);res(c.toDataURL(\"image/png\"))}catch{res(dockIcon())}};"
          "img.onerror=()=>res(dockIcon());img.src=\"data:image/svg+xml;charset=utf-8,\"+encodeURIComponent(DOCK_SVG)})}\n" + END + "\n")
    if START in s:
        a, b = s.index(START), s.index(END) + len(END) + 1
        s = s[:a] + fn + s[b:]
    else:
        i = s.index("function dockIcon(")
        s = s[:i] + fn + s[i:]
    n0 = s.count("setIcon(dockIcon())")
    s = re.sub(r"desktop\.app(\??)\.dock(\??)\.setIcon(\?\.)?\(dockIcon\(\)\)", lambda m: f"dockIconArt().then(u=>desktop.app{m[1]}.dock{m[2]}.setIcon{m[3] or ''}(u))", s)
    f.write_text(s)
    print(id_, "replaced calls:", n0, "remaining:", s.count("setIcon(dockIcon())"), "setIcon total:", s.count("setIcon("))
