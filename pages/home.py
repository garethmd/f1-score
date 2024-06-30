from pathlib import Path

import dash_ag_grid as dag
import pandas as pd
from dash import html  # , callback # If you need callbacks, import it here.
from dash import dcc, register_page

# Data
THIS_FOLDER = Path(__file__).parent.parent.resolve()
points_file = THIS_FOLDER / "data/points.csv"
df = pd.read_csv(points_file).sort_values(by="Points", ascending=False)
columnDefs = [
    {"field": "Position"},
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
            dcc.Markdown(
                """
                ### Standings
                The following table contains the Formula Monash Datasets.
                """
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
    )

    return layout
