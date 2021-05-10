import os
import time
import requests
import sys
from time import sleep
import json
from colorama import Fore, Back

sys.stdout.write("\x1b]2;Experience\x07")
refresh_time = 15


with open('config.json') as f:
    js = json.load(f)
salad_auth = js['salad_key']
cookie = {
    "Salad.Authentication": salad_auth
}
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.4.2 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
}
with open('./Art/art.txt', encoding='utf-8') as f:
    art = f.read()


def main():
    while True:
        os.system('cls')
        rxp = requests.get(
            url='https://app-api.salad.io/api/v1/profile/xp', headers=headers, cookies=cookie)
        if rxp.status_code != 200:
            print(f'{Fore.RED}REPLACE YOUR SALAD AUTH CODE!')
            input(f'{Fore.RED}Press Enter to Exit...')
        rxp = rxp.json()

        print(Fore.GREEN + art)

        print(f'{Fore.LIGHTRED_EX}Experience {Fore.BLUE}> {Fore.YELLOW}' +
              str(rxp['lifetimeXp']) + ' XP')
        print(Fore.GREEN)
        print('-------------------------------------')

        try:
            print(
                f'\n{Fore.GREEN}Press {Fore.RED}ctrl+c {Fore.GREEN}to Return to the menu!')
            sleep(5)
        except KeyboardInterrupt:
            print("Quitting...")
            os.system('python "./Start.py"')


main()
