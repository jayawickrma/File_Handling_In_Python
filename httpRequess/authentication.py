import requests

url ='https://httpbin.org/get'

username ='user'
password ='pass'

response =requests.get(url,auth=(username,password))

if response.status_code == 200:
    print("Authentication successful")
    print(response.text)

else:
    print("something went worng" +response.status_code)