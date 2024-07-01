# app.py
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash_bootstrap_templates import load_figure_template

from navbar import create_navbar

NAVBAR = create_navbar()
# To use Font Awesome Icons
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
APP_TITLE = "The F1 Score Championship"
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
custom_css = "/assets/custom.css"
load_figure_template("Superhero")

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.SUPERHERO,  # Dash Themes CSS
        FA621,  # Font Awesome Icons CSS
        dbc_css,
        custom_css,
    ],
    title=APP_TITLE,
    use_pages=True,  # New in Dash 2.7 - Allows us to register pages
)

page_container = html.Div(
    [
        dcc.Location(id="_pages_location", refresh="callback-nav"),
        html.Div(id="_pages_content", disable_n_clicks=True, style={"height": "100%"}),
        dcc.Store(id="_pages_store"),
        html.Div(id="_pages_dummy", disable_n_clicks=True),
    ],
    id="parent_page_content",
)

app.layout = dbc.Container(
    [
        NAVBAR,
        page_container,
    ],
    fluid=True,
    className="dbc dbc-ag-grid bg-dark",
    style={"height": "100vh"},
)

server = app.server


if __name__ == "__main__":
    app.run_server(debug=True)
