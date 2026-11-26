"""Builds the app icons as 1024x1024 SVGs (full-bleed squircle tile).
Run: python3 data/icons/build_icons.py  -> data/icons/<id>.svg + preview.html"""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))

def tile(id_, c1, c2, body, extra_defs="", sheen=.22):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<radialGradient id="sh" cx=".28" cy=".05" r=".9"><stop offset="0" stop-color="#fff" stop-opacity="{sheen}"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></radialGradient>
<filter id="ds" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="22" stdDeviation="26" flood-color="#000" flood-opacity=".28"/></filter>
<filter id="ds2" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".22"/></filter>
{extra_defs}
</defs>
<rect width="1024" height="1024" rx="230" fill="url(#bg)"/>
<rect width="1024" height="1024" rx="230" fill="url(#sh)"/>
{body}
<rect x="3" y="3" width="1018" height="1018" rx="228" fill="none" stroke="#fff" stroke-opacity=".14" stroke-width="6"/>
</svg>'''

I = {}

# Document Editor: lifted paper sheet + gold fountain-pen nib
I["document-editor"] = tile("de", "#3D7BFF", "#1638B5", '''
<g filter="url(#ds)" transform="rotate(-7 512 520)">
 <path d="M282 190h360l118 118v526a30 30 0 0 1-30 30H282a30 30 0 0 1-30-30V220a30 30 0 0 1 30-30z" fill="#fff"/>
 <path d="M642 190v88a30 30 0 0 0 30 30h88z" fill="#D7E2FF"/>
 <rect x="320" y="290" width="250" height="40" rx="20" fill="#2F64F5"/>
 <rect x="320" y="380" width="380" height="24" rx="12" fill="#C9D3E8"/>
 <rect x="320" y="436" width="380" height="24" rx="12" fill="#C9D3E8"/>
 <rect x="320" y="492" width="300" height="24" rx="12" fill="#C9D3E8"/>
 <rect x="320" y="572" width="380" height="24" rx="12" fill="#C9D3E8"/>
 <rect x="320" y="628" width="220" height="24" rx="12" fill="#C9D3E8"/>
</g>
<g filter="url(#ds2)" transform="translate(690 690) rotate(45)">
 <path d="M-62-230h124v150c0 40-14 80-40 118L0 70l-22-32c-26-38-40-78-40-118z" fill="url(#gold)"/>
 <path d="M0-70v128" stroke="#7A4A06" stroke-width="10" stroke-linecap="round"/>
 <circle cx="0" cy="-78" r="18" fill="#7A4A06"/>
 <rect x="-70" y="-300" width="140" height="84" rx="16" fill="#20242E"/>
</g>''', '<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE08A"/><stop offset="1" stop-color="#E0A21C"/></linearGradient>')

# Spreadsheet: grid card with a selected cell + rising bars
cells = "".join(f'<rect x="{262+c*128}" y="{372+r*104}" width="120" height="96" rx="10" fill="{"#E6F7EE" if r==0 else "#F4F6F5"}"/>' for r in range(4) for c in range(4))
cells2 = "".join(f'<rect x="{214+c*128}" y="{254+r*104}" width="120" height="96" rx="10" fill="{"#E6F7EE" if r==0 or c==0 else "#F4F6F5"}"/>' for r in range(4) for c in range(4))
I["spreadsheet"] = tile("xl", "#2BD27A", "#0B8443", f'''
<g filter="url(#ds)" transform="rotate(-4 470 470)">
 <rect x="190" y="230" width="548" height="460" rx="40" fill="#fff"/>
 {cells2}
 <rect x="470" y="462" width="120" height="96" rx="10" fill="#DFF7EA" stroke="#0E9F52" stroke-width="12"/>
 <rect x="574" y="542" width="30" height="30" rx="6" fill="#0E9F52" stroke="#fff" stroke-width="6"/>
</g>
<g filter="url(#ds)">
 <rect x="520" y="560" width="330" height="250" rx="34" fill="#13301F"/>
 <rect x="566" y="700" width="46" height="70" rx="10" fill="#5BE39A"/>
 <rect x="636" y="650" width="46" height="120" rx="10" fill="#8BF0B8"/>
 <rect x="706" y="610" width="46" height="160" rx="10" fill="#C8FADC"/>
 <path d="M566 660l70-40 70 10 90-60" fill="none" stroke="#FFD45C" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
