import plotly_express as px
import pandas as pd
from dash.dependencies import Output, Input
from services.components.main import get_filter1
from app import app

@app.callback(
    Output(component_id="filter-1", component_property="options"),
    Input(component_id="filter-1", component_property="options")
)

def load_filters(initial):
    results_filter1 = get_filter1()
    
    return results_filter1