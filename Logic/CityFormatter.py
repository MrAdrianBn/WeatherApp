from Logic.Query import Query
from Logic.QueryCreator import QueryCreator


class CityFormatter(QueryCreator):
    def __init__(self, city_name, limit):
        self.city_name = city_name
        self.limit = limit
        self.amount_of_info = 5
        self.city_information = [['' for _ in range(self.amount_of_info)] for _ in range(self.limit)]
        self.lat = []
        self.lon = []
        self.chosen_cords = [None for _ in range(2)]  # 2 cords (lat, lon)

    def get_city_information(self):
        return self.city_information

    def get_respond(self):
        query = Query(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        return query.send_query()

    def pop_empty(self, info):
        # pop empty elements from list
        if len(info) < self.limit:
            for i in range(self.limit - 1, len(info) - 1, -1):
                self.city_information.pop(i)

    def rewrite_cords(self):
        for i in range(len(self.city_information)):
            self.lat.append(self.city_information[i][1])
            self.lon.append(self.city_information[i][2])

    def set_chosen_cords(self, index):
        self.chosen_cords[0] = self.lat[index]
        self.chosen_cords[1] = self.lon[index]

    def get_chosen_cords(self):
        return self.chosen_cords

    def show_available_cities(self):  # returns information about city specified by user
        info = self.get_respond()

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

        self.pop_empty(info)
        self.remove_duplicates()
        self.rewrite_cords()
        self.set_chosen_cords(0)

        return self.get_city_information()

    def remove_duplicates(self):
        temp_lat = ''
        temp_lon = ''
        for i in range(len(self.city_information) - 1):
            j = i
            while j < len(self.city_information):
                if temp_lat == self.city_information[j][1] and temp_lon == self.city_information[j][2]:
                    self.city_information.pop(j)
                else:
                    j += 1
            else:
                temp_lat = self.city_information[i][1]
                temp_lon = self.city_information[i][2]
