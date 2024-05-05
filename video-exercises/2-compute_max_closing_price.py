# https://youtu.be/y9yNIgy681Q?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx

import pandas as pd

DATA_FILE = "data/AAPL.csv"

def get_max_close(data_file):
    """Returns the max closing value for stock data in data_file"""
    df = pd.read_csv(data_file)
    return df['Close'].max()

def test_run():
    print(get_max_close(DATA_FILE))

if __name__ == "__main__":
    test_run()