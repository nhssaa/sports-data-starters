import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import requests
    return mo, pd, requests


@app.cell
def _(mo):
    mo.md(
        """
        # Cricket starter: bat first or chase?

        **Data:** [Cricsheet](https://cricsheet.org/) - free ball-by-ball data for T20, ODI, and Test matches. Credit Cricsheet when you use it.

        The coin toss decides who bats first - but should you *want* to? Let's answer it with every Women's Premier League T20 ever played (about 370 KB of data; the men's IPL is one folder up on Cricsheet).

        **Where you have seen this:** every rain-hit international uses the Duckworth-Lewis-Stern formula to reset the target, and pro T20 teams employ analysts to answer 'bat first or chase?' for each venue.
        """
    )
    return


@app.cell
def _(requests):
    import io
    import json
    import zipfile

    blob = requests.get("https://cricsheet.org/downloads/wpl_female_json.zip").content
    archive = zipfile.ZipFile(io.BytesIO(blob))
    matches = [
        json.loads(archive.read(name))
        for name in archive.namelist()
        if name.endswith(".json")
    ]
    print(f"{len(matches)} matches")
    return (matches,)


@app.cell
def _(matches, pd):
    rows = []
    for m in matches:
        outcome = m["info"].get("outcome", {})
        if "winner" not in outcome:
            continue
        by = outcome.get("by", {})
        rows.append(
            {
                "winner": outcome["winner"],
                "won_by": "chasing" if "wickets" in by else "batting first",
            }
        )
    results = pd.DataFrame(rows)
    results["won_by"].value_counts(normalize=True).round(3)
    return (results,)


@app.cell
def _(mo, results):
    chase_pct = 100 * (results["won_by"] == "chasing").mean()
    mo.md(
        f"""
        Teams **chasing won {chase_pct:.0f}%** of these matches. So: win the toss, bowl first?

        ## Your turn

        - Is the chase advantage bigger in some **venues**? `info["venue"]` is in every match.
        - Ball by ball: every delivery is in `innings` - who are the top run-scorers and wicket-takers?
        - The real question is *par score*: given the first-innings total, how often does the chase succeed? (That's the road to Duckworth-Lewis.)

        **What good looks like:** you can explain your chart in one plain sentence, and name one thing it does *not* tell you.
        """
    )
    return


if __name__ == "__main__":
    app.run()
