from dash import html
from dash import dcc

panel = html.Div(children=[
    html.Div([
        html.Img(src="assets/imagem-perfil.png", className="panel__image-img"),
        
        html.P("Olá, Usuário!", className="panel__image-txt")
    ], className="panel__image"),
], className="panel"),