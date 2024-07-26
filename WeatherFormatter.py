from Query import Query


class WeatherFormatter:
    # wziac koniecznie kod ikony zeby potem moc ja pobrac ze strony, dodac tez informacje raczej jako lista
    def __init__(self):
        self.weather_information = ['' for _ in range(19)]
        self.unit = 'metric'  # default metric

    def get_weather_information(self):
        return self.weather_information

    def set_unit(self, unit):
        self.unit = unit

    def get_unit(self):
        return self.unit

    def extract_weather_information(self, lat, lon):
        query = Query(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}'
                      f'&appid=c614ed968bb3ba231528a9e4546a27f1&units={self.unit}')

        info = query.send_query()

        counter = 0
        wanted_keys = ['description', 'icon', 'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity',
                       'sea_level', 'grnd_level', 'visibility', 'speed', 'deg', 'all', 'sunrise', 'sunset', 'timezone']
        for key in info:
            if key in wanted_keys:
                self.weather_information[counter] = info[f'{key}']
                counter += 1

        return self.get_weather_information()
