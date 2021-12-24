import json
from app import logger

def get_filter1():
    try: 
        with open ("services/json/filter1.json") as file:
            results = json.load(file)
        return results
    except Exception as e:
        print(f'Load filter 1: {e}')
        return []