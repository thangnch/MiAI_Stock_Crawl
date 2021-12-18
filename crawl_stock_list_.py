import pandas as pd
import requests


def craw_stock_list():
    url = "https://finfo-api.vndirect.com.vn/v4/stocks?fields=code,shortName,floor&q=type:stock,ifc~floor:HOSE,HNX&size=9999"
    x = requests.get(url)
    json_x = x.json()['data']

    # print(json_x)
    stock_df = pd.DataFrame()


    for stock in json_x:
        print(stock)
        stock_df = stock_df.append(stock, ignore_index=True)

    print(stock_df.head())
    stock_df.to_csv("data/stock_list.csv", index=None)

craw_stock_list()