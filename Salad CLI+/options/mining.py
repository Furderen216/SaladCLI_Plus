import os
import sys
from time import sleep
import json
from colorama import Fore, Back, Style
from options import choose
import win32gui
window = win32gui.GetForegroundWindow()


def choose_pool(logo):
    os.system('cls')

    sys.stdout.write("\x1b]2;Choose mining region.\x07")

    print(Fore.LIGHTBLACK_EX + logo)

<<<<<<< HEAD:Salad CLI+/options/mining.py
    select_pool = input(
        f"{Fore.CYAN}Select a pool: \n\n{Fore.RED}1 - {Fore.CYAN}Nicehash \n{Fore.RED}2 - {Fore.CYAN}Ethermine \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
    )
=======
    # pool

    print(f"{Fore.CYAN}Select a pool:{Style.RESET_ALL}")

    name, pool = choose.create([f'{Fore.RED}1 - {Fore.CYAN}Nicehash{Style.RESET_ALL}',
                               f'{Fore.RED}2 - {Fore.CYAN}Ethermine{Style.RESET_ALL}', f'{Fore.RED}Exit{Style.RESET_ALL}'], window)

    pool += 1

    if pool == 3:
        return False

    if pool == 1:

        # region
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py

        os.system('cls')

        print(Fore.LIGHTBLACK_EX + logo)

<<<<<<< HEAD:Salad CLI+/options/mining.py
        print(Fore.LIGHTBLACK_EX + logo)

        select_region = input(
            f"{Fore.CYAN}Select a pool region: \n\n{Fore.RED}1 - {Fore.CYAN}EU-West \n{Fore.RED}2 - {Fore.CYAN}EU-North \n{Fore.RED}3 - {Fore.CYAN}USA-West \n{Fore.RED}4 - {Fore.CYAN}USA-East \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
        )
=======
        print(f"{Fore.CYAN}Select a pool region:{Style.RESET_ALL}")

        name, region = choose.create([f'{Fore.RED}1 - {Fore.CYAN}EU-West{Style.RESET_ALL}', f'{Fore.RED}2 - {Fore.CYAN}EU-North{Style.RESET_ALL}',
                                     f'{Fore.RED}3 - {Fore.CYAN}USA-West{Style.RESET_ALL}', f'{Fore.RED}4 - {Fore.CYAN}USA-East{Style.RESET_ALL}', f'{Fore.RED}Exit{Style.RESET_ALL}'], window)

        region += 1
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py

        if region == 1:
            region = "eu-west"

        if region == 2:
            region = "eu-north"

        if region == 3:
            region = "usa-west"

        if region == 4:
            region = "usa-east"

        if region == 5:
            return False

        # Additional miner commands

        os.system("cls")
        print(Fore.LIGHTBLACK_EX + logo)

        miner_commands = input(
            f"{Fore.CYAN}Type additional miner commands here (optional) \nPress enter to skip. \n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
        )

        # Select miner

        os.system("cls")
        print(Fore.LIGHTBLACK_EX + logo)

        with open('config.json') as f:
            js = json.load(f)
        nicehash_wallet = js['nicehash_wallet']

<<<<<<< HEAD:Salad CLI+/options/mining.py
        select = input(
            f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.RED} = GPU Miner\n{Fore.BLACK}{Back.LIGHTBLACK_EX}Gray{Back.BLACK}{Fore.RED} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.RED}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.RED}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.RED}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.RED}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.RED}9 - {Fore.CYAN}Gminer (Zhash) \n{Fore.RED}10 - {Fore.LIGHTBLACK_EX}XMRig (RandomXMonero)\n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")
