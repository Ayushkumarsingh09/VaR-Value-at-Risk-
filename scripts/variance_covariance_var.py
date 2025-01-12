import numpy as np

def variance_covariance_var(portfolio_std, portfolio_mean=0, confidence_level=0.95, time_horizon=1):
    # Z-Score for the given confidence level
    z = abs(np.percentile(np.random.normal(size=100000), (1 - confidence_level) * 100))

    # Calculate VaR
    var = z * portfolio_std * np.sqrt(time_horizon)
    return var

if __name__ == "__main__":
    portfolio_std = 0.02  # Example: 2% daily standard deviation
    confidence_level = 0.95
    time_horizon = 1  # One-day VaR
    var = variance_covariance_var(portfolio_std, confidence_level=confidence_level, time_horizon=time_horizon)
    print(f"Variance-Covariance VaR: {var}")
