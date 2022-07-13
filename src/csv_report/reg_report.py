import subprocess
from pathlib import Path

import pandas as pd
from fire import Fire
from tabulate import tabulate

DEFAULT_FILE = "~/wks/data/csv/main_kakei.csv"
DEFAULT_ACCOUNT = "資産:現金:家計財布"


def read_dataframe(file: str) -> pd.DataFrame:
    return pd.read_csv(file)


def register_account(df: pd.DataFrame, account: str) -> pd.DataFrame:
    df = df[df["account"] == account]
    df["amount"] = df["amount"].astype(int)
    df = df.sort_values("date amount".split(), ascending=[True, False])
    df["sum"] = df["amount"].cumsum()
    df = df["date payee account amount sum".split()]
    df = df.loc[::-1]

    return df


def print_table(df: pd.DataFrame) -> None:
    print(tabulate(df, df.columns, tablefmt="psql"))


def main(file: str = DEFAULT_FILE, account: str = DEFAULT_ACCOUNT) -> None:
    df = read_dataframe(file)
    df = register_account(df, account)

    print_table(df)


def entry():
    Fire(main)
