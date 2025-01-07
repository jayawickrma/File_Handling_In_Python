import requests

url ='https://example.com/search'

params ={'q':'python','category':'books'}

response=requests.get(url, params=params)  
print(response.url)
print(response.text)