</g>''')

# Slide Maker: stacked slides, front one with a donut chart and title
I["slide-maker"] = tile("pp", "#FF9A4A", "#E2471A", '''
<rect x="250" y="250" width="560" height="380" rx="34" fill="#fff" opacity=".35" transform="rotate(8 530 440)"/>
<rect x="230" y="270" width="560" height="380" rx="34" fill="#fff" opacity=".6" transform="rotate(4 510 460)"/>
<g filter="url(#ds)">
 <rect x="200" y="300" width="624" height="420" rx="36" fill="#fff"/>
 <rect x="256" y="360" width="220" height="36" rx="18" fill="#2A2F3A"/>
 <rect x="256" y="424" width="170" height="22" rx="11" fill="#D5D9E0"/>
 <rect x="256" y="470" width="190" height="22" rx="11" fill="#D5D9E0"/>
 <rect x="256" y="516" width="150" height="22" rx="11" fill="#D5D9E0"/>
 <circle cx="650" cy="510" r="118" fill="none" stroke="#FFD25E" stroke-width="64"/>
 <path d="M650 392a118 118 0 0 1 112 154" fill="none" stroke="#F25A22" stroke-width="64"/>
 <path d="M762 546a118 118 0 0 1-60 70" fill="none" stroke="#2A2F3A" stroke-width="64"/>
</g>
<g filter="url(#ds2)"><rect x="492" y="720" width="40" height="110" rx="12" fill="#fff"/><rect x="392" y="812" width="240" height="40" rx="20" fill="#fff"/></g>''')

# PDF Chat: document with red band + chat bubble
I["pdf-chat"] = tile("pdf", "#FF5A67", "#C2102B", '''
<g filter="url(#ds)" transform="rotate(-5 470 480)">
 <path d="M240 170h330l120 120v500a30 30 0 0 1-30 30H240a30 30 0 0 1-30-30V200a30 30 0 0 1 30-30z" fill="#fff"/>
 <path d="M570 170v90a30 30 0 0 0 30 30h90z" fill="#FFD3D8"/>
 <rect x="262" y="250" width="180" height="70" rx="16" fill="#E3192F"/>
 <text x="352" y="302" text-anchor="middle" font-family="-apple-system,Helvetica,Arial" font-weight="800" font-size="50" fill="#fff">PDF</text>
 <rect x="262" y="370" width="360" height="24" rx="12" fill="#D9DCE3"/>
 <rect x="262" y="424" width="360" height="24" rx="12" fill="#FFE27A"/>
 <rect x="262" y="478" width="300" height="24" rx="12" fill="#D9DCE3"/>
 <rect x="262" y="532" width="340" height="24" rx="12" fill="#D9DCE3"/>
</g>
<g filter="url(#ds)">
 <path d="M560 560h230a70 70 0 0 1 70 70v120a70 70 0 0 1-70 70H700l-80 70v-70h-60a70 70 0 0 1-70-70V630a70 70 0 0 1 70-70z" fill="#22263A"/>
 <circle cx="600" cy="690" r="26" fill="#fff"/><circle cx="675" cy="690" r="26" fill="#fff"/><circle cx="750" cy="690" r="26" fill="#fff"/>
</g>''')

# Grammar Checker: big serif "a", red squiggle, green check badge
I["grammar-checker"] = tile("gc", "#22CDB0", "#08806F", '''
<g filter="url(#ds)">
 <text x="470" y="700" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-weight="700" font-size="620" fill="#fff">a</text>
</g>
<path d="M230 790q35-40 70 0t70 0 70 0 70 0 70 0 70 0" fill="none" stroke="#FF5B5B" stroke-width="26" stroke-linecap="round"/>
<g filter="url(#ds2)">
 <circle cx="740" cy="330" r="128" fill="#fff"/>
 <path d="M680 332l45 45 85-95" fill="none" stroke="#0FA88C" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>
