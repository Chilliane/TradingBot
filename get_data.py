
import talib
import csv
from binance.client import Client

client = Client('')

#prices = client.get_all_tickers()

#for price in prices:
#    print(price)

candles = client.get_klines(symbol='BTCUSDT',interval=Client.KLINE_INTERVAL_15MINUTE)
print(len(candles))

csvfile = open('data.csv','w',newline='')
candilestick_writer = csv.writer(csvfile,delimiter=',')

#for candlesticks in candles:
#    print(candlesticks)

#    candilestick_writer.writerow(candlesticks)

#print (len(candles))
#candlesticks = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_1MINUTE, "1 Dec, 2020", "14 August, 2022")
#for candlestick in candlesticks:
#    candilestick_writer.writerow(candlestick)

#csvfile.close()
