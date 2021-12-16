import asyncio
import requests
import tkinter as tk
from PIL import ImageTk, Image
import sys
from playsound import playsound
from random import randrange, uniform
import time
import webbrowser
from colorama import Fore, init
init()
r = requests.get('https://crazychicken334.2ix.at/cheesefunversion.html') # Checks for updates
if "1.0" not in r.text:
    print("Newer version found! Please update on Github")
    webbrowser.open("https://github.com/crazychicken334/CheeseFun/releases")
    quit()
def credits():
    print(Fore.YELLOW+"""
   ____   _                                  _____                
  / ___| | |__     ___    ___   ___    ___  |  ___|_   _   _ __  
 | |     | '_ \   / _ \  / _ \ / __|  / _ \ | |_  | | | | | '_ \ 
 | |___  | | | | |  __/ |  __/ \__ \ |  __/ |  _| | |_| | | | | |
  \____| |_| |_|  \___|  \___| |___/  \___| |_|    \__,_| |_| |_|
""")
    print(Fore.GREEN + "Made by @CrazyChicken334"+Fore.RED+"\nGithub: https://github.com/crazychicken334")
def cheesesound():
    playsound("cheese.wav")
def tab():
    window = tk.Tk()
    window.title("CHEESE")
    wrand1 = randrange(120, 900)
    wrand2 = randrange(120, 900)
    wert = f"{wrand1}x{wrand2}"
    window.geometry(wert)
    window.configure(background='white')
    path = "cheese-rem.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(window, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    window.mainloop()
    #cheesesound()

credits()
#playsound("cheese-ful.wav")
print(Fore.BLUE+"CheeseFun is loading...")
time.sleep(1)
for counter in range (15):
    tab()
print("Closing CheeseFun...")
time.sleep(2)
quit()

