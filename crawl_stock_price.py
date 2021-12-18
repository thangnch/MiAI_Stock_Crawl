import pandas as pd
import requests
import json
from datetime import date
from datetime import timedelta
import time


def craw_stock_price():
    to_date = date.today()
    from_date = to_date - timedelta(days=30)

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

        import urllib.request
        get_ok  = False
        while not get_ok:
            try:
                with urllib.request.urlopen(url, timeout=5) as response:
                    x = response.read()
                    get_ok = True
            except:
                print("Error, wait 1s ")
                time.sleep(1)
                continue


        # x = requests.get(url , timeout=10)
        print(json.loads(x))
        json_x = json.loads(x)['data']
        #json_x = x.json()['data']


        for stock in json_x:
            print(stock)
            stock_price_df = stock_price_df.append(stock, ignore_index=True)

        #time.sleep(1)

    stock_price_df.to_csv("data/stock_price.csv", index=None)

    stock_price_avg_df = stock_price_df.groupby('code').mean()['nmVolume']
    stock_price_avg_df.to_csv("data/stock_price_avg.csv")

craw_stock_price()