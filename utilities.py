# method for calculating compounded value over time
def compound_value(prinipal, rate, time):
    """
    :param prinipal: Initial amount
    :param rate: Percentage apprecitation / depreciation
    :param time: duration in years
    :return: value compunded over time period
    """
    time -= 1
    rate /= 100.0
    net_value = prinipal*pow((1+rate), time)
    return net_value


# method for calculating cummulative compounded value over time
def cummulative_compound_value(principal, rate, time):
    """
    :param prinipal: Initial amount
    :param rate: Percentage apprecitation / depreciation
    :param time: duration in years
    :return: cummulative value compunded over time period
    """
    time -= 1
    rate /= 100.0
    cummulative_value = principal*((1-pow(rate, time+1))/(1-rate))
    return cummulative_value

