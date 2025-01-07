import requests

def weatherFunction(latitude, longitude):
    """
    Fetches weather data from the Open-Meteo API for the specified coordinates.
    
    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    :return: JSON response data or None if the request fails
    """
    base_url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': True
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Response:", response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def weatherFunctionDetails(data):
    """
    Extracts and prints weather details from the API response data.
    
    :param data: JSON response data from the weather API
    """
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

def main():
    """
    Main function to fetch and display weather data.
    """
    latitude = 51.5074  # Example: London latitude
    longitude = -0.1278  # Example: London longitude
    
    print("Fetching weather data...")
    data = weatherFunction(latitude, longitude)
    
    if data:
        print("Full Weather Data:")
        print(data)
        weatherFunctionDetails(data)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
