
from flask import Flask, jsonify
from web3 import Web3
from config import ETHEREUM_NODE_URL, UNISWAP_FACTORY_ADDRESS, UNISWAP_FACTORY_ABI

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))
uniswap_factory = w3.eth.contract(address=UNISWAP_FACTORY_ADDRESS, abi=UNISWAP_FACTORY_ABI)

@app.route('/scrape_events/<token_address>/<int:n_blocks>')
def scrape_events(token_address, n_blocks):
    current_block = w3.eth.block_number
    from_block = current_block - n_blocks
    
    events = uniswap_factory.events.PairCreated.get_logs(
        fromBlock=from_block,
        toBlock='latest',
        argument_filters={'token0': token_address}
    ) + uniswap_factory.events.PairCreated.get_logs(
        fromBlock=from_block,
        toBlock='latest',
        argument_filters={'token1': token_address}
    )
    
    event_data = []
    for event in events:
        event_data.append({
            'pair_address': event['args']['pair'],
            'token0': event['args']['token0'],
            'token1': event['args']['token1'],
            'block_number': event['blockNumber']
        })
    
    return jsonify(event_data)

@app.route('/pair_data/<token1_address>/<token2_address>/<int:n_blocks>')
def pair_data(token1_address, token2_address, n_blocks):
    pair_address = uniswap_factory.functions.getPair(token1_address, token2_address).call()
    
    if pair_address == '0x0000000000000000000000000000000000000000':
        return jsonify({'error': 'Pair does not exist'})
    
    current_block = w3.eth.block_number
    from_block = current_block - n_blocks
    
    pair_abi = [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"}]
    pair_contract = w3.eth.contract(address=pair_address, abi=pair_abi)
    
    events = pair_contract.events.Mint.get_logs(fromBlock=from_block, toBlock='latest') + \
             pair_contract.events.Burn.get_logs(fromBlock=from_block, toBlock='latest') + \
             pair_contract.events.Swap.get_logs(fromBlock=from_block, toBlock='latest')
    
    event_data = []
    for event in events:
        event_data.append({
            'event_type': event['event'],
            'block_number': event['blockNumber'],
            'transaction_hash': event['transactionHash'].hex(),
            'args': {k: v for k, v in event['args'].items() if k not in ('sender', 'to')}
        })
    
    return jsonify(event_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
