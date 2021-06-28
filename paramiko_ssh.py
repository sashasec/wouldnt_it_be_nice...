# requirements: 
# sudo apt install python3-paramiko
# pip3 install colorama

# in your current working directory, place a file called "hosts.txt" that has new-line separated values. 

import paramiko
import colorama 
from colorama import Fore, Style
import getpass

#passwhat = getpass.getpass(prompt='Password: ', stream=None) #.strip() 
#command = 'ls -alh'
#command = 'echo JUSTKIDDINGy0 | sudo -S useradd -p $(openssl passwd -1 NOTKIDDING_NEWPASS) networking'
#command = 'echo JUSTKIDDINGy0 | sudo -S usermod -aG sudo networking'
#command = input("What would you like executied? ").strip()


def connect_ssh(host, user, passwhat, command):
    #print("\n\nLogging into " + host + " . . . \n")
    print("\n" + Fore.RED + Style.BRIGHT+ user + "@" + host + Style.RESET_ALL + ":" + Fore.CYAN + Style.BRIGHT + "/home/" + user + Style.RESET_ALL + "# " + command)
    client = paramiko.SSHClient()
    #client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=passwhat)
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout: 
        print('... ' + line.strip('\n'))
    client.close()

def main():
    filename = "./hosts.txt"
    print("Let's run some commands on remote linux servers over SSH!\n\n")
    user = input("User: ").strip()
    passwhat = getpass.getpass(prompt="Password: ", stream=None) 
    rolling = True 
    while(rolling):
        command = input("What do you want to run on all hosts? ").strip()

        with open(filename) as importfile:
            for host in importfile:
                connect_ssh(host.strip(), user, passwhat, command)
        more = int(input("\n\n\nAnything else? (0 or 1) "))
        print("\n")
        if not more: 
            rolling = False
    print(Fore.GREEN + Style.BRIGHT + "\n\nHave a cookie! You earned it. " + Style.RESET_ALL)
    print("\n\n\n")
#    print(Fore.RED + Style.BRIGHT + "Please select a valid option . . . " + Style.RESET_ALL)

if __name__ == "__main__":
    main()
