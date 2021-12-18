import pandas as pd
import requests
from datetime import date
from datetime import timedelta
import time

def craw_stock_price():
    to_date = date.today()
    from_date = to_date - timedelta(days=60)

    to_date = to_date.strftime("%Y-%m-%d")
    from_date = from_date.strftime("%Y-%m-%d")

    input("Chuẩn bị crawl {} {}".format(from_date, to_date))

    # print(json_x)
    stock_price_df = pd.DataFrame()

    stock_df = pd.read_csv("data/stock_list.csv")

    for idx, row in stock_df.iterrows():
        print("Process... {} - {}".format(idx, row['code']))
        stock_code = row['code']

        url = "https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{}~date:gte:{}~date:lte:{}&size=9990&page=1".format(stock_code, from_date, to_date)
        print(url)
        x = requests.get(url, timeout=10)
        json_x = x.json()['data']

        for stock in json_x:
            print(stock)
            stock_price_df = stock_price_df.append(stock, ignore_index=True)

        time.sleep(5)



    stock_price_df.to_csv("data/stock_price.csv", index=None)

    stock_price_avg_df = stock_price_df.groupby['code'].mean()['ptVolume']
    stock_price_avg_df.to_csv("data/stock_price_avg.csv", index=None)


craw_stock_price()