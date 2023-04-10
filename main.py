import json
import gtts
import requests
from playsound import playsound


def weather_reader():
    # greets
    greetings = "Hello there, I am the bot created by Uplaksh Tyagi, i can tell you the weather details of various cities around the globe."
    speaks = gtts.gTTS(greetings)
    speaks.save('greetings.mp3')
    playsound('greetings.mp3')

    # asks for city name
    speaks = gtts.gTTS("Enter the name of the city in the writing area or to end the interaction press x")
    speaks.save('asks_for_city_name.mp3')
    playsound('asks_for_city_name.mp3')
    while True:
        city_name = input()
        if city_name == "x":
            speaks = gtts.gTTS(f"I see you are satisfied with my service. Have a nice day. Bye!")
            speaks.save('signout.mp3')
            playsound('signout.mp3')
            break

        # confirms city name
        speaks = gtts.gTTS(f'you asked for the details of {city_name}')
        speaks.save('city_name.mp3')
        playsound('city_name.mp3')

        # fetches the details
        url = f'https://api.weatherapi.com/v1/current.json?key=9758dd7b099a4e52b53184228231004&q={city_name}'
        info = requests.get(url)
        info_dict = json.loads(info.text)
        info_dict_location_region = info_dict['location']['region']
        info_dict_location_country = info_dict['location']['country']
        info_dict_temp_in_c = info_dict["current"]["temp_c"]
        info_dict_temp_feelslike_in_c = info_dict["current"]["feelslike_c"]
        info_dict_temp_in_f = info_dict["current"]["temp_f"]
        info_dict_temp_feelslike_in_f = info_dict["current"]["feelslike_f"]
        info_dict_wind_speed_mph = info_dict["current"]["wind_mph"]
        info_dict_wind_speed_kph = info_dict["current"]["wind_kph"]
        info_dict_wind_direction = info_dict["current"]["wind_dir"]

        # gives the output
        speaks = gtts.gTTS(
            f"{city_name} is located in the region of {info_dict_location_region} in {info_dict_location_country}. The temperature in {city_name} is {info_dict_temp_in_c} degrees celsius and {info_dict_temp_in_f} degrees fahrenheit but it feels like {info_dict_temp_feelslike_in_c} degrees celsius and {info_dict_temp_feelslike_in_f} degrees fahrenheit respectively. The speed of wind in {city_name} is {info_dict_wind_speed_mph} miles per hour or {info_dict_wind_speed_kph} kilometers per hour")
        speaks.save("temperature.mp3")
        playsound('temperature.mp3')

        speaks = gtts.gTTS(f"If you want to get the weather report of any other city then enter the name of that city in writing area or to end the interaction press x.")
        speaks.save("repeats.mp3")
        playsound('repeats.mp3')

# main loop
if __name__ == "__main__":
    weather_reader()
