import unittest
from calculations import calculate_profit

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
        self.assertAlmostEqual(result['Allstate']['net_gain'], 9579, delta=1)
        self.assertAlmostEqual(result['Allstate']['per_ro_net_profit'], 177, delta=1)

if __name__ == '__main__':
    unittest.main()
