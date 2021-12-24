import json
import pandas as pd

def get_data_graph1():
    with open ("services\json\graph1.json") as file:
        data_graph1 = json.load(file)
        
    df = pd.DataFrame(data_graph1)
    return df