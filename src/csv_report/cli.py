import subprocess
from pathlib import Path

import pandas as pd
from fire import Fire
from tabulate import tabulate


def exec_main():
    filename = Path("test.csv")
    cmd = "ls -l | sort"
    with filename.open("w") as fp:
        ret = subprocess.run(cmd, shell=True, stdout=fp)


def exec_fire():
    Fire(exec_main)


def kakei_main(
    file: str = "~/wks/data/csv/main_kakei.csv", account: str = "資産:現金:家計財布"
) -> None:
    df = pd.read_csv(file)
    df = df[df["account"] == account]
    df["amount"] = df["amount"].astype(int)
    df = df.sort_values("date amount".split(), ascending=[True, False])
    df["sum"] = df["amount"].cumsum()
    df = df["date payee account amount sum".split()]
    df = df.loc[::-1]

    print(tabulate(df, df.columns, tablefmt="psql"))


def kakei_fire():
    Fire(kakei_main)


def tadatoshi_main(
    file: str = "~/wks/data/csv/main_tadatoshi.csv", account: str = "資産:現金:財布"
) -> None:
    df = pd.read_csv(file)
    df = df[df["account"] == account]
    df["amount"] = df["amount"].astype(int)
    df = df.sort_values("date amount".split(), ascending=[True, False])
    df["sum"] = df["amount"].cumsum()
    df = df["date payee account amount sum".split()]
    df = df.loc[::-1]

    print(tabulate(df, df.columns, tablefmt="psql"))


def tadatoshi_fire():
    Fire(tadatoshi_main)
