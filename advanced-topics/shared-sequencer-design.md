# Shared Sequencer Design

Shared sequencers are a proposed architecture where multiple rollups rely on the same decentralized sequencing layer.

This design aims to improve interoperability and reduce fragmentation.

---

# Motivation

Current rollups operate independent sequencers.

This causes several problems.

Cross-rollup latency

Transactions between rollups require bridging.

Liquidity fragmentation

Assets exist across multiple rollup ecosystems.

MEV fragmentation

Arbitrage opportunities appear across different rollups.

---

# Shared Sequencer Architecture

A shared sequencer network would coordinate ordering across multiple rollups.

The architecture typically includes:

Sequencer nodes

Nodes responsible for ordering transactions.

Consensus layer

Determines which sequencer produces the next batch.

Settlement layer

Rollups publish final transaction data to Ethereum.

---

# Benefits

Shared sequencing provides several advantages.

Atomic cross-rollup transactions

Users can interact with multiple rollups within a single transaction.

Reduced MEV fragmentation

Arbitrage opportunities can be executed more efficiently.

Improved composability

Applications across rollups can interact seamlessly.

---

# Challenges

Shared sequencers also introduce design challenges.

Latency

Cross-rollup coordination may increase execution time.

Security

Sequencer networks must resist collusion.

Economic incentives

Reward systems must align participants.

---

# Conclusion

Shared sequencing represents a major research direction in rollup infrastructure.

If successful, it could significantly improve cross-rollup composability.
