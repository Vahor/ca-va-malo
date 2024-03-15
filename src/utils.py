import pandas as pd

data = None

def get_data():
    """Get data from the data directory."""
    global data
    if data is not None:
        return data
    data = pd.read_csv('../data/googleplaystore.csv')
    return data

get_data()
