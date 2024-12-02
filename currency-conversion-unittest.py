import unittest
from Financial_USD_Currency_Converter import to_usd, from_usd, convert

class TestCurrencyConversion(unittest.TestCase):
    def test_to_usd_valid(self):
        self.assertEqual(to_usd('EUR', 100), 109)
        self.assertEqual(to_usd('YEN', 10000), 64)
        self.assertEqual(to_usd('GBP', 50), 65)

    def test_to_usd_invalid_currency(self):
        with self.assertRaises(ValueError):
            to_usd('XYZ', 100)

    def test_to_usd_negative_amount(self):
        with self.assertRaises(ValueError):
            to_usd('EUR', -100)

    def test_from_usd_valid(self):
        self.assertEqual(from_usd('EUR', 109), 100)
        self.assertEqual(from_usd('YEN', 64), 10000)
        self.assertEqual(from_usd('GBP', 65), 50)

    def test_from_usd_invalid_currency(self):
        with self.assertRaises(ValueError):
            from_usd('XYZ', 100)

    def test_from_usd_negative_amount(self):
        with self.assertRaises(ValueError):
            from_usd('EUR', -100)

    def test_convert_valid(self):
        self.assertEqual(
            convert('EUR', 100, 'GBP'),
            "100 EUR is equivalent to 83.85 GBP"
        )
        self.assertEqual(
            convert('USD', 100, 'AUD'),
            "100 USD is equivalent to 149.25 AUD"
        )

    def test_convert_unsupported_currency(self):
        self.assertEqual(
            convert('XYZ', 100, 'EUR'),
            "XYZ currency is not supported"
        )
        self.assertEqual(
            convert('USD', 100, 'ABC'),
            "ABC currency is not supported"
        )

    def test_convert_invalid_amount(self):
        self.assertEqual(convert('USD', -100, 'EUR'), "Invalid amount")

if __name__ == "__main__":
    unittest.main()
