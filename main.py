from property import Property
from purchase import Purchase
from propertyPerformance import PropertyPerformance
import utilities


def total_rental_revenue(property_obj, purchase_performance_obj):
    return utilities.delta_summation(purchase_performance_obj.duration, property_obj.annual_rent,
                                     purchase_performance_obj.rental_rate_increase_percent, 0,
                                     purchase_performance_obj.rental_occupancy_rate)


def home_exit_value(purchase_obj, purchase_performance_obj):
    return utilities.interest_compound(purchase_performance_obj.duration, purchase_obj.equity+purchase_obj.debt_amount,
                                       purchase_performance_obj.home_appreciation_percent)


def total_taxes_paid(property_obj, purchase_obj, purchase_performance_obj):
    return utilities.no_principal_summation(purchase_performance_obj.duration,
                                            purchase_obj.equity+purchase_obj.debt_amount, property_obj.tax_rate,
                                            purchase_performance_obj.tax_rate_increase_percent)


def total_maintainance_spend(purchase_obj, purchase_performance_obj):
    return utilities.summation_of_percentation_of_interest_compound(purchase_performance_obj.duration,
                                                                    purchase_obj.equity + purchase_obj.debt_amount,
                                                                    purchase_performance_obj.home_appreciation_percent,
                                                                    purchase_performance_obj.maintainace_cost_percent)


def total_insurance_costs(purchase_obj, purchase_performance_obj):
    return utilities.summation_of_percentation_of_interest_compound(purchase_performance_obj.duration,
                                                                    purchase_obj.equity + purchase_obj.debt_amount,
                                                                    purchase_performance_obj.home_appreciation_percent,
                                                                    purchase_performance_obj.insurance_cost_percent)


def main():
    annual_rent = input("Property Annual Rent: ")
    property_tax_rate = input("Property Tax Rate: ")

    property_tax_rate /= 100.0
    myProperty = Property(annual_rent=annual_rent, tax_rate=property_tax_rate)

    equity = input("Equity: ")
    closing_costs = input("Closing Costs: ")
    debt_amount = input("Debt Amount: ")
    interest_rate = input("Interest Rate: ")
    interest_rate /= 100.0

    term = input("Term: ")
    myPurchase = Purchase(equity=equity, closing_cost=closing_costs, debt_amount=debt_amount,
                          interest_rate=interest_rate, term=term)

    duration = input("Duration: ")
    rental_rate_increase_percent = input("Rental rate increase %: ")
    rental_rate_increase_percent /= 100.0

    rental_rate_occupancy = input("Rental rate occupancy: ")
    rental_rate_occupancy /= 100.0

    tax_rate_increase_percent = input("Tax Rate increase %: ")
    tax_rate_increase_percent /= 100.0

    home_appreciation_annual_percent = input("Home Appreciation Annual %: ")
    home_appreciation_annual_percent /= 100.0

    maintainance_cost_annual_percent = input("Maintainance Cost Annual %: ")
    maintainance_cost_annual_percent /= 100.0

    insurance_cost_percent = input("Insurance Cost %: ")
    insurance_cost_percent /= 100.0

    exit_closing_costs = input("Exit Closing Cost: ")
    myPropertyPerformace = PropertyPerformance(duration, rental_rate_increase_percent, rental_rate_occupancy,
                                               tax_rate_increase_percent, home_appreciation_annual_percent,
                                               maintainance_cost_annual_percent, insurance_cost_percent,
                                               exit_closing_costs)

    print "Upfront Costs: ", myPurchase.upfront_costs()
    print "Total Rental Revenue: ", total_rental_revenue(myProperty, myPropertyPerformace)
    print "Home Exit value: ", home_exit_value(myPurchase, myPropertyPerformace)
    print "Total Taxes Paid: ", total_taxes_paid(myProperty, myPurchase, myPropertyPerformace)
    print "Total Mainatainance: ", total_maintainance_spend(myPurchase, myPropertyPerformace)
    print "Total Insurance: ", total_insurance_costs(myPurchase, myPropertyPerformace)

if __name__ == "__main__":
    main()
