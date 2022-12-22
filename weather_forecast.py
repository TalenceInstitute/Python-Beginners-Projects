'''
python3 weather_forecast.py 
Enter your location (city name): New-York City
Enter your OpenWeatherMap API key: cd38d998a0e66fc9e6eb372373a0732a
Latitude: 40.7127281
'''

import requests

# Function to retrieve the latitude and longitude for a given location using the OpenWeatherMap API
def get_coordinates(location, api_key):
    # Construct the API request URL
    api_url = f"https://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
    
    # Send the request to the API and retrieve the response
    response = requests.get(api_url)
    
    # Check the status code of the response
    if response.status_code == 404:
        # Return an empty dictionary if the location is not found
        return {}
    else:
        # Return the first element of the list of dictionaries as a dictionary
        return response.json()[0]

# Function to retrieve weather data from the OpenWeatherMap API
def get_weather_data(location, api_key):
    # Retrieve the latitude and longitude for the location
    coordinates = get_coordinates(location, api_key)
    
    # Check if the location was found
    if coordinates:
        # Extract the latitude and longitude from the response
        lat = coordinates["lat"]
        lon = coordinates["lon"]
        
        # Construct the API request URL
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        print("Latitude:", lat)
        print("Longitude:", lon)
        print("API URL:", api_url)
        
        # Send the request to the API and retrieve the response
        response = requests.get(api_url)
        
        # Return the response as a dictionary
        return response.json()
    else:
        # Return an empty dictionary if the location is not found
        return {}

# Function to parse the weather data into a usable format
def parse_weather_data(weather_data):
    # Extract the relevant data from the weather data dictionary
    forecast = {
        "temperature": weather_data["main"]["temp"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"],
        "description": weather_data["weather"][0]["description"]
    }
    
    # Return the forecast data
    return forecast

# Function to display the forecast to the user
def display_forecast(forecast):
    # Print out the forecast data
    print(f"Temperature: {forecast['temperature']} degrees Celsius")
    print(f"Humidity: {forecast['humidity']}%")
    print(f"Wind speed: {forecast['wind_speed']} m/s")
    print(f"Description: {forecast['description']}")

# Main program
def main():
    # Ask the user for their location and API key
    location = input("Enter your location (city name): ")
    api_key = input("Enter your OpenWeatherMap API key: ")

    # Retrieve the weather data for the location
    weather_data = get_weather_data(location, api_key)

    # Parse the weather data into a usable format
    forecast = parse_weather_data(weather_data)

    # Display the forecast to the user
    display_forecast(forecast)
    
# Run the main program
if __name__ == "__main__":
    main()
