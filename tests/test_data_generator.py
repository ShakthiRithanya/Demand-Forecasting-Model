import unittest
import pandas as pd
from datetime import datetime
from src.data_generator import generate_demand_data

class TestDataGenerator(unittest.TestCase):
    def test_generate_demand_data_shape(self):
        start_date = datetime(2023, 1, 1)
        periods = 100
        df = generate_demand_data(start_date, periods)
        self.assertEqual(len(df), periods)
        self.assertIn('date', df.columns)
        self.assertIn('demand', df.columns)

    def test_generate_demand_data_non_negative(self):
        start_date = datetime(2023, 1, 1)
        df = generate_demand_data(start_date, 365)
        self.assertTrue((df['demand'] >= 0).all())

if __name__ == '__main__':
    unittest.main()
