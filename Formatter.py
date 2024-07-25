from Query import QueryCreator


class Formatter:
    def __init__(self, city_name, limit):
        self.city_name = city_name
        self.limit = limit
        self.information = [['' for _ in range(5)] for _ in range(self.limit)]

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
                match key:
                    case 'name':
                        self.information[i][col] = info[i]['name']
                        col += 1
                    case 'lat':
                        self.information[i][col] = info[i]['lat']
                        col += 1
                    case 'lon':
                        self.information[i][col] = info[i]['lon']
                        col += 1
                    case 'country':
                        self.information[i][col] = info[i]['country']
                        col += 1
                    case 'state':
                        self.information[i][col] = info[i]['state']
                        col += 1
            col = 0

        # print(self.information)
        # print(info)
