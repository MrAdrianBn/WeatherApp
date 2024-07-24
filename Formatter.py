from Query import QueryCreator


class Formatter:
    def __init__(self, city_name, limit):
        self.city_name = city_name
        self.limit = limit

    def show_available_cities(self):  # returns information about city specified by user

        query = QueryCreator('')
        query.set_url(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        return query.make_query()
