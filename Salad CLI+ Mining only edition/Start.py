import os
import sys
import json

try:
    from time import sleep
    from colorama import Fore, Back

except ImportError:
    print("One or more Modules not found. Press enter to install! After installing please restart Salad CLI+")
    input()
    os.system("pip install -r ./essentials/requirements.txt")
    exit()

art = open('./essentials/art.txt', 'r')

logo = art.read()


os.system('cls')import os
import sys
import json

##[[---------------------------------------------]]##
##                                                 ##
##   ____     __        __  _______   ____  __     ##
##  / __/__ _/ /__ ____/ / / ___/ /  /  _/_/ /_    ##
## _\ \/ _ `/ / _ `/ _  / / /__/ /___/ //_  __/    ##
##/___/\_,_/_/\_,_/\_,_/  \___/____/___/ /_/       ##
##                                                 ##
## by WalkxCode                                    ##
##                                                 ##
##[[---------------------------------------------]]##

try:
    from time import sleep
    from colorama import Fore, Back

except ImportError:
    print("One or more Modules not found. Press enter to install! After installing please restart Salad CLI+")
    input()
    os.system("pip install -r ./essentials/requirements.txt")
    exit()

art = open('./essentials/art.txt', 'r')

logo = art.read()

os.system('cls')

sys.stdout.write("\x1b]2;Choose mining region.\x07")

print(Fore.LIGHTBLACK_EX + logo)

select_pool = input(
    f"{Fore.CYAN}Select a pool: \n\n{Fore.RED}1 - {Fore.CYAN}Nicehash \n{Fore.RED}2 - {Fore.CYAN}Ethermine \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
)

