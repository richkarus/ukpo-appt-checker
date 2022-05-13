import time
import requests
import webbrowser
import sys
from typing import Tuple
from datetime import datetime as dt
from colorama import Fore, Style
from bs4 import BeautifulSoup


def get_page() -> Tuple[BeautifulSoup, float]:
    pp_url = "https://www.passportappointment.service.gov.uk"
    headers = {"User-Agent": "Prawntastic", "From": "beeboop@robot.com"}
    page = requests.get(pp_url, headers=headers)

    return (BeautifulSoup(page.content, "html.parser"), page.elapsed.total_seconds())


while True:
    print(
        f"{Fore.CYAN}[{dt.now().strftime('%H:%M:%S')}] {Fore.YELLOW}[!]{Style.RESET_ALL} Getting HMPO page..."
    )
    soup = get_page()
    print(
        f"{Fore.CYAN}[{dt.now().strftime('%H:%M:%S')}] {Fore.BLUE}[*]{Style.RESET_ALL} Got page in {soup[1]} secs..."
    )
    if not soup[0].body.findAll(text="Sorry, there are no available appointments"):
        print(
            f"[{dt.now().strftime('%H:%M:%S')}] {Fore.GREEN}[+]{Style.RESET_ALL} Found appointments! Opening URL!"
        )
        webbrowser.open(pp_url)

        # Keep hitting the bell until user ends it.
        while True:
            print("\a")
    print(
        f"{Fore.CYAN}[{dt.now().strftime('%H:%M:%S')}] {Fore.RED}[-]{Style.RESET_ALL} No appointments added yet, waiting 5 seconds."
    )
    print("\n")
    time.sleep(5)
