import pandas as pd
import numpy as np

def historical_var(data_path, confidence_level=0.95):
    # Load historical returns
    data = pd.read_csv(data_path)
    returns = data['returns']

    # Sort returns in ascending order
    sorted_returns = np.sort(returns)

    # Calculate the index of the VaR threshold
    var_index = int((1 - confidence_level) * len(sorted_returns))

    # Retrieve VaR
    var = sorted_returns[var_index]
    return var

if __name__ == "__main__":
    data_path = "../data/portfolio_returns.csv"
    confidence_level = 0.95
    var = historical_var(data_path, confidence_level)
    print(f"Historical VaR at {confidence_level * 100}% confidence: {var}")
