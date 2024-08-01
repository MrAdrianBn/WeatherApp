import unittest
from Logic.Query import Query


class QueryTest(unittest.TestCase):
    def getter_setter_test(self):
        query = Query('')
        query.set_url('https://www.ibm.com/us-en')
        self.assertEqual("https://www.ibm.com/us-en", query.get_url())

    def server_respond_test(self):
        query = Query('http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        result = query.send_query()
        self.assertEqual(result['name'], 'London')

    def server_failure_test(self):
        query = Query('http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid'
                      '=c614ed968bb3ba231528a9e4546a27f1')
        result = query.send_query()
        self.assertEqual(result, ConnectionError)


if __name__ == '__main__':
    unittest.main()
