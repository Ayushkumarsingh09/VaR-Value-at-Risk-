from scripts.historical_var import historical_var
from scripts.variance_covariance_var import variance_covariance_var
from scripts.monte_carlo_var import monte_carlo_var
from scripts.stress_testing import stress_test

if __name__ == "__main__":
    # Historical VaR
    historical_var_result = historical_var("data/portfolio_returns.csv", confidence_level=0.95)
    print(f"Historical VaR: {historical_var_result}")

    # Variance-Covariance VaR
    portfolio_std = 0.02
    vc_var_result = variance_covariance_var(portfolio_std, confidence_level=0.95)
    print(f"Variance-Covariance VaR: {vc_var_result}")

    # Monte Carlo VaR
    mc_var_result = monte_carlo_var(initial_value=1_000_000, mean=0.001, std_dev=0.02, iterations=100_000)
    print(f"Monte Carlo VaR: {mc_var_result}")

    # Stress Testing
    stress_results = stress_test(portfolio_value=1_000_000, shock_percentages=[-10, -20, -30])
    for scenario, value in stress_results.items():
        print(f"{scenario}: ${value:,.2f}")
