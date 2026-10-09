import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import requests
    import matplotlib.pyplot as plt
    return mo, pd, requests, plt


@app.cell
def _(mo):
    mo.md(
        """
        # Hockey starter: do goals predict points?

        **Data:** the NHL's public web API (`api-web.nhle.com`) - live standings, no key needed. Credit the NHL when you use it.

        Standings give every team's points and goal differential. A first modeling question: **how much of winning is just out-scoring opponents?**

        **Where you have seen this:** sites like MoneyPuck publish live win probability for every NHL game, built from exactly this kind of data.
        """
    )
    return


@app.cell
def _(pd, requests):
    data = requests.get("https://api-web.nhle.com/v1/standings/now").json()
    rows = [
        (
            r["teamAbbrev"]["default"], r["gamesPlayed"], r["points"],
            r["goalFor"], r["goalAgainst"],
        )
        for r in data["standings"]
    ]
    nhl = pd.DataFrame(rows, columns=["team", "games", "points", "goals_for", "goals_against"])
    nhl["points_pct"] = nhl["points"] / (2 * nhl["games"])
    nhl["goal_diff_per_game"] = (nhl["goals_for"] - nhl["goals_against"]) / nhl["games"]
    print(f"As of {data.get('standingsDateTimeUtc', 'now')[:10]}: {len(nhl)} teams")
    return (nhl,)


@app.cell
def _(nhl, plt):
    import numpy as np
    slope, intercept = np.polyfit(nhl["goal_diff_per_game"], nhl["points_pct"], 1)
    ax = nhl.plot(
        kind="scatter", x="goal_diff_per_game", y="points_pct", figsize=(7, 5),
        xlabel="Goal differential per game", ylabel="Points %",
        title=f"NHL standings: +1 goal/game is worth about {slope * 82 * 2:.0f} standings points a season",
    )
    xs = np.linspace(nhl["goal_diff_per_game"].min(), nhl["goal_diff_per_game"].max(), 50)
    ax.plot(xs, slope * xs + intercept, color="red", linestyle="--")
    ax
    return


@app.cell
def _(mo, nhl):
    best = nhl.sort_values("points_pct", ascending=False).iloc[0]
    mo.md(
        f"""
        Top of the league right now: **{best['team']}** ({best['points']} pts in {best['games']} games).

        ## Your turn

        - Who are this season's **overachievers** - points well above what their goals predict? Do they win tight games or lose blowouts?
        - Go deeper with [MoneyPuck's free team data](http://moneypuck.com/data.htm): shots, expected goals, and more.
        - Is home-ice advantage real? The API also serves every game's score.

        **What good looks like:** you can explain your chart in one plain sentence, and name one thing it does *not* tell you.
        """
    )
    return


if __name__ == "__main__":
    app.run()
