import json
import logging
from time import sleep
from art import art
import os
logo = art.read_art('./art/art.txt')

try:
    from time import sleep
    from colorama import Fore, Back
    import pyperclip
    import requests
    import dateutil.parser
except ImportError:
    print("Installing important software, please wait...")
    os.system("pip install -r ./Options/requirements.txt")
    os.system("python Start.py")
    exit()


def get_auth_key():
    with open('./config.json') as f:
        js = json.load(f)
    if 'salad_key' not in js:
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.RED}It looks like your config.json file is incorrectly configured.\n{Fore.CYAN}Your Salad Auth token is missing.')
        exit()
    if 'sIdRefreshToken' not in js:
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.RED}It looks like your config.json file is incorrectly configured.\n{Fore.CYAN}Your Salad Refresh token is missing.')
        exit()
    salad_auth = js['salad_key']
    sIdRefreshToken = js['sIdRefreshToken']
    cookie = {"sAccessToken": salad_auth, "sIdRefreshToken": sIdRefreshToken}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.5.3 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
    }
    return cookie, headers


def authenticate(url, cookie, headers, file_handler):
    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    try:
        saladuser = requests.get(url=url,
                                 headers=headers, cookies=cookie, timeout=10)
        saladuser.raise_for_status()
        logger.info("Authentication succeeded.")

    except requests.exceptions.HTTPError as errh:
        logger.error("Http Error:" + str(errh))
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.RED}Connection error! D:')
        if saladuser.status_code == 401:
            print(f'{Fore.WHITE}Your Salad Auth code or Refresh Token is incorrect. Please update it.')
            logger.error("REPLACE YOUR SALAD AUTH CODE!")
        exit()

    except requests.exceptions.ConnectionError as errc:
        logger.error("Error Connecting:" + str(errc))
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.RED}Connection error! D:\n{Fore.WHITE}You appear to be offline. Check your internet connection.')
        exit()

    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error:", str(errt))
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.RED}Connection error! D:\n{Fore.WHITE}The Salad servers didn\'t respond. Please try again later.')
        exit()

    except requests.exceptions.RequestException as err:
        logger.error("Oops: Something Else:" + str(err))
        print(Fore.LIGHTBLACK_EX + logo)
        print(f'{Fore.RED}Connection error! D:\n{Fore.WHITE}Unfortunately, we\'re having trouble connecting to the Salad servers.\nInformation for CLI+ developers: {str(err)}\nPlease try again later.')
        exit()

    return saladuser
