import os
import requests
import sys
from time import sleep
from colorama import Fore, Back
from options import authentication


def show_experience(logo, cookie, headers, file_handler):
    sys.stdout.write("\x1b]2;Experience\x07")
    while True:
        os.system('cls')
        experience = authentication.authenticate('https://app-api.salad.io/api/v1/profile/xp',
                                                 cookie, headers, file_handler)
        experience = experience.json()

        print(Fore.LIGHTBLACK_EX + logo)

        print(f'{Fore.CYAN}Experience {Fore.BLUE}> {Fore.RED}' +
              str(experience['lifetimeXp']) + ' XP')
        print(Fore.LIGHTBLACK_EX)
        print('-------------------------------------')

        try:
            print(
                f'\n{Fore.LIGHTBLACK_EX}Press {Fore.CYAN}ctrl+c {Fore.LIGHTBLACK_EX}to Return to the menu!')
            sleep(5)
        except (KeyboardInterrupt):
            return False
