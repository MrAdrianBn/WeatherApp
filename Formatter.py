from Query import QueryCreator


class Formatter:
    def __init__(self, city_name, limit):
        self.city_name = city_name
        self.limit = limit
        self.information = [[''] * 4] * limit

    def show_available_cities(self):  # returns information about city specified by user

        query = QueryCreator('')
        query.set_url(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        info = query.make_query()

        col = 0
        row = 0
        info = info[0]

        for key in info:
            if key == 'lat':
                self.information[row][col] = info['lat']
                col += 1
        # trzeba zrobic tak by nie duplikowal wierszy - warszawa wystepuje tylko raz, jak ustawimy wiekszy limit to beda
        # duplikaty, nalezy potem jakos znalezc powtorzenia i je wyeliminowac
        print(self.information)
        print(info)
