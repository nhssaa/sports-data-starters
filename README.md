# NHSSAA Data Starters

**Clone-and-go datasets and starter models for high-school sports analytics - and the training ground for the NHSSAA hackathon at the February conference.**

The hackathon format: students run phone-based agents against common datasets and get creative with analysis and technique. This repo holds those common datasets (as live, credited, public sources) plus a tiny working model for each sport, so a student can clone, run one notebook, understand the data, and then ask their own question.

No installs required: every starter notebook runs in the browser with one click (marimo + molab, no sign-in).

| Sport | Folder | Dataset (free, credited) | First model |
|---|---|---|---|
| Soccer | [`soccer/`](soccer/) | [StatsBomb Open Data](https://github.com/statsbomb/open-data) | Shots & goals from real event data |
| Football (NFL) | [`football/`](football/) | [nflverse data](https://github.com/nflverse/nflverse-data) | Elo power ratings from final scores |
| Baseball (MLB) | [`baseball/`](baseball/) | [Lahman Baseball Database](https://www.seanlahman.com/baseball-archive/statistics/) (via [Rdatasets](https://github.com/vincentarelbundock/Rdatasets)) | Pythagorean expectation |
| Hockey (NHL) | [`hockey/`](hockey/) | [NHL public API](https://api-web.nhle.com/v1/standings/now) | Do goals predict points? |
| Cricket | [`cricket/`](cricket/) | [Cricsheet](https://cricsheet.org/) | Bat first or chase? |

## Run any starter in one click

Open the preview, then press **Run** (for full interactivity without sign-in, add `/wasm` at the end of the URL):

- Soccer: https://molab.marimo.io/github/nhssaa/sports-data-starters/blob/main/soccer/starter_notebook.py
- Football: https://molab.marimo.io/github/nhssaa/sports-data-starters/blob/main/football/starter_notebook.py
- Baseball: https://molab.marimo.io/github/nhssaa/sports-data-starters/blob/main/baseball/starter_notebook.py
- Hockey: https://molab.marimo.io/github/nhssaa/sports-data-starters/blob/main/hockey/starter_notebook.py
- Cricket: https://molab.marimo.io/github/nhssaa/sports-data-starters/blob/main/cricket/starter_notebook.py

If the browser preview offers to install packages, click **Install** once, then Run.

To work locally instead: `pip install -r requirements.txt`, then `marimo edit soccer/starter_notebook.py`.

## Start here

New to all of this? Our flagship lesson is **[xg-for-beginners](https://github.com/nhssaa/xg-for-beginners)** - build your first expected-goals model from 8,000+ real Bundesliga shots, one clue at a time, in the browser.

## For NHSSAA chapters and students

- Students work in **their own GitHub accounts**. This org hosts only copies of finished, public-ready work (with credit) - never student personal data.
- No API keys, ever. Every dataset here is free and public, loaded from its source at run time. Nothing is copied into this repo, so the data owners' terms stay with the data.
- **Credit every source** in your own projects. It gets the field's name out there and it is how open data keeps existing.
- Finished a project from one of these starters? Talk to your chapter ambassador about featuring it.

## Credits

Data: StatsBomb Open Data (soccer) - nflverse (football) - the Lahman Baseball Database by Sean Lahman, mirrored by Rdatasets (baseball) - the NHL's public web API (hockey) - Cricsheet (cricket) - Impect Open Data (soccer, in the xG lesson). Teaching approach inspired by Chris Dove's NHSSAA Summer Symposium webinar (June 2026).

## License

Code: MIT (see [LICENSE](LICENSE)). Data: each dataset keeps its own license/terms - follow the links above and respect them.
