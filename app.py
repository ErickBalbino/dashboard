import dash
from layouts.main import layout

app = dash.Dash(__name__)

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)