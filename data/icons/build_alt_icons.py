import pathlib,sys,math
def hx(c): c=c.lstrip("#"); return tuple(int(c[i:i+2],16)/255 for i in (0,2,4))
def th(v): return "#%02X%02X%02X"%tuple(max(0,min(255,round(x*255))) for x in v)
def mix(a,b,t): A,B=hx(a),hx(b); return th([A[i]*(1-t)+B[i]*t for i in range(3)])
def R(x,y,w,h,r,f,e=""): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}" {e}/>'
def E(x,y,w,h,r): return f'<rect x="{x+3}" y="{y+3}" width="{w-6}" height="{h-6}" rx="{max(r-3,0)}" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="6"/>'
def P(d,f,e=""): return f'<path d="{d}" fill="{f}" {e}/>'
def S(d,st,w,e=""): return f'<path d="{d}" fill="none" stroke="{st}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {e}/>'
def C(x,y,r,f,e=""): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" {e}/>'
class K:
    def __init__(s,p,c1,c2,fgA="#FFFFFF",fgB=None,dark=None,acA=None,acB=None,glass="#FFFFFF"):
        s.p=p;s.c1=c1;s.c2=c2;s.fgA=fgA;s.fgB=fgB or mix("#FFFFFF",c1,.16);s.dark=dark or mix(c2,"#000000",.5)
        s.acA=acA or mix(c1,"#FFFFFF",.1);s.acB=acB or c2;s.glass=glass
        s.F=f"url(#{p}fg)";s.A=f"url(#{p}ac)";s.G=f"url(#{p}gl)";s.BG=f"url(#{p}bg)"
        s.lt=mix(c1,"#FFFFFF",.38);s.lt2=mix(c1,"#FFFFFF",.62)
    def sh(s,x,t=""): return f'<g filter="url(#{s.p}sh)" {t}>{x}</g>'
    def s2(s,x,t=""): return f'<g filter="url(#{s.p}s2)" {t}>{x}</g>'
    def svg(s,body):
        p=s.p
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs>'
        f'<linearGradient id="{p}bg" x1=".1" y1="0" x2=".9" y2="1"><stop offset="0" stop-color="{s.c1}"/><stop offset="1" stop-color="{s.c2}"/></linearGradient>'
        f'<radialGradient id="{p}hl" cx=".22" cy=".02" r=".95"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{p}lo" cx=".8" cy="1.05" r=".8"><stop offset="0" stop-color="{s.dark}" stop-opacity=".42"/><stop offset=".7" stop-color="{s.dark}" stop-opacity="0"/></radialGradient>'
        f'<linearGradient id="{p}fg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s.fgA}"/><stop offset="1" stop-color="{s.fgB}"/></linearGradient>'
        f'<linearGradient id="{p}ac" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{s.acA}"/><stop offset="1" stop-color="{s.acB}"/></linearGradient>'
        f'<linearGradient id="{p}gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s.glass}" stop-opacity=".55"/><stop offset="1" stop-color="{s.glass}" stop-opacity=".22"/></linearGradient>'
        f'<filter id="{p}sh" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="26" stdDeviation="26" flood-color="{s.dark}" flood-opacity=".5"/></filter>'
        f'<filter id="{p}s2" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="{s.dark}" flood-opacity=".3"/></filter></defs>'
        f'<rect width="1024" height="1024" rx="230" fill="url(#{p}bg)"/><rect width="1024" height="1024" rx="230" fill="url(#{p}lo)"/><rect width="1024" height="1024" rx="230" fill="url(#{p}hl)"/>'
        f'{body}<rect x="4" y="4" width="1016" height="1016" rx="226" fill="none" stroke="#fff" stroke-opacity=".2" stroke-width="8"/></svg>')
# ---- shared carriers
def sheets(k,content,rot=4,brot=-9):
    return f'<g transform="rotate({brot} 512 540)">{R(250,214,470,610,70,k.G)}</g>'+k.sh(R(290,206,470,620,72,k.F)+E(290,206,470,620,72)+content,f'transform="rotate({rot} 512 540)"')
def tile(k,content,x=200,y=220,w=584,h=640,r=84,dx=46,dy=-46):
    return f'<g transform="translate({dx} {dy})">{R(x+20,y-20,w,h,r,k.G)}</g>'+k.sh(R(x,y,w,h,r,k.F)+E(x,y,w,h,r)+content)
