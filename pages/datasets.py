from pathlib import Path

import dash_ag_grid as dag
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html, register_page

# Data
THIS_FOLDER = Path(__file__).parent.parent.resolve()
datasets_file = THIS_FOLDER / "data/datasets.csv"
df = pd.read_csv(datasets_file).sort_values(by="Dataset", ascending=True)
columnDefs = [
    {
        "field": "Dataset",
        "sortable": True,
        "cellRenderer": "DatasetLink",
    },
    {"field": "Frequency"},
    {"field": "Forecast Horizon"},
    {"field": "MASE"},
    {"field": "Leader"},
]

register_page(__name__, name="Datasets", top_nav=True, path="/datasets")


fig = px.scatter(
    df,
    x="Frequency",
    y="MASE",
    color="Leader_Type",
    hover_data=["Dataset", "Leader", "Frequency", "Forecast Horizon"],
)
fig.update_xaxes(
    categoryarray=[
        "Yearly",
        "Quarterly",
        "Monthly",
        "Weekly",
        "Daily",
        "Hourly",
        "Half Hourly",
        "10 Mins",
        "Other",
    ],
    categoryorder="array",
)


def layout():
    layout = html.Div(
        children=[
            dcc.Markdown(
                """
                        ### Datasets
                        The following table contains the Formula Monash Datasets.
                        """
            ),
            dcc.Tabs(
                [
                    dcc.Tab(
                        label="Scatter Plot",
                        children=[
                            dcc.Graph(figure=fig),
                        ],
                    ),
                    dcc.Tab(
                        label="Table",
                        children=[
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
                    ),
                ]
            ),
        ],
    )

    return layout
