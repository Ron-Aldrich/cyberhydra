import os
import time
import shutil
import assets
import readline
import glob


assets.banner()
assets.option()

while True:
    if shutil.which("hydra") is None:
        print("[!] hydra IS NOT INSTALLED. INSTALL IT DIRST TO USE THIS TOOL!")
    else:

        try:
            user = int(input("Enter: "))
            
            match user:
                case 1:
                    
                    readline.set_completer(lambda text, state: glob.glob(text + '*')[state] if state < len(glob.glob(text + '*')) else None)
                    readline.parse_and_bind("tab: complete")

                    clientchooseuser = input("Enter 1 to use file, or type 2 to enter username: ")

                    if clientchooseuser == "1":
                        user = input("Enter File: (e.g. /home/alias/user.txt): ")
                        usernamepath = f"-L {user}"

                    elif clientchooseuser == "2":
                        user = input("Enter Username: ")
                        usernamepath = f"-l {user}"

                    else:
                        print("Choose between 1 and 2.")
                        exit()  

                    print(usernamepath)


                    clientchoosepassword = input("Enter 1 to use file, or type 2 to enter password: ")

                    if clientchoosepassword == "1":
                        passwd = input("Enter File: (e.g. /home/alias/pass.txt): ")
                        passwordpath = f"-P {passwd}"  

                    elif clientchoosepassword == "2":
                        passwd = input("Enter Password: ")
                        passwordpath = f"-p {passwd}"  

                    else:
                        print("Choose between 1 and 2.")

                    clientdomain = input("Enter the domain (e.g. cyberronsite.com, without http/https): ")

                    clientlogin = input("Enter target login page (e.g. /login.php): ")
                    clientusertype = input("Enter form field for username (e.g. username): ")
                    clientpasstype = input("Enter form field for password (e.g. password): ")
                    clientf = input("What message appears when login fails? (e.g. 'Invalid login'): ")

                    hydra = f"hydra {usernamepath} {passwordpath} {clientdomain} -f https-post-form \"{clientlogin}:{clientusertype}=^USER^&{clientpasstype}=^PASS^:F={clientf}\""
                    os.system(hydra)
                    exit()
                case _:
                    print("Invlid. Please try again")
                    



        except KeyboardInterrupt:
            print("[!] Thank you for using this script!")
            exit()