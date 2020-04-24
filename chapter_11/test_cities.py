"""Test case for city_functions.py"""

import unittest
from city_functions import city_country

class CityCountryNameTestCase(unittest.TestCase):
    """Tests for country and name"""

    def test_city_country(self):
        """Verify that function values result in correct string"""
        city_country_name = city_country('san diego', 'united states')
        self.assertEqual(city_country_name, 'San Diego, United States')

    def test_city_country_population(self):
        """Verify that function values result in correct string w/ pop"""
        city_country_population_name = city_country(
            'san diego', 'united states', 1_410_000)
        self.assertEqual(
            city_country_population_name,
            'San Diego, United States - population 1410000')

if __name__ == '__main__':
    unittest.main()
