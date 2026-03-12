# DeFi Glossary

This glossary defines key terms used in decentralized finance (DeFi).

The goal is to provide quick explanations of important mechanisms, concepts, and infrastructure used across DeFi protocols.

---

# A

## AMM (Automated Market Maker)

A decentralized exchange mechanism where prices are determined algorithmically using liquidity pools instead of order books.

Example formula:

x * y = k

---

## Arbitrage

A trading strategy that profits from price differences between markets.

Arbitrageurs help align prices across different exchanges.

---

# B

## Batch Auctions

A trading mechanism where multiple orders are grouped together and executed at a single clearing price.

Used to reduce front-running and MEV.

---

## Block Builder

An actor in the MEV supply chain that constructs optimized blocks containing profitable transaction ordering.

---

# C

## Collateral

Assets deposited by a borrower to secure a loan in lending protocols.

If collateral value falls below a threshold, liquidation may occur.

---

## Concentrated Liquidity

A liquidity model where LPs provide liquidity within specific price ranges instead of across the entire curve.

Introduced by Uniswap v3.

---

# D

## Decentralized Exchange (DEX)

A trading platform that allows peer-to-peer token trading without intermediaries.

Examples include AMM-based exchanges.

---

# F

## Flash Loan

A loan that is borrowed and repaid within the same blockchain transaction.

If the loan is not repaid within the transaction, the entire transaction reverts.

---

## Front-Running

An attack where a trader submits a transaction before another transaction to profit from expected price movements.

---

# H

## Health Factor

A metric used in lending protocols that determines the safety of a borrower's position.

If the health factor drops below a threshold, liquidation can occur.

---

# I

## Impermanent Loss

A temporary loss experienced by liquidity providers when the relative price of pooled assets changes.

This occurs due to rebalancing of AMM liquidity pools.

---

# L

## Liquidity Pool

A smart contract that holds tokens used for trading in AMM systems.

Liquidity providers deposit assets into the pool and earn fees.

---

## Liquidation

The process of closing a borrower's position when collateral value falls below required thresholds.

Liquidators repay the debt and receive discounted collateral.

---

# M

## MEV (Maximal Extractable Value)

The profit that block producers or searchers can extract by reordering, including, or excluding transactions.

Common MEV strategies include:

- arbitrage
- sandwich attacks
- liquidations

---

## MEV Bundles

Groups of transactions submitted by searchers to builders to capture MEV opportunities.

---

# O

## Oracle

A system that provides external data (such as prices) to blockchain smart contracts.

Price oracles are critical for lending protocols.

---

# P

## Proposer-Builder Separation (PBS)

A blockchain design where block proposers and block builders are separated to improve fairness and reduce centralization.

---

# S

## Sandwich Attack

A form of MEV where an attacker places transactions before and after a victim trade to profit from price slippage.

---

## Slippage

The difference between the expected price of a trade and the actual execution price.

Occurs when liquidity is limited.

---

# T

## Tokenomics

The economic design of a cryptocurrency or protocol token.

Includes:

- token supply
- distribution
- incentives
- governance

---

# V

## veToken (Vote-Escrow Token)

A token model where users lock tokens to gain governance power and increased rewards.

Voting power usually depends on lock duration.

---

# Y

## Yield Farming

A strategy where users move funds across DeFi protocols to maximize returns from incentives or rewards.

---

# Conclusion

Understanding these terms is essential for studying DeFi protocol design, risk analysis, and market structure.