</g>''')

# Mind Map: glossy center pill with organic colored branches
def br(x1,y1,x2,y2,col):
    cx=(x1+x2)/2
    return f'<path d="M{x1} {y1}C{cx} {y1} {cx} {y2} {x2} {y2}" fill="none" stroke="{col}" stroke-width="22" stroke-linecap="round"/><rect x="{x2-(0 if x2>x1 else 150)}" y="{y2-34}" width="150" height="68" rx="34" fill="{col}"/>'
I["mind-map"] = tile("mm", "#8B6BFF", "#3A1EC0", '''
<g filter="url(#ds2)">''' + br(512,512,700,290,"#FF6FA8") + br(512,512,720,512,"#FFD45C") + br(512,512,700,734,"#5CE1E6") + br(512,512,324,330,"#9CF06B") + br(512,512,324,694,"#FF9F5A") + '''</g>
<g filter="url(#ds)"><rect x="362" y="420" width="300" height="184" rx="56" fill="#fff"/><rect x="410" y="472" width="204" height="34" rx="17" fill="#4B2FD6"/><rect x="410" y="526" width="140" height="26" rx="13" fill="#C9C2F5"/></g>''')

# Image to Text: photo card with scan brackets + laser line + text card
I["image-to-text"] = tile("ocr", "#39CBFF", "#0A6FD0", '''
<g filter="url(#ds)" transform="rotate(-6 420 450)">
 <rect x="200" y="230" width="440" height="380" rx="34" fill="#fff"/>
 <rect x="226" y="256" width="388" height="328" rx="20" fill="#BFE9FF"/>
 <circle cx="530" cy="330" r="38" fill="#FFC94A"/>
 <path d="M226 584l120-170 90 110 60-70 118 130z" fill="#1E9E6A"/>
 <path d="M226 584l120-170 70 86-50 84z" fill="#167A52"/>
</g>
<g fill="none" stroke="#fff" stroke-width="30" stroke-linecap="round">
 <path d="M150 300v-90a50 50 0 0 1 50-50h90"/><path d="M734 160h90a50 50 0 0 1 50 50v90"/>
 <path d="M874 724v90a50 50 0 0 1-50 50h-90"/><path d="M290 864h-90a50 50 0 0 1-50-50v-90"/>
</g>
<g filter="url(#ds)">
 <rect x="470" y="540" width="350" height="250" rx="30" fill="#fff"/>
 <rect x="510" y="590" width="200" height="28" rx="14" fill="#0A6FD0"/>
 <rect x="510" y="646" width="270" height="22" rx="11" fill="#C8D6E6"/>
 <rect x="510" y="692" width="230" height="22" rx="11" fill="#C8D6E6"/>
 <rect x="510" y="738" width="160" height="22" rx="11" fill="#C8D6E6"/>
</g>
<rect x="120" y="496" width="784" height="16" rx="8" fill="#FF4D6D" opacity=".9"/>''')

# Pomodoro: glossy tomato with a timer arc, on cream
I["pomodoro"] = tile("pomo", "#FFF3E6", "#FFD3B8", '''
<g filter="url(#ds)">
 <ellipse cx="512" cy="580" rx="310" ry="275" fill="url(#tom)"/>
 <ellipse cx="400" cy="450" rx="90" ry="44" fill="#fff" opacity=".35" transform="rotate(-28 400 450)"/>
 <path d="M512 318c-40-40-110-40-150-10 50 0 80 20 96 40-60 0-110 30-130 70 60-26 110-30 150-18 10 40 60 50 64 50s54-10 64-50c40-12 90-8 150 18-20-40-70-70-130-70 16-20 46-40 96-40-40-30-110-30-150 10z" fill="#2FA84F"/>
 <path d="M512 330c0-50 10-90 40-120" fill="none" stroke="#1F7A38" stroke-width="24" stroke-linecap="round"/>
 <text x="512" y="700" text-anchor="middle" font-family="-apple-system,'SF Pro Rounded',Helvetica,Arial" font-weight="800" font-size="210" fill="#fff" letter-spacing="-6">25</text>
</g>''',
 '<radialGradient id="tom" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#FF7A5C"/><stop offset="1" stop-color="#D9271C"/></radialGradient>', sheen=.5)

# World Clock: day/night split face
I["world-clock"] = tile("wc", "#22337E", "#0A1238", '''
<defs><clipPath id="face"><circle cx="512" cy="512" r="320"/></clipPath></defs>
<g filter="url(#ds)"><circle cx="512" cy="512" r="320" fill="#fff"/></g>
<g clip-path="url(#face)">
 <rect x="0" y="0" width="1024" height="1024" fill="url(#day)"/>
 <path d="M150 1000L1000 150V1024H150z" fill="#14205A"/>
 <circle cx="390" cy="380" r="70" fill="#FFF6C9"/>
 <circle cx="660" cy="690" r="10" fill="#fff"/><circle cx="730" cy="600" r="7" fill="#fff"/><circle cx="600" cy="780" r="6" fill="#fff"/>
 <path d="M720 700a70 70 0 1 1-80-90 55 55 0 1 0 80 90z" fill="#FFE27A"/>
