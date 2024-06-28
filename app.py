# app.py

from pathlib import Path

import dash_ag_grid as dag
import pandas as pd
from dash import Dash, dcc, html

THIS_FOLDER = Path(__file__).parent.resolve()
points_file = THIS_FOLDER / "points.csv"


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?" "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "The F1 Score Championship"

df = pd.read_csv(points_file).sort_values(by="Points", ascending=False)


columnDefs = [
    {"field": "Model", "sortable": True},
    {"field": "Engine"},
    {"field": "Points"},
]


app.layout = html.Div(
    children=[
        html.H1(children="F1 Score Championship Points", className="header-title"),
        html.P(children=("Monash MASE"), className="header-description"),
        html.P(
            children=(
                "Analyze the performance of time series models"
                " based on F1 Championship Points."
            ),
            className="header-description",
        ),
        dag.AgGrid(
            id="column-definitions-basic",
            rowData=df.to_dict("records"),
            defaultColDef={"filter": True},
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": True},
            style={"height": "700px"},
        ),
    ],
    className="header",
    style={"height": "768px"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
