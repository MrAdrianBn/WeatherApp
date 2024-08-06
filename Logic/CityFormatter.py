
from Logic.Query import Query


class CityFormatter:
    def __init__(self, city_name, limit):
        self.city_name = city_name
        self.limit = limit
        self.city_information = [['' for _ in range(5)] for _ in range(self.limit)]

    def get_city_information(self):
        return self.city_information

    def show_available_cities(self):  # returns information about city specified by user

        query = Query(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        info = query.send_query()

        temp = [None for _ in range(len(info))]
        counter = 0
        for city in info:
            temp[counter] = city
            counter += 1

        col = 0
        for i in range(len(temp)):
            for key in temp[i]:
                if key != 'local_names':
                    self.city_information[i][col] = info[i][f'{key}']
                    col += 1
            col = 0

        # pop empty elements from list
        if len(info) < self.limit:
            for i in range(self.limit - 1, len(info) - 1, -1):
                self.city_information.pop(i)

        self.remove_duplicates()

        return self.get_city_information()

    def remove_duplicates(self):
        temp_lat = ''
        temp_lon = ''
        for i in range(len(self.city_information) - 1):
            if temp_lat == self.city_information[i][1] and temp_lon == self.city_information[i][2]:
                self.city_information.pop(i)
            else:
                for j in range(1, 3):
                    if j == 1:
                        temp_lat = self.city_information[i][j]
                    else:
                        temp_lon = self.city_information[i][j]

