

def delta_summation(term, amount, rate, rate_delta, occupancy):
    summation = 0
    for i in range(term):
        current_amount = amount*rate
        summation += current_amount*occupancy
        rate += rate*rate_delta
    return summation


def no_principal_summation(term, amount, rate, rate_delta):
    summation = 0
    for i in range(term):
        calcRate = rate * pow(1+rate_delta, i)
        totAmt = amount * calcRate
        summation += totAmt
    return summation


def summation_of_percentation_of_interest_compound(term, amount, rate, percent_interest):
    summation = 0
    for i in range(term):
        totAmt = amount * pow(1+rate, i) * percent_interest
    summation += totAmt
    return summation


def interest_compound(term, amount, rate):
    return amount*pow(1+rate, term-1)
