
from web3 import Web3
from datetime import datetime

class UniswapEventScraper:
    def __init__(self, w3):
        self.w3 = w3
        self.uniswap_v3_pool_abi = [
            {
                "anonymous": False,
                "inputs": [
                    {"indexed": True, "name": "owner", "type": "address"},
                    {"indexed": True, "name": "tickLower", "type": "int24"},
                    {"indexed": True, "name": "tickUpper", "type": "int24"},
                    {"indexed": False, "name": "amount", "type": "uint128"},
                    {"indexed": False, "name": "amount0", "type": "uint256"},
                    {"indexed": False, "name": "amount1", "type": "uint256"}
                ],
                "name": "Mint",
                "type": "event"
            },
            {
                "anonymous": False,
                "inputs": [
                    {"indexed": True, "name": "owner", "type": "address"},
                    {"indexed": False, "name": "recipient", "type": "address"},
                    {"indexed": True, "name": "tickLower", "type": "int24"},
                    {"indexed": True, "name": "tickUpper", "type": "int24"},
                    {"indexed": False, "name": "amount0", "type": "uint128"},
                    {"indexed": False, "name": "amount1", "type": "uint128"}
                ],
                "name": "Collect",
                "type": "event"
            },
            {
                "anonymous": False,
                "inputs": [
                    {"indexed": True, "name": "owner", "type": "address"},
                    {"indexed": True, "name": "tickLower", "type": "int24"},
                    {"indexed": True, "name": "tickUpper", "type": "int24"},
                    {"indexed": False, "name": "amount", "type": "uint128"},
                    {"indexed": False, "name": "amount0", "type": "uint256"},
                    {"indexed": False, "name": "amount1", "type": "uint256"}
                ],
                "name": "Burn",
                "type": "event"
            },
            {
                "anonymous": False,
                "inputs": [
                    {"indexed": True, "name": "sender", "type": "address"},
                    {"indexed": True, "name": "recipient", "type": "address"},
                    {"indexed": False, "name": "amount0", "type": "int256"},
                    {"indexed": False, "name": "amount1", "type": "int256"},
                    {"indexed": False, "name": "sqrtPriceX96", "type": "uint160"},
                    {"indexed": False, "name": "liquidity", "type": "uint128"},
                    {"indexed": False, "name": "tick", "type": "int24"}
                ],
                "name": "Swap",
                "type": "event"
            }
        ]

    def scrape_events(self, pool_address, start_date, end_date):
        contract = self.w3.eth.contract(address=Web3.toChecksumAddress(pool_address), abi=self.uniswap_v3_pool_abi)
        
        start_block = self._get_block_number(start_date)
        end_block = self._get_block_number(end_date)
        
        events = []
        
        for event_name in ['Mint', 'Collect', 'Burn', 'Swap']:
            event_filter = contract.events[event_name].createFilter(fromBlock=start_block, toBlock=end_block)
            for event in event_filter.get_all_entries():
                event_data = {
                    'event': event_name,
                    'blockNumber': event['blockNumber'],
                    'transactionHash': event['transactionHash'].hex(),
                    'args': dict(event['args'])
                }
                events.append(event_data)
        
        return events

    def _get_block_number(self, date):
        timestamp = int(date.timestamp())
        return self.w3.eth.get_block_number_by_timestamp(timestamp)
