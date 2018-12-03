from requests import get

def check():
    try:
        ip = get('https://api.ipify.org').text
        print('My public IP address is:', ip)
    except:
        print("Site down")

def host():
    host = input("IP Client'a: ")
    if host!="":
        return host
    else:
        return "localhost"
