import math,sys,pathlib,colorsys
def hx(c): c=c.lstrip("#"); return tuple(int(c[i:i+2],16)/255 for i in (0,2,4))
def th(r,g,b): return "#%02X%02X%02X"%tuple(max(0,min(255,round(v*255))) for v in (r,g,b))
def mix(a,b,t): A,B=hx(a),hx(b); return th(*(A[i]*(1-t)+B[i]*t for i in range(3)))
def rr(x,y,w,h,r,f,extra=""): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}" {extra}/>'
def ln(x,y,w,f,h=30): return rr(x,y,w,h,h/2,f)
class K:  # palette for one icon
    def __init__(s,pid,c1,c2,fg="#FFFFFF",light=False):
        s.p=pid; s.c1=c1; s.c2=c2; s.light=light
        s.F=f"url(#{pid}-fg)"; s.fg=fg
        s.B=c2 if not light else c1            # cut-out / detail colour drawn on top of fg shapes
        s.A=mix(fg,c1,.38) if not light else mix(fg,c1,.45)   # secondary shape
        s.A2=mix(fg,c1,.62) if not light else mix(fg,c1,.7)
def wrap(k,inner):
    fg2=mix(k.fg,k.c2,.10) if not k.light else mix(k.fg,"#000000",.25)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs>'
     f'<linearGradient id="{k.p}-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{k.c1}"/><stop offset="1" stop-color="{k.c2}"/></linearGradient>'
     f'<radialGradient id="{k.p}-hl" cx=".3" cy="0" r="1"><stop offset="0" stop-color="#fff" stop-opacity=".34"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/></radialGradient>'
     f'<linearGradient id="{k.p}-fg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{k.fg}"/><stop offset="1" stop-color="{fg2}"/></linearGradient>'
     f'<filter id="{k.p}-sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="{mix(k.c2,"#000000",.55)}" flood-opacity=".38"/></filter></defs>'
     f'<rect width="1024" height="1024" rx="230" fill="url(#{k.p}-bg)"/><rect width="1024" height="1024" rx="230" fill="url(#{k.p}-hl)"/>'
     f'<g filter="url(#{k.p}-sh)">{inner}</g><rect x="3" y="3" width="1018" height="1018" rx="228" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="6"/></svg>')
PAGE='<path d="M312 186h280l160 160v440a52 52 0 0 1-52 52H312a52 52 0 0 1-52-52V238a52 52 0 0 1 52-52z" fill="{F}"/><path d="M592 186l160 160H644a52 52 0 0 1-52-52z" fill="{A}"/>'
def page(k): return PAGE.format(F=k.F,A=k.A)
def doc(k): return page(k)+"".join(ln(336,430+i*86,[340,340,340,210][i],k.B,34) for i in range(4))
def doc2(k): return page(k)+rr(336,420,150,150,24,k.B)+ln(520,430,150,k.B,34)+ln(520,516,110,k.B,34)+ln(336,626,340,k.B,34)+ln(336,712,240,k.B,34)
def grid(k): return rr(232,232,560,560,64,k.F)+f'<path d="M232 296a64 64 0 0 1 64-64h432a64 64 0 0 1 64 64v84H232z" fill="{k.B}"/><g stroke="{k.B}" stroke-width="20"><path d="M232 518h560M232 656h560M418 380v412M606 380v412"/></g>'
def chart(k): return rr(232,232,560,560,64,k.F)+rr(310,560,100,160,22,k.B)+rr(462,430,100,290,22,k.B)+rr(614,320,100,400,22,k.B)
def slide(k,key=False):
    s=rr(190,240,644,440,56,k.F)+f'<path d="M512 680v96M384 800h256" stroke="{k.fg}" stroke-width="44" stroke-linecap="round"/>'
    if key: return s+f'<circle cx="380" cy="460" r="96" fill="{k.B}"/><path d="M520 556l110-190 110 190z" fill="{k.A2}" stroke="{k.A2}" stroke-width="24" stroke-linejoin="round"/>'
    return s+f'<path d="M370 460m-110 0a110 110 0 1 0 110-110v110z" fill="{k.B}"/><path d="M394 326a110 110 0 0 1 110 110H394z" fill="{k.A2}"/>'+ln(560,400,200,k.B,36)+ln(560,480,150,k.B,36)+ln(560,560,180,k.B,36)
