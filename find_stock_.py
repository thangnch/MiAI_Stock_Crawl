import pandas as pd
import numpy as np

green = 1
red = 6

def is_valid(y, num_green, num_red):
    if len(y) == 0:
        return False
    # Get only enough items
    y = y[-(num_red+num_green):]

    # Check last green
    if num_green > 0:
        greens = y[-num_green:]
        for item in greens:
            if item <= 0:
                return False

    reds = y[:len(y)-num_green]
    for item in reds:
        if item >= 0:
            return False

    return True

stock_df = pd.read_csv("data/stock_list.csv")
stock_price_df = pd.read_csv("data/stock_price.csv")

for idx, row in stock_df.iterrows():
    # print("Process... {} - {}".format(idx, row['code']))

    c_stock_price_df = stock_price_df[stock_price_df.code == row['code']][['date','code','pctChange']]
    y = c_stock_price_df['pctChange'].values
    y = np.flip(y)

    if is_valid(y, num_green=green, num_red=red):
        #print(y)
        print("--------- Vào ngay mã {} https://dstock.vndirect.com.vn/lich-su-gia/{}".format(row['code'],row['code']))
        #input()
