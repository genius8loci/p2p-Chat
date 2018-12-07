from requests import get
import subprocess
import socket
from colorama import *
init()

print(Style.BRIGHT, end='')


def check():
    print(Fore.GREEN, end='')

    #Public ip
    try:
        ip = get('https://api.ipify.org').text
        print('Public IP is:', ip)
    except:
        print(Fore.RED + "Site down")
    finally:
        #Local ip
        local = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE)
        IP = local.communicate()
        local.stdout.close()
        local.wait()
        s=str(IP).split('\\r\\n')
        for i in s:
            c=i.find(':')
            if c!=-1 and i.find('IPv4')!=-1:
                print('Local IP is:', i[c+2:])
                break


def host():
    print(Fore.CYAN, end='')

    with open("host.txt", "r+") as f:
        host = f.read()

        if host=='':
            f.write(input("IP your friend (enter to localhost): "))
            if host=='':
                f.write("localhost")
                f.close()
                return "localhost"
        if host!='':
            f.close()
            return host


def startServer():
    print(Fore.MAGENTA, end='')

    program = ['python.exe', 'server.py']
    server = subprocess.Popen(program)
    print("Hello Valle")
    return server
#code = process.wait()
#print(code) # 0

def confirm(msg):
    print(Back.GREEN + '\033[A\033[A' + ': ' + msg)
    print(Style.RESET_ALL, end='')