def pdf(k): return page(k)+f'<path d="M336 600c60-150 110-150 120-60s50 100 90 20 70-60 130 20" fill="none" stroke="{k.B}" stroke-width="34" stroke-linecap="round"/>'+ln(336,700,340,k.A2,26)+ln(336,440,200,k.B,34)
def gcheck(k): return f'<circle cx="512" cy="450" r="250" fill="{k.F}"/><path d="M392 456l84 84 160-176" fill="none" stroke="{k.B}" stroke-width="64" stroke-linecap="round" stroke-linejoin="round"/><path d="M262 800q42-64 84 0t84 0 84 0 84 0 84 0 84 0" fill="none" stroke="{k.fg}" stroke-width="40" stroke-linecap="round"/>'
def rewrite(k): return page(k)+f'<g fill="none" stroke="{k.B}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"><path d="M360 520a150 150 0 0 1 270-60M650 620a150 150 0 0 1-270 60"/><path d="M640 380v90h-90M370 760v-90h90"/></g>'
def nodes(k,both=False):
    cx=512 if both else 380
    r=f'<g fill="none" stroke="{k.fg}" stroke-width="36" stroke-linecap="round"><path d="M{cx} 512C{cx+220} 512 {cx+200} 280 820 280M{cx} 512H820M{cx} 512c{220} 0 {200} 232 {820-cx} 232"/>'
    if both: r+=f'<path d="M512 512C292 512 312 280 204 280M512 512H204M512 512c-220 0-200 232-308 232"/>'
    r+='</g>'+"".join(f'<circle cx="{x}" cy="{y}" r="58" fill="{k.F if y!=512 else k.A}"/>' for x in ((820,204) if both else (820,)) for y in (280,512,744))
    return r+(f'<circle cx="512" cy="512" r="150" fill="{k.F}"/>' if both else rr(190,392,380,240,120,k.F))
