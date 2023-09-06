from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Output, Input
from . import ids

MEDAL_DATA = px.data.medals_long()


def render(app: Dash) -> html.Div:
    """This callback gets as an input the value (list) of the dropdown.
    This list is generated when the user adds or remove a selection in
    the drop down.

    Upon receiving a list of new values, we filter the pandas data using the
    query method

                    nation   medal count
            0  South Korea    gold     24
            1        China    gold     10
            3  South Korea  silver     13
            4        China  silver     15
            6  South Korea  bronze     11
            7        China  bronze      8

    create a new figure, this time using the filtered data, and create a new
    div containing a new graph

    """

    @app.callback(
        Output(ids.MEDAL_BAR_CHART, "children"), Input(ids.NATION_DROPDOWN, "value")
    )
    def update_barchart(nations: list[str]) -> html.Div:
        filtered_data = MEDAL_DATA.query("nation in @nations")
        print(filtered_data)
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")
        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(dcc.Graph(figure=fig), id=ids.MEDAL_BAR_CHART)

    """
    When the page is initialized, we return an empty div
    howeverm when the Dropdown control will be initialized with data,
    this will trigger this method call with the initial data
    """
    return html.Div(id=ids.MEDAL_BAR_CHART)
