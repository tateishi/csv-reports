import subprocess
from pathlib import Path

import pandas as pd
from fire import Fire
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter, WordCompleter
from tabulate import tabulate

ACCOUNT_FILE = "~/wks/ledger/accounts/accounts.txt"

DEFAULT_FILE = "~/wks/data/csv/main_kakei.csv"
DEFAULT_ACCOUNT = "資産:現金:家計財布"


def read_accounts(file: str = ACCOUNT_FILE) -> list:
    return Path(file).expanduser().read_text().split("\n")


def read_dataframe(file: str) -> pd.DataFrame:
    return pd.read_csv(file)


def register_account(
    df: pd.DataFrame, account: str, reverse: bool = False
) -> pd.DataFrame:
    df = df[df["account"] == account]
    df["amount"] = df["amount"].astype(int)
    df = df.sort_values("date amount".split(), ascending=[True, False])
    df["sum"] = df["amount"].cumsum()
    df = df["date payee account amount sum".split()]
    if reverse:
        df = df.loc[::-1]

    return df


def print_table(df: pd.DataFrame) -> None:
    print(tabulate(df, df.columns, tablefmt="psql"))


def input_filename(message: str = "FILENAME: ", default: str = DEFAULT_FILE) -> str:
    file_completer = PathCompleter(expanduser=True)
    filename = prompt(message=message, default=default, completer=file_completer)

    return filename


def input_account(message: str = "ACCOUNT: ", default: str = DEFAULT_ACCOUNT) -> str:
    account_completer = WordCompleter(read_accounts(), match_middle=True)
    account = prompt(message=message, default=default, completer=account_completer)

    return account


def main(filename: str = DEFAULT_FILE, account: str = DEFAULT_ACCOUNT) -> None:
    df = read_dataframe(filename)
    df = register_account(df, account)

    print_table(df)


def test() -> None:
    filename = input_filename()
    account = input_account()

    df = read_dataframe(filename)
    df = register_account(df, account)

    print_table(df)


def entry():
    #    Fire(main)
    Fire(test)
