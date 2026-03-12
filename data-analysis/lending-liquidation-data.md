# Lending Liquidation Data Analysis

Liquidations are a critical mechanism that protects lending protocols from insolvency.

This analysis explores how liquidation events occur and how they affect DeFi markets.

---

# Liquidation Mechanics

When collateral value falls below a threshold, a borrower's position becomes eligible for liquidation.

Liquidators repay part of the debt and receive collateral at a discount.

---

# Health Factor

Most lending protocols use a health factor to evaluate the safety of a position.

The health factor can be approximated as:

\text{Health Factor} = \frac{\text{Collateral Value} \times \text{Liquidation Threshold}}{\text{Borrowed Value}}

If the health factor falls below 1, the position can be liquidated.

---

# Market Dynamics

Liquidation events often occur during periods of high volatility.

Price crashes can trigger cascading liquidations across lending platforms.

This can lead to:

- rapid collateral sales
- increased market volatility
- temporary liquidity stress

---

# Historical Observations

Major liquidation waves have occurred during several market events.

Examples include:

- the 2020 DeFi market crash
- the Terra collapse
- large market corrections

---

# Risk Management

Protocols manage liquidation risk through several mechanisms.

Examples include:

- overcollateralization
- liquidation penalties
- oracle price feeds

---

# Conclusion

Liquidation data provides valuable insights into market risk and protocol resilience in decentralized finance.
