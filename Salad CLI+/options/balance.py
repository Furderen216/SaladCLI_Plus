import os
import requests
import sys
from time import sleep
from colorama import Fore, Back
from options import authentication


def show_balance(logo, cookie, headers, file_handler):
    sys.stdout.write("\x1b]2;Current Balance\x07")
    while True:
        os.system('cls')
        balance = authentication.authenticate('https://app-api.salad.io/api/v1/profile/balance',
                                              cookie, headers, file_handler)
        balance = balance.json()

        print(Fore.LIGHTBLACK_EX + logo)

        print(f'{Fore.CYAN}Current Balance {Fore.BLUE}> {Fore.RED}$' +
              str(balance['currentBalance']))
        print(f'{Fore.CYAN}Lifetime Balance {Fore.BLUE}> {Fore.RED}$' +
              str(balance['lifetimeBalance']))
        print(Fore.LIGHTBLACK_EX)
        print('-------------------------------------')

        try:
            print(
                f'\n{Fore.LIGHTBLACK_EX}Press {Fore.CYAN}CTRL+C {Fore.LIGHTBLACK_EX}to return to the menu!')
            sleep(5)
        except (KeyboardInterrupt):
            return False
