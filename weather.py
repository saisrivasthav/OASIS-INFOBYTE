import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An Error Occurred: {err}")
    return None

def display_weather(weather_data):
    if weather_data and weather_data.get('main'):
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        conditions = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {conditions.capitalize()}")
    else:
        print("Failed to retrieve weather data. Please check the location and try again.")

def is_valid_location(location):
    
    return bool(location.strip())

def main():
    api_key = "96579d893c2ba2c8e915a5a7ab904f2e"  
    location = input("Enter a city name or ZIP code: ").strip()
    
    if not is_valid_location(location):
        print("Invalid input. Please enter a valid city name or ZIP code.")
        return
    
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()