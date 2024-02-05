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

# Variables:
# S: Current stock price
# K: Option strike price
# r: Risk-free rate
# T: Time to maturity
# u: Up factor
# d: Down factor
# n: Number of time steps
