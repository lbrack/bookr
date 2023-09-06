from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids


def render(app: Dash) -> html.Div:
    all_nations = ["South Korea", "China", "Canada"]

    """ This call back takes as an input the number of times the button was clicked. 
        In this case, we do not care about the value as we only treat this as a event
        notifying us that the button was click. 
        
        The output of that callback will be a list of values. Because it is mapped to
        value, it will update the value property of the dropdown. 
        
        When this property is updated, this will trigger the callback on the barchart. 
        see barchart.py for details. 
    """

    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_NATION_BUTTON, "n_clicks"),
    )
    def select_all_nations(_: int) -> list[str]:
        print(_)
        return all_nations

    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                multi=True,
                value=all_nations,
                options=[{"label": nation, "value": nation} for nation in all_nations],
            ),
            html.Button(
                className="dropdown-button",
                id=ids.SELECT_ALL_NATION_BUTTON,
                children=["Select All"],
            ),
        ]
    )
