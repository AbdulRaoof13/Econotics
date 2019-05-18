import requests
import json

class Stock:
    def __init__(self, symbol, name, currency, price, price_open, day_high, day_low, week_high, week_low, day_change, change_pct, close_yesterday, market_cap, volume_avg, stock_exchange_long, stock_exchange_short, timezone, timezone_name, gmt_offset, last_trade_time):
        self.symbol = symbol
        self.name = name
        self.currency = currency
        self.price = price
        self.price_open = price_open
        self.day_high = day_high
        self.day_low = day_low
        self.week_high = week_high
        self.week_low = week_low
        self.day_change = day_change
        self.change_pct = change_pct
        self.close_yesterday = close_yesterday
        self.market_cap = market_cap
        self.volume_avg = volume_avg
        self.stock_exchange_long = stock_exchange_long
        self.stock_exchange_short = stock_exchange_short
        self.timezone = timezone
        self.timezone_name = timezone_name
        self.gmt_offset = gmt_offset
        self.last_trade_time = last_trade_time

    def printstock(self):
        print(
            "Symbol: " + self.symbol + "\n" +
            "Name: " + self.name + "\n" +
            "Currency: " + self.currency + "\n" +
            "Price: " + self.price + "\n" +
            "Open: " + self.price_open + "\n" +
            "High: " + self.day_high + "\n" +
            "Low: " + self.day_low + "\n" +
            "52-Week High: " + self.week_high + "\n" +
            "52-Week low: " + self.week_low + "\n" +
            "Day Change: " + self.day_change + "\n" +
            "Day Change(%): " + self.change_pct + "\n" +
            "Prev Close: " + self.close_yesterday + "\n" +
            "Mkt Cap: " + self.market_cap + "\n" +
            "Volume Avg: " + self.volume_avg + "\n" +
            "Stock Exchange Long: " + self.stock_exchange_long + "\n" +
            "Stock Exchange short: " + self.stock_exchange_short + "\n" +
            "Timezone: " + self.timezone + "\n" +
            "Timezone Name: " + self.timezone_name + "\n" +
            "GMT: " + self.gmt_offset + "\n"
            "Last Trade Time: " + self.last_trade_time + "\n"
        )

    def __lt__(self, other):
        return self.symbol < other.symbol

    def __gt__(self, other):
        return self.symbol > other.symbol

    def __eq__(self, other):
        return self.symbol == other.symbol


url = "https://www.worldtradingdata.com/api/v1/stock?api_token=94cSAnpTVJCJlzWjqiPNYSZtAR8l4FAwmODMsz3tEVucWrE2cfc1l6R3JTwr&symbol="
urla = "https://financialmodelingprep.com/api/stock/real-time/all?datatype=json"

symbols = requests.get(urla)
symbols = json.loads(symbols.content)

arrayofstocks = []
group = []
limit = 250 # for each day

count = 0

for i in range(0, len(symbols)-3, 4):
    symbolz = symbols[i]['symbol']+','+symbols[i+1]['symbol']+','+symbols[i+2]['symbol']+','+symbols[i+3]['symbol']

    if count > 5:
        break

    if (limit > 0):
        req = requests.get(url+symbolz)
        limit = limit-1
    else:
        break

    data = json.loads(req.content)
    stockdata = data['data'][0]

    for d in stockdata:
        dict = {}
        #get(if exists return this, else return this)
        dict["symbol"] = d.get("symbol",'N/A')
        dict["name"] = d.get("name",'N/A')
        dict["currency"] = d.get("currency",'N/A')
        dict["price"] = d.get("price",'N/A')
        dict["price_open"] = d.get("price_open",'N/A')
        dict["day_high"] = d.get("day_high",'N/A')
        dict["day_low"] = d.get("day_low",'N/A')
        dict["52_week_high"] = d.get("52_week_high",'N/A')
        dict["52_week_low"] = d.get("52_week_low",'N/A')
        dict["day_change"] = d.get("day_change",'N/A')
        dict["change_pct"] = d.get("change_pct",'N/A')
        dict["close_yesterday"] = d.get("close_yesterday",'N/A')
        dict["market_cap"] = d.get("market_cap",'N/A')
        dict["volume_avg"] = d.get("volume_avg",'N/A')
        dict["stock_exchange_long"] = d.get("stock_exchange_long",'N/A')
        dict["stock_exchange_short"] = d.get("stock_exchange_short",'N/A')
        dict["timezone"] = d.get("timezone",'N/A')
        dict["timezone_name"] = d.get("timezone_name",'N/A')
        dict["gmt_offset"] = d.get("gmt_offset", 'N/A')
        dict["last_trade_time"] = d.get("last_trade_time",'N/A')

        obj = Stock(dict["symbol"],
        dict["name"],
        dict["currency"],
        dict["price"],
        dict["price_open"],
        dict["day_high"],
        dict["day_low"],
        dict["52_week_high"],
        dict["52_week_low"],
        dict["day_change"],
        dict["change_pct"],
        dict["close_yesterday"],
        dict["market_cap"],
        dict["volume_avg"],
        dict["stock_exchange_long"],
        dict["stock_exchange_short"],
        dict["timezone"],
        dict["timezone_name"],
        dict["gmt_offset"],
        dict["last_trade_time"])

        arrayofstocks.append(obj)

        count += 1

    """if count > 20:
        break
    try:
        json.loads(his.content)
        hisdata = json.loads(his.content)
        history = hisdata['historical'][0]
        arrayofstocks.append(
            Stock(x['symbol'], x['price'], history['date'], history['open'], history['high'], history['low'],
                  history['close'], history['volume'], history['unadjustedVolume'], history['change'],
                  history['changePercent'], history['changeOverTime']))
        count += 1
    except:
        pass

print(count)

arrayofstocks.sort()

for x in arrayofstocks:
   x.printstock()
   print("\n\n")"""

print(count)

for x in arrayofstocks:
    x.printstock()