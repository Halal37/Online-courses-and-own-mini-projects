from input_taker import take_float, take_string
from price_calculator import PriceCalculator


class Main:

    calc = PriceCalculator()

    def current_vat_info(self):
        vat = self.calc.get_vat()
        print("Hi there! Current VAT is " + str(vat))

    def take_vat_if_necessary(self):
        print("Do you want to change VAT? y/n")
        decision = take_string()

        if decision == "y":
            print("Please type VAT (from 0.0 to 1.0)")
            new_vat = take_float()
            self.calc.change_vat(new_vat)
            print("Got ya! New VAT is " + str(new_vat))

    def calculate_gross_price(self):
        print("Type net price: ")
        net_price = take_float()
        gross_price = self.calc.calculate_gross_price(net_price)
        print("Gross price is: " + str(gross_price))


main = Main()
main.current_vat_info()
main.take_vat_if_necessary()
main.calculate_gross_price()