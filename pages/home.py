from pathlib import Path

import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html  # , callback # If you need callbacks, import it here.
from dash import dcc, register_page

# Data
THIS_FOLDER = Path(__file__).parent.parent.resolve()
points_file = THIS_FOLDER / "data/leaderboard.csv"
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


datasets_file = THIS_FOLDER / "data/datasets_leader.csv"
datasets_df = pd.read_csv(datasets_file).sort_values(by="Dataset", ascending=True)
datasets_columnDefs = [
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


def dataset_scatter():

    fig = px.scatter(
        datasets_df,
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
    return fig


fig = dataset_scatter()
grid = dag.AgGrid(
    id="column-definitions-basic",
    rowData=df.to_dict("records"),
    defaultColDef={
        "flex": 1,
        "minWidth": 150,
        "sortable": True,
        "resizable": True,
        "filter": True,
    },
    columnDefs=columnDefs,
    dashGridOptions={"animateRows": True},
    className="ag-theme-alpine dbc-ag-grid",
    style={"height": "70vh"},
)
dataset_grid = dag.AgGrid(
    id="column-definitions-basic",
    rowData=datasets_df.to_dict("records"),
    defaultColDef={"filter": True},
    columnDefs=datasets_columnDefs,
    columnSize="sizeToFit",
    dashGridOptions={"animateRows": True},
    style={"height": "100vh"},
)

register_page(__name__, name="Standings", top_nav=True, path="/")

tabs = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Leaderboard",
                    children=[
                        dcc.Markdown(
                            """
                                ### Model Championship Standings
                                These benchmarks were measured by Monash University 
                                using the mean absolute scaled error (MASE). See https://forecastingdata.org/ for further information.
                                Points for each dataset are awarded based on the Formula 1 scoring system.  
                                *Note: Informer has not currently been benchmarked across all datasets* 
                                """
                        ),
                        grid,
                    ],
                ),
                dcc.Tab(
                    label="Analysis",
                    children=[
                        dcc.Markdown(
                            """
                                ### Analysis
                                The following is a scatter plot of the leading model performance 
                                for each dataset in the series, plotted as a function of the time 
                                series frequency.
                                """
                        ),
                        dcc.Graph(figure=fig),
                    ],
                ),
                dcc.Tab(
                    label="Datasets",
                    children=[
                        dcc.Markdown(
                            """
                            ### Datasets  
                            The complete set of datasets used in the championship. See https://forecastingdata.org/ for further information.  
                            *Note: Kaggle Daily and M4 Yearly are currently excluded as these haven't been benchmarked across all models.*
                            """
                        ),
                        dataset_grid,
                    ],
                ),
            ]
        ),
    ]
)


def layout():
    layout = dbc.Container([tabs])
    return layout
