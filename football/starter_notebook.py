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
        # Football starter: build NFL power ratings from final scores

        **Data:** [nflverse](https://github.com/nflverse/nflverse-data) - free NFL data maintained by the community. Credit nflverse when you use it.

        **Elo** is the classic rating system from chess: every team has a number, winners take points from losers, and bigger upsets move more points. From just final scores we can rank all 32 teams.
        """
    )
    return


@app.cell
def _(pd):
    games = pd.read_csv(
        "https://github.com/nflverse/nflverse-data/releases/download/schedules/games.csv"
    )
    reg = games[
        (games["game_type"] == "REG")
        & games["away_score"].notna()
        & (games["season"] >= 2015)
    ].copy()
    print(f"{len(reg):,} regular-season games since 2015")
    return (reg,)


@app.cell
def _(reg):
    K, HOME_EDGE, START = 20.0, 48.0, 1500.0
    elo = {}
    for g in reg.itertuples():
        away, home = g.away_team, g.home_team
        ra, rh = elo.get(away, START), elo.get(home, START)
        expected_home = 1.0 / (1.0 + 10 ** (-((rh + HOME_EDGE) - ra) / 400))
        home_result = 1.0 if g.home_score > g.away_score else (0.5 if g.home_score == g.away_score else 0.0)
        change = K * (home_result - expected_home)
        elo[home], elo[away] = rh + change, ra - change
    ratings = pd.Series(elo).sort_values(ascending=False).rename("elo")
    return (ratings,)


@app.cell
def _(plt, ratings):
    ax = ratings.head(12).plot(
        kind="bar", figsize=(9, 4), ylabel="Elo",
        title="NFL Elo ratings - after the most recent regular-season game",
    )
    ax
    return


@app.cell
def _(mo, ratings):
    mo.md(
        f"""
        Right now the top-rated team is **{ratings.index[0]}** ({ratings.iloc[0]:.0f}) and the lowest is **{ratings.index[-1]}** ({ratings.iloc[-1]:.0f}).

        ## Your turn

        - Turn it into a **predictor**: who wins each game this week, and how often is Elo right over a season?
        - Make blowouts count more: scale `K` by the margin of victory.
        - Estimate the true **home-field edge**: which `HOME_EDGE` makes Elo predict best?
        """
    )
    return


if __name__ == "__main__":
    app.run()
