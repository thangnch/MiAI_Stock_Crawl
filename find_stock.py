import pandas as pd
import numpy as np
from datetime import date
import time
import json


stock_df = pd.read_csv("data/stock_list.csv")[-5:]
stock_price_df = pd.read_csv("data/stock_price_avg.csv")

for idx, row in stock_df.iterrows():
    print("Process... {} - {}".format(idx, row['code']))

    c_stock_price_df = stock_price_df[stock_price_df.code == row['code']][['code','nmVolume']]
    avg_volume = c_stock_price_df['nmVolume'].values[0]

    print("AVG volume = ", avg_volume)

    to_date = date.today()
    from_date = to_date
    stock_code = row['code']

    to_date = to_date.strftime("%Y-%m-%d")
    from_date = from_date.strftime("%Y-%m-%d")

    url = "https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{}~date:gte:{}~date:lte:{}&size=9990&page=1".format(
        stock_code, from_date, to_date)
    # print(url)

    import urllib.request

    get_ok = False
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
    # print(json.loads(x))
    json_x = json.loads(x)['data']
    # json_x = x.json()['data']

    for stock in json_x:
        # print(stock)
        current_volume = stock['nmVolume']
        print("Current volume = ", current_volume)
        if (current_volume > avg_volume) and ( (current_volume > avg_volume)/avg_volume > 0.5) :
            print(" >>>>>>>>> Current change = ", ((current_volume-avg_volume)/avg_volume)*100, "%")


