import unittest
from Logic.CityFormatter import CityFormatter


class CityTest(unittest.TestCase):

    def test_get_city_information(self):
        city = CityFormatter('krakow', 1)
        self.assertEqual(city.show_available_cities()[0][0], 'Krakow')

    def test_pop_empty(self):
        city = CityFormatter('example', 6)
        flag = False
        counter = [1, 2, 3]
        for i in range(len(city.city_information)):
            for j in range(len(city.city_information[0])):
                if i < len(counter):
                    city.city_information[i][j] = 'example'
                    # 3 rows are filled with 'example', 3 last rows are empty (default '')
        city.pop_empty(counter)
        temp = 0
        for i in range(len(city.city_information)):
            for j in range(len(city.city_information[0])):
                if city.city_information[i][j] == '':
                    temp += 1
            if temp == len(city.city_information[0]):
                flag = True
            else:
                temp = 0
        self.assertFalse(flag)


if __name__ == '__main__':
    unittest.main()
