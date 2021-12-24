from dash import html, dcc

filters = html.Div([
    dcc.Dropdown(
        id="filter-1",
        className="panel__filters__item",
        options=[
            {'label': 'Filter 1', 'value': 'Filter 1'},
            {'label': 'Filter 2', 'value': 'Filter 2'},
            {'label': 'Filter 3', 'value': 'Filter 3'},
        ],
        value=[],
        clearable=False,
        multi=True,
        placeholder="Selecione um filtro"
    ),

    dcc.Dropdown(
        id="filter-2",
        className="panel__filters__item",
        options=[
            {'label': 'Filter 1', 'value': 'Filter 1'},
            {'label': 'Filter 2', 'value': 'Filter 2'},
            {'label': 'Filter 3', 'value': 'Filter 3'},
        ],
        clearable=False,
        multi=True,
        placeholder="Selecione um filtro"
    ),

    dcc.Dropdown(
        id="filter-3",
        className="panel__filters__item",
        options=[
            {'label': 'Filter 1', 'value': 'Filter 1'},
            {'label': 'Filter 2', 'value': 'Filter 2'},
            {'label': 'Filter 3', 'value': 'Filter 3'},
        ],
        clearable=False,
        multi=True,
        placeholder="Selecione um filtro"
    ),

    dcc.Dropdown(
        id="filter-4",
        className="panel__filters__item",
        options=[
            {'label': 'Filter 1', 'value': 'Filter 1'},
            {'label': 'Filter 2', 'value': 'Filter 2'},
            {'label': 'Filter 3', 'value': 'Filter 3'},
        ],
        clearable=False,
        multi=True,
        placeholder="Selecione um filtro"
    )
], className="panel__filters")