def scan(k): return f'<path d="M230 400V300a70 70 0 0 1 70-70h100M624 230h100a70 70 0 0 1 70 70v100M794 624v100a70 70 0 0 1-70 70H624M400 794H300a70 70 0 0 1-70-70V624" fill="none" stroke="{k.fg}" stroke-width="60" stroke-linecap="round"/>'+ln(360,410,304,k.F,50)+ln(360,500,304,k.A,50)+ln(360,590,200,k.A,50)
BUB='<path d="M{x} {y}h{w}a70 70 0 0 1 70 70v{h}a70 70 0 0 1-70 70h-{t}l-{q} {q}v-{q}h-{u}a70 70 0 0 1-70-70v-{h}a70 70 0 0 1 70-70z" fill="{f}"/>'
def bub(x,y,w,h,f,q=110): return BUB.format(x=x,y=y,w=w,h=h,f=f,q=q,t=w-170,u=170-q)
def bubbles(k): return f'<g transform="translate(1024 150) scale(-1 1)">{bub(250,300,330,170,k.A)}</g>'+bub(240,210,360,210,k.F)+ln(290,300,260,k.B,40)+ln(290,390,170,k.B,40)
def micb(k): return bub(250,220,524,330,k.F)+rr(462,290,100,200,50,k.B)+f'<path d="M400 440a112 112 0 0 0 224 0M512 552v50" fill="none" stroke="{k.B}" stroke-width="34" stroke-linecap="round"/>'
def think(k): return bub(250,220,524,330,k.F)+"".join(f'<circle cx="{392+i*120}" cy="455" r="44" fill="{k.B if i<2 else k.A2}"/>' for i in range(3))
def timer(k): return f'<circle cx="512" cy="540" r="250" fill="none" stroke="{k.A2}" stroke-width="80"/><path d="M512 290a250 250 0 1 1-216.5 125" fill="none" stroke="{k.fg}" stroke-width="80" stroke-linecap="round"/><path d="M430 170h164" stroke="{k.fg}" stroke-width="64" stroke-linecap="round"/><circle cx="512" cy="540" r="70" fill="{k.F}"/>'
def clock(k): return f'<circle cx="512" cy="512" r="300" fill="{k.F}"/>'+"".join(f'<rect x="496" y="250" width="32" height="64" rx="16" fill="{k.A2}" transform="rotate({i*90} 512 512)"/>' for i in range(4))+f'<path d="M512 512V350M512 512l120 76" stroke="{k.B}" stroke-width="44" stroke-linecap="round"/><circle cx="512" cy="512" r="34" fill="{k.B}"/>'
def envelope(k): return rr(200,300,560,400,56,k.F)+f'<path d="M224 340l256 190 256-190" fill="none" stroke="{k.B}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><circle cx="720" cy="660" r="140" fill="{k.A}" stroke="{k.c2}" stroke-width="26"/><path d="M720 590v140M670 640h100" stroke="{k.B}" stroke-width="0"/><circle cx="720" cy="660" r="62" fill="none" stroke="{k.B}" stroke-width="26"/>'
def wave(k,hs=(140,300,520,360,560,240,400,160)): return "".join(rr(190+i*86,512-h/2,56,h,28,k.F if i%3 else k.A) for i,h in enumerate(hs))
def note(k,tag=False):
    s=f'<path d="M276 216h472a44 44 0 0 1 44 44v340L596 808H276a44 44 0 0 1-44-44V260a44 44 0 0 1 44-44z" fill="{k.F}"/><path d="M596 808V644a44 44 0 0 1 44-44h152z" fill="{k.A}"/>'
    if tag: return s+f'<path d="M430 330l-40 240M560 330l-40 240M340 400h280M320 500h280" stroke="{k.B}" stroke-width="36" stroke-linecap="round"/>'
    return s+ln(310,330,400,k.B,40)+ln(310,430,400,k.B,40)+ln(310,530,250,k.B,40)
def film(k): return rr(170,250,684,524,70,k.F)+"".join(rr(x,y,64,64,18,k.B) for x in (206,754) for y in (300,420,540,660))+f'<path d="M440 400l190 112-190 112z" fill="{k.B}" stroke="{k.B}" stroke-width="30" stroke-linejoin="round"/>'
def shapes(k): return rr(200,220,624,584,70,k.F)+f'<circle cx="400" cy="420" r="110" fill="{k.B}"/>'+rr(560,320,180,180,36,k.A2)+f'<path d="M300 720l120-150 100 110 90-80 120 120z" fill="{k.c1}" stroke="{k.c1}" stroke-width="20" stroke-linejoin="round"/>'
def frame4(k,cols):
    return rr(190,190,300,300,150,cols[0])+rr(534,190,300,300,60,cols[1])+rr(190,534,300,300,60,cols[2])+f'<circle cx="684" cy="684" r="150" fill="{cols[3]}"/><path d="M560 560l250 110-106 36-36 106z" fill="#1E1E1E" stroke="#fff" stroke-width="26" stroke-linejoin="round"/>'
