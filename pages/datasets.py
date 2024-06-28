from dash import html  # , callback # If you need callbacks, import it here.
from dash import register_page

register_page(__name__, name="Datasets", top_nav=True, path="/datasets")


def layout():
    layout = html.Div([html.H1(["Datasets"])])
    return layout