def bubble_path(x=180,y=220,w=664,h=470,r=120,tail=140): 
    return f'M{x+r} {y}h{w-2*r}a{r} {r} 0 0 1 {r} {r}v{h-2*r}a{r} {r} 0 0 1-{r} {r}H{x+290}L{x+150} {y+h+tail}V{y+h}h-{150-r}a{r} {r} 0 0 1-{r}-{r}V{y+r}a{r} {r} 0 0 1 {r}-{r}z'
def bubble(k,content): return f'<g transform="translate(60 -50)">{R(230,210,560,430,120,k.G)}</g>'+k.sh(P(bubble_path(),k.F)+content)
# ---- 45 icons
def word(k): return sheets(k,R(352,300,250,74,37,k.A)+"".join(R(352,430+i*106,[346,346,210][i],56,28,k.lt) for i in range(3)))
def pages(k): return sheets(k,R(352,290,190,190,44,k.A)+R(578,300,120,56,28,k.lt)+R(578,400,120,56,28,k.lt)+R(352,540,346,56,28,k.lt)+R(352,646,230,56,28,k.lt))
def excel(k):
    cells="".join(R(238+c*176,360+r*150,152,126,30,k.A if (r,c)==(1,1) else k.lt2) for r in range(3) for c in range(3))
    return tile(k,P("M200 304a84 84 0 0 1 84-84h416a84 84 0 0 1 84 84v32H200z",k.A)+cells)
def numbers(k): return tile(k,R(280,560,120,210,36,k.lt)+R(432,430,120,340,36,k.lt)+R(584,300,120,470,36,k.A))
def ppt(k): return f'<g transform="translate(50 -56)">{R(190,250,620,440,70,k.G)}</g>'+k.sh(R(164,280,650,470,76,k.F)+E(164,280,650,470,76)+P("M390 515m-150 0a150 150 0 1 0 150-150v150z",k.A)+P("M416 339a150 150 0 0 1 150 150H416z",k.lt)+"".join(R(610,430+i*96,[150,110,150][i],54,27,k.lt) for i in range(3)))
def keynote(k): return S("M512 690v110M372 820h280",k.fgA,52)+f'<g transform="translate(46 -50)">{R(180,220,640,440,70,k.G)}</g>'+k.sh(R(160,240,704,470,76,k.F)+E(160,240,704,470,76)+C(380,475,125,k.A)+P("M560 600l130-240 130 240z".replace("560","545").replace("130-240 130 240","125-230 125 230"),k.lt,f'stroke="{k.lt}" stroke-width="36" stroke-linejoin="round"'))
def acrobat(k): return f'<g transform="rotate(8 512 540)">{R(300,200,470,620,72,k.G)}</g>'+k.sh(P("M322 196h270l170 170v398a72 72 0 0 1-72 72H322a72 72 0 0 1-72-72V268a72 72 0 0 1 72-72z",k.F)+P("M592 196l170 170H664a72 72 0 0 1-72-72z",k.lt)+S("M330 640c50-230 130-250 150-110s70 160 120 40 80-90 110 0",k.A,58),'transform="rotate(-4 512 540)"')
def grammarly(k): return C(512,512,350,k.G)+k.sh(C(512,512,270,k.F)+f'<circle cx="512" cy="512" r="267" fill="none" stroke="#fff" stroke-width="6"/>'+S("M380 520l96 96 176-200",k.A,84))
def quill(k): return sheets(k,S("M370 430h270l-80-80M654 650H384l80 80",k.A,64)+R(370,520,284,44,22,k.lt2),rot=-4,brot=8)
def xmind(k): return S("M430 512C640 512 600 270 800 270M430 512H800M430 512c210 0 170 242 370 242",k.fgA,44,'opacity=".9"')+C(800,270,64,k.lt2)+C(800,512,64,k.lt2)+C(800,754,64,k.lt2)+k.sh(R(140,372,400,280,140,k.F)+E(140,372,400,280,140)+R(230,484,220,56,28,k.A))
def mindnode(k):
    pts=[(210,260),(190,512),(210,764),(814,260),(834,512),(814,764)]
    return "".join(S(f"M512 512L{x} {y}",k.fgA,40,'opacity=".85"') for x,y in pts)+"".join(C(x,y,66,k.lt2) for x,y in pts)+C(512,512,220,k.G)+k.sh(C(512,512,160,k.F)+C(512,512,62,k.A))