</g>
<circle cx="512" cy="512" r="320" fill="none" stroke="#fff" stroke-width="22"/>
<path d="M512 512V330M512 512l120 70" stroke="#fff" stroke-width="30" stroke-linecap="round"/>
<circle cx="512" cy="512" r="30" fill="#fff"/>''',
 '<linearGradient id="day" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFB45C"/><stop offset=".5" stop-color="#5CB8FF"/></linearGradient>')

# Sticky Notes: stacked colored notes, curled corner
I["sticky-notes"] = tile("sn", "#34343C", "#16161A", '''
<rect x="300" y="200" width="460" height="460" rx="28" fill="#7FE3C4" transform="rotate(12 530 430)" filter="url(#ds2)"/>
<rect x="270" y="240" width="460" height="460" rx="28" fill="#FF8FB1" transform="rotate(-8 500 470)" filter="url(#ds2)"/>
<g filter="url(#ds)" transform="rotate(3 512 560)">
 <path d="M262 330h500v360l-110 110H262z" fill="#FFD84D"/>
 <path d="M762 690H682a30 30 0 0 0-30 30v80z" fill="#E8B92A"/>
 <rect x="316" y="410" width="52" height="52" rx="12" fill="none" stroke="#8A6A00" stroke-width="12"/>
 <path d="M326 436l16 16 30-36" fill="none" stroke="#8A6A00" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="398" y="424" width="250" height="24" rx="12" fill="#B58D00" opacity=".55"/>
 <rect x="316" y="510" width="52" height="52" rx="12" fill="none" stroke="#8A6A00" stroke-width="12"/>
 <rect x="398" y="524" width="210" height="24" rx="12" fill="#8A6A00"/>
 <rect x="316" y="610" width="52" height="52" rx="12" fill="none" stroke="#8A6A00" stroke-width="12"/>
 <rect x="398" y="624" width="170" height="24" rx="12" fill="#8A6A00"/>
</g>''')

# Translator: two overlapping bubbles 文 / A
I["translator"] = tile("tr", "#4F7BFF", "#1BB5C9", '''
<g filter="url(#ds2)">
 <path d="M200 220h360a60 60 0 0 1 60 60v220a60 60 0 0 1-60 60H340l-90 80v-80h-50a60 60 0 0 1-60-60V280a60 60 0 0 1 60-60z" fill="#fff" opacity=".92"/>
 <text x="380" y="485" text-anchor="middle" font-family="'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif" font-weight="700" font-size="230" fill="#3554E0">文</text>
</g>
<g filter="url(#ds)">
 <path d="M470 440h360a60 60 0 0 1 60 60v220a60 60 0 0 1-60 60h-50v80l-90-80H470a60 60 0 0 1-60-60V500a60 60 0 0 1 60-60z" fill="#1A2350"/>
 <text x="650" y="712" text-anchor="middle" font-family="-apple-system,Helvetica,Arial" font-weight="800" font-size="240" fill="#5FF0E0">A</text>
</g>''')

# Speaking Coach: mic with sound waves
I["speaking-coach"] = tile("sc", "#FF6BAA", "#C2185B", '''
<g fill="none" stroke="#fff" stroke-linecap="round">
 <path d="M240 400q-50 110 0 220" stroke-width="30" stroke-opacity=".55"/><path d="M784 400q50 110 0 220" stroke-width="30" stroke-opacity=".55"/>
 <path d="M310 440q-30 70 0 140" stroke-width="30"/><path d="M714 440q30 70 0 140" stroke-width="30"/>
</g>
<g filter="url(#ds)">
 <rect x="402" y="180" width="220" height="400" rx="110" fill="url(#mic)"/>
 <path d="M440 300h144M440 360h144M440 420h144" stroke="#C9CDD6" stroke-width="14" stroke-linecap="round"/>
 <path d="M352 500a160 160 0 0 0 320 0" fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round"/>
 <rect x="495" y="660" width="34" height="120" rx="17" fill="#fff"/>
 <rect x="400" y="770" width="224" height="40" rx="20" fill="#fff"/>