def brief(k): return f'<path d="M400 320v-56a56 56 0 0 1 56-56h112a56 56 0 0 1 56 56v56" fill="none" stroke="{k.fg}" stroke-width="56"/>'+rr(180,320,664,470,72,k.F)+f'<path d="M180 520h664" stroke="{k.B}" stroke-width="30"/>'+rr(452,470,120,100,26,k.B)
def cards(k,flip=False):
    s=f'<g transform="rotate(-12 512 512)">{rr(280,230,470,580,60,k.A)}</g><g transform="rotate(5 512 512)">{rr(270,230,470,580,60,k.F)}'
    if flip: s+=f'<path d="M400 500a120 120 0 1 1 40 110" fill="none" stroke="{k.B}" stroke-width="44" stroke-linecap="round"/><path d="M370 600l66 26 16-76" fill="none" stroke="{k.B}" stroke-width="44" stroke-linecap="round" stroke-linejoin="round"/>'
    else: s+=ln(340,330,330,k.B,44)+ln(340,430,220,k.B,44)+f'<path d="M270 590h470" stroke="{k.A2}" stroke-width="16" stroke-dasharray="26 22"/>'+ln(340,680,280,k.A2,44)
    return s+'</g>'
def calc(k): return rr(220,220,584,584,80,k.F)+f'<g stroke="{k.B}" stroke-width="42" stroke-linecap="round"><path d="M320 380h140M390 310v140M574 380h130M330 590l120 120M450 590L330 710M574 610h130M574 690h130"/></g><path d="M512 250v524M250 512h524" stroke="{k.A2}" stroke-width="14"/>'
def board(k,kind):
    s=rr(170,240,684,470,60,k.F)
    if kind=="stickies": s+=rr(240,310,170,170,26,k.B)+rr(450,310,170,170,26,k.A2)+rr(450,510,170,140,26,k.B)+f'<path d="M660 395h60a40 40 0 0 1 40 40v120" fill="none" stroke="{k.B}" stroke-width="26" stroke-linecap="round"/><circle cx="760" cy="590" r="34" fill="{k.B}"/>'
    if kind=="tiles": s+="".join(rr(240+c*190,300+r*180,160,150,28,k.B if (r+c)%2==0 else k.A2) for r in range(2) for c in range(3))+f'<path d="M330 710l-56 120M694 710l56 120" stroke="{k.fg}" stroke-width="48" stroke-linecap="round"/>'
    return s
