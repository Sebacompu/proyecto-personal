import unittest

from decimal_numbers import decimal_to_roman

class TestDecimalToRomanNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman(1)  
        self.assertEqual(roman_number, 'I')

    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman(2)
        self.assertEqual(roman_number,'II')

    def test_decimal_3_to_roman(self):
        roman_number = decimal_to_roman(3)
        self.assertEqual(roman_number,'III')

    def test_decimal_4_to_roman(self):
        roman_number = decimal_to_roman(4)
        self.assertEqual(roman_number,'IV')

    def test_decimal_5_to_roman(self):
        roman_number = decimal_to_roman(5)
        self.assertEqual(roman_number,'V')

    def test_decimal_6_to_roman(self):
        roman_number = decimal_to_roman(6)
        self.assertEqual(roman_number,'VI')

    def test_decimal_7_to_roman(self):
        roman_number = decimal_to_roman(7)
        self.assertEqual(roman_number,'VII')

    def test_decimal_8_to_roman(self):
        roman_number = decimal_to_roman(8)
        self.assertEqual(roman_number,'VIII')

    def test_decimal_9_to_roman(self):
        roman_number = decimal_to_roman(9)
        self.assertEqual(roman_number,'IX')

    def test_decimal_19_to_roman(self):
        roman_number = decimal_to_roman(19)
        self.assertEqual(roman_number,'XIX')

    def test_decimal_20_to_roman(self):
        roman_number = decimal_to_roman(20)
        self.assertEqual(roman_number,'XX')

    def test_decimal_38_to_roman(self):
        roman_number = decimal_to_roman(38)
        self.assertEqual(roman_number,'XXXVIII')

    def test_decimal_76_to_roman(self):
        roman_number = decimal_to_roman(76)
        self.assertEqual(roman_number,'LXXVI')

    def test_decimal_119_to_roman(self):
        roman_number = decimal_to_roman(119)
        self.assertEqual(roman_number,'CXIX')

    def test_decimal_234_to_roman(self):
        roman_number = decimal_to_roman(234)
        self.assertEqual(roman_number,'CCXXXIV')

    def test_decimal_399_to_roman(self):
        roman_number = decimal_to_roman(399)
        self.assertEqual(roman_number,'CCCXCIX')

    def test_decimal_442_to_roman(self):
        roman_number = decimal_to_roman(442)
        self.assertEqual(roman_number,'CDXLII')

    def test_decimal_592_to_roman(self):
        roman_number = decimal_to_roman(592)
        self.assertEqual(roman_number,'DXCII')

    def test_decimal_678_to_roman(self):
        roman_number = decimal_to_roman(678)
        self.assertEqual(roman_number,'DCLXXVIII')

    def test_decimal_719_to_roman(self):
        roman_number = decimal_to_roman(719)
        self.assertEqual(roman_number,'DCCXIX')

    def test_decimal_853_to_roman(self):
        roman_number = decimal_to_roman(853)
        self.assertEqual(roman_number,'DCCCLIII')

    def test_decimal_947_to_roman(self):
        roman_number = decimal_to_roman(947)
        self.assertEqual(roman_number,'CMXLVII')

    def test_decimal_999_to_roman(self):
        roman_number = decimal_to_roman(999)
        self.assertEqual(roman_number,'CMXCIX')

    def test_decimal_409_to_roman(self):
        roman_number = decimal_to_roman(409)
        self.assertEqual(roman_number,'CDIX')

    

if __name__ == '__main__':
unittest.main()