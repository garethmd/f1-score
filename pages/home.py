from pathlib import Path

import dash_ag_grid as dag
import pandas as pd
from dash import html  # , callback # If you need callbacks, import it here.
from dash import register_page

# Data
THIS_FOLDER = Path(__file__).parent.parent.resolve()
points_file = THIS_FOLDER / "data/points.csv"
df = pd.read_csv(points_file).sort_values(by="Points", ascending=False)
columnDefs = [
    {
        "field": "Model",
        "sortable": True,
        "cellRenderer": "ModelLink",
    },
    {"field": "Engine"},
    {"field": "Points"},
]


register_page(__name__, name="Standings", top_nav=True, path="/")


def layout():
    layout = html.Div(
        children=[
            html.P(
                children=("Formula Monash Standings"), className="header-description"
            ),
            html.P(
                children=(
                    "Analyze the MASE performance of time series models"
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

    return layout
