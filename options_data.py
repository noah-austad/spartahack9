#API Key:
#G6H0CSGDHM0L3VGB
import requests
#Option Trading Classes
class Option:
    #constructor method
    def __init__(self, spread, stock, E1, E2):
        self.spread= spread
        self.stock=stock
        self.E1= E1
        self.E2= E2

#display recent activity
#show option choices
class stock:
    def __init__(self, ticker,price=[]):
        self.ticker=ticker
        self.price_history=price
    def update_prices(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+self.ticker+'&apikey=G6H0CSGDHM0L3VGB'
        r = requests.get(url)
        data = r.json()
        close_data = [entry['4. close'] for entry in data['Time Series (Daily)'].values()]
        self.price_history=close_data

def trending_req():
    url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=G6H0CSGDHM0L3VGB'
    r = requests.get(url)
    data = r.json()
    return(data)
