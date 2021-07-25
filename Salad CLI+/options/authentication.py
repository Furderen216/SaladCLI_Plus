import json
import logging
from time import sleep
import os

try:
    from time import sleep
    from colorama import Fore, Back
    import pyperclip
    import requests
    import dateutil.parser
except ImportError:
    print("One or more Modules not found. Press enter to install! After installing please restart Salad CLI+")
    input()
    os.system("pip install -r ./Options/requirements.txt")
    exit()


def get_auth_key():
    with open('./config.json') as f:
        js = json.load(f)
    salad_auth = js['salad_key']
    RefreshToken = js['sIdRefreshToken']
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
        print(f'{Fore.CYAN}AN ERROR OCCURRED DURING THE REQUEST FOR AUTHENTICATION!')
        if saladuser.status_code == 401:
            print(f'{Fore.CYAN}REPLACE YOUR SALAD AUTH CODE OR SIDREFRESHTOKEN!')
            logger.error("REPLACE YOUR SALAD AUTH CODE OR SIDREFRESHTOKEN!")
        sleep(20)

    except requests.exceptions.ConnectionError as errc:
        logger.error("Error Connecting:" + str(errc))
        print(f'{Fore.CYAN}CHECK YOUR INTERNET CONNECTION!')
        sleep(20)

    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error:", str(errt))
        print(f'{Fore.CYAN}TIMEOUT ERROR!')
        sleep(20)

    except requests.exceptions.RequestException as err:
        logger.error("Oops: Something Else:" + str(err))
        print(f'{Fore.CYAN}AN ERROR OCCURRED DURING THE REQUEST FOR AUTHENTICATION!')
        sleep(20)

    return saladuser
