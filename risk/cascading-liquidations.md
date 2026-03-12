# Cascading Liquidations

Cascading liquidations occur when falling asset prices trigger a chain reaction of forced liquidations across lending markets.

These events can accelerate market crashes and create systemic risk within DeFi ecosystems.

---

# How Liquidations Work

Lending protocols require borrowers to maintain a minimum collateral ratio.

When collateral value drops below the required threshold, the position becomes eligible for liquidation.

Liquidators repay the debt and receive the collateral at a discounted price.

---

# What Causes Cascading Liquidations

During periods of high volatility, many positions may approach liquidation thresholds simultaneously.

When liquidations begin:

- collateral is sold on the market
- asset prices fall further
- additional positions become liquidatable

This feedback loop can trigger a cascade of liquidations.

---

# Example Scenario

1. ETH price drops rapidly
2. Borrowers with ETH collateral approach liquidation
3. Liquidators sell ETH to recover value
4. ETH price falls further
5. More positions become liquidatable

This chain reaction increases selling pressure and accelerates price declines.

---

# Liquidity Constraints

If market liquidity is insufficient, liquidations can push prices down sharply.

Low liquidity environments amplify the impact of cascading liquidations.

---

# Network Congestion

During extreme market events, blockchain networks may become congested.

If liquidations cannot be executed quickly enough, positions may become severely undercollateralized.

This increases the risk of bad debt.

---

# Risk Management Strategies

Protocols attempt to reduce cascading risk through:

- conservative collateral ratios
- partial liquidation mechanisms
- diversified collateral types
- deep liquidity markets

---

# Conclusion

Cascading liquidations represent a systemic risk in DeFi lending systems.

Understanding how liquidation feedback loops interact with market liquidity is essential for designing resilient protocols.
