from pathlib import Path

from dash import html  # , callback # If you need callbacks, import it here.
from dash import dcc, register_page

content = dcc.Markdown(
    """
            ## 🏁 The scoring system 🏁 ##
            The recorded MASE metric for each model is used to determine the position of a model for a given dataset. The points are then awarded as per the Formula 1 scoring system: 

            | Position | Points |
            |----------|--------|
            | 1        | 25     |
            | 2        | 18     |
            | 3        | 15     |
            | 4        | 13     |
            | 5        | 10     |
            | 6        | 8      |
            | 7        | 6      |
            | 8        | 4      |
            | 9        | 2      |
            | 10       | 1      |


            ## The Rules ##  
            Paricipants are required to adhere to the following rules:  
            1. The model must be trained to generate forecasts the entire forecast horizon.  
            1. One set of hyperparameters must be used for all datasets.  
            1. Covariate features are permitted but must be and must the same for all datasets or be speicific to the frequency of the dataset.  
            1. The results must be reproducible.  
            1. Submissions using the mean from multiple runs will replace the original submission.  
            """
)


register_page(__name__, name="About", top_nav=True, path="/about")


def layout():
    layout = html.Div(
        children=[
            content,
        ]
    )
    return layout
