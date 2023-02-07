import requests, os, hashlib, time, json, string, random
from threading import RLock, Thread
from colorama import init, Fore, Style, Back
from colorama import init as colorama_init
from capmonster_python import HCaptchaTask
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System 
import secrets

config = json.load(open('./config.json', 'r'))

class SynchronizedEcho(object):
    print_lock = RLock()

    def __init__(self, global_lock=True):
        if not global_lock:
            self.print_lock = RLock()

    def __call__(self, msg):
        with self.print_lock:
            print(msg)

def randomPassword(length):
    all = string.ascii_lowercase + string.ascii_uppercase +  string.digits
    passw = "".join(random.sample(all, length))
    return passw

def getheaders(Token):
    header = {
        'Authorization': Token,
		'accept': '*/*',
		'accept-language': 'en-US',
		'connection': 'keep-alive',
		'cookie': f'__cfduid = {secrets.token_hex(43)}; __dcfduid={secrets.token_hex(32)}; locale=en-US',
		'DNT': '1',
		'origin': 'https://discord.com',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'referer': 'https://discord.com/channels/@me',
		'TE': 'Trailers',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
		'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
    }
    return header
        

def get_new_token(email, password, token):

    headers = getheaders(token)
    
    payload = {
        "login": email,
        "password": password,
    }

    r = requests.post(f"https://discord.com/api/v10/auth/login", json=payload, headers=headers)

    newToken = r.json().get("token")
    
    if(newToken):
        emailpass = f"{email}:{password}:{newToken}"
        if config['streamer_mode'] == True:
            print(f' {Fore.BLUE}{Style.BRIGHT}[{Fore.RESET}{Fore.YELLOW}{Style.BRIGHT}DGT{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}]{Fore.RESET} {Fore.GREEN}{Style.BRIGHT}Token Alındı{Fore.RESET} {Fore.CYAN}{Style.BRIGHT}{newToken[:52]}=={Fore.RESET}')
        else:
            print(f' {Fore.BLUE}{Style.BRIGHT}[{Fore.RESET}{Fore.YELLOW}{Style.BRIGHT}DGT{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}]{Fore.RESET} {Fore.GREEN}{Style.BRIGHT}Token Alındı{Fore.RESET} {Fore.CYAN}{Style.BRIGHT}{newToken}{Fore.RESET}')
        with open("./data/newpass.txt", "a") as x: x.write(f'{email}:{password}:{newToken}\n')
        with open("./data/emailpass.txt", "r+") as io:
            tokens = io.readlines()
            io.seek(0)
            for line in tokens:
                if not (emailpass in line):
                    io.write(line)
                    io.truncate()
    else:
        if config['streamer_mode'] == True:
            print(f' {Fore.BLUE}{Style.BRIGHT}[{Fore.RESET}{Fore.YELLOW}{Style.BRIGHT}DGT{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}]{Fore.RESET} {Fore.RED}{Style.BRIGHT}Token Alınamadı{Fore.RESET} {Fore.CYAN}{Style.BRIGHT}{newToken[:52]}=={Fore.RESET} ')
        else:
            print(f' {Fore.BLUE}{Style.BRIGHT}[{Fore.RESET}{Fore.YELLOW}{Style.BRIGHT}DGT{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}]{Fore.RESET} {Fore.RED}{Style.BRIGHT}Token Alınamadı{Fore.RESET} {Fore.CYAN}{Style.BRIGHT}{newToken}{Fore.RESET}')

        emailpass = f"{email}:{password}:{newToken}"
        with open("data/emailpass.txt", "r+") as io:
            tokens = io.readlines()
            io.seek(0)
            for line in tokens:
                if not (emailpass in line):
                    io.write(line)
                    io.truncate()

if __name__ == "__main__":

    os.system("title Get Token V3 PRO Version")

    System.Size(150, 40)

    print('')
    print('')
    Write.Print("""
   ██████╗ ███████╗████████╗    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██╗   ██╗██████╗ 
  ██╔════╝ ██╔════╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██║   ██║╚════██╗
  ██║  ███╗█████╗     ██║          ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║   ██║ █████╔╝
  ██║   ██║██╔══╝     ██║          ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ╚██╗ ██╔╝ ╚═══██╗
  ╚██████╔╝███████╗   ██║          ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║     ╚████╔╝ ██████╔╝
   ╚═════╝ ╚══════╝   ╚═╝          ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝      ╚═══╝  ╚═════╝ 
    """, Colors.yellow_to_red, interval=0)
    print('')
    print('')

    emailpass =  open('./data/emailpass.txt','r').read().replace(" "," ").splitlines()
    for line in emailpass:
        email = line.split(':')[0]
        passw = line.split(':')[1]
        token = line.split(':')[2]
        get_new_token(email, passw, token)
        time.sleep(2)


"""
 if "captcha-required" in r.text:
        print('Captcha tespit edildi')
        while True:
            try:
                capmonster = HCaptchaTask(config["capmonster_key"])
                task_id = capmonster.create_task("https://discord.com/login", "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34")
                print(task_id)
                captcha_token = capmonster.join_task_result(task_id)["gRecaptchaResponse"]
                print(captcha_token)
                payload2 = {
                    "login": email,
                    "password": password,
                    "captcha_key": captcha_token
                }
                
                r = requests.post(f"https://discord.com/api/v10/auth/login", json=payload2, headers=headers)

                print(r.json())

                newToken = r.json().get("token")

                print(newToken)

                if(newToken):
                    emailpass = f"{email}:{password}:{newToken}"
                    print(f'{Fore.BLUE}{Style.BRIGHT}[{Fore.RESET}{Fore.YELLOW}{Style.BRIGHT}JNX{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}]{Fore.RESET} {Fore.GREEN}{Style.BRIGHT}Token2 Alındı{Fore.RESET} ' + newToken)
                    with open("./data/newpass.txt", "a") as x: x.write(f'{email}:{password}:{newToken}\n')
                    with open("data/emailpass.txt", "r+") as io:
                        tokens = io.readlines()
                        io.seek(0)
                        for line in tokens:
                            if not (emailpass in line):
                                io.write(line)
                                io.truncate()
                else:
                    print(f'{Fore.BLUE}{Style.BRIGHT}[{Fore.RESET}{Fore.YELLOW}{Style.BRIGHT}>{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}]{Fore.RESET} {Fore.RED}{Style.BRIGHT}Token2 Alınamadı{Fore.RESET} ' + token)
                    emailpass = f"{email}:{password}:{newToken}"
                    with open("data/emailpass.txt", "r+") as io:
                        tokens = io.readlines()
                        io.seek(0)
                        for line in tokens:
                            if not (emailpass in line):
                                io.write(line)
                                io.truncate()
            except Exception as e:
                print(e)
                continue
"""