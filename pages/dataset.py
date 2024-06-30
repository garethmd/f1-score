from pathlib import Path

import dash_ag_grid as dag
import pandas as pd
from dash import html  # , callback # If you need callbacks, import it here.
from dash import dcc, register_page

register_page(
    __name__, name="Dataset", top_nav=True, path_template="/dataset/<dataset_id>"
)

THIS_FOLDER = Path(__file__).parent.parent.resolve()
results_file = THIS_FOLDER / "data/results.csv"
df = pd.read_csv(results_file).sort_values(by="position", ascending=True)
columnDefs = [
    {
        "field": "model",
        "sortable": True,
        "cellRenderer": "ModelLink",
    },
    {"field": "position"},
    {"field": "points"},
    {"field": "mase"},
]


def layout(dataset_id: str):
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
                rowData=df.loc[df["Dataset"] == dataset_id.replace("%20", " ")].to_dict(
                    "records"
                ),
                defaultColDef={"filter": True},
                columnDefs=columnDefs,
                columnSize="sizeToFit",
                dashGridOptions={"animateRows": True},
                style={"height": "700px"},
            ),
        ],
    )

    return layout