def flow(k): return rr(372,180,280,170,44,k.F)+rr(170,640,280,170,44,k.F)+rr(574,640,280,170,44,k.A)+f'<path d="M512 350v140M310 640V560a70 70 0 0 1 70-70h264a70 70 0 0 1 70 70v80" fill="none" stroke="{k.fg}" stroke-width="40" stroke-linecap="round"/>'
def dumbbell(k): return f'<g transform="rotate(-35 512 512)">'+rr(300,480,424,64,20,k.A)+rr(250,350,110,324,40,k.F)+rr(664,350,110,324,40,k.F)+rr(160,410,90,204,36,k.F)+rr(774,410,90,204,36,k.F)+'</g>'
def donut(k): return f'<circle cx="512" cy="512" r="230" fill="none" stroke="{k.A2}" stroke-width="120"/><path d="M512 282a230 230 0 0 1 199 345" fill="none" stroke="{k.fg}" stroke-width="120" stroke-linecap="round"/><path d="M313 627a230 230 0 0 1 0-230" fill="none" stroke="{k.A}" stroke-width="120" stroke-linecap="round"/>'
def blocks(k): return rr(232,192,560,640,60,k.F)+rr(310,290,90,90,20,k.B)+ln(440,315,250,k.B,40)+"".join(rr(310,450+i*100,44,44,12,k.B)+ln(390,452+i*100,[300,220,270][i],k.A2 if i else k.B,40) for i in range(3))
def spiral(k): return rr(280,192,520,640,60,k.F)+"".join(rr(210,280+i*118,130,48,24,k.A)+f'<circle cx="344" cy="{304+i*118}" r="26" fill="{k.B}"/>' for i in range(5))+ln(440,330,280,k.B,40)+ln(440,430,280,k.B,40)+ln(440,530,180,k.B,40)
def todo(k): return rr(222,212,580,600,70,k.F)+"".join(f'<circle cx="340" cy="{350+i*160}" r="46" fill="{k.B if i==0 else "none"}" stroke="{k.B}" stroke-width="22"/>'+ln(430,330+i*160,[290,220,260][i],k.A2 if i==0 else k.B,40) for i in range(3))+f'<path d="M318 350l18 18 30-36" fill="none" stroke="{k.fg}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>'
def bigcheck(k): return f'<circle cx="512" cy="512" r="290" fill="{k.F}"/><path d="M372 520l100 100 190-210" fill="none" stroke="{k.B}" stroke-width="76" stroke-linecap="round" stroke-linejoin="round"/>'
def kanban(k): return rr(190,220,180,584,44,k.F)+rr(422,220,180,400,44,k.F)+rr(654,220,180,260,44,k.A)+"".join(rr(214,250+i*130,132,100,22,k.B if i<2 else k.A2) for i in range(4))+"".join(rr(446,250+i*130,132,100,22,k.B) for i in range(2))
def cal(k): return rr(212,236,600,590,72,k.F)+f'<path d="M212 420V308a72 72 0 0 1 72-72h456a72 72 0 0 1 72 72v112z" fill="{k.B}"/>'+rr(340,176,48,130,24,k.fg)+rr(636,176,48,130,24,k.fg)+"".join(rr(290+c*130,490+r*120,74,74,20,k.B if (r,c)==(1,2) else k.A2) for r in range(2) for c in range(4))
def book(k): return f'<path d="M512 300c-90-70-200-70-320-40v500c120-30 230-30 320 40z" fill="{k.F}"/><path d="M512 300c90-70 200-70 320-40v500c-120-30-230-30-320 40z" fill="{k.A}"/><path d="M660 236h100v230l-50-44-50 44z" fill="{k.B}"/>'+ln(260,400,180,k.B,30)+ln(260,480,180,k.B,30)+ln(260,560,120,k.B,30)
def clip(k): return rr(232,240,560,600,64,k.F)+rr(392,176,240,130,44,k.A)+rr(450,210,124,50,25,k.B)+"".join(rr(300,380+i*130,424,96,26,[k.B,k.A2,k.A2][i]) for i in range(3))
def launcher(k): return rr(160,270,704,200,100,k.F)+f'<circle cx="290" cy="362" r="52" fill="none" stroke="{k.B}" stroke-width="30"/><path d="M328 400l46 46" stroke="{k.B}" stroke-width="30" stroke-linecap="round"/>'+ln(420,345,300,k.A2,44)+"".join(rr(200,540+i*110,624,74,37,k.A if i else k.F,'opacity=".9"') for i in range(2))
def windows(k): return rr(170,220,684,584,64,k.A2)+rr(206,256,300,512,40,k.F)+rr(538,256,280,240,40,k.F)+rr(538,528,280,240,40,k.A)
def micnotes(k): return rr(232,180,170,330,85,k.F)+f'<path d="M170 420a147 147 0 0 0 294 0M317 567v110M230 690h174" fill="none" stroke="{k.fg}" stroke-width="44" stroke-linecap="round"/>'+ln(540,300,300,k.F,56)+ln(540,430,220,k.A,56)+ln(540,560,300,k.A,56)+ln(540,690,160,k.A,56)
def lesson(k): return bub(220,200,584,380,k.F,130)+"".join(f'<circle cx="{362+i*150}" cy="460" r="56" fill="{k.B if i<2 else k.A2}"/>' for i in range(3))+f'<path d="M338 460l18 18 32-38M488 460l18 18 32-38" fill="none" stroke="{k.fg}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>'
SPEC={ # id:(symbol, c1, c2, fg, light?)
"document-editor":(doc,"#4A9BF0","#1F5FBF"),"alt-pages":(doc2,"#FFB23E","#F07F12"),
"spreadsheet":(grid,"#3DBB73","#0F7A41"),"alt-numbers":(chart,"#5FD86B","#1FA53C"),
"slide-maker":(slide,"#F3774B","#C9401F"),"alt-keynote":(lambda k:slide(k,True),"#4FB2FF","#1672E0"),
"pdf-chat":(pdf,"#F0524B","#B3140F"),"grammar-checker":(gcheck,"#2FD3A5","#0E9E7B"),"rewriter":(rewrite,"#6CBB6E","#3A8A4B"),
"mind-map":(nodes,"#FF7A52","#E13A22"),"alt-mindnode":(lambda k:nodes(k,True),"#B58BFF","#6B4BE0"),
"image-to-text":(scan,"#8E7BFF","#4C3BD6"),"translator":(bubbles,"#2E5C8F","#0F2B46"),"speaking-coach":(micb,"#8C6BFF","#4A2FD0"),"thinking-partner":(think,"#3A3A3F","#111114"),
"pomodoro":(timer,"#FF6B5E","#D92B25"),"world-clock":(clock,"#5C6B8A","#232C40"),"budget":(envelope,"#6E8BFF","#3350D8"),"read-aloud":(wave,"#4D6BFF","#1B2FE0"),
"sticky-notes":(note,"#FFE066","#F5B400","#FFFDF2"),"video-studio":(film,"#8A7BFF","#4B37E0"),
"design-studio":(shapes,"#22D3D8","#7B3FF2"),"alt-figma":("figma","#FFFFFF","#EDEDED"),
"job-search":(brief,"#2FC4B2","#0A8577"),"flashcards":(cards,"#6BC3FF","#2585E0"),"alt-quizlet":(lambda k:cards(k,True),"#6B7BFF","#3644E6"),
"homework-helper":(calc,"#FF5A5F","#D01F2A"),"whiteboard":(lambda k:board(k,"stickies"),"#FFE14D","#FFC400","#1F1F24",True),
"alt-lucidchart":(flow,"#FF9547","#EE5A0C"),"classroom":(lambda k:board(k,"tiles"),"#4DA3FF","#1C63D9"),
"fitness-coach":(dumbbell,"#FF5C7A","#DB1F4B"),"alt-myfitnesspal":(donut,"#3D9BFF","#0A5BE0"),
"alt-notion":(blocks,"#FFFFFF","#E9E9E7","#1F1F1F",True),"alt-evernote":(spiral,"#3CCB5A","#0A9A2E"),"alt-bear":(lambda k:note(k,True),"#F26A66","#C9302F"),
"alt-todoist":(todo,"#F5604E","#D3301F"),"alt-things":(bigcheck,"#5AA9FF","#1F6BE8"),"alt-trello":(kanban,"#3D9BE8","#0A63B0"),
"alt-fantastical":(cal,"#FF6A6A","#D62A3A"),"alt-day-one":(book,"#5FD0FF","#1E9BE8"),"alt-paste":(clip,"#C77BFF","#7A3BE0"),
"alt-raycast":(launcher,"#FF6B6B","#8F1D1D"),"alt-magnet":(windows,"#6A8DFF","#2E4BD0"),"alt-otter":(micnotes,"#4D8DFF","#1558D6"),"alt-duolingo":(lesson,"#7BDB2B","#46A302"),
}
out=pathlib.Path(sys.argv[1]); out.mkdir(exist_ok=True)
for i,(pid,sp) in enumerate(SPEC.items()):
    fn,c1,c2=sp[0],sp[1],sp[2]; fg=sp[3] if len(sp)>3 else "#FFFFFF"; light=sp[4] if len(sp)>4 else False
    k=K("a"+str(i),c1,c2,fg,light)
    if fn=="figma": inner=frame4(k,["#F24E1E","#A259FF","#1ABCFE","#0ACF83"])
    else: inner=fn(k)
    (out/f"{pid}.svg").write_text(wrap(k,inner))
h='<body style="margin:0;background:#FAF9F5;display:flex;flex-wrap:wrap;gap:22px;padding:28px;font:12px system-ui">'+"".join(f'<div style="text-align:center;width:120px"><img src="{k}.svg" width="110"><br>{k}<br><img src="{k}.svg" width="28"></div>' for k in SPEC)+'</body>'
(out/"sheet.html").write_text(h); print(len(SPEC))
