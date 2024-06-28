# app.py
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

from navbar import create_navbar

NAVBAR = create_navbar()
# To use Font Awesome Icons
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
APP_TITLE = "The F1 Score Championship"


app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.LUX,  # Dash Themes CSS
        FA621,  # Font Awesome Icons CSS
    ],
    title=APP_TITLE,
    use_pages=True,  # New in Dash 2.7 - Allows us to register pages
)

# To use if you're planning on using Google Analytics
app.index_string = f"""
<!DOCTYPE html>
<html>
    <head>
        {{%metas%}}
        <title>{APP_TITLE}</title>
        {{%favicon%}}
        {{%css%}}
    </head>
    <body>
        {{%app_entry%}}
        <footer>
            {{%config%}}
            {{%scripts%}}
            {{%renderer%}}
        </footer>
        
    </body>
</html>
"""


app.layout = dcc.Loading(  # <- Wrap App with Loading Component
    id="loading_page_content",
    children=[html.Div([NAVBAR, dash.page_container])],
    color="primary",  # <- Color of the loading spinner
    fullscreen=True,  # <- Loading Spinner should take up full screen
)

server = app.server


if __name__ == "__main__":
    app.run_server(debug=True)
