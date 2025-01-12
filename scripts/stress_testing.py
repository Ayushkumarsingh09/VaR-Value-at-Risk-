import numpy as np

def stress_test(portfolio_value, shock_percentages):
    results = {}
    for shock in shock_percentages:
        stressed_value = portfolio_value * (1 + shock / 100)
        results[f"{shock}% Shock"] = stressed_value
    return results

if __name__ == "__main__":
    portfolio_value = 1_000_000  # Example: $1,000,000 portfolio value
    shock_percentages = [-10, -20, -30, -50]  # Simulating market crashes

    stress_results = stress_test(portfolio_value, shock_percentages)
    for scenario, value in stress_results.items():
        print(f"{scenario}: ${value:,.2f}")
