
from getch import pause
import pyautogui as pg
from time import sleep
from os import system, name
import sys


def clear():
    if name == "nt":  # pentru windows
        system('cls')
    else:  # pentru mac si linux
        system('clear')


def whatsappspammer():
    global message
    message = input("\033[1;33mChoose a message to spam: ")

    def retimes():
        global times
        times = int(
            input("\033[1;33mHow many times do you want to send the message(integer):"))

    def check():
        try:
            retimes()

            def redelay():
                global delay
                delay = float(
                    input("\033[1;33mPlease choose a delay between the messages!(float or integer):"))

            def check2():
                try:
                    redelay()

                    def finaltask():
                        print("\033[1;35mNow open whatsapp web on your computer.\nSelect a conversation(your target)and open the conversation.\nAfter that come back to this program and press any key to start\033[1;31m(don't close Whatsapp!)\033[1;35m.")
                        pause(
                            "\033[1;35mPress any key to start!\033[1;31mAfter you start the program open back Whatsapp and just wait 5 seconds!\t")
                        sleep(6)
                        global times
                        while times != 0:
                            pg.write(message)
                            pg.press('enter')
                            times -= 1
                            sleep(delay)
                        clear()
                        print('''\033[1;31m
                        
██████╗░██████╗░░█████╗░░█████╗░███████╗░██████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
██████╔╝██████╔╝██║░░██║██║░░╚═╝█████╗░░╚█████╗░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░

░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░██║░░██║
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░

░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗███████╗██╗░░░██╗██╗░░░░░██╗░░░░░██╗░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██║░░░██║██║░░░░░██║░░░░░╚██╗░██╔╝
╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░█████╗░░██║░░░██║██║░░░░░██║░░░░░░╚████╔╝░
░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║░░░██║██║░░░░░██║░░░░░░░╚██╔╝░░
██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝██║░░░░░╚██████╔╝███████╗███████╗░░░██║░░░
╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░''')
                        pause("Press any key to leave:")
                        clear()
                        sys.exit()
                    finaltask()
                except ValueError:
                    print("\033[1;31mPlease input a valid delay!")
                    sleep(2)
                    check2()
            check2()
        except ValueError:
            print("\033[1;31mERROR!\nPlease input an valid value!")
            sleep(2)
            check()
    check()


def showoptions():
    try:
        options = int(
            input("\033[1;34mOPTIONS:\n1)Whatsapp spammer\n\033[1;33mChoose one option: "))
        if options == 1:
            clear()
            printcool()
            try:
                whatsappspammer()
            except KeyboardInterrupt:
                print("\n\033[1;31mERROR!PROGRAM INTERRUPTED!")
        else:
            print("\033[1;31mTry again!")
            showoptions()
    except ValueError:
        print("\033[1;31mPlease input a valid value!")
        showoptions()


def printcool():
    print("""\033[1;31m
    ██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗██████╗░██╗░░██╗██╗░░░██╗
    ██║░░░██║██║██╔══██╗██║░░░██║██╔════╝██╔══██╗██║░░██║╚██╗░██╔╝
    ╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░██████╔╝███████║░╚████╔╝░
    ░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗██╔═══╝░██╔══██║░░╚██╔╝░░
    ░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝██║░░░░░██║░░██║░░░██║░░░
    ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░
                ░░██╗███████╗░█████╗░██████╗░██╗██╗░░
                ░██╔╝██╔════╝██╔══██╗██╔══██╗██║╚██╗░
                ██╔╝░█████╗░░███████║██████╦╝██║░╚██╗
                ╚██╗░██╔══╝░░██╔══██║██╔══██╗██║░██╔╝
                ░╚██╗██║░░░░░██║░░██║██████╦╝██║██╔╝░
                ░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░
""")


printcool()
try:
    showoptions()
except KeyboardInterrupt:
    print("\n\033[1;31m!ROGRAM INTERRUPTED!")
except ValueError:
    print("\033[1;31mPlease input a valid value!")
    showoptions()
