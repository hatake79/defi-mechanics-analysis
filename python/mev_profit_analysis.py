"""
MEV Profit Analysis

This script analyzes profit distribution from MEV strategies.

Dataset example:

date, strategy, profit_usd
"""

import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def profit_by_strategy(df):
    return df.groupby("strategy")["profit_usd"].sum().sort_values(ascending=False)


def daily_mev_profit(df):
    return df.groupby("date")["profit_usd"].sum()


def strategy_share(df):
    total = df["profit_usd"].sum()
    share = df.groupby("strategy")["profit_usd"].sum() / total
    return share.sort_values(ascending=False)


if __name__ == "__main__":
    data = load_data("data/mev_profit.csv")

    print("\nMEV Profit by Strategy:")
    print(profit_by_strategy(data))

    print("\nDaily MEV Profit:")
    print(daily_mev_profit(data).tail())

    print("\nStrategy Market Share:")
    print(strategy_share(data))
