import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return option_price

# Variables:
# S: Current stock price
# K: Option strike price
# T: Time to maturity
# r: Annual risk-free rate
# sigma: Volatility
# option_type: Either 'call' or 'put'