</g>''', '<linearGradient id="mic" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#E4E7EE"/></linearGradient>')

# Video Studio: video frame with play button over a keyframed timeline
I["video-studio"] = tile("vs", "#FF6B4A", "#C2185B", '''
<g filter="url(#ds)" transform="rotate(-5 500 420)">
 <rect x="190" y="210" width="620" height="400" rx="40" fill="#1B1530"/>
 <rect x="222" y="242" width="556" height="336" rx="22" fill="url(#vsky)"/>
 <path d="M222 520l150-120 110 90 90-70 206 150v8a22 22 0 0 1-22 22H244a22 22 0 0 1-22-22z" fill="#2B1F4F" opacity=".85"/>
 <circle cx="500" cy="410" r="86" fill="#fff"/>
 <path d="M472 362l82 48-82 48z" fill="#E0245E"/>
</g>
<g filter="url(#ds)">
 <rect x="170" y="668" width="684" height="150" rx="36" fill="#fff"/>
 <rect x="214" y="706" width="250" height="30" rx="10" fill="#FF8A65"/>
 <rect x="478" y="706" width="170" height="30" rx="10" fill="#7C4DFF"/>
 <rect x="662" y="706" width="150" height="30" rx="10" fill="#26C6DA"/>
 <rect x="214" y="752" width="598" height="22" rx="8" fill="#ECE7F3"/>
 <path d="M330 763l14-14 14 14-14 14zM560 763l14-14 14 14-14 14zM720 763l14-14 14 14-14 14z" fill="#1B1530"/>
 <rect x="436" y="684" width="10" height="114" rx="5" fill="#E0245E"/>
</g>''', '<linearGradient id="vsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB86B"/><stop offset="1" stop-color="#FF5E7E"/></linearGradient>')

# Design Studio: phone screen with colorful blocks and a pen-tool bezier
I["design-studio"] = tile("ds", "#FF5CC8", "#7B1FA2", '''
<g filter="url(#ds)" transform="rotate(-8 430 500)">
 <rect x="250" y="160" width="360" height="700" rx="64" fill="#15121F"/>
 <rect x="272" y="182" width="316" height="656" rx="46" fill="#fff"/>
 <rect x="404" y="200" width="52" height="14" rx="7" fill="#15121F"/>
 <rect x="300" y="238" width="260" height="170" rx="26" fill="url(#dsg)"/>
 <rect x="300" y="432" width="170" height="26" rx="13" fill="#2A2438"/>
 <rect x="300" y="474" width="230" height="18" rx="9" fill="#D7D2E2"/>
 <rect x="300" y="506" width="200" height="18" rx="9" fill="#D7D2E2"/>
 <rect x="300" y="556" width="120" height="120" rx="24" fill="#FFD54F"/>
 <rect x="440" y="556" width="120" height="120" rx="24" fill="#4DD0E1"/>
 <rect x="300" y="700" width="260" height="60" rx="30" fill="#7C4DFF"/>
</g>
<g filter="url(#ds2)">
 <path d="M560 790C620 600 760 640 820 470" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round"/>
 <path d="M560 790L650 700M820 470L760 560" stroke="#fff" stroke-width="6" stroke-dasharray="14 10" opacity=".85"/>
 <rect x="538" y="768" width="44" height="44" rx="8" fill="#fff" stroke="#7B1FA2" stroke-width="8"/>
 <rect x="798" y="448" width="44" height="44" rx="8" fill="#fff" stroke="#7B1FA2" stroke-width="8"/>
 <circle cx="650" cy="700" r="16" fill="#fff"/><circle cx="760" cy="560" r="16" fill="#fff"/>
</g>''', '<linearGradient id="dsg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF8A80"/><stop offset="1" stop-color="#7C4DFF"/></linearGradient>')

# Thinking Partner: question bubble over a checked decision list
I["thinking-partner"] = tile("tp", "#FFC94D", "#EF7A00", '''
<g filter="url(#ds)" transform="rotate(4 560 640)">
 <rect x="360" y="430" width="470" height="420" rx="44" fill="#fff"/>
 <rect x="404" y="486" width="56" height="56" rx="16" fill="#2EB872"/>
 <path d="M418 514l12 12 20-24" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="484" y="500" width="290" height="28" rx="14" fill="#3B2A12"/>
 <rect x="404" y="584" width="56" height="56" rx="16" fill="#2EB872"/>
 <path d="M418 612l12 12 20-24" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="484" y="598" width="240" height="28" rx="14" fill="#3B2A12"/>
 <rect x="404" y="682" width="56" height="56" rx="16" fill="none" stroke="#E0C9A6" stroke-width="8"/>
 <rect x="484" y="696" width="270" height="28" rx="14" fill="#E9DCC6"/>
 <rect x="404" y="770" width="56" height="56" rx="16" fill="none" stroke="#E0C9A6" stroke-width="8"/>
 <rect x="484" y="784" width="200" height="28" rx="14" fill="#E9DCC6"/>
