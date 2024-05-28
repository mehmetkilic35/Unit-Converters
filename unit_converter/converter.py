class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'length': {
                'meter': 1.0,
                'kilometer': 1000.0,
                'centimeter': 0.01,
                'millimeter': 0.001,
                'mile': 1609.34,
                'yard': 0.9144,
                'foot': 0.3048,
                'inch': 0.0254,
            },
            'weight': {
                'kilogram': 1.0,
                'gram': 0.001,
                'milligram': 0.000001,
                'ton': 1000.0,
                'pound': 0.453592,
                'ounce': 0.0283495,
            },
        }

    def convert(self, value, from_unit, to_unit, unit_type):
        if unit_type not in self.conversion_factors and unit_type != 'temperature':
            raise ValueError(f"Unknown unit type: {unit_type}")

        if unit_type == 'temperature':
            return self.convert_temperature(value, from_unit, to_unit)

        factors = self.conversion_factors[unit_type]
        if from_unit not in factors or to_unit not in factors:
            raise ValueError(f"Unknown units: {from_unit} or {to_unit}")

        base_value = value * factors[from_unit]
        return base_value / factors[to_unit]

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return value * 9/5 + 32
            elif to_unit == 'kelvin':
                return value + 273.15
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
        return value

def main():
    converter = UnitConverter()
    print(converter.convert(100, 'meter', 'kilometer', 'length'))  # Example usage
    print(converter.convert(0, 'celsius', 'fahrenheit', 'temperature'))  # Example usage

if __name__ == '__main__':
    main()
