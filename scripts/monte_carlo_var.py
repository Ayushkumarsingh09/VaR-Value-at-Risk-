import numpy as np

def monte_carlo_var(initial_value, mean, std_dev, iterations, confidence_level=0.95):
    # Simulate portfolio returns
    simulated_returns = np.random.normal(mean, std_dev, iterations)
    portfolio_values = initial_value * (1 + simulated_returns)

    # Calculate VaR as the percentile loss
    var = initial_value - np.percentile(portfolio_values, (1 - confidence_level) * 100)
    return var

if __name__ == "__main__":
    initial_value = 1_000_000  # Example: $1,000,000 portfolio value
    mean = 0.001  # Expected daily return
    std_dev = 0.02  # Daily standard deviation
    iterations = 100_000  # Number of simulations
    confidence_level = 0.95

    var = monte_carlo_var(initial_value, mean, std_dev, iterations, confidence_level)
    print(f"Monte Carlo VaR: {var}")

