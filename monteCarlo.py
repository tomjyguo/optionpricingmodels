import numpy as np

def monte_carlo_option_price(S, K, r, T, sigma, num_simulations, option_type='call'):
    dt = T / 252
    simulated_paths = S * np.exp(np.cumsum((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1, (252, num_simulations)), axis=0))
    
    if option_type == 'call':
        option_payoffs = np.maximum(simulated_paths[-1] - K, 0)
    if option_type == 'put':
        option_payoffs = np.maximum(K - simulated_paths[-1], 0)
    
    option_price = np.exp(-r * T) * np.mean(option_payoffs)
    
    return option_price

# Variables: 
# S: Current stock price
# K: Option strike price
# r: Risk-free rate
# T: Time to maturity
# sigma: Volatility
# num_simulations: simulations ran

# Example:
# call_price_mc = monte_carlo_option_price(S0, K, r, T, sigma, num_simulations, option_type='call')
# put_price_mc = monte_carlo_option_price(S0, K, r, T, sigma, num_simulations, option_type='put')
