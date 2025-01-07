import requests


base_url = 'https://api.open-meteo.com/v1/forecast'

params = {
    'latitude': 51.5074,          
    'longitude': -0.1278,       
    'current_weather': True       
}

try:

    response = requests.get(base_url, params=params)


    if response.status_code == 200:
        print("Request successful!")
        

        data = response.json()
        print("Full Weather Data:")
        print(data)
        

        if 'current_weather' in data:
            current_weather = data['current_weather']
            temperature = current_weather.get('temperature', 'N/A')
            windspeed = current_weather.get('windspeed', 'N/A')
            winddirection = current_weather.get('winddirection', 'N/A')
            
            print("\nExtracted Weather Details:")
            print(f"Temperature: {temperature}°C")
            print(f"Wind Speed: {windspeed} km/h")
            print(f"Wind Direction: {winddirection}°")
        else:
            print("Current weather data is not available.")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print("Response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")