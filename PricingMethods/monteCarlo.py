import numpy as np

def monte_carlo_option_price(S, K, r, T, sigma, num_simulations, option_type='call'):
    dt = T / 252
    simulated_paths = S * np.exp(np.cumsum((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1, (252, num_simulations)), axis=0))
    
    if option_type == 'call':
        option_payoffs = np.maximum(simulated_paths[-1] - K, 0)
    elif option_type == 'put':
        option_payoffs = np.maximum(K - simulated_paths[-1], 0)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    option_price = np.exp(-r * T) * np.mean(option_payoffs)
    
    return option_price

# Example usage:
S0 = 100  # Current stock price
K = 100   # Option strike price
r = 0.05  # Risk-free rate
T = 1     # Time to maturity
sigma = 0.2  # Volatility
num_simulations = 100000

call_price_mc = monte_carlo_option_price(S0, K, r, T, sigma, num_simulations, option_type='call')
put_price_mc = monte_carlo_option_price(S0, K, r, T, sigma, num_simulations, option_type='put')

print(f'Monte Carlo Call Option Price: {call_price_mc}')
print(f'Monte Carlo Put Option Price: {put_price_mc}')