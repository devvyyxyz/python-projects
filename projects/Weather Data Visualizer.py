import requests
import matplotlib.pyplot as plt

def fetch_weather(city):
    api_key = 'your_api_key'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def visualize_weather(weather_data):
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']

    labels = ['Temperature', 'Feels Like', 'Min Temp', 'Max Temp']
    values = [temp, feels_like, temp_min, temp_max]

    plt.bar(labels, values)
    plt.title('Weather Data')
    plt.show()

# Example usage
city = 'London'
weather_data = fetch_weather(city)
visualize_weather(weather_data)