from requests import get
import subprocess

def check():
    try:
        ip = get('https://api.ipify.org').text
        print('My public IP address is:', ip)
    except:
        print("Site down")

def host(name):
    host = input("IP " + name[0:-3] + "'a: ")
    if host!="":
        return host
    else:
        return "localhost"

def startServer():
    program = ['python.exe', 'server.py']
    server = subprocess.Popen(program)
    print("Hello Valle")
    return server
#code = process.wait()
#print(code) # 0
