# MEV-Boost Architecture

MEV-Boost is an off-chain infrastructure used by Ethereum validators to maximize block revenue by outsourcing block construction to specialized builders.

It is a practical implementation of Proposer-Builder Separation (PBS).

---

# Background

In early Ethereum, validators both built and proposed blocks.

However, MEV opportunities created an incentive for specialized actors to optimize block construction.

PBS separates these responsibilities:

- builders construct blocks
- proposers (validators) propose blocks

This separation improves efficiency and reduces centralization pressure.

---

# Core Architecture

The MEV supply chain consists of several actors.

Searchers  
Identify profitable opportunities such as arbitrage, liquidations, and sandwich attacks.

Builders  
Construct optimized blocks containing MEV bundles.

Relays  
Act as intermediaries between builders and validators.

Validators  
Select the most profitable block and propose it to the network.

---

# How MEV-Boost Works

1. Searchers create transaction bundles.
2. Builders assemble bundles into blocks.
3. Builders submit blocks to relays.
4. Relays forward block bids to validators.
5. Validators choose the highest bid and sign the block.

The selected block is then broadcast to the Ethereum network.

This creates a competitive auction for blockspace. :contentReference[oaicite:0]{index=0}

---

# Advantages

Higher validator revenue

Competition between block builders improves efficiency.

Reduced validator complexity

Validators do not need to run sophisticated MEV strategies.

Improved market structure

Open builder markets increase competition.

---

# Risks

MEV-Boost also introduces potential risks.

Builder centralization

A small number of builders may dominate block production.

Relay trust assumptions

Relays act as intermediaries and introduce additional infrastructure dependencies.

---

# Future: Enshrined PBS

Ethereum researchers are exploring "enshrined proposer-builder separation".

This would move PBS directly into the Ethereum protocol.

The goal is to reduce reliance on off-chain infrastructure.
