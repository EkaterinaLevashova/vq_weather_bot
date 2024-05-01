import requests
from bs4 import BeautifulSoup


class Weather:
    def __init__(self):
        self.temperature = None
        self.description = None

    @classmethod
    def get_weather(cls):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            url = "https://meteofor.com.ua/weather-odesa-4982/now/"
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            weather_block = soup.find("div", class_="widget now")
            if weather_block:
                temperature = weather_block.find("div", class_="now-weather").text.strip()
                description = weather_block.find("div", class_="now-desc").text.strip()
                return {
                    "temperature": temperature,
                    "description": description
                }
            else:
                return None

        except Exception as e:
            print("An error occurred:", e)

        return None
