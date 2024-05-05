import pandas as pd

DATA_FILE = "data/BTC-Daily.csv"

def get_max_close(data_file):
    """Returns the max closing value for stock data in data_file"""
    df = pd.read_csv(data_file)
    return df['close'].max()

def test_run():
    print(get_max_close(DATA_FILE))

if __name__ == "__main__":
    test_run()