if select_pool == "1":
    # Select Region
    os.system('cls')

    sys.stdout.write("\x1b]2;Choose mining region.\x07")

    print(Fore.LIGHTBLACK_EX + logo)

    select_region = input(
        f"{Fore.CYAN}Select a pool region: \n\n{Fore.RED}1 - {Fore.CYAN}EU-West \n{Fore.RED}2 - {Fore.CYAN}EU-North \n{Fore.RED}3 - {Fore.CYAN}USA-West \n{Fore.RED}4 - {Fore.CYAN}USA-East \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
    )

    if select_region == "1":
        region = "eu-west"

    if select_region == "2":
        region = "eu-north"

    if select_region == "3":
        region = "usa-west"

    if select_region == "4":
        region = "usa-east"

    if select_region == "exit":
        os.system("exit")

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
    nicehash = nicehash_wallet[0:3

    if nicehash == '3FSqW1MFAdzekG6DdvfUhPVnwVY4C9zBAG':
        select = input(
            f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.RED} = GPU Miner\n{Fore.BLACK}{Back.LIGHTBLACK_EX}Gray{Back.BLACK}{Fore.RED} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.RED}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.RED}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.RED}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.RED}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.RED}9 - {Fore.CYAN}Gminer (Zhash) \n{Fore.RED}10 - {Fore.LIGHTBLACK_EX}XMRig (RandomXMonero)\n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")

        if select == "1":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 --user " + (nicehash_wallet) + " " + (miner_commands))

        if select == "2":
            os.system("OptimizeGPU.bat")
            os.system(
                r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (nicehash_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

        if select == "3":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 -ewal " + (nicehash_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))

        if select == "4":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
                      (nicehash_wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U" + " " + (miner_commands))

        if select == "5":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
                      region + ".nicehash.com:3387 -u " + (nicehash_wallet) + " " + (miner_commands))

        if select == "6":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
                      region + ".nicehash.com:3385 --user " + (nicehash_wallet) + " " + (miner_commands))

        if select == "7":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\XMRig-Cuda\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "8":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\XMRig-amd\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "9":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Gminer\miner.exe -a 144_5 --pers auto --proto stratum --server zhash." +
                      region + ".nicehash.com:3369 -u " + (nicehash_wallet) + " " + (miner_commands))

        if select == "10":
            os.system("cls")
            os.system(r"Miners\XMRig-CPU\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "exit":
            os.system('exit')

        sleep(3)
        os.system('exit')
    else:
        warn = input(
            f"{Fore.RED}Salad nicehash wallet : Incorrect.\n\n\n{Fore.CYAN}Are you sure you want to mine? \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}Yes \n{Fore.RED}2 - {Fore.CYAN}No\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")
        if warn == "1":
            select = input(
                f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.RED} = GPU Miner\n{Fore.BLACK}{Back.LIGHTBLACK_EX}Gray{Back.BLACK}{Fore.RED} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.RED}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.RED}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.RED}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.RED}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.RED}9 - {Fore.CYAN}Gminer (Zhash) \n{Fore.RED}10 - {Fore.LIGHTBLACK_EX}XMRig (RandomXMonero)\n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")

            if select == "1":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
                          region + ".nicehash.com:3353 --user " + (nicehash_wallet) + " " + (miner_commands))

            if select == "2":
                os.system("OptimizeGPU.bat")
                os.system(
                    r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (nicehash_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

            if select == "3":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto." +
                          region + ".nicehash.com:3353 -ewal " + (nicehash_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))

            if select == "4":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
                          (nicehash_wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U" + " " + (miner_commands))

            if select == "5":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
                          region + ".nicehash.com:3387 -u " + (nicehash_wallet) + " " + (miner_commands))

            if select == "6":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
                          region + ".nicehash.com:3385 --user " + (nicehash_wallet) + " " + (miner_commands))

            if select == "7":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\XMRig-Cuda\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                          (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

            if select == "8":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\XMRig-amd\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                          (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

            if select == "9":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Gminer\miner.exe -a 144_5 --pers auto --proto stratum --server zhash." +
                          region + ".nicehash.com:3369 -u " + (nicehash_wallet) + " " + (miner_commands))

            if select == "10":
                os.system("cls")
                os.system(r"Miners\XMRig-CPU\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
                          (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

            if select == "exit":
                os.system('exit')

            sleep(3)
            os.system('exit')
        else:
            print("Wallet checking: Incorrect : Nicehash")
            os.system('exit')

        warn = input(
            f"{Fore.RED}Salad nicehash wallet Incorrect.\n\n\n{Fore.CYAN}Are you sure you want to mine? \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}Yes \n{Fore.RED}2 - {Fore.CYAN}No\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")
        if warn == "1":
            select = input(
                f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.RED} = GPU Miner\n{Fore.BLACK}{Back.LIGHTBLACK_EX}Gray{Back.BLACK}{Fore.RED} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.RED}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.RED}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.RED}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.RED}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.RED}9 - {Fore.CYAN}Gminer (Zhash) \n{Fore.RED}10 - {Fore.LIGHTBLACK_EX}XMRig (RandomXMonero)\n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")


            if select == "1":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
                          region + ".nicehash.com:3353 --user " + (nicehash_wallet) + " " + (miner_commands))

            if select == "2":
                os.system("OptimizeGPU.bat")
                os.system(
                    r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (nicehash_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

            if select == "3":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto." +
                          region + ".nicehash.com:3353 -ewal " + (nicehash_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))

            if select == "4":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
                          (nicehash_wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U" + " " + (miner_commands))

            if select == "5":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
                          region + ".nicehash.com:3387 -u " + (nicehash_wallet) + " " + (miner_commands))

            if select == "6":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
                          region + ".nicehash.com:3385 --user " + (nicehash_wallet) + " " + (miner_commands))

            if select == "7":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\XMRig-Cuda\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                          (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

            if select == "8":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\XMRig-amd\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                          (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

            if select == "9":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Gminer\miner.exe -a 144_5 --pers auto --proto stratum --server zhash." +
                          region + ".nicehash.com:3369 -u " + (nicehash_wallet) + " " + (miner_commands))

            if select == "10":
                os.system("cls")
                os.system(r"Miners\XMRig-CPU\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
                          (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

            if select == "exit":
                os.system('exit')

            sleep(3)
            os.system('exit')


if select_pool == "2":
    # Select Region
    os.system('cls')

    sys.stdout.write("\x1b]2;Choose mining region.\x07")

    print(Fore.LIGHTBLACK_EX + logo)

    select_region = input(
        f"{Fore.CYAN}Select a pool region: \n\n{Fore.RED}1 - {Fore.CYAN}Europe \n{Fore.RED}2 - {Fore.CYAN}Asia \n{Fore.RED}3 - {Fore.CYAN}USA-West \n{Fore.RED}4 - {Fore.CYAN}USA-East \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
    )

    if select_region == "1":
        region = "eu1"

    if select_region == "2":
        region = "asia1"

    if select_region == "3":
        region = "us2"

    if select_region == "4":
        region = "us1"

    if select_region == "exit":
        os.system('exit')
    os.system('exit')

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
    ethermine = ethermine_wallet[0:42]

    if ethermine == '0x6ff85749ffac2d3a36efa2bc916305433fa93731':
        select = input(
            f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")

        if select == "1":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Trex\t-rex.exe --algo ethash --url ssl://" +
                      region + ".ethermine.org:5555 --user " + (ethermine_wallet) + " " + (miner_commands))

        if select == "2":
            os.system("OptimizeGPU.bat")
            os.system(
            r"Miners\NBMiner\nbminer.exe -a ethash -o ssl://" + region + ".ethermine.org:5555 -u " + (ethermine_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

        if select == "3":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -pool ssl://" +
                      region + ".ethermine.org:5555 -ewal " + (ethermine_wallet) + (miner_commands))

        if select == "4":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\ETHMiner\ethminer.exe -P ssl://" +
                      (ethermine_wallet) + r"@" + region + ".ethermine.org:5555" + " " + (miner_commands))

        if select == "exit":
            os.system('exit')

            sleep(3)
            os.system('exit')
    else:
        warn = input(
            f"{Fore.RED}Salad Ethermine wallet Incorrect.\n\n\n{Fore.CYAN}Are you sure you want to mine? \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}Yes \n{Fore.RED}2 - {Fore.CYAN}No")
        if warn == "1":
            select = input(
                f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")

            if select == "1":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\Trex\t-rex.exe --algo ethash --url ssl://" +
                          region + ".ethermine.org:5555 --user " + (ethermine_wallet) + " " + (miner_commands))

            if select == "2":
                os.system("OptimizeGPU.bat")
                os.system(
                    r"Miners\NBMiner\nbminer.exe -a ethash -o ssl://" + region + ".ethermine.org:5555 -u " + (ethermine_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

            if select == "3":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -pool ssl://" +
                          region + ".ethermine.org:5555 -ewal " + (ethermine_wallet) + (miner_commands))

            if select == "4":
                os.system("OptimizeGPU.bat")
                os.system(r"Miners\ETHMiner\ethminer.exe -P ssl://" +
                          (ethermine_wallet) + r"@" + region + ".ethermine.org:5555" + " " + (miner_commands))

            if select == "exit":
                os.system('exit')

            sleep(3)
            os.system('exit')
        else:
            print("Wallet checking: Incorrect : Ethermine")
            os.system('exit')

sys.stdout.write("\x1b]2;Choose mining region.\x07")

print(Fore.LIGHTBLACK_EX + logo)

select_pool = input(
    f"{Fore.CYAN}Select a pool: \n\n{Fore.RED}1 - {Fore.CYAN}Nicehash \n{Fore.RED}2 - {Fore.CYAN}Ethermine \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
)

if select_pool == "1":
    # Select Region
    os.system('cls')

    sys.stdout.write("\x1b]2;Choose mining region.\x07")

    print(Fore.LIGHTBLACK_EX + logo)

    select_region = input(
        f"{Fore.CYAN}Select a pool region: \n\n{Fore.RED}1 - {Fore.CYAN}EU-West \n{Fore.RED}2 - {Fore.CYAN}EU-North \n{Fore.RED}3 - {Fore.CYAN}USA-West \n{Fore.RED}4 - {Fore.CYAN}USA-East \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
    )

    if select_region == "1":
        region = "eu-west"

    if select_region == "2":
        region = "eu-north"

    if select_region == "3":
        region = "usa-west"

    if select_region == "4":
        region = "usa-east"

    if select_region == "exit":
        os.system('exit')

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

    select = input(
        f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.RED} = GPU Miner\n{Fore.BLACK}{Back.LIGHTBLACK_EX}Gray{Back.BLACK}{Fore.RED} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.RED}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.RED}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.RED}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.RED}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.RED}9 - {Fore.CYAN}Gminer (Zhash) \n{Fore.RED}10 - {Fore.LIGHTBLACK_EX}XMRig (RandomXMonero)\n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")

    if select == "1":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
                  region + ".nicehash.com:3353 --user " + (nicehash_wallet) + " " + (miner_commands))

    if select == "2":
        os.system("OptimizeGPU.bat")
        os.system(
            r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (nicehash_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

    if select == "3":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto." +
                  region + ".nicehash.com:3353 -ewal " + (nicehash_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))

    if select == "4":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
                  (nicehash_wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U" + " " + (miner_commands))

    if select == "5":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
                  region + ".nicehash.com:3387 -u " + (nicehash_wallet) + " " + (miner_commands))

    if select == "6":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
                  region + ".nicehash.com:3385 --user " + (nicehash_wallet) + " " + (miner_commands))

    if select == "7":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\XMRig-Cuda\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                  (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

    if select == "8":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\XMRig-amd\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                  (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

    if select == "9":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\Gminer\miner.exe -a 144_5 --pers auto --proto stratum --server zhash." +
                  region + ".nicehash.com:3369 -u " + (nicehash_wallet) + " " + (miner_commands))

    if select == "10":
        os.system("cls")
        os.system(r"Miners\XMRig-CPU\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
                  (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

    if select == "exit":
        os.system('exit')

    sleep(10)
    os.system('exit')

if select_pool == "2":
    # Select Region
    os.system('cls')

    sys.stdout.write("\x1b]2;Choose mining region.\x07")

    print(Fore.LIGHTBLACK_EX + logo)

    select_region = input(
        f"{Fore.CYAN}Select a pool region: \n\n{Fore.RED}1 - {Fore.CYAN}Europe \n{Fore.RED}2 - {Fore.CYAN}Asia \n{Fore.RED}3 - {Fore.CYAN}USA-West \n{Fore.RED}4 - {Fore.CYAN}USA-East \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}"
    )

    if select_region == "1":
        region = "eu1"

    if select_region == "2":
        region = "asia1"

    if select_region == "3":
        region = "us2"

    if select_region == "4":
        region = "us1"

    if select_region == "exit":
        os.system('exit')

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

    select = input(
        f"{Fore.RED}Miners are listed from 'best' to 'worst'.\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.RED}{Fore.RED}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.RED}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.RED}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.RED}4 - {Fore.CYAN}ETHMiner (Ethash) \n\n{Fore.RED}Type {Fore.CYAN}exit {Fore.RED}to exit.\n\n{Fore.LIGHTBLACK_EX}Select {Fore.BLUE}>> {Fore.LIGHTBLACK_EX}")

    if select == "1":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\Trex\t-rex.exe --algo ethash --url ssl://" +
                  region + ".ethermine.org:5555 --user " + (ethermine_wallet) + " " + (miner_commands))

    if select == "2":
        os.system("OptimizeGPU.bat")
        os.system(
            r"Miners\NBMiner\nbminer.exe -a ethash -o ssl://" + region + ".ethermine.org:5555 -u " + (ethermine_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

    if select == "3":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -pool ssl://" +
                  region + ".ethermine.org:5555 -ewal " + (ethermine_wallet) + (miner_commands))

    if select == "4":
        os.system("OptimizeGPU.bat")
        os.system(r"Miners\ETHMiner\ethminer.exe -P ssl://" +
                  (ethermine_wallet) + r"@" + region + ".ethermine.org:5555" + " " + (miner_commands))

    if select == "exit":
        os.system('exit')

    sleep(10)
    os.system('exit')
