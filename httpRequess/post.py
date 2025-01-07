import requests

inputs ={'Username':'user' ,'password':'pass'}

response =requests.post('https://httpbin.org/post',inputs)

if response.status_code==200:
    print("login successfull")
    print(response.text)

else:
    print('login failed...'+response.status_code)
