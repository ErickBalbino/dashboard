import dash
from dash import html
from dash import dcc
from layouts.filters import filters
from layouts.body import body

layout = html.Div([
    html.Div(children=[
        html.Div([
            html.Img(src="assets/imagem-perfil.png", className="panel__image-img"),
            html.P("Olá, Usuário!", className="panel__image-txt")
        ], className="panel__image"),
        
        filters
    ], className="panel"),

    body
], className="dashboard")