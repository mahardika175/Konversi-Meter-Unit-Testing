import unittest
from unittest.mock import patch
from uts import konversi_meter

class TestKonversiMeter(unittest.TestCase):
    # [Meter ke Milimeter]
    @patch('builtins.input', side_effect = ['1', '24'])
    def test_metertomili(self, input):
        result = konversi_meter()
        self.assertEqual(round(result, 1), 24000.0)

    # [Meter ke Centimeter]
    @patch('builtins.input', side_effect = ['2', '7'])
    def test_metertocenti(self, input):
        result = konversi_meter()
        self.assertEqual(round(result, 1), 750.0) # ini salah, hasil harusnya 700

    # [Meter ke Inci]
    @patch('builtins.input', side_effect = ['3', '182'])
    def test_metertoinci(self, input):
        result = konversi_meter()
        self.assertEqual(round(result, 1), 7165.4)

    # [Meter ke Kaki]
    @patch('builtins.input', side_effect = ['4', '50'])
    def test_metertokaki(self, input):
        result = konversi_meter()
        self.assertEqual(round(result, 1), 164.0)

    # [Meter ke Yard]
    @patch('builtins.input', side_effect = ['5', '16'])
    def test_metertoyard(self, input):
        result = konversi_meter()
        self.assertEqual(round(result, 1), 17.0) # ini salah, hasil harusnya 17.5
        
if __name__ == "__main__":
    unittest.main()