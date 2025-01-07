# fletch the webpage,check if the request was successful,and ectract the main heading text from the page's content.
# yoy can assume that the base url is "http://example.com"
import requests
from bs4 import BeautifulSoup

# Base URL
baseUrl = 'http://example.com'


response = requests.get(baseUrl)


if response.status_code == 200:
 
    if 'application/json' in response.headers.get('Content-Type', ''):
        data = response.json()
        print("JSON Response:", data)
    else:
       
        soup = BeautifulSoup(response.content, 'html.parser')
     
        main_heading = soup.find('h1')
        if main_heading:
            print("Main Heading:", main_heading.text.strip())
        else:
            print("No <h1> tag found on the page.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
