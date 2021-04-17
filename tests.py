import unittest
from src.calculator import calc_net_pay


class TestCalculator(unittest.TestCase):
    def test_calc_net_pay(self):
        test_cases = [
            {"salary": 14000, "tax_due": 0, "ni_due": 0, "net_pay": 14000},
            {"salary": 20000, "tax_due": 1000, "ni_due": 600, "net_pay": 18400},
            {"salary": 55000, "tax_due": 9000, "ni_due": 4300, "net_pay": 41700}
        ]
        for test_case in test_cases:
            net_pay = calc_net_pay(test_case["salary"])
            assert net_pay["tax_due"] == test_case["tax_due"]
            assert net_pay["ni_due"] == test_case["ni_due"]
            assert net_pay["net_pay"] == test_case["net_pay"]
