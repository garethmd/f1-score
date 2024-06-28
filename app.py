# app.py

import dash_ag_grid as dag
import pandas as pd
from dash import Dash, dcc, html

external_scripts = [
    # add the tailwind cdn url hosting the files with the utility classes
    {"src": "https://cdn.tailwindcss.com"}
]

app = Dash(__name__, external_scripts=external_scripts)

df = pd.read_csv("points.csv").sort_values(by="Points", ascending=False)


columnDefs = [{"field": "Model", "sortable": True}, {"field": "Points"}]


app.layout = html.Div(
    children=[
        html.H1(children="F1 Score Championship Points"),
        html.P(
            children=("Monash MASE"),
        ),
        dag.AgGrid(
            id="column-definitions-basic",
            rowData=df.to_dict("records"),
            defaultColDef={"filter": True},
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": True},
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
