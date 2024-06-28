from dash import html  # , callback # If you need callbacks, import it here.
from dash import register_page

register_page(__name__, name="Model", top_nav=True, path_template="/model/<model_id>")


def layout(model_id=None, **kwargs):
    return html.Div(f"The user requested Model ID: {model_id}.")
