from os import system as c
import time

#----------- COLOUR -----------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

#----------- LOGO -----------#
def logo():
    c('clear')
    print(f"""{G}
██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║█████╗  ██║
██║███╗██║██║██╔══╝  ██║
╚███╔███╔╝██║███████╗██║
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝
{P} HACKING WORLD - WIFI HACK VIP TOOL
{A}------------------------------------------
""")

#----------- MAIN FUNCTION -----------#
def main():
    logo()
    c('espeak "WiFi Hacking Tool Starting"')
    wifi_name = input(f"{C}ENTER TARGET WIFI NAME (SSID): ")
    print(f"\n{Y}[+] Connecting to {wifi_name} Server...")
    time.sleep(2)
    print(f"{R}[!] This is a Premium Tool. 400 Taka Credit Required.")
    time.sleep(2)

    choice = input(f"{Y}Have You Purchased Credit? (yes/no): ").lower()
    if choice == "yes":
        print(f"\n{Y}[+] Redirecting to WhatsApp for Payment Confirmation...")
        time.sleep(2)
        whatsapp_number = "8801846390932"  # তোর নাম্বার বসা
        link = f"https://wa.me/{whatsapp_number}?text=I%20want%20to%20buy%20WiFi%20hack%20credit"
        c(f"xdg-open {link}")
        time.sleep(2)
        print(f"{G}[✓] WhatsApp Opened Successfully!")
    else:
        print(f"\n{R}[×] Sorry! Without Credit You Can't Hack {wifi_name}")
        time.sleep(2)

#----------- RUN TOOL -----------#
main()