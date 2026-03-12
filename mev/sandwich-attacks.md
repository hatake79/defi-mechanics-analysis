# Sandwich Attacks

A sandwich attack is one of the most common forms of MEV in decentralized exchanges.

The attacker exploits the predictable pricing mechanism of automated market makers (AMMs).

The attack surrounds a victim's trade with two transactions.

---

# Attack Structure

A typical sandwich attack involves three transactions:

1. Front-run transaction (attacker buys the asset)
2. Victim transaction (large trade moves the price)
3. Back-run transaction (attacker sells the asset)

This sequence allows the attacker to profit from the price movement caused by the victim's trade.

---

# Example

A user submits a large swap on a DEX.

Before the transaction executes:

- the attacker detects the trade in the mempool
- the attacker buys the token first

The victim trade executes and pushes the price higher.

The attacker then sells immediately, capturing the price difference.

---

# Why AMMs Are Vulnerable

AMM pricing formulas are deterministic.

Bots can simulate the exact price impact of pending transactions.

This makes it easy to calculate profitable front-running strategies.

---

# Impact on Users

Sandwich attacks cause:

- worse execution prices
- increased slippage
- higher trading costs

Retail users are particularly vulnerable.

---

# Mitigation Approaches

Several solutions attempt to reduce sandwich attacks.

Examples include:

- private transaction relays
- batch auction systems
- intent-based execution
- MEV-protected RPC endpoints
