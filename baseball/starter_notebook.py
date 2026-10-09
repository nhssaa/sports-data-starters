import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md(
        """
        # Baseball starter: Pythagorean expectation

        **Data:** the [Lahman Baseball Database](https://www.seanlahman.com/baseball-archive/statistics/) (Sean Lahman), mirrored as CSV by [Rdatasets](https://github.com/vincentarelbundock/Rdatasets). Credit both when you use them.

        Bill James's famous idea: a team's **wins** are predicted almost scarily well by just two numbers - runs scored and runs allowed. Let's check on 20+ years of MLB seasons.

        **Where you have seen this:** this is the *Moneyball* idea - the 2002 Oakland A's, the Michael Lewis book, the Brad Pitt film. A low-budget team winning by trusting numbers over gut feel.
        """
    )
    return


@app.cell
def _(pd):
    teams = pd.read_csv(
        "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/Lahman/Teams.csv"
    )
    modern = teams[teams["yearID"] >= 2000].copy()
    modern["win_pct"] = modern["W"] / modern["G"]
    modern["pyth_pct"] = modern["R"] ** 2 / (modern["R"] ** 2 + modern["RA"] ** 2)
    print(f"{len(modern):,} team-seasons since 2000")
    return (modern,)


@app.cell
def _(modern, plt):
    ax = modern.plot(
        kind="scatter", x="pyth_pct", y="win_pct", alpha=0.3, figsize=(6, 6),
        xlabel="Pythagorean win % (from runs)", ylabel="Actual win %",
        title="Runs scored and allowed predict wins",
    )
    ax.plot([0.3, 0.7], [0.3, 0.7], color="red", linestyle="--", label="perfect prediction")
    ax.legend()
    ax
    return


@app.cell
def _(modern, mo):
    err_in_wins = (modern["win_pct"] - modern["pyth_pct"]).abs() * modern["G"]
    mo.md(
        f"""
        On average a team's Pythagorean record is off by only **{err_in_wins.mean():.1f} wins** over a season.

        ## Your turn

        - Find the biggest **overachievers** (won way more than their runs suggest). What did they do? (Look at one-run games.)
        - The exponent doesn't have to be 2: which exponent minimizes the error?
        - Same idea, other sports: does it work on the NFL or NHL starters in this repo?

        **What good looks like:** you can explain your chart in one plain sentence, and name one thing it does *not* tell you.
        """
    )
    return


if __name__ == "__main__":
    app.run()