</g>
<g filter="url(#ds)">
 <path d="M200 170h330a80 80 0 0 1 80 80v170a80 80 0 0 1-80 80H330l-100 86v-86h-30a80 80 0 0 1-80-80V250a80 80 0 0 1 80-80z" fill="#2B1D0E"/>
 <text x="365" y="440" text-anchor="middle" font-family="-apple-system,'SF Pro Rounded',Helvetica,Arial" font-weight="900" font-size="300" fill="#FFC94D">?</text>
</g>''')

# Store: an App Store-style "A" built from three rounded bars, in Claude's colors, with the Claude spark
I["store"] = tile("store", "#E58B68", "#B9532F", '''
<g filter="url(#ds)" stroke-linecap="round" fill="none">
 <path d="M512 262L318 706" stroke="url(#stA)" stroke-width="92"/>
 <path d="M512 262L706 706" stroke="url(#stB)" stroke-width="92"/>
 <path d="M300 572H724" stroke="#FAF9F5" stroke-width="80"/>
</g>
<g filter="url(#ds2)" transform="translate(770 250)">
 <rect x="-11" y="-96" width="22" height="78" rx="11" fill="#FAF9F5" transform="rotate(0)"/><rect x="-11" y="-78" width="22" height="60" rx="11" fill="#FAF9F5" transform="rotate(37)"/><rect x="-11" y="-92" width="22" height="74" rx="11" fill="#FAF9F5" transform="rotate(60)"/><rect x="-11" y="-74" width="22" height="56" rx="11" fill="#FAF9F5" transform="rotate(97)"/><rect x="-11" y="-96" width="22" height="78" rx="11" fill="#FAF9F5" transform="rotate(120)"/><rect x="-11" y="-80" width="22" height="62" rx="11" fill="#FAF9F5" transform="rotate(157)"/><rect x="-11" y="-90" width="22" height="72" rx="11" fill="#FAF9F5" transform="rotate(180)"/><rect x="-11" y="-76" width="22" height="58" rx="11" fill="#FAF9F5" transform="rotate(217)"/><rect x="-11" y="-96" width="22" height="78" rx="11" fill="#FAF9F5" transform="rotate(240)"/><rect x="-11" y="-78" width="22" height="60" rx="11" fill="#FAF9F5" transform="rotate(277)"/><rect x="-11" y="-92" width="22" height="74" rx="11" fill="#FAF9F5" transform="rotate(300)"/><rect x="-11" y="-74" width="22" height="56" rx="11" fill="#FAF9F5" transform="rotate(337)"/><circle r="26" fill="#FAF9F5"/>
</g>''', '<linearGradient id="stA" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F3E9DF"/></linearGradient><linearGradient id="stB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EADCCD"/></linearGradient>', sheen=.28)

import re
def ns(k, v):
    # namespace ids so many icons can be inlined on one page
    ids = set(re.findall(r'id="([^"]+)"', v))
    for i in ids:
        v = v.replace(f'id="{i}"', f'id="{k}-{i}"').replace(f'url(#{i})', f'url(#{k}-{i})')
    return re.sub(r">\s+<", "><", v).strip()
for k, v in I.items():
    I[k] = ns(k, v)
    open(os.path.join(HERE, k + ".svg"), "w").write(I[k])
cards = "".join(f'<figure><img src="{k}.svg"><figcaption>{k}</figcaption></figure>' for k in I)
open(os.path.join(HERE, "preview.html"), "w").write(f'<!doctype html><meta charset=utf-8><body style="margin:0;padding:30px;background:#ececf0;font:13px -apple-system;display:grid;grid-template-columns:repeat(7,150px);gap:26px">{cards}<style>img{{width:150px;height:150px}}figure{{margin:0;text-align:center}}</style>')
print(len(I), "icons")
