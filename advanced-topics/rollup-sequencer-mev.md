# Rollup Sequencer MEV

Rollups are layer-2 scaling solutions that process transactions off-chain and submit compressed data to Ethereum.

Most rollups rely on a centralized sequencer to order transactions.

Because sequencers control transaction ordering, they can extract MEV.

---

# Role of the Sequencer

The sequencer performs several functions:

- ordering transactions
- batching transactions
- submitting batches to L1

This makes the sequencer similar to a block producer.

---

# Sources of MEV in Rollups

Several MEV strategies exist within rollup environments.

DEX arbitrage

Price differences between rollups and L1 can create arbitrage opportunities.

Liquidations

Sequencers can prioritize liquidation transactions.

Front-running

Sequencers may reorder transactions to capture trading profits.

---

# Centralization Risks

Most rollups currently operate with a single sequencer.

This creates several risks.

Censorship

Sequencers can delay or censor transactions.

MEV extraction

Sequencers may capture MEV without competition.

Fairness concerns

Users cannot verify whether ordering is neutral.

---

# Research Directions

Several solutions are being explored.

Decentralized sequencer networks

Multiple validators compete to produce rollup blocks.

Shared sequencers

Multiple rollups use the same sequencing infrastructure.

Encrypted mempools

Transactions remain hidden until execution.

---

# Conclusion

Sequencer design is one of the most important challenges in rollup architecture.

MEV management will likely shape the future of L2 infrastructure.
