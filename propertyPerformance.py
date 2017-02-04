class PropertyPerformance(object):
    def __init__(self, duration, rental_rate_increase_percent, rental_occupancy_rate, tax_rate_increase_percent,
                 home_appreciation_percent, maintainace_cost_percent, insurance_cost_percent, exit_closing_cost):
        self.duration = duration
        self.rental_rate_increase_percent = rental_rate_increase_percent
        self.rental_occupancy_rate = rental_occupancy_rate
        self.tax_rate_increase_percent = tax_rate_increase_percent
        self.home_appreciation_percent = home_appreciation_percent
        self.maintainace_cost_percent = maintainace_cost_percent
        self.insurance_cost_percent = insurance_cost_percent
        self.exit_closing_cost = exit_closing_cost