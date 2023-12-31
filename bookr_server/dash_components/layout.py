from dash import Dash, html
from . import nation_dropdown
from . import bar_chart


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        style={"height": "100vh"},
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container", children=nation_dropdown.render(app=app)
            ),
            bar_chart.render(app),
        ],
    )
