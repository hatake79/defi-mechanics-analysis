# MEV Supply Chain

The modern MEV ecosystem operates through a specialized supply chain involving multiple actors.

These actors coordinate to extract value from transaction ordering.

---

# Key Participants

## Searchers

Searchers identify profitable opportunities such as:

- arbitrage
- sandwich attacks
- liquidations

They create transaction bundles designed to capture these opportunities.

---

## Builders

Builders assemble blocks by selecting and ordering transactions.

They receive bundles from searchers and construct blocks that maximize profitability.

---

## Relays

Relays act as intermediaries between builders and validators.

They facilitate secure communication and bundle delivery.

---

## Validators

Validators ultimately produce blocks and add them to the blockchain.

They choose the most profitable block proposals from builders.

---

# MEV-Boost Model

Ethereum's MEV ecosystem now uses a system known as **Proposer-Builder Separation (PBS)**.

In this model:

- builders construct blocks
- validators select the most profitable block

This separation allows specialized actors to optimize block construction.

---

# Implications

The MEV supply chain increases block production efficiency but also introduces centralization concerns.

Large builders and relays may accumulate significant influence over transaction ordering.

---

# Conclusion

Understanding the MEV supply chain is critical for analyzing modern blockchain market structure and designing mechanisms that mitigate harmful MEV extraction.
