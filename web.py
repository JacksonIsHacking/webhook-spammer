import requests
import threading
from colorama import Fore
import pystyle
import time
def s(webhook, message, amount):
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'content': message
    }

    response = requests.post(webhook, headers=headers, json=data)
    if response.status_code == 204:
        print(time.strftime(f"\033[90m%H:%M:%S \033[90m[{Fore.LIGHTRED_EX}INFO\033[90m] - {Fore.WHITE}Sent: {message}"))
    else:
        print(time.strftime(f"\033[90m%H:%M:%S \033[90m[{Fore.LIGHTRED_EX}INFO\033[90m] - {Fore.WHITE}Can't Sent: {message}"))

def main():
    print(f"""{Fore.LIGHTRED_EX}
              _           
__      _____| |__  _   _ 
\ \ /\ / / _ \ '_ \| | | |
 \ V  V /  __/ |_) | |_| |
  \_/\_/ \___|_.__/ \__, |
                    |___/ 
    """)
    webhook = input(time.strftime(f"\033[90m%H:%M:%S \033[90m[{Fore.LIGHTRED_EX}>>>>\033[90m] - {Fore.WHITE}Enter Webhook{Fore.LIGHTRED_EX}: "))
    amount = int(input(time.strftime(f"\033[90m%H:%M:%S \033[90m[{Fore.LIGHTRED_EX}>>>>\033[90m] - {Fore.WHITE}Enter Amount Of Messages{Fore.LIGHTRED_EX}: ")))
    message = input(time.strftime(f"\033[90m%H:%M:%S \033[90m[{Fore.LIGHTRED_EX}>>>>\033[90m] - {Fore.WHITE}Enter Message{Fore.LIGHTRED_EX}: "))
    threads = []
    for _ in range(amount):
        thread = threading.Thread(target=s, args=(webhook, message, 1))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        input()

main()