import pytest
from price_calculator import PriceCalculator

class TestPriceCalculator:
    def test_adding_two_numbers(self):
        the_sum = 2 + 2
        assert the_sum == 4
    def test_calculating_ross_price_with_default_vat(self):
        calc = PriceCalculator()
        result = calc.calculate_gross_price(100)
        assert result == 123

    def test_calculating_gross_price_with_different_vat(self):
            #given 
            calc = PriceCalculator()
            calc.change_vat(0.08)

            #when
            result=calc.calculate_gross_price(100)

            #then
            assert result == 108

    def test_changing_vat_with_incorrect_value(self):
            calc = PriceCalculator()
            with pytest.raises(ValueError):
                    calc.change_vat(-1)