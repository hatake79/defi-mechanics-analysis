"""
DeFi Liquidation Tracker

This script analyzes liquidation data from lending protocols.

Dataset example:

date, protocol, asset, liquidation_usd
"""

import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def total_liquidations(df):
    return df["liquidation_usd"].sum()


def liquidations_by_protocol(df):
    return df.groupby("protocol")["liquidation_usd"].sum().sort_values(ascending=False)


def largest_liquidation_days(df):
    return df.groupby("date")["liquidation_usd"].sum().sort_values(ascending=False).head(10)


if __name__ == "__main__":
    data = load_data("data/liquidations.csv")

    print("\nTotal Liquidations:")
    print(total_liquidations(data))

    print("\nLiquidations by Protocol:")
    print(liquidations_by_protocol(data))

    print("\nLargest Liquidation Days:")
    print(largest_liquidation_days(data))
