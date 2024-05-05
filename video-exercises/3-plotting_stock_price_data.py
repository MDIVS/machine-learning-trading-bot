# https://youtu.be/0-Pg0Mw2Pm0?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "data/AAPL.csv"

def test_run():
    df = pd.read_csv(DATA_FILE)
    print(df['Close'])
    df['Close'].plot()
    plt.show()

if __name__ == "__main__":
    test_run()