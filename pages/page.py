import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path='/')

navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.NavbarBrand("My Second NavBar", className="ms-2"),
                )
        ],
    color="red",
    dark=False,
    className="mb-5",
    style = {'margin-top': '-50px', 'margin-bottom':'0px', 'padding-left': '15px', 'padding-right': '10px'},
    sticky='top'
)





layout = html.Div([
    navbar,
    html.H1('This is my page!')
])