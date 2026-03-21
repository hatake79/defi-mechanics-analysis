import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/dex_volume.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Plot total volume
plt.figure()
plt.plot(df["date"], df["volume_usd"])
plt.title("DEX Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume (USD)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("../charts/dex_volume_trend.png")

# Plot whale vs total
plt.figure()
plt.plot(df["date"], df["volume_usd"])
plt.plot(df["date"], df["whale_volume_usd"])
plt.title("Whale Volume vs Total Volume")
plt.xlabel("Date")
plt.ylabel("Volume (USD)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("../charts/whale_vs_total.png")

print("Charts generated successfully.")
