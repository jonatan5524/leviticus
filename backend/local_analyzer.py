import polars as pl
import random

TRAFFICS_AMOUNT = 99

df = pl.DataFrame(
    {
        "SourceIp": ["10.0.1.1"] * TRAFFICS_AMOUNT
        + ["10.0.1.2"] * TRAFFICS_AMOUNT
        + ["10.0.1.3"] * TRAFFICS_AMOUNT
        + ["10.0.1.4"] * TRAFFICS_AMOUNT
        + ["10.0.1.5"] * TRAFFICS_AMOUNT
        + ["10.0.1.6"] * TRAFFICS_AMOUNT
        + ["10.0.1.7"] * TRAFFICS_AMOUNT
        + ["10.0.1.8"] * TRAFFICS_AMOUNT,
        "SourcePort": [random.randint(10**4, 65535)] * TRAFFICS_AMOUNT * 8,
        "DestIp":
        # 1
        ["10.0.2.1"] * 33 + ["10.0.2.2"] * 33 + ["10.0.2.3"] * 33 +
        # 2
        ["10.0.2.1"] * 33 + ["10.0.2.2"] * 33 + ["10.0.2.3"] * 33 +
        # 3
        ["10.0.2.1"] * 32 + ["10.0.2.2"] * 32 + ["10.0.2.3"] * 32 + ["10.0.2.4"] * 3 +
        # 4
        ["10.0.2.1"] * 33 + ["10.0.2.2"] * 33 + ["10.0.2.3"] * 33 +
        # 5
        ["10.0.2.1"] * 33 + ["10.0.2.2"] * 33 + ["10.0.2.3"] * 33 +
        # 6
        ["10.0.2.1"] * 32
        + ["10.0.2.2"] * 32
        + ["10.0.2.3"] * 32
        + ["10.0.2.4"] * 2
        + ["10.0.2.5"] * 1
        +
        # 7
        ["10.0.2.1"] * 33 + ["10.0.2.2"] * 33 + ["10.0.2.3"] * 33 +
        # 8
        ["10.0.2.1"] * 33 + ["10.0.2.2"] * 33 + ["10.0.2.3"] * 33,
        "DestPort": [443] * TRAFFICS_AMOUNT * 8,
    }
)

print(df.row(200))

df.write_parquet("connections.parquet")
