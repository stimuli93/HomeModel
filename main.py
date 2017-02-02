from home import Home
import utilities


def main():
    purchase_cost = input("Purchase Cost: ")
    down_payment = input("Initial Downpayment: ")
    loan_taken = purchase_cost - down_payment
    mortgage_rate = input("Mortgage Rate in %: ")
    time_period = input("Time period of holding property (in yrs): ")
    maintainance_cost = input("Maintainance Cost (1st year cost): ")
    property_tax = input("Property Tax in %: ")
    rent = input("Rental Revenue (1st year): ")
    apprecitaion_rate = input("Property appreciation rate in %: ")
    maintaince_rate_increment = 10
    prop_tax_increment_rate = 10
    rental_increment_rate = 10

    my_home = Home(purchase_cost, maintainance_cost, property_tax)
    home_expenses = my_home.get_home_expenses(maintainance_increment_rate=maintaince_rate_increment,
                                              prop_tax_increment_rate=prop_tax_increment_rate, time=time_period)

    # this needs work
    loan_expenses = (loan_taken*mortgage_rate*time_period)/100.0
    net_expenses = purchase_cost + loan_expenses + home_expenses

    net_rental_revenue = utilities.cummulative_compound_value(rent, rental_increment_rate, time_period)
    home_value = my_home.get_home_value(apprecitaion_rate, time_period)

    net_return = home_value + net_rental_revenue - net_expenses
    roi = net_return*100.0/(purchase_cost*time_period)
    print "Net Profit: ", net_return
    print "ROI: ", roi

if __name__ == "__main__":
    main()
