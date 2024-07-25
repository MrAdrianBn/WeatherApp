from Query import QueryCreator


class CityFormatter:
    def __init__(self, city_name, limit):
        self.city_name = city_name
        self.limit = limit
        self.information = [['' for _ in range(5)] for _ in range(self.limit)]

    def get_information(self):
        return self.information

    def show_available_cities(self):  # returns information about city specified by user

        query = QueryCreator('')
        query.set_url(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        info = query.make_query()

        temp = [None for _ in range(self.limit)]
        counter = 0
        for city in info:
            temp[counter] = city
            counter += 1

        col = 0
        for i in range(len(temp)):
            for key in temp[i]:
                if key != 'local_names':
                    self.information[i][col] = info[i][f'{key}']
                    col += 1
            col = 0
