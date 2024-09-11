from pathlib import Path

import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from dash import dcc, html, register_page

# Data
THIS_FOLDER = Path(__file__).parent.parent.resolve()
datasets_file = THIS_FOLDER / "data/datasets_leader.csv"
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
    color="Type",
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
                        The following is a scatter plot of the leading model performance 
                        for each dataset in the series, plotted as a function of the time 
                        series frequency.
                        """
            ),
            dcc.Tabs(
                [
                    dcc.Tab(
                        label="Analysis",
                        children=[
                            dcc.Graph(figure=fig),
                        ],
                    ),
                    dcc.Tab(
                        label="Datasets",
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
