import requests

response =requests.get('https://api.github.com/events')
# print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)

if 'application/json' in response.headers.get('Content-Type',''):
    data =response.json()

    print(data)