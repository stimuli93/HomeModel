import utilities


class Home(object):
        def __init__(self, purchase_cost, maintainance_cost, property_tax):
            self.purchase_cost = purchase_cost
            self.maintainance_cost = maintainance_cost
            self.property_tax = property_tax/100.0

        def get_home_value(self, appreciation_rate, time):
            """
            :param appreciation_rate: Percentage
            :param time: time in yrs
            :return: net house value
            """
            return utilities.compound_value(self.purchase_cost, appreciation_rate, time)

        def get_home_expenses(self, maintainance_increment_rate, prop_tax_increment_rate, time):
            """
            :param maintainance_increment_rate: rate of increase in maintainance cost
            :param prop_tax_increment_rate: rate of increase in property tax
            :param time: duration in years
            :return: total expenses after given time period
            """
            net_expenses = \
                utilities.cummulative_compound_value(self.maintainance_cost, maintainance_increment_rate, time) +\
                utilities.cummulative_compound_value(self.property_tax*self.purchase_cost, prop_tax_increment_rate, time)
            return net_expenses