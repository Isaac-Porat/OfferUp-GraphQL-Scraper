from colorama import Fore
from typing import Literal

class HelperObject:
    def __init__(self):
        pass

    def print_text(self, status: Literal['information', 'update', 'error'], text: str):
        if status == "information":
            print(Fore.GREEN + text + Fore.RESET)
        elif status == "update":
            print(Fore.YELLOW + text + Fore.RESET)
        elif status == "error":
            print(Fore.RED + text + Fore.RESET)
        else:
            print(text)
