import os
import time
import pyperclip
import webbrowser
from colorama import Fore
from options import authentication


def menu(saladuser, loginscreen, logo, cookie, headers, file_handler):

    os.system('cls')
    print(Fore.LIGHTBLACK_EX + loginscreen)
    print(f'{Fore.CYAN}Username {Fore.BLUE}> {Fore.RED}' +
          str(saladuser['username']))
    print(f'{Fore.CYAN}Email {Fore.BLUE}> {Fore.RED}' +
          str(saladuser['email']))
    print(f'{Fore.CYAN}User id {Fore.BLUE}> {Fore.RED}' +
          str(saladuser['id']))
    print("\n\n")

    # Input Selection

<<<<<<< HEAD
    print(f"{Fore.CYAN}Select an option: {Fore.RED}")
=======
    select = input(
        f"{Fore.CYAN}Select an option: {Fore.RED}\n\n{Fore.RED}1 - {Fore.WHITE}Start Mining \n{Fore.RED}2 - {Fore.WHITE}Show Balance \n{Fore.RED}3 - {Fore.WHITE}Show Lifetime Balance \n{Fore.RED}4 - {Fore.WHITE}Show XP \n{Fore.RED}5 - {Fore.WHITE}Show Earning Graph \n{Fore.RED}6 - {Fore.WHITE}Copy Referral Code \n{Fore.RED}7 - {Fore.WHITE}Open Salad Store \n{Fore.RED}8 - {Fore.WHITE}Help{Fore.LIGHTBLACK_EX} \n{Fore.RED}x - {Fore.WHITE}Exit\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")
>>>>>>> parent of 75ba50d (Pushed to V9)

    if select == "1":
        from options import mining
        mining.choose_pool(logo)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "2":
        from options import balance
        balance.show_balance(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "3":
        from options import lifetime
        lifetime.show_lifetime(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "4":
        from options import xp
        xp.show_experience(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "5":
        from options import salad_earnings_update
        salad_earnings_update.get_history(cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "6":
        referral = authentication.authenticate('https://app-api.salad.io/api/v1/profile/referral-code',
                                               cookie, headers, file_handler)
        referral = referral.json()
        pyperclip.copy('Support me and use code ' + str(
            referral['code']) + ' for a 2x earning rate bonus on Salad! https://www.salad.com')
        print(f'\nCode copied to clipboard!')
        time.sleep(2)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "7":
        webbrowser.open('http://app.salad.io')

    elif select == "8":
        webbrowser.open('https://discord.gg/D2VBbJDz8c')

    elif select == "x":
        exit()
