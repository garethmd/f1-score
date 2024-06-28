import dash_bootstrap_components as dbc
from dash import html


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-github"),  # Font Awesome Icon
                        " ",  # Text beside icon
                    ],
                    href="models",
                    target="_blank",
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-medium"),  # Font Awesome Icon
                        " ",  # Text beside icon
                    ],
                    href="datasets",
                    target="_blank",
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-linkedin"),  # Font Awesome Icon
                        " ",  # Text beside icon
                    ],
                    href="engines",
                    target="_blank",
                )
            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # Add as many menu items as you need
                    dbc.DropdownMenuItem("Standings", href="/"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Datasets", href="/datasets"),
                    dbc.DropdownMenuItem("Models", href="/models"),
                ],
            ),
        ],
        brand="The FITs Championship",
        brand_href="/",
        # sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
