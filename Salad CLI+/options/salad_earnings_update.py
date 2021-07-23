import requests
import json
import time
import sys
import os
from colorama import Fore
from options import authentication


def get_history(logo, cookie, headers, file_handler):
    sys.stdout.write("\x1b]2;Downloading History\x07")

    history = authentication.authenticate('https://app-api.salad.io/api/v2/reports/1-day-earning-history',
                                          cookie, headers, file_handler)
    history = history.json()

    with open('./data.json', 'w+') as f:
        f.write(json.dumps(history))
    os.system('cls')
    print(Fore.LIGHTBLACK_EX + logo)
    print(f'{Fore.CYAN}Downloading your earning history...')
    time.sleep(2)

    os.system(
        'python "./Options/earning_graph.py" --asd -f data.json --smh -min -rev')
