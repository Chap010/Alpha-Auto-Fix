import os, time
from sys import stdout


def red():
    RED = "\033[1,31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;3m"
    stdout.write(WHITE)


Tool = """

  ___  _       _              ___        _         ______ _      
 / _ \| |     | |            / _ \      | |        |  ___(_)     
/ /_\ \ |_ __ | |__   __ _  / /_\ \_   _| |_ ___   | |_   ___  __
|  _  | | '_ \| '_ \ / _` | |  _  | | | | __/ _ \  |  _| | \ \/ /
| | | | | |_) | | | | (_| | | | | | |_| | || (_) | | |   | |>  < 
\_| |_/_| .__/|_| |_|\__,_| \_| |_/\__,_|\__\___/  \_|   |_/_/\_
        |_|                        
        """
Dev = "Creator: " + "Greaser"

def menu():
    red()
    print(Tool)
    blue()
    time.sleep(1)
    print(Dev)
    green()
    

    yellow()
    time.sleep(1)
    print("\nPlease Chose What to Install!")
    time.sleep(1)
    print("\n1 --> Install All Necessary Drivers and Update System")
    #time.sleep(1)
    print("\n2 --> Install Alpha Drivers Only")
    #time.sleep(1)
    print("\n3 --> Exit")
    #time.sleep(1)
    
    option = input("\n-->> ")
    if option == "1":
        Autofix()  
    if option == "2":
        Driversonly()
    if option == "3":
        exit()
    if option == "0":
        print("Thats Not An Option!")  
        menu()
    if option >= "3":
        print("Thats Not An Option!")  
        menu() 

# Updating and Installing Alpha Drivers
def Autofix():
    green()
    print("[+] Updating and Installing Necessary Drivers ...\n")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt dist-upgrade -y")
    os.system("sudo apt update")
    os.system("sudo apt install realtek-rtl88xxau-dkms")
    os.system("sudo apt install dkms")
    os.system("git clone https://github.com/aircrack-ng/rtl8812au")
    os.system("cd rtl8812au/")
    os.system("make")
    os.system("sudo make install")
    os.system("lsusb | iwconfig")
    time.sleep(2)
    print("[+] System has been Updated and Drivers Installed, Happy Hacking! :)")

# Downloading Alpha Drivers Only
def Driversonly():
    green()
    print("[+] Installing Alpha Adapter Drivers...\n")
    os.system("sudo apt install realtek-rtl88xxau-dkms")
    os.system("sudo apt install dkms")
    os.system("git clone https://github.com/aircrack-ng/rtl8812au")
    os.system("cd rtl8812au/")
    os.system("make")
    os.system("sudo make install")
    os.system("lsusb | iwconfig")
    time.sleep(2)
    print("[+] Drivers Instelled, Happy Hacking!:)")

if __name__ == '__main__':
    menu()

