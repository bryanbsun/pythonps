# 
# Python Problem Solver
# Week 12 Example 1: Text Flag 
#

from colorama import init, Fore, Back, Style

brightness = Style.NORMAL
s = "      "

for _ in range(5):
    color = Fore.BLACK + Back.BLUE
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", end = "")
    color = Fore.BLACK + Back.WHITE
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", end = "")
    color = Fore.BLACK + Back.RED
    print(f"{brightness}{color}{s}{Style.RESET_ALL}")
