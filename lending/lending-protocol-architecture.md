# Lending Protocol Architecture

Decentralized lending protocols are one of the most important primitives in decentralized finance (DeFi). They allow users to supply assets to earn interest or borrow assets by depositing collateral.

Unlike traditional financial institutions, DeFi lending markets operate entirely through smart contracts and are accessible without intermediaries.

This document explores the architecture and core components of modern DeFi lending protocols.

---

# Core Components of Lending Protocols

Most lending protocols share a similar architecture composed of several key modules.

## 1. Liquidity Pools

Liquidity pools store user deposits and provide the capital that borrowers can access.

Users deposit assets such as ETH, USDC, or DAI into the pool and receive interest in return.

Key characteristics:

- pooled liquidity model
- interest-bearing deposits
- dynamic interest rates

Examples of lending pools exist in protocols such as Aave and Compound.

---

## 2. Collateral Vaults

Borrowers must deposit collateral before borrowing assets.

Collateral ensures that the protocol remains solvent even if the borrower fails to repay the loan.

Typical properties:

- overcollateralization
- collateral ratio requirements
- liquidation thresholds

Example:

A user deposits $10,000 worth of ETH and may borrow up to $7,000 depending on the protocol's loan-to-value ratio.

---

## 3. Interest Rate Model

Interest rates in DeFi lending markets are typically determined by supply and demand.

Most protocols use a **utilization-based interest rate model**.

Utilization rate:

