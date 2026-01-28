import unittest
import numpy as np
from src.models import calculate_metrics

class TestMetrics(unittest.TestCase):
    def test_calculate_metrics_perfect(self):
        y_true = np.array([10, 20, 30])
        y_pred = np.array([10, 20, 30])
        metrics = calculate_metrics(y_true, y_pred)
        self.assertEqual(metrics['MSE'], 0)
        self.assertEqual(metrics['MAE'], 0)
        self.assertEqual(metrics['RMSE'], 0)

    def test_calculate_metrics_values(self):
        y_true = np.array([10, 20])
        y_pred = np.array([12, 18])
        metrics = calculate_metrics(y_true, y_pred)
        # MSE = (2^2 + 2^2) / 2 = 4
        # MAE = (2 + 2) / 2 = 2
        # RMSE = 2
        self.assertEqual(metrics['MSE'], 4)
        self.assertEqual(metrics['MAE'], 2)
        self.assertEqual(metrics['RMSE'], 2)

if __name__ == '__main__':
    unittest.main()
