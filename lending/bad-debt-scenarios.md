# Bad Debt Scenarios in DeFi Lending

Bad debt occurs when a borrower's collateral becomes insufficient to cover their outstanding loan.

When this happens, the protocol may suffer a loss.

Understanding bad debt scenarios is critical for risk analysis.

---

# Causes of Bad Debt

Several factors can lead to bad debt.

## Extreme Market Volatility

Rapid price crashes can reduce collateral value faster than liquidations can occur.

Example:

A 30–50% price drop within minutes may trigger widespread liquidations.

---

## Oracle Failures

Lending protocols rely on price oracles.

If oracle prices become inaccurate, liquidations may not trigger when necessary.

This can result in undercollateralized positions.

---

## Liquidity Crises

If collateral assets cannot be sold quickly, liquidators may avoid executing liquidations.

Low liquidity can cause positions to remain underwater.

---

## Network Congestion

During periods of heavy network activity, liquidation bots may fail to execute transactions quickly enough.

This delay can allow collateral values to fall further.

---

# Historical Examples

Several DeFi incidents have demonstrated the risks of bad debt.

Examples include:

- large market crashes
- oracle manipulation events
- liquidity crises during extreme volatility

---

# Mitigation Strategies

Protocols reduce bad debt risk through several mechanisms.

These include:

- conservative collateral factors
- fast oracle updates
- liquidation incentives
- insurance funds or protocol reserves

---

# Conclusion

Bad debt represents one of the most serious risks in decentralized lending systems.

Robust risk management and efficient liquidation infrastructure are essential for maintaining protocol stability.
