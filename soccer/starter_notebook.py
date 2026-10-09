import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(mo):
    mo.md(
        """
        # Soccer starter: shots and goals from real event data

        **Data:** [StatsBomb Open Data](https://github.com/statsbomb/open-data) - free event data for learning and teaching. Credit StatsBomb when you use it.

        Event data records *every action in a match* - who did what, where, and what happened next. Here we load the **2018 FIFA World Cup final** and count shots and goals by player.

        Want the full guided soccer lesson? Start with our flagship: [xg-for-beginners](https://github.com/nhssaa/xg-for-beginners).
        """
    )
    return


@app.cell
def _(pd):
    comps = pd.read_json(
        "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json"
    )
    comps[["competition_id", "season_id", "competition_name", "season_name"]].head(10)
    return (comps,)


@app.cell
def _(comps, mo):
    mo.md(
        f"StatsBomb currently lists **{len(comps)} free competition-seasons**. "
        "Below we load the last match of the 2018 World Cup - the final - straight from the files above."
    )
    return


@app.cell
def _(pd):
    matches = pd.read_json(
        "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/43/3.json"
    )
    the_final = matches.sort_values("match_date").iloc[-1]
    match_id = int(the_final["match_id"])
    events = pd.read_json(
        f"https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{match_id}.json"
    )
    print(f"{the_final['home_team']['home_team_name']} vs {the_final['away_team']['away_team_name']}: {len(events)} events")
    return (events,)


@app.cell
def _(events):
    shots = events[events["type"].apply(lambda t: t["name"] == "Shot")].copy()
    shots["player"] = shots["player"].apply(lambda p: p["name"])
    shots["is_goal"] = shots["shot"].apply(lambda s: s["outcome"]["name"] == "Goal")
    by_player = (
        shots.groupby("player")
        .agg(shots=("is_goal", "size"), goals=("is_goal", "sum"))
        .sort_values(["goals", "shots"], ascending=False)
    )
    by_player
    return (by_player,)


@app.cell
def _(mo):
    mo.md(
        """
        ## Your turn

        - Who had the best **conversion rate** (goals / shots)? Add a column and sort by it.
        - Loop over *every* match in the competition and build a golden-boot table for the whole World Cup.
        - Each shot has a `location` - draw a shot map. The [xg-for-beginners](https://github.com/nhssaa/xg-for-beginners) lesson shows how, then teaches you to turn shots into expected goals.
        """
    )
    return


if __name__ == "__main__":
    app.run()
