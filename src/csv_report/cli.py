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


def reg_main(file: str = "~/download/main.csv", account: str = "資産:現金:家計財布") -> None:
    df = pd.read_csv(file)
    df = df[df["account"] == account]
    df["amount"] = df["amount"].astype(int)
    df = df.sort_values("date amount".split(), ascending=[True, False])
    df["sum"] = df["amount"].cumsum()
    df = df["date payee account amount sum".split()]
    df = df.loc[::-1]

    print(tabulate(df, df.columns, tablefmt="psql"))


def reg_fire():
    Fire(reg_main)
