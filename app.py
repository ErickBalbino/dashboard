import dash
from layouts.main import layout
import logging

logging.basicConfig(
    filename='web.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

logger = logging.getLogger(__name__)

app = dash.Dash(__name__, suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'}],
    external_stylesheets=[{
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
        "integrity": "sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==",
        "crossorigin": "anonymous",
        "referrerpolicy": "no-referrer",
    }],
)

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)