def sniper(k): return k.s2(S("M220 400V310a90 90 0 0 1 90-90h90M624 220h90a90 90 0 0 1 90 90v90M804 624v90a90 90 0 0 1-90 90h-90M400 804h-90a90 90 0 0 1-90-90v-90",k.fgA,72))+k.sh(R(330,392,364,96,48,k.F)+R(330,536,240,96,48,k.lt2))
def deepl(k): return f'<g transform="translate(1094 150) scale(-1 1)">{P(bubble_path(250,250,480,340,100,110),k.G)}</g>'+k.sh(P(bubble_path(150,190,520,370,110,120),k.F)+R(250,300,320,64,32,k.A)+R(250,410,200,64,32,k.lt))
def elsa(k): return bubble(k,R(452,290,120,220,60,k.A)+S("M370 470a142 142 0 0 0 284 0M512 612v20",k.A,48))
def chatprd(k): return bubble(k,"".join(C(362+i*150,455,58,k.A if i<2 else k.lt) for i in range(3)))
def focus(k): return f'<circle cx="512" cy="548" r="262" fill="none" stroke="{k.glass}" stroke-opacity=".38" stroke-width="96"/>'+k.sh(S("M512 286a262 262 0 1 1-227 131",k.fgA,96)+S("M420 150h184",k.fgA,76)+C(512,548,84,k.F))
def dato(k): return C(512,512,360,k.G)+k.sh(C(512,512,290,k.F)+f'<circle cx="512" cy="512" r="287" fill="none" stroke="#fff" stroke-width="6"/>'+S("M512 512V340M512 512l130 84",k.A,64)+C(512,512,44,k.A))
def ynab(k): return f'<g transform="translate(44 -46)">{R(190,280,600,430,80,k.G)}</g>'+k.sh(R(160,300,620,440,84,k.F)+E(160,300,620,440,84)+S("M210 370l260 180 260-180",k.A,52))+k.sh(C(730,690,160,k.A)+f'<circle cx="730" cy="690" r="157" fill="none" stroke="#fff" stroke-opacity=".7" stroke-width="6"/><circle cx="730" cy="690" r="70" fill="none" stroke="{k.fgA}" stroke-width="40"/>')
def speechify(k):
    hs=[220,460,640,400,560,280]
    return "".join(R(150+i*130,512-h/2-30,84,h,42,k.G,'transform="translate(40 0)"') for i,h in enumerate(hs[:5]))+k.sh("".join(R(128+i*132,512-h/2,96,h,48,k.F if i%2==0 else k.lt2) for i,h in enumerate(hs)))
