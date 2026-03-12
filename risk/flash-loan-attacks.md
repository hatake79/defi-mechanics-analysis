# Flash Loan Attacks in DeFi

Flash loans are a unique financial primitive in decentralized finance.  
They allow users to borrow large amounts of capital without collateral, provided the loan is repaid within the same transaction.

While flash loans are useful for arbitrage and liquidity management, they have also enabled a new class of DeFi exploits.

---

# What Is a Flash Loan

A flash loan allows a user to borrow funds instantly from a liquidity pool.

The only requirement is that the borrowed funds must be returned before the transaction ends.

If repayment fails, the entire transaction is reverted.

This mechanism makes flash loans risk-free for lenders.

---

# Why Flash Loans Enable Attacks

Flash loans allow attackers to temporarily access extremely large amounts of liquidity.

This capital can be used to manipulate market conditions in a single transaction.

Because blockchain transactions are atomic, attackers can execute complex exploit strategies without long-term capital risk.

---

# Common Flash Loan Attack Strategies

## Price Manipulation

Attackers manipulate the price of an asset in a low-liquidity market.

Protocols that rely on these prices may miscalculate collateral values or swap rates.

---

## Oracle Exploits

If a protocol relies on an on-chain price feed, attackers can distort the price used by the oracle.

This allows them to borrow more assets than their collateral should allow.

---

## Governance Attacks

Flash loans can temporarily accumulate large token balances, potentially enabling attackers to influence governance voting.

---

# Typical Attack Sequence

1. Borrow large capital via flash loan  
2. Manipulate a DeFi protocol condition (price, collateral, liquidity)  
3. Exploit the protocol logic  
4. Repay the flash loan  
5. Keep the remaining profit

All steps occur in a single blockchain transaction.

---

# Historical Impact

Flash loan attacks have caused significant financial losses in DeFi.

Many early DeFi protocols underestimated how quickly large capital could be mobilized through flash loans.

---

# Mitigation Techniques

Protocols can reduce flash loan risk through several methods:

- robust oracle systems
- liquidity-weighted price feeds
- rate limits on sensitive operations
- multi-block price verification

---

# Conclusion

Flash loans are a powerful financial innovation, but they also increase the attack surface of DeFi protocols.

Designing secure systems requires anticipating how attackers might use temporary liquidity to manipulate protocol logic.
