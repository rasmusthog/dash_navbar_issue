import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row([dbc.Col(dbc.NavbarBrand("My NavBar", className="ms-2"))],
                    align="left",
                    className="g-0",
                ),
                style={"textDecoration": "none"},
            )
        ],
    color="dark",
    dark=True,
    className="mb-5",
    style = {'margin-bottom':'0px', 'padding-left': '15px', 'padding-right': '10px'},
)

app.layout = html.Div(
    [navbar,
    dash.page_container
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)