def stickies(k): return f'<g transform="rotate(-10 512 512)">{R(230,230,540,540,60,k.G)}</g>'+k.sh(P("M286 216h452a60 60 0 0 1 60 60v300L580 808H286a60 60 0 0 1-60-60V276a60 60 0 0 1 60-60z",k.F)+P("M580 808V636a60 60 0 0 1 60-60h158z",k.acB)+R(300,330,380,62,31,k.A)+R(300,450,380,62,31,k.A)+R(300,570,200,62,31,k.A),'transform="rotate(4 512 512)"')
def lumen(k): return tile(k,"".join(R(x,y,70,70,22,k.lt) for x in (188,714) for y in (300,430,560,690))+P("M430 400l210 122-210 122z",k.A,f'stroke="url(#{k.p}ac)" stroke-width="48" stroke-linejoin="round"'),x=150,y=240,w=672,h=560,r=84)
def canva(k): return C(400,400,210,k.G)+k.sh(R(430,300,400,400,96,k.F)+E(430,300,400,400,96))+k.s2(P("M210 800l170-290a34 34 0 0 1 60 0l170 290a34 34 0 0 1-30 50H240a34 34 0 0 1-30-50z","#FFE45C"))+C(630,500,92,k.BG)
def figma(k): return k.sh(R(190,190,300,300,150,"#F24E1E")+R(534,190,300,300,84,"#A259FF")+R(190,534,300,300,84,"#1ABCFE")+C(684,684,150,"#0ACF83"))+k.sh(P("M540 540l270 118-114 40-40 114z","#1E1E1E",'stroke="#fff" stroke-width="30" stroke-linejoin="round"'))
def teal(k): return S("M392 330v-60a64 64 0 0 1 64-64h112a64 64 0 0 1 64 64v60",k.fgA,64,'opacity=".9"')+k.sh(R(150,320,724,500,90,k.F)+E(150,320,724,500,90)+P("M150 540h724v-130a90 90 0 0 0-90-90H240a90 90 0 0 0-90 90z",k.lt2)+R(440,480,144,120,36,k.A))
def anki(k): return f'<g transform="rotate(-13 512 512)">{R(260,220,480,600,72,k.G)}</g>'+k.sh(R(280,214,480,610,74,k.F)+E(280,214,480,610,74)+R(344,310,300,72,36,k.A)+R(344,430,200,72,36,k.lt)+S("M300 600h440",k.lt2,14,'stroke-dasharray="30 26"')+R(344,680,260,72,36,k.lt),'transform="rotate(5 512 512)"')
def quizlet(k): return f'<g transform="rotate(12 512 512)">{R(270,220,480,600,72,k.G)}</g>'+k.sh(R(270,214,480,610,74,k.F)+E(270,214,480,610,74)+S("M400 500a130 130 0 1 1 50 122",k.A,64)+S("M360 590l92 36 22-100",k.A,64),'transform="rotate(-5 512 512)"')
def photomath(k): return tile(k,S("M300 390h150M375 315v150M560 390h150M322 600l106 106M428 600L322 706M560 610h150M560 700h150",k.A,56),x=200,y=200,w=624,h=624,r=110,dx=0,dy=0).replace(f'<g transform="translate(0 0)">',f'<g transform="rotate(-8 512 512)">')
def miro(k): return f'<g transform="translate(40 -44)">{R(170,250,664,470,70,k.G)}</g>'+k.sh(R(150,270,724,500,80,k.F)+R(220,340,200,200,36,"#FFD43B")+R(460,340,200,200,36,"#FF8FB1")+R(460,580,200,130,36,"#7CD4FF")+S("M700 440h40a50 50 0 0 1 50 50v110","#FFD43B",30)+C(790,640,40,"#FFD43B"))
def lucid(k): return S("M512 380v120M310 640v-70a70 70 0 0 1 70-70h264a70 70 0 0 1 70 70v70",k.fgA,48,'opacity=".9"')+k.sh(R(352,170,320,210,60,k.F)+E(352,170,320,210,60)+R(416,247,192,56,28,k.A))+k.sh(R(150,640,320,210,60,k.F)+R(554,640,320,210,60,k.lt2))
def wordwall(k): return S("M320 760l-60 130M704 760l60 130",k.fgA,60,'opacity=".9"')+f'<g transform="translate(40 -44)">{R(170,210,684,500,70,k.G)}</g>'+k.sh(R(140,230,744,540,84,k.F)+E(140,230,744,540,84)+"".join(R(206+c*216,296+r*216,180,180,40,k.A if (r+c)%2==0 else k.lt2) for r in range(2) for c in range(3)))
def fitbod(k): return k.sh(R(280,472,464,80,24,k.lt2)+R(236,330,130,364,50,k.F)+R(658,330,130,364,50,k.F)+R(130,400,106,224,44,k.F)+R(788,400,106,224,44,k.F),'transform="rotate(-38 512 512)"')
def mfp(k): return f'<circle cx="512" cy="512" r="240" fill="none" stroke="{k.glass}" stroke-opacity=".35" stroke-width="140"/>'+k.sh(S("M512 272a240 240 0 0 1 208 360",k.fgA,140)+S("M304 632a240 240 0 0 1 0-240",k.lt2,140))
def notion(k): return k.sh(R(214,206,596,150,54,k.A)+R(214,438,430,150,54,k.A)+R(214,670,596,150,54,k.A))+R(700,438,110,150,54,"#C9C9C4")+"".join(C(290,281+i*232,34,"#fff") for i in range(3))
def evernote(k): return "".join(R(170,270+i*124,170,60,30,k.G) for i in range(5))+k.sh(R(260,180,560,664,84,k.F)+E(260,180,560,664,84)+"".join(C(340,300+i*124,30,k.A) for i in range(5))+R(430,300,300,64,32,k.A)+R(430,424,300,64,32,k.lt)+R(430,548,190,64,32,k.lt))
def bear(k): return f'<g transform="rotate(9 512 512)">{R(240,220,540,560,70,k.G)}</g>'+k.sh(P("M286 206h452a66 66 0 0 1 66 66v300L580 818H286a66 66 0 0 1-66-66V272a66 66 0 0 1 66-66z",k.F)+P("M580 818V636a66 66 0 0 1 66-66h158z",k.lt)+S("M450 320l-50 290M610 320l-50 290M340 410h340M310 520h340",k.A,56),'transform="rotate(-4 512 512)"')
def todoist(k): return tile(k,"".join((C(320,340+i*170,56,k.A) if i==0 else f'<circle cx="320" cy="{340+i*170}" r="45" fill="none" stroke="{k.lt}" stroke-width="24"/>')+R(420,308+i*170,[290,220,260][i],64,32,k.lt2 if i==0 else k.lt) for i in range(3))+S("M294 340l20 20 34-40",k.fgA,22),x=200,y=200,w=624,h=624,r=96)
def things(k): return f'<g transform="rotate(-10 512 512)">{R(220,220,584,584,150,k.G)}</g>'+k.sh(R(212,212,600,600,160,k.F)+E(212,212,600,600,160)+S("M370 520l104 104 190-216",k.A,90),'transform="rotate(4 512 512)"')
def trello(k): return k.sh(R(150,200,220,624,60,k.F)+R(402,200,220,440,60,k.F)+R(654,200,220,280,60,k.lt2))+"".join(R(180,234+i*144,160,112,30,k.A if i<1 else k.lt) for i in range(4))+"".join(R(432,234+i*144,160,112,30,k.lt) for i in range(2))
def fantastical(k): return R(330,150,60,150,30,k.fgA)+R(634,150,60,150,30,k.fgA)+f'<g transform="translate(40 -40)">{R(190,230,640,600,84,k.G)}</g>'+k.sh(R(172,236,680,620,90,k.F)+E(172,236,680,620,90)+P("M172 440V326a90 90 0 0 1 90-90h500a90 90 0 0 1 90 90v114z",k.A)+"".join(R(250+c*146,500+r*150,100,100,30,k.A if (r,c)==(1,2) else k.lt2) for r in range(2) for c in range(4)))
def dayone(k): return k.sh(P("M512 290c-100-80-220-80-360-40v530c140-40 260-40 360 40z",k.F)+P("M512 290c100-80 220-80 360-40v530c-140-40-260-40-360 40z",k.lt2)+R(220,390,200,52,26,k.lt)+R(220,490,200,52,26,k.lt)+R(220,590,130,52,26,k.lt))+k.s2(P("M650 180h130v290l-65-56-65 56z",k.A))
def paste(k): return R(382,150,260,150,56,k.lt2)+k.sh(R(212,220,600,650,84,k.F)+E(212,220,600,650,84)+R(440,186,144,64,32,k.A)+R(280,370,464,120,36,k.A)+R(280,530,464,120,36,"#FF9EC8")+R(280,690,464,120,36,"#FFD36E"))
def raycast(k): return R(190,560,644,96,48,k.G)+R(190,700,644,96,48,k.G)+k.sh(R(120,250,784,240,120,k.F)+E(120,250,784,240,120)+f'<circle cx="270" cy="360" r="60" fill="none" stroke="url(#{k.p}ac)" stroke-width="40"/>'+S("M315 405l50 50",k.A,40)+R(440,334,330,60,30,k.lt))
def magnet(k): return R(130,190,764,644,90,k.G)+k.sh(R(176,236,320,552,56,k.F)+E(176,236,320,552,56))+k.s2(R(528,236,320,260,56,k.F)+R(528,528,320,260,56,k.lt2))
def otter(k): return k.sh(R(190,160,220,400,110,k.F)+S("M110 440a190 190 0 0 0 380 0M300 630v130M200 780h200",k.fgA,60))+k.s2(R(580,250,290,84,42,k.F)+R(580,400,210,84,42,k.lt2)+R(580,550,290,84,42,k.lt2)+R(580,700,150,84,42,k.lt2))
def duo(k):
    star=" ".join(f"{512+(150 if i%2==0 else 66)*math.sin(math.radians(i*36)):.0f},{460-(150 if i%2==0 else 66)*math.cos(math.radians(i*36)):.0f}" for i in range(10))
    return bubble(k,f'<polygon points="{star}" fill="{k.A}" stroke="url(#{k.p}ac)" stroke-width="34" stroke-linejoin="round"/>')
SPEC=[("document-editor",word,"#57A6FF","#1B55C4"),("alt-pages",pages,"#FFC046","#F07A0A"),("spreadsheet",excel,"#46D184","#0B7A3F"),("alt-numbers",numbers,"#6BE677","#17A035"),
("slide-maker",ppt,"#FF8A5C","#C6361A"),("alt-keynote",keynote,"#5CBBFF","#126BE0"),("pdf-chat",acrobat,"#FF6259","#B5120E"),("grammar-checker",grammarly,"#3BE0B0","#07946F"),("rewriter",quill,"#7CCB7E","#2F8545"),
("mind-map",xmind,"#FF8559","#DE331C"),("alt-mindnode",mindnode,"#BE96FF","#6442DC"),("image-to-text",sniper,"#9A88FF","#4633D2"),("translator",deepl,"#3A6EA8","#0C2540"),("speaking-coach",elsa,"#9A78FF","#4527CC"),
("thinking-partner",chatprd,"#4A4A52","#0E0E11",dict(acA="#55555E",acB="#17171B")),("pomodoro",focus,"#FF7A6B","#D52420"),("world-clock",dato,"#6A7A9C","#1E2638"),("budget",ynab,"#7A96FF","#2D49D4"),("read-aloud",speechify,"#5C78FF","#1526DC"),
("sticky-notes",stickies,"#FFE873","#F5AE00",dict(fgA="#FFFDF0",fgB="#FFF3C2",acA="#F5B400",acB="#E09400",dark="#8A5A00")),("video-studio",lumen,"#9A8AFF","#4630DC"),("design-studio",canva,"#16D4DC","#7C3BF4"),
("alt-figma",figma,"#FFFFFF","#E6E6E3",dict(dark="#8C8C86")),("job-search",teal,"#3AD3C0","#06806F"),("flashcards",anki,"#7ACBFF","#1E7EDC"),("alt-quizlet",quizlet,"#7A88FF","#2F3DE2"),
("homework-helper",photomath,"#FF6B70","#CC1A26"),("whiteboard",miro,"#FFE65C","#FFBE00",dict(fgA="#34343A",fgB="#141418",dark="#8A6400",glass="#3A3A3A")),("alt-lucidchart",lucid,"#FFA257","#EA540A"),("classroom",wordwall,"#5CADFF","#1759D4"),
("fitness-coach",fitbod,"#FF6C88","#D61944"),("alt-myfitnesspal",mfp,"#4DA6FF","#0652DC"),("alt-notion",notion,"#FFFFFF","#E6E6E3",dict(acA="#4A4A4A",acB="#141414",dark="#8C8C86")),("alt-evernote",evernote,"#4AD768","#06942A"),
("alt-bear",bear,"#FF7A75","#C42A2A"),("alt-todoist",todoist,"#FF705E","#CE2B1B"),("alt-things",things,"#68B4FF","#1A64E4"),("alt-trello",trello,"#4AA8F0","#075CAA"),
("alt-fantastical",fantastical,"#FF7A7A","#D12436"),("alt-day-one",dayone,"#6AD8FF","#1894E4"),("alt-paste",paste,"#D08AFF","#7334DC"),("alt-raycast",raycast,"#FF7A7A","#861818"),
("alt-magnet",magnet,"#7A9AFF","#2944CC"),("alt-otter",otter,"#5C9AFF","#1052D2"),("alt-duolingo",duo,"#8BE62F","#3E9A00")]
out=pathlib.Path(sys.argv[1]); out.mkdir(exist_ok=True)
for i,s in enumerate(SPEC):
    kw=s[4] if len(s)>4 else {}
    k=K("v"+str(i),s[2],s[3],**kw); (out/f"{s[0]}.svg").write_text(k.svg(s[1](k)))
h='<body style="margin:0;background:#FAF9F5;display:flex;flex-wrap:wrap;gap:20px;padding:26px;font:11px system-ui">'+"".join(f'<div style="text-align:center;width:122px"><img src="{s[0]}.svg" width="116"><br>{s[0]}<br><img src="{s[0]}.svg" width="30"></div>' for s in SPEC)+'</body>'
(out/"sheet.html").write_text(h); print(len(SPEC))
