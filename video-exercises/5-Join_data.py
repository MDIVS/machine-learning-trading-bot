# https://youtu.be/P483hKA-3MU?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx

import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import os

os.system("cls") # clear terminal
yf.pdr_override() # fix pdr.get_data_yahoo

LAST_N_DAYS = 15
END_DATE = dt.date.today()
START_DATE = END_DATE - dt.timedelta(days=LAST_N_DAYS)
SYMBOLS = ['BTC-USD', 'SPY', 'IBM', 'GLD']

# SYMBOLS = ['SPY']

# stockList = ['AAPL', 'SPY']
# # stockList = ['CBA', 'NAB', 'WBC', 'ANZ']
# stocks = [i + '.AX' for i in stockList]
# print(stocks)

# print('getting yahoo data...')
# # data = pdr.get_data_yahoo(stocks, start, end)
# # print(data.head())
# print()

def test_run():
    df1 = pd.DataFrame(index=pd.date_range(end=END_DATE, periods=LAST_N_DAYS))

    for symbol in SYMBOLS:
        print(f'getting {symbol} data...')
        stock_df = pdr.get_data_yahoo(symbol, START_DATE, END_DATE)
        stock_df = stock_df.filter(items=['Adj Close'])
        print()

        print('retrieved data:')
        print(stock_df)
        print()

        stock_df = stock_df.rename(columns={'Adj Close': symbol})
        df1 = df1.join(stock_df, how='inner').dropna()
    
    print('joined data:')
    print(df1)
    print()
    
    df1[SYMBOLS].plot()
    plt.show()

if __name__ == "__main__":
    test_run()