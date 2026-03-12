# Interest Rate Models in DeFi Lending

Interest rate models are a critical component of decentralized lending protocols. They determine the borrowing cost for users and the yield earned by liquidity providers.

In most DeFi systems, interest rates are not fixed but dynamically adjusted based on market conditions.

---

# Utilization-Based Interest Rates

Most lending protocols rely on a utilization-based model.

Utilization rate is defined as:

Utilization = Total Borrowed / Total Liquidity

Example:

Total liquidity: 1,000,000 USDC  
Total borrowed: 700,000 USDC

Utilization = 70%

As utilization increases:

- borrowing rates increase
- lending yields increase

This mechanism encourages additional liquidity to enter the market.

---

# The Kink Model

Many lending protocols use a piecewise interest curve often called the **kink model**.

Before the kink point:

- interest rates grow slowly

After the kink point:

- interest rates increase sharply

This design discourages extreme utilization levels that could threaten liquidity.

Example parameters:

Base rate = 0%  
Kink utilization = 80%  
Slope before kink = low  
Slope after kink = very steep

---

# Why Dynamic Interest Rates Matter

Dynamic interest rates ensure that markets remain balanced.

If borrowing demand increases:

- rates increase
- more suppliers are incentivized to deposit assets

If borrowing demand decreases:

- rates fall
- borrowing becomes cheaper

---

# Protocol Examples

Different protocols implement variations of this model.

Examples include:

- Aave
- Compound
- Euler
- Morpho

Each protocol optimizes parameters differently to manage liquidity risk.

---

# Conclusion

Interest rate models act as the economic engine of lending protocols.

By dynamically adjusting borrowing costs based on utilization, these models help maintain liquidity, incentivize deposits, and reduce the risk of insolvency.
