def two_state_option_tree(S, K, r, T, u, d, n):
    dt = T / n
    p = (1 + r * dt - d) / (u - d)
    
    # Initialize option values at maturity
    option_values = [max(0, S * (u ** (n - k)) * (d ** k) - K) for k in range(n + 1)]
    
    # Calculate option values at each node backward in time
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            option_values[i] = max(0, np.exp(-r * dt) * (p * option_values[i] + (1 - p) * option_values[i + 1]))
    
    return option_values[0]

# Example usage:
S0 = 100  # Current stock price
K = 100   # Option strike price
r = 0.05  # Risk-free rate
T = 1     # Time to maturity
u = 1.2   # Up factor
d = 0.8   # Down factor
n = 3     # Number of time steps

option_price = two_state_option_tree(S0, K, r, T, u, d, n)
print(f'Two-State Option Tree Price: {option_price}')