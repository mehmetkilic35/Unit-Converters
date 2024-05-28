import unittest
from unit_converter.converter import UnitConverter

class TestUnitConverter(unittest.TestCase):
    def setUp(self):
        self.converter = UnitConverter()

    def test_length_conversion(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'kilometer', 'length'), 0.001)
        self.assertAlmostEqual(self.converter.convert(100, 'centimeter', 'meter', 'length'), 1)

    def test_weight_conversion(self):
        self.assertAlmostEqual(self.converter.convert(1, 'kilogram', 'gram', 'weight'), 1000)
        self.assertAlmostEqual(self.converter.convert(1, 'pound', 'kilogram', 'weight'), 0.453592)

    def test_temperature_conversion(self):
        self.assertAlmostEqual(self.converter.convert(0, 'celsius', 'fahrenheit', 'temperature'), 32)
        self.assertAlmostEqual(self.converter.convert(273.15, 'kelvin', 'celsius', 'temperature'), 0)

if __name__ == '__main__':
    unittest.main()
