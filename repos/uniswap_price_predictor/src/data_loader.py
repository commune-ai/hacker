
import requests
import pandas as pd
import pickle
from config import config

class UniswapDataLoader:
    def __init__(self):
        self.api_url = config.DATA_SOURCE

    def fetch_pair_data(self, pair_address, num_blocks):
        query = f"""
        {{
          pairDayDatas(first: {num_blocks}, orderBy: date, orderDirection: desc, where: {{ pairAddress: "{pair_address}" }}) {{
            date
            reserve0
            reserve1
            reserveUSD
            dailyVolumeToken0
            dailyVolumeToken1
            dailyVolumeUSD
            token0 {{
              symbol
            }}
            token1 {{
              symbol
            }}
          }}
        }}
        """
        response = requests.post(self.api_url, json={'query': query})
        data = response.json()['data']['pairDayDatas']
        return pd.DataFrame(data)

    def preprocess_data(self, df):
        df['date'] = pd.to_datetime(df['date'], unit='s')
        df['price'] = df['reserveUSD'].astype(float) / df['reserve0'].astype(float)
        df = df.sort_values('date')
        return df[['date', 'price', 'dailyVolumeUSD']]

    def load_data(self, pair_address):
        try:
            with open(config.DATA_CACHE_PATH, 'rb') as f:
                cached_data = pickle.load(f)
                if pair_address in cached_data:
                    return cached_data[pair_address]
        except FileNotFoundError:
            cached_data = {}

        df = self.fetch_pair_data(pair_address, config.BLOCKS_IN_PAST)
        processed_df = self.preprocess_data(df)

        cached_data[pair_address] = processed_df
        with open(config.DATA_CACHE_PATH, 'wb') as f:
            pickle.dump(cached_data, f)

        return processed_df

    def prepare_data_for_model(self, df):
        X = df[['price', 'dailyVolumeUSD']].values
        y = df['price'].values[1:]
        return X[:-1], y
