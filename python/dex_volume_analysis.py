"""
DEX Volume Analysis

This script analyzes decentralized exchange trading volume data.
The dataset is expected to contain:

date, protocol, volume_usd
"""

import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df


def total_volume_by_protocol(df):
    return df.groupby("protocol")["volume_usd"].sum().sort_values(ascending=False)


def daily_volume(df):
    return df.groupby("date")["volume_usd"].sum()


def protocol_market_share(df):
    total_volume = df["volume_usd"].sum()
    share = df.groupby("protocol")["volume_usd"].sum() / total_volume
    return share.sort_values(ascending=False)


if __name__ == "__main__":
    data = load_data("data/dex_volume.csv")

    print("\nTotal Volume by Protocol:")
    print(total_volume_by_protocol(data))

    print("\nDaily Volume:")
    print(daily_volume(data).tail())

    print("\nProtocol Market Share:")
    print(protocol_market_share(data))