=======
        print(f"{Fore.RED}Miners are listed from 'best' to 'worst'.")

        print(f'{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.RED} = GPU Miner')
        print(f'{Fore.BLACK}{Back.LIGHTBLACK_EX}Gray{Back.BLACK}{Fore.RED} = CPU Miner')
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py

        print(f'{Fore.CYAN}Select a miner:{Style.RESET_ALL}')

        name, miner = choose.create([f'{Fore.RED} - {Fore.CYAN}T-rex (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}NBMiner (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}Phoenixminer (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}ETHMiner (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}Teamredminer [AMD Only] (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}Teamredminer [AMD 4GB or less Only] (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}Gminer (BeamhashIII){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}T-rex (KawPow){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}Teamredminer [AMD Only] (KawPow){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}XMRig nVidia (KawPow){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.CYAN}Gminer (Zhash){Style.RESET_ALL}',
                                     f'{Fore.RED} - {Fore.LIGHTBLACK_EX}XMRig (RandomXMonero){Style.RESET_ALL}',
                                     f'{Fore.RED}Exit{Style.RESET_ALL}'], window)

        miner += 1

        if miner != 13:
            os.system("OptimizeGPU.bat")
        else:
            return False

        if miner == 1:
            os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 --user " + (nicehash_wallet) + " " + (miner_commands))

        if miner == 2:
            os.system(
                r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (nicehash_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

        if miner == 3:
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 1 -pool stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 -ewal " + (nicehash_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))
        if miner == 4:
            os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
                      (nicehash_wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U" + " " + (miner_commands))

        if miner == 5:
            os.system(r"Miners\Teamredminer\teamredminer.exe -a ethash -o stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 -u " + (nicehash_wallet) + " " + (miner_commands))
        if miner == 6:
            os.system(r"Miners\Teamredminer\teamredminer.exe -a ethash -o stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 -u " + (nicehash_wallet) + " --restart_gpus --uac --eth_alloc_epoch=374 --eth_4g_max_alloc=374 " + (miner_commands))

        if miner == 7:
            os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
                      region + ".nicehash.com:3387 -u " + (nicehash_wallet) + " " + (miner_commands))

        if miner == 8:
            os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
                      region + ".nicehash.com:3385 --user " + (nicehash_wallet) + " " + (miner_commands))

<<<<<<< HEAD:Salad CLI+/options/mining.py
        if select == "7":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\XMRig-Cuda\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "8":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\XMRig-amd\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
=======
        if miner == 9:
            os.system(r"Miners\Teamredminer\teamredminer.exe -a kawpow -o stratum+tcp://kawpow." +
                      region + ".nicehash.com:3385 -u " + (nicehash_wallet) + " " + (miner_commands))

        if miner == 10:
            os.system(r"Miners\XMRig-Cuda\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if miner == 11:
            os.system(r"Miners\Gminer\miner.exe -a 144_5 --pers auto --proto stratum --server zhash." +
                      region + ".nicehash.com:3369 -u " + (nicehash_wallet) + " " + (miner_commands))

<<<<<<< HEAD:Salad CLI+/options/mining.py
        if select == "10":
            os.system("cls")
=======
        if miner == 12:
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py
            os.system(r"Miners\XMRig-CPU\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        sleep(10)
        return False

    if pool == 2:
        # Select Region
        os.system('cls')

        sys.stdout.write("\x1b]2;Choose mining region.\x07")

        print(Fore.LIGHTBLACK_EX + logo)

<<<<<<< HEAD:Salad CLI+/options/mining.py
        select_region = input(
            f"{Fore.CYAN}Select a pool region: \n\n{Fore.RED}1 - {Fore.CYAN}Europe \n{Fore.RED}2 - {Fore.CYAN}Asia \n{Fore.RED}3 - {Fore.CYAN}USA-West \n{Fore.RED}4 - {Fore.CYAN}USA-East \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
        )
=======
        print(f"{Fore.RED}When using Ethermine it can take 30+ minutes before you'll see earnings in Salad!\n{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Select a pool region:{Style.RESET_ALL}")

        name, region = choose.create([f'{Fore.RED}1 - {Fore.CYAN}Europe{Style.RESET_ALL}',
                                      f'{Fore.RED}2 - {Fore.CYAN}Asia{Style.RESET_ALL}',
                                      f'{Fore.RED}3 - {Fore.CYAN}USA{Style.RESET_ALL}',
                                      f'{Fore.RED}Exit{Style.RESET_ALL}'], window)
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py

        region += 1

        if region == 1:
            region = "eu1"

        if region == 2:
            region = "asia1"

        if region == 3:
            region = "us1"

        if region == 5:
            return False

        # Additional miner commands

        os.system("cls")
        print(Fore.LIGHTBLACK_EX + logo)

        miner_commands = input(
            f"{Fore.CYAN}Type additional miner commands here (optional) \nPress enter to skip. \n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
        )

        # Select miner

        os.system("cls")
        print(Fore.LIGHTBLACK_EX + logo)

        with open('config.json') as f:
            js = json.load(f)
        ethermine_wallet = js['ethermine_wallet']

<<<<<<< HEAD:Salad CLI+/options/mining.py
        select = input(
            f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")
=======
        print(f"{Fore.RED}Miners are listed from 'best' to 'worst'.")

        print(f'{Fore.CYAN}Select a miner:{Style.RESET_ALL}')
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py

        name, miner = choose.create([f'{Fore.RED}- {Fore.CYAN}T-rex (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}NBMiner (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}Phoenixminer (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}Teamredminer [AMD Only] (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}ETHMiner (Ethash){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}T-rex (ETC){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}Phoenixminer (ETC){Style.RESET_ALL}',
                                     f'{Fore.RED}- {Fore.CYAN}Teamredminer [AMD Only] (ETC){Style.RESET_ALL}',
                                     f'{Fore.RED}Exit{Style.RESET_ALL}'], window)

        miner += 1

        if miner != 9:
            os.system("OptimizeGPU.bat")
<<<<<<< HEAD:Salad CLI+/options/mining.py
=======
        else:
            return False

        if miner == 1:
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py
            os.system(r"Miners\Trex\t-rex.exe --algo ethash --url ssl://" +
                      region + ".ethermine.org:5555 --user " + (ethermine_wallet) + " " + (miner_commands))

        if miner == 2:
            os.system(
                r"Miners\NBMiner\nbminer.exe -a ethash -o ssl://" + region + ".ethermine.org:5555 -u " + (ethermine_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

<<<<<<< HEAD:Salad CLI+/options/mining.py
        if select == "3":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -log 0 -pool ssl://" +
                      region + ".ethermine.org:5555 -ewal " + (ethermine_wallet) + (miner_commands))

        if select == "4":
            os.system("OptimizeGPU.bat")
=======
        if miner == 3:
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -pool ssl://" +
                      region + ".ethermine.org:5555 -ewal " + (ethermine_wallet) + (miner_commands))
        if miner == 4:
            os.system(
                r"Miners\Teamredminer\teamredminer.exe -a ethash -o stratum+ssl://" + region + ".ethermine.org:5555 -u " + (ethermine_wallet) + " " + (miner_commands))

        if miner == 5:
>>>>>>> upstream/main:Salad CLI+/Options/Mining.py
            os.system(r"Miners\ETHMiner\ethminer.exe -P ssl://" +
                      (ethermine_wallet) + r"@" + region + ".ethermine.org:5555" + " " + (miner_commands))

        if miner == 6:
            os.system(r"Miners\Trex\t-rex.exe -a etchash -o ssl://" +
                      region + "-etc.ethermine.org:5555 -u " + (ethermine_wallet) + " " + (miner_commands))

        if miner == 7:
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -pool ssl://" +
                      region + "-etc.ethermine.org:5555 -ewal " + (ethermine_wallet) + (miner_commands))

        if miner == 8:
            os.system(
                r"Miners\Teamredminer\teamredminer.exe -a etchash -o stratum+ssl://" + region + "-etc.ethermine.org:5555 -u " + (ethermine_wallet) + " " + (miner_commands))

        sleep(10)
        return False
