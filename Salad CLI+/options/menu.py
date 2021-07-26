import sys
import os
import time
import pyperclip
import webbrowser
from colorama import Fore, Style
from options import authentication
from options import choose
import win32gui
window = win32gui.GetForegroundWindow()


def menu(saladuser, loginscreen, logo, cookie, headers, file_handler):
  
    os.system('cls')
    sys.stdout.write("\x1b]2;Salad CLI+ | By Walkx\x07")
    print(Fore.LIGHTBLACK_EX + loginscreen)
    print(f'{Fore.RED}[----------- Profile -----------]\n')
    print(f'{Fore.CYAN}Username {Fore.BLUE}> {Fore.RED}' +
          str(saladuser['username']))
    print(f'{Fore.CYAN}Email {Fore.BLUE}> {Fore.RED}' +
          str(saladuser['email']))
    print(f'{Fore.RED}[----------- Session -----------]\n')
    print(f'{Fore.CYAN}Current Session {Fore.BLUE}> {Fore.RED}' +
          str(session['name']))
    print(f'{Fore.CYAN}Current level {Fore.BLUE}> {Fore.RED}' +
          str(session['currentLevelId']))
    print(f'{Fore.CYAN}You need {Fore.BLUE}> ' + Fore.RED + str(session['totalXp'] - session['levelXp']) + Fore.BLUE +' < ' + Fore.CYAN + 'minutes left until level up')
    print("\n\n")

    # Input Selection

    print(f"{Fore.CYAN}Select an option: {Fore.RED}")

    name, opt = choose.create([f'{Fore.WHITE}Start Mining{Style.RESET_ALL}',
                               f'{Fore.WHITE}Show Balance{Style.RESET_ALL}',
                               f'{Fore.WHITE}Show XP{Style.RESET_ALL}',
                               f'{Fore.WHITE}Show Earning Graph{Style.RESET_ALL}',
                               f'{Fore.WHITE}Copy Referral Code{Style.RESET_ALL}',
                               f'{Fore.WHITE}Open Salad Store{Style.RESET_ALL}',
                               f'{Fore.WHITE}Help{Fore.LIGHTBLACK_EX}{Style.RESET_ALL}',
                               f'{Fore.WHITE}Exit{Style.RESET_ALL}'], window)

    opt += 1

    if opt == 1:
        from options import mining
        mining.choose_pool(logo)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif opt == 2:
        from options import balance
        balance.show_balance(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif opt == 3:
        from options import xp
        xp.show_experience(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif opt == 4:
        from options import salad_earnings_update
        salad_earnings_update.get_history(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif opt == 5:
        referral = authentication.authenticate('https://app-api.salad.io/api/v1/profile/referral-code',
                                               cookie, headers, file_handler)
        referral = referral.json()
        pyperclip.copy('Support me and use code ' + str(
            referral['code']) + ' for a 2x earning rate bonus on Salad! https://www.salad.com')
        os.system('cls')
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.CYAN}Code copied to clipboard!')
        time.sleep(2)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif opt == 6:
        webbrowser.open('http://app.salad.io')

    elif opt == 7:
        webbrowser.open('https://discord.gg/D2VBbJDz8c')

    elif opt == 8:
        exit()
