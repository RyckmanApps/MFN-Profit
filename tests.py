import unittest
from unittest.mock import patch
from calculations import calculate_profit
from handlers import handle_input

class TestCalculations(unittest.TestCase):
    def test_calculate_profit(self):
        user_input = {
            'Allstate': {
                'is_drp': 1,
                'per_ro_pre_tax_sales': 3800,
                'parts_sale': 0.4,
                'oem_percentage_of_parts': 0.65,
                'parts_disc_apply': 1,
                'bld_disc_apply': 0,
                'ro_count': 54,
                'volume_share': 0.25
            },
            'foreign_domestic': 1,
            'discount_rate': 0.075,
            'sample_ro_count': 216,
            'net_p': 0.12
        }
        result = calculate_profit(user_input)
        self.assertEqual(result['Allstate']['net_gain'], 9579)
        self.assertEqual(result['Allstate']['per_ro_net_profit'], 177)

class TestHandlers(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, 3800, 0.4, 0.65, 1, 0, 54, 0.25, 1, 0.075, 216, 0.12])
    def test_handle_input(self, mock_input):
        result = handle_input()
        self.assertEqual(result['Allstate']['is_drp'], 1)
        self.assertEqual(result['Allstate']['per_ro_pre_tax_sales'], 3800)
        self.assertEqual(result['Allstate']['parts_sale'], 0.4)
        self.assertEqual(result['Allstate']['oem_percentage_of_parts'], 0.65)
        self.assertEqual(result['Allstate']['parts_disc_apply'], 1)
        self.assertEqual(result['Allstate']['bld_disc_apply'], 0)
        self.assertEqual(result['Allstate']['ro_count'], 54)
        self.assertEqual(result['Allstate']['volume_share'], 0.25)
        self.assertEqual(result['foreign_domestic'], 1)
        self.assertEqual(result['discount_rate'], 0.075)
        self.assertEqual(result['sample_ro_count'], 216)
        self.assertEqual(result['net_p'], 0.12)

if __name__ == '__main__':
    unittest.main()
