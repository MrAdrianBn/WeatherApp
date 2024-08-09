import json

from Logic.Query import Query
from Logic.QueryCreator import QueryCreator
from Logic.CityFormatter import CityFormatter


class WeatherFormatter(QueryCreator):
    def __init__(self, city_formatter):
        self.amount_of_info = 17
        self.weather_information = ['' for _ in range(self.amount_of_info)]
        self.unit = 'metric'  # default metric
        self.city_formatter = city_formatter
        self.wanted_keys = ['description', 'icon', 'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity',
                            'sea_level', 'grnd_level', 'visibility', 'speed', 'deg', 'all', 'sunrise', 'sunset',
                            'timezone']

    def get_weather_information(self):
        return self.weather_information

    def set_unit(self, unit):
        self.unit = unit

    def get_unit(self):
        return self.unit

    def get_respond(self):
        query = Query(f'https://api.openweathermap.org/data/2.5/weather?lat={self.city_formatter.get_chosen_cords()[0]}&lon={self.city_formatter.get_chosen_cords()[1]}'
                      f'&appid=c614ed968bb3ba231528a9e4546a27f1&units={self.get_unit()}')
        return query.send_query()  # dict

    def extract_weather_information(self):

        info = self.get_respond()
        temp = str(info).replace("'", '"')

        info = json.loads(temp.replace('[', '').replace(']', ''))

        counter = 0
        for x, obj in info.items():
            if not isinstance(obj, int):
                for y in obj:
                    if y not in self.wanted_keys:
                        continue
                    else:
                        # self.weather_information[counter] = f'{y}:' + str(info[f'{x}'][f'{y}'])
                        self.weather_information[counter] = str(info[f'{x}'][f'{y}'])
                        counter += 1
            else:
                if x in self.wanted_keys:
                    # self.weather_information[counter] = f'{x}:' + str(info[f'{x}'])
                    self.weather_information[counter] = str(info[f'{x}'])
                    counter += 1

        return self.get_weather_information()
