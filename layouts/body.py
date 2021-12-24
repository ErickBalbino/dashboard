from dash import html
from dash import dcc

body =  html.Div(children=[

    html.Div([
        html.Div([
            html.I(className="fas fa-bars body__header__first__section-iconBar"),
            dcc.Input(
                type="text",
                id="txt-search",
                className="body__header__first__section-search",
                placeholder="Digite algo para pesquisar..."
            )
        ], className="body__header__first__section"),

        html.Div([
            html.I(className="fas fa-cog"),
            html.I(className="fas fa-adjust"),
            html.I(className="fas fa-bell"),
            html.I(className="fas fa-user")
        ], className="body__header__second__section")
    ], className="body__header"),

    html.Div([
        html.Div([
            html.Div([
                html.Span('26030'),
                html.P('Total de vendas')
            ], className="body__cards__card-text"),
            html.Div([
                html.I(className="fas fa-shopping-cart")
            ], className="body__card__card-icon")
        ], className="body__cards__card"),

        html.Div([
            html.Div([
                html.Span('120000'),
                html.P('Renda liquida')
            ], className="body__cards__card-text"),
            html.Div([
                html.I(className="fas fa-wallet")
            ], className="body__card__card-icon")
        ], className="body__cards__card"),

        html.Div([
            html.Div([
                html.Span('2030'),
                html.P('Vendas este mês')
            ], className="body__cards__card-text"),
            html.Div([
                html.I(className="fas fa-chart-bar")
            ], className="body__card__card-icon")
        ], className="body__cards__card"),

        html.Div([
            html.Div([
                html.Span('2030'),
                html.P('Total de clientes')
            ], className="body__cards__card-text"),
            html.Div([
                html.I(className="fas fa-user")
            ], className="body__card__card-icon")
        ], className="body__cards__card"),

    ], className="body__cards"),

    html.Div([

    ], className="body__graphs")
], className="body")