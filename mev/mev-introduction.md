# MEV Introduction

MEV stands for **Maximal Extractable Value**.

It refers to the profit that block producers or specialized traders can extract by controlling the ordering, inclusion, or exclusion of transactions within a block.

MEV opportunities arise because blockchain transactions are visible in the public mempool before they are finalized.

Actors can analyze pending transactions and strategically insert their own transactions to capture value.

---

# Why MEV Exists

MEV emerges due to several characteristics of blockchain systems:

- transparent transaction mempools
- deterministic smart contract execution
- block producers controlling transaction ordering

Because transaction execution is predictable, sophisticated bots can simulate outcomes and identify profitable opportunities.

---

# Common Sources of MEV

The most common MEV strategies include:

- arbitrage between decentralized exchanges
- sandwich attacks on large trades
- liquidation opportunities in lending protocols
- NFT mint manipulation

These opportunities are typically executed by automated trading bots.

---

# Economic Impact

MEV has both positive and negative effects.

Positive effects:

- improves price efficiency through arbitrage
- ensures liquidations occur quickly

Negative effects:

- increases transaction costs for users
- enables front-running attacks
- reduces fairness in transaction execution

---

# Evolution of the MEV Ecosystem

The MEV ecosystem has evolved significantly.

Originally, miners captured MEV directly.

Today, the ecosystem includes:

- searchers
- block builders
- validators
- relays

This structure forms the **MEV supply chain**, which coordinates how profitable transactions are bundled and included in blocks.

---

# Conclusion

MEV is now a fundamental part of blockchain market structure.

Understanding how MEV works is essential for analyzing DeFi trading dynamics and designing protocols that mitigate harmful extraction.
