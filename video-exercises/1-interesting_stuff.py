# https://youtu.be/2UEzsw5n-II?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print(df[10:21])

if __name__ == "__main__":
    test_run()