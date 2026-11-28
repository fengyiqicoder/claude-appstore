import math,sys,pathlib
O="#D97757";C="#F5F0E6";L="#E6D6C1";D="#B9532F"
def T(ch,x=512,y=620,s=320,fill=O):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="{s}" fill="{fill}">{ch}</text>'
def wrap(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" rx="230" fill="{O}"/>{inner}</svg>'
def rr(x,y,w,h,r,f=C,extra=""): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}" {extra}/>'
def line(x,y,w,f=L,h=26): return rr(x,y,w,h,h/2,f)
PAGE=f'<path d="M312 196h290l150 150v430a52 52 0 0 1-52 52H312a52 52 0 0 1-52-52V248a52 52 0 0 1 52-52z" fill="{C}"/><path d="M602 196l150 150H654a52 52 0 0 1-52-52z" fill="{L}"/>'
def page(ch,extra=None):
    extra=extra if extra is not None else line(330,712,352)+line(330,762,230)
    return wrap(PAGE+T(ch,506,640,330)+extra)
wavy=f'<path d="M330 742q29-44 58 0t58 0 58 0 58 0 58 0 58 0" fill="none" stroke="{O}" stroke-width="24" stroke-linecap="round"/>'
band=rr(260,700,492,128,0,L).replace('rx="0"','rx="0"')+f'<path d="M260 700h492v76a52 52 0 0 1-52 52H312a52 52 0 0 1-52-52z" fill="{L}"/>'
chev=f'<path d="M400 716l44 34-44 34M500 716l44 34-44 34M600 716l44 34-44 34" fill="none" stroke="{O}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>'
def sheet(ch): return wrap(rr(250,196,524,632,56)+T(ch,512,560,330)+f'<g stroke="{L}" stroke-width="12"><path d="M250 640H774M250 734H774M425 640V828M600 640V828"/></g>')
def screen(ch): return wrap(rr(196,270,632,420,52)+f'<path d="M512 690v90M392 800h240" stroke="{C}" stroke-width="40" stroke-linecap="round"/>'+T(ch,512,596,320))
def bubble(ch,back=False,arcs=False):
    b=""
    if back: b=f'<path d="M420 250h330a60 60 0 0 1 60 60v250a60 60 0 0 1-60 60h-30v90l-100-90H420a60 60 0 0 1-60-60V310a60 60 0 0 1 60-60z" fill="{L}" opacity=".75" transform="translate(40 110)"/>'
    f=f'<path d="M270 220h400a64 64 0 0 1 64 64v300a64 64 0 0 1-64 64H450L330 760V648h-60a64 64 0 0 1-64-64V284a64 64 0 0 1 64-64z" fill="{C}"/>'
    a=f'<path d="M800 330q70 100 0 210M870 270q120 160 0 330" fill="none" stroke="{C}" stroke-width="34" stroke-linecap="round"/>' if arcs else ""
    return wrap(b+f+a+T(ch,470,545,300))
def disc(ch,kind):
    base=f'<circle cx="512" cy="512" r="310" fill="{C}"/>'
    if kind=="progress": ex=f'<circle cx="512" cy="512" r="256" fill="none" stroke="{L}" stroke-width="30"/><path d="M512 256a256 256 0 0 1 222 384" fill="none" stroke="{O}" stroke-width="30" stroke-linecap="round"/>'
    elif kind=="clock": ex="".join(f'<rect x="500" y="232" width="24" height="{60 if i%3==0 else 34}" rx="12" fill="{L if i%3 else O}" transform="rotate({i*30} 512 512)"/>' for i in range(12))
    elif kind=="coin": ex=f'<circle cx="512" cy="512" r="250" fill="none" stroke="{L}" stroke-width="22" stroke-dasharray="6 30" stroke-linecap="round"/>'
    else: ex=""
    s=250 if kind in("progress","clock") else 300
    return wrap(base+ex+T(ch,512,512+s*0.33,s))
def speaker(ch): return wrap(f'<circle cx="440" cy="512" r="270" fill="{C}"/><path d="M770 380q90 132 0 264M850 300q150 212 0 424" fill="none" stroke="{C}" stroke-width="38" stroke-linecap="round"/>'+T(ch,440,610,290))
def wave(ch):
    hs=[60,120,80,150,100,150,80,120,60]
    bars="".join(f'<rect x="{282+i*54}" y="{730-h/2}" width="28" height="{h}" rx="14" fill="{L if i%2 else O}"/>' for i,h in enumerate(hs))
    return wrap(rr(220,196,584,632,70)+T(ch,512,570,330)+bars)
def note(ch): return wrap(f'<path d="M286 226h452a40 40 0 0 1 40 40v330L616 798H286a40 40 0 0 1-40-40V266a40 40 0 0 1 40-40z" fill="{C}"/><path d="M616 798V636a40 40 0 0 1 40-40h122z" fill="{L}"/>'+T(ch,500,600,320))
def cards(ch,rot=-10): return wrap(f'<g transform="rotate({rot} 512 512)">{rr(300,230,470,560,56,L)}</g><g transform="rotate({-rot*0.4} 512 512)">{rr(280,240,470,560,56)}'+T(ch,515,635,330)+'</g>')
def board(ch,kind):
    b=rr(180,250,664,460,48)+f'<rect x="204" y="274" width="616" height="412" rx="30" fill="none" stroke="{L}" stroke-width="14"/>'
    if kind=="legs": b+=f'<path d="M330 710l-50 110M694 710l50 110" stroke="{C}" stroke-width="40" stroke-linecap="round"/>'
    if kind=="dots": b+=rr(650,310,110,110,18,O)+rr(264,560,110,90,18,L)
    if kind=="flow": b+=rr(250,560,120,80,16,L)+rr(654,560,120,80,16,L)+f'<path d="M370 600h284" stroke="{L}" stroke-width="16"/>'
    return wrap(b+T(ch,512,590,300))
def film(ch):
    holes="".join(rr(x,y,56,56,14,O) for x in (214,754) for y in (300,410,520,630))
    return wrap(rr(180,250,664,500,56)+holes+T(ch,512,610,320)+f'<path d="M650 700l70 40-70 40z" fill="{O}" transform="translate(-10 -120)" opacity="0"/>')
def artboard(ch,cursor=False):
    h="".join(rr(x-28,y-28,56,56,12,C)+rr(x-14,y-14,28,28,6,O) for x in (230,794) for y in (250,774))
    c=f'<path d="M690 640l150 70-64 22-22 64z" fill="{D}" stroke="{C}" stroke-width="14" stroke-linejoin="round"/>' if cursor else ""
    return wrap(rr(230,250,564,524,24)+h+T(ch,512,625,330)+c)
def brief(ch): return wrap(f'<path d="M410 300v-40a50 50 0 0 1 50-50h104a50 50 0 0 1 50 50v40" fill="none" stroke="{C}" stroke-width="44"/>'+rr(190,300,644,500,64)+f'<path d="M190 520h644" stroke="{L}" stroke-width="16"/>'+T(ch,512,660,300))
def scan(ch): return wrap(f'<path d="M240 400V300a60 60 0 0 1 60-60h100M624 240h100a60 60 0 0 1 60 60v100M784 624v100a60 60 0 0 1-60 60H624M400 784H300a60 60 0 0 1-60-60V624" fill="none" stroke="{C}" stroke-width="52" stroke-linecap="round"/>'+T(ch,512,625,330,C))
def gridpaper(ch): 
    g="".join(f'<path d="M{250+i*105} 220v584M230 {240+i*105}h564" stroke="{L}" stroke-width="8"/>' for i in range(1,5))
    return wrap(rr(230,220,564,584,56)+g+T(ch,512,625,330))
def blocks(ch): return wrap(rr(230,196,564,632,56)+T(ch,512,540,300)+"".join(rr(300,610+i*64,34,34,8,O if i==0 else L)+line(356,614+i*64,[330,250,300][i]) for i in range(3)))
def spiral(ch): return wrap(rr(270,196,524,632,56)+"".join(rr(226,268+i*100,100,36,18,L)+f'<circle cx="320" cy="{286+i*100}" r="20" fill="{O}"/>' for i in range(6))+T(ch,560,625,320))
def poly(ch,n): 
    pts=" ".join(f"{512+330*math.cos(math.radians(a)):.0f},{512+330*math.sin(math.radians(a)):.0f}" for a in range(-90,270,360//n))
    return wrap(f'<polygon points="{pts}" fill="{C}" stroke="{C}" stroke-width="60" stroke-linejoin="round"/>'+T(ch,512,618,310))
def shield(ch): return wrap(f'<path d="M512 190l270 90v230c0 170-110 280-270 340-160-60-270-170-270-340V280z" fill="{C}" stroke="{C}" stroke-width="40" stroke-linejoin="round"/>'+T(ch,512,600,300))
def nodes(ch,both):
    br=f'<g fill="none" stroke="{C}" stroke-width="30" stroke-linecap="round"><path d="M600 512C700 512 690 290 800 290M600 512h200M600 512c100 0 90 222 200 222"/>'+(f'<path d="M424 512C324 512 334 290 224 290M424 512H224M424 512c-100 0-90 222-200 222"/>' if both else "")+'</g>'
    ends="".join(f'<circle cx="{x}" cy="{y}" r="44" fill="{C}"/>' for x in ((800,) if not both else (800,224)) for y in (290,512,734))
    cx=512 if both else 400
    return wrap(br.replace("600",str(cx+ (88 if both else 200))) .replace("424",str(cx-88)) +ends+f'<circle cx="{cx}" cy="512" r="{200 if both else 230}" fill="{C}"/>'+T(ch,cx,512+ (72 if both else 84),220 if both else 250))
def check(ch,kind):
    if kind=="list": ex="".join(f'<circle cx="320" cy="{660+i*74}" r="24" fill="{O if i==0 else "none"}" stroke="{O if i==0 else L}" stroke-width="12"/>'+line(370,648+i*74,[300,220][i]) for i in range(2)); return wrap(rr(230,196,564,632,56)+T(ch,512,560,320)+ex)
    return wrap(rr(220,220,584,584,120)+T(ch,480,610,320)+f'<circle cx="716" cy="716" r="110" fill="{D}" stroke="{O}" stroke-width="24"/><path d="M668 716l34 34 62-70" fill="none" stroke="{C}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>')
def cal(ch): return wrap(rr(220,240,584,580,64)+f'<path d="M220 400V304a64 64 0 0 1 64-64h456a64 64 0 0 1 64 64v96z" fill="{L}"/>'+rr(350,190,40,120,20,C)+rr(634,190,40,120,20,C)+T(ch,512,720,300))
def clip(ch): return wrap(rr(240,250,544,580,60)+rr(392,196,240,120,36,L)+rr(452,226,120,40,20,O)+T(ch,512,690,320))
def kanban(ch): return wrap(rr(200,220,624,584,64)+rr(250,270,150,300,24,L)+rr(437,270,150,440,24,L)+rr(624,270,150,220,24,L)+T(ch,512,640,300,D))
def lesson(ch): return wrap(rr(220,196,584,632,90)+T(ch,512,560,330)+"".join(f'<circle cx="{372+i*140}" cy="720" r="{40}" fill="{O if i<2 else L}"/>' for i in range(3))+f'<path d="M372 720h280" stroke="{L}" stroke-width="14"/>'.replace("/>"," opacity='.0'/>"))
def book(ch): return wrap(rr(250,196,524,632,48)+f'<path d="M250 244a48 48 0 0 1 48-48h50v632h-50a48 48 0 0 1-48-48z" fill="{L}"/><path d="M640 196h80v190l-40-36-40 36z" fill="{O}"/>'+T(ch,545,660,320))
def launcher(ch): return wrap(rr(170,300,684,200,100)+f'<circle cx="290" cy="400" r="50" fill="none" stroke="{O}" stroke-width="26"/><path d="M326 436l44 44" stroke="{O}" stroke-width="26" stroke-linecap="round"/>'+T(ch,560,470,200)+"".join(line(230,570+i*90,[560,420,480][i],C if i==0 else L,44) for i in range(3)))
def windows(ch): return wrap(rr(180,230,664,564,56)+rr(210,260,290,504,34,L)+rr(530,260,284,236,34,L)+rr(530,526,284,238,34,L)+T(ch,355,610,280,D))
def quote(ch): return wrap(f'<path d="M286 226h452a40 40 0 0 1 40 40v492a40 40 0 0 1-40 40H286a40 40 0 0 1-40-40V266a40 40 0 0 1 40-40z" fill="{C}"/>'+rr(246,226,70,572,0,L).replace('rx="0"','rx="0"')+T(ch,540,560,300)+line(380,650,300)+line(380,706,200)+f'<path d="M246 266a40 40 0 0 1 40-40h30v572h-30a40 40 0 0 1-40-40z" fill="{L}"/>')
ICONS={
"document-editor":page("W"),"alt-pages":page("P"),"spreadsheet":sheet("X"),"alt-numbers":sheet("N"),"slide-maker":screen("P"),"alt-keynote":screen("K"),
"pdf-chat":page("A",band),"grammar-checker":page("G",wavy),"rewriter":page("Q",chev),
"mind-map":nodes("X",False),"alt-mindnode":nodes("M",True),"image-to-text":scan("T"),
"translator":bubble("D",back=True),"speaking-coach":bubble("E",arcs=True),"thinking-partner":bubble("C"),
"pomodoro":disc("B","progress"),"world-clock":disc("D","clock"),"budget":disc("Y","coin"),"read-aloud":speaker("S"),
"sticky-notes":note("S"),"video-studio":film("L"),"design-studio":artboard("C"),"alt-figma":artboard("F",True),
"job-search":brief("T"),"flashcards":cards("A"),"alt-quizlet":cards("Q",12),"homework-helper":gridpaper("P"),
"whiteboard":board("M","dots"),"alt-lucidchart":board("L","flow"),"classroom":board("W","legs"),
"fitness-coach":poly("F",6),"alt-myfitnesspal":shield("M"),
"alt-notion":blocks("N"),"alt-evernote":spiral("E"),"alt-todoist":check("T","list"),"alt-things":check("T","big"),
"alt-fantastical":cal("F"),"alt-day-one":book("D"),"alt-paste":clip("P"),"alt-trello":kanban("T"),"alt-otter":wave("O"),"alt-duolingo":lesson("D"),"alt-raycast":launcher("R"),"alt-magnet":windows("M"),"alt-bear":quote("B"),
}
out=pathlib.Path(sys.argv[1]); out.mkdir(exist_ok=True)
for k,v in ICONS.items(): (out/f"{k}.svg").write_text(v)
h='<body style="margin:0;background:#FAF9F5;display:flex;flex-wrap:wrap;gap:22px;padding:28px;font:12px system-ui">'+"".join(f'<div style="text-align:center;width:120px"><img src="{k}.svg" width="110"><br>{k}<br><img src="{k}.svg" width="28"></div>' for k in ICONS)+'</body>'
(out/"sheet.html").write_text(h); print(len(ICONS))
