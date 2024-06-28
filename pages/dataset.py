from dash import html  # , callback # If you need callbacks, import it here.
from dash import register_page

register_page(
    __name__, name="Dataset", top_nav=True, path_template="/dataset/<dataset_id>"
)


def layout(dataset_id=None, **kwargs):
    return html.Div(f"The user requested dataset ID: {dataset_id}.")
