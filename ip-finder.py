import os
import socket

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "Unable to get IP address. Make sure the URL is valid."

def show_banner():
    banner = """
\033[92m  _____ _____    ______ _____ _   _ _____  ______ _____  
\033[92m |_   _|  __ \  |  ____|_   _| \ | |  __ \|  ____|  __ \ 
\033[92m   | | | |__) | | |__    | | |  \| | |  | | |__  | |__) |
\033[92m   | | |  ___/  |  __|   | | | . ` | |  | |  __| |  _  / 
\033[92m  _| |_| |      | |     _| |_| |\  | |__| | |____| | \ \ 
\033[92m |_____|_|      |_|    |_____|_| \_|_____/|______|_|  \_\
                                                         
                                                          """
    print(banner)

def show_menu():
    clear_screen()
    show_banner()
    print("\033[92m1. Get IP address of a URL")
    print("\033[92m2. Exit")

# Main function
def main():
    while True:
        show_menu()
        option = input("\033[92mSelect an option: ")
        if option == "1":
            url = input("\033[92mEnter the URL of the website: ")
            ip_address = get_ip_address(url)
            print("\033[92mThe IP address of", url, "is:", ip_address)
            input("\033[92mPress Enter to continue...")
        elif option == "2":
            print("\033[92mGoodbye!")
            break
        else:
            print("\033[92mInvalid option. Please try again.")
            input("\033[92mPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
