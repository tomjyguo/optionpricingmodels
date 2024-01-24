def lattice_option_pricing(S, K, r, T, sigma, n, option_type='call'):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize option values at maturity
    option_values = np.maximum(0, S * (u ** np.arange(n + 1)) * (d ** np.arange(n, -1, -1)) - K)
    
    # Calculate option values at each node backward in time
    for j in range(n - 1, -1, -1):
        option_values = np.exp(-r * dt) * (p * option_values[:-1] + (1 - p) * option_values[1:])
        if option_type == 'put':
            option_values = np.maximum(option_values, K - S * (u ** np.arange(j + 1)) * (d ** np.arange(j, -1, -1)))
    
    return option_values[0]

# Example usage:
S0 = 100  # Current stock price
K = 100   # Option strike price
r = 0.05  # Risk-free rate
T = 1     # Time to maturity
sigma = 0.2  # Volatility
n = 100   # Number of time steps

call_price_lattice = lattice_option_pricing(S0, K, r, T, sigma, n, option_type='call')
put_price_lattice = lattice_option_pricing(S0, K, r, T, sigma, n, option_type='put')

print(f'Lattice Pricing Call Option Price: {call_price_lattice}')
print(f'Lattice Pricing Put Option Price: {put_price_lattice}')