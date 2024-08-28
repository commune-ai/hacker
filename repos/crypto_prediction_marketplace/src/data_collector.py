
import ccxt
import pandas as pd

class DataCollector:
    def __init__(self):
        self.exchanges = [
            ccxt.binance(),
            ccxt.coinbasepro(),
            ccxt.kraken()
        ]

    def collect_data(self):
        data = {}
        for exchange in self.exchanges:
            try:
                tickers = exchange.fetch_tickers()
                for symbol, ticker in tickers.items():
                    if symbol not in data:
                        data[symbol] = []
                    data[symbol].append({
                        'exchange': exchange.id,
                        'price': ticker['last'],
                        'volume': ticker['baseVolume']
                    })
            except Exception as e:
                print(f"Error collecting data from {exchange.id}: {str(e)}")
        
        return pd.DataFrame([(symbol, item['exchange'], item['price'], item['volume']) 
                             for symbol, items in data.items() 
                             for item in items],
                            columns=['symbol', 'exchange', 'price', 'volume'])

