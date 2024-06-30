from pathlib import Path

import dash_ag_grid as dag
import pandas as pd
from dash import html  # , callback # If you need callbacks, import it here.
from dash import dcc, register_page

register_page(__name__, name="Model", top_nav=True, path_template="/model/<model_id>")

THIS_FOLDER = Path(__file__).parent.parent.resolve()
results_file = THIS_FOLDER / "data/results.csv"
df = pd.read_csv(results_file).sort_values(by="Dataset", ascending=True)
columnDefs = [
    {
        "field": "Dataset",
        "sortable": True,
        "cellRenderer": "DatasetLink",
    },
    {"field": "position"},
    {"field": "points"},
    {"field": "mase"},
]


def layout(model_id):
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
                rowData=df.loc[df["model"] == model_id].to_dict("records"),
                defaultColDef={"filter": True},
                columnDefs=columnDefs,
                columnSize="sizeToFit",
                dashGridOptions={"animateRows": True},
                style={"height": "700px"},
            ),
        ],
    )

    return layout
