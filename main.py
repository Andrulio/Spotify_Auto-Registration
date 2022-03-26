# coding: utf8
# -*- coding: utf-8 -*-
import requests
import string as st
import random
import time
import pyfiglet
global start_time
payload = {
    "collect_personal_info": "undefined",
    "creation_flow": "",
    "creation_point": "https://www.spotify.com/ru-ru/signup/",
    "gender": "male",
    "iagree": "1",
    "platform": "www",
    "referrer": "",
    "send-email": "1",
    "thirdpartyemail": "1",
}
def generate_random_string(length):
    letters = st.ascii_lowercase
    global rand_string
    rand_string = ''.join(random.choice(letters) for i in range(length))
def baner():
    ascii_banner = pyfiglet.figlet_format("   Spotify Maker")
    print(ascii_banner)
def main():
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'sp_m=ru-ru; sp_t=2a89a2ef-1998-4642-b48b-a76a7c250a76; sp_new=1; sp_landing=https%3A%2F%2Fwww.spotify.com%2Fru-ru%2Fsignup%2F; __Host-sp_csrf_sid=97c76b4e1d2c2b2ec2c2c3bc0d221bb90588c12264588a09daf421cc321efd5a; _gcl_au=1.1.163465826.1629471732; OptanonConsent=isIABGlobal=false&datestamp=Fri+Aug+20+2021+18%3A02%3A13+GMT%2B0300+(Eastern+European+Summer+Time)&version=6.21.0&hosts=&landingPath=https%3A%2F%2Fwww.spotify.com%2Fru-ru%2Fsignup%2F%3Fforward_url%3Dhttps%253A%252F%252Fwww.spotify.com%252Fru-ru%252Fpurchase%252Foffer%252Fdefault-trial-1m%252F%253Fcountry%253DRU%26sp_t_counter%3D1&groups=s00%3A1%2Cf00%3A1%2Cm00%3A1%2Ct00%3A1%2Ci00%3A1; _ga=GA1.1.2127814292.1629471734; _fbp=fb.1.1629471733637.223759738; sp_adid=018f5ec7-8b58-452e-ad87-ca306cd1f7d4; _ga_S35RN5WNT2=GS1.1.1629471732.1.1.1629471763.29',
        'Origin': 'https://www.spotify.com',
        'Referer': 'https://www.spotify.com/ru-ru/signup/?forward_url=https%3A%2F%2Fwww.spotify.com%2Fru-ru%2Fpurchase%2Foffer%2Fdefault-trial-1m%2F%3Fcountry%3DRU&sp_t_counter=1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'
    }
    year = '2000'
    key = "a1e486e2729f46d6bb368d6b2bcda326"
    global repeats
    repeats = int(input("Pieces of accounts: "))
    y = 0
    global start_time
    start_time = time.time()
    for y in range(repeats):
        day = random.randrange(10, 29)
        month = random.randrange(10, 12)
        generate_random_string(16)
        email = rand_string + "@gmail.com"
        generate_random_string(16)
        password = rand_string

        x = {
            "birth_day": day,
            "birth_month": month,
            "birth_year": year,
            "displayname": email,
            "key": key,
            "email": email,
            "password": password,
            "password_repeat": password
        }
        payload.update(x)
        response = requests.post("https://spclient.wg.spotify.com/signup/public/v1/account", params=payload,
                                 headers=header)

        if response.status_code == 200:
            y = y + 1
            print(f"Successfully done: {email}:{password}[{str(y)}/{str(repeats)}]")
            f = open("accounts.txt", "a+")
            f.write((email + ":" + password) + '\n')
        else:
            print("Error...")
if __name__ == "__main__":
        baner()
        main()
        print("--- %s seconds ---" % (time.time() - start_time))
        input('Press Enter to exit')