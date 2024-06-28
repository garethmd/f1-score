from dash import html  # , callback # If you need callbacks, import it here.
from dash import register_page

register_page(__name__, name="Models", top_nav=True, path="/models")


def layout():
    layout = html.Div([html.H1(["Models"])])
    return layout
