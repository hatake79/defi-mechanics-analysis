# Liquidation Mechanisms in DeFi Lending

Liquidations are a core risk management mechanism in lending protocols.

They ensure that loans remain sufficiently collateralized and protect the system from bad debt.

---

# Health Factor

Most protocols track borrower positions using a health metric.

Health Factor = Collateral Value / Borrowed Value

If the health factor falls below a threshold, the position becomes eligible for liquidation.

Example:

Collateral value = $10,000  
Borrowed value = $8,500

If the protocol requires a minimum ratio of 1.2, the position may be liquidated.

---

# Liquidation Process

The typical liquidation flow:

1. Borrower's collateral value drops
2. Health factor falls below threshold
3. Liquidators repay part of the debt
4. Liquidators receive collateral at a discount

This discount is known as the **liquidation bonus**.

---

# Role of Liquidators

Liquidators are external participants who monitor the protocol for unhealthy positions.

They use automated bots to detect and execute liquidation opportunities.

In return, they earn profits from the liquidation bonus.

---

# Partial Liquidations

Many protocols allow partial liquidations.

Instead of closing the entire position, only a portion of the debt is repaid.

This helps stabilize markets and prevents excessive selling pressure.

---

# Liquidation Competition

Liquidation opportunities are highly competitive.

Bots continuously monitor on-chain data and attempt to execute transactions faster than competitors.

This dynamic often intersects with MEV strategies.

---

# Conclusion

Liquidation mechanisms play a critical role in maintaining the solvency of lending markets.

Without efficient liquidations, lending protocols would accumulate bad debt and become unstable.
