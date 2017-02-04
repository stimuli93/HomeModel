

def upfront_costs(equity, closing_cost):
    return -1 * (equity + closing_cost)


def delta_summation(term, amount, rate, rate_delta, discount):
    summation = 0
    for i in range(term):
        current_amount = amount*rate
        summation += current_amount*(1-discount)
        rate += rate*rate_delta
    return summation


def no_principal_summation(term, amount, rate, rate_delta):
    summation = 0
    for i in range(term):
        calcRate = rate * pow(1+rate_delta,i-1)
        totAmt = amount * calcRate
        summation += totAmt
    return summation


def summation_of_percentation_of_interest_compound(term, amount, rate, percent_interest):
    summation = 0
    for i in range(term):
        totAmt = amount * pow(1+rate, i-1) * percent_interest
    summation += totAmt
    return summation
