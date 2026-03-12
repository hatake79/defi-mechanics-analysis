# Order Flow Auctions

Order flow auctions are a mechanism designed to capture and redistribute value created by transaction ordering.

In traditional financial markets, brokers often sell order flow to market makers.

A similar concept is emerging in decentralized trading systems.

---

# What Is Order Flow

Order flow refers to the stream of buy and sell transactions submitted by users.

This flow contains valuable information because it reveals trading intentions before execution.

Market participants may profit from predicting how these trades affect prices.

---

# Auction Mechanism

In an order flow auction system:

1. A user's trade request is broadcast to solvers or market makers.
2. Participants compete to execute the trade.
3. The participant offering the best price wins the auction.

The winning solver executes the trade and captures part of the value.

---

# Benefits

Order flow auctions can improve trading outcomes by:

- reducing slippage
- improving price execution
- redistributing MEV to users

Instead of MEV being captured solely by searchers, some value can be returned to traders.

---

# Tradeoffs

However, order flow auctions may introduce new challenges.

These include:

- potential centralization of solvers
- complexity in execution systems
- trust assumptions in off-chain infrastructure

---

# Conclusion

Order flow auctions represent an emerging approach to redesigning how value from transaction ordering is distributed in decentralized markets.
