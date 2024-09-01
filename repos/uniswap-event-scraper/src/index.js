
const express = require('express');
const Web3 = require('web3');
const UniswapV2Pair = require('@uniswap/v2-core/build/UniswapV2Pair.json');

const app = express();
const port = 3000;

const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

app.get('/scrape', async (req, res) => {
  const { token0, token1, blocks = 1000 } = req.query;

  if (!token0 || !token1) {
    return res.status(400).json({ error: 'Both token0 and token1 addresses are required' });
  }

  try {
    const pairAddress = await getPairAddress(token0, token1);
    const events = await scrapeEvents(pairAddress, blocks);
    res.json(events);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

async function getPairAddress(token0, token1) {
  // Implementation to get the pair address from Uniswap factory
  // This is a placeholder and needs to be implemented
  return '0x...'; // Return the actual pair address
}

async function scrapeEvents(pairAddress, blocks) {
  const pair = new web3.eth.Contract(UniswapV2Pair.abi, pairAddress);
  const latestBlock = await web3.eth.getBlockNumber();
  const fromBlock = latestBlock - blocks;

  const events = await pair.getPastEvents('allEvents', {
    fromBlock,
    toBlock: 'latest'
  });

  return events.map(event => ({
    event: event.event,
    blockNumber: event.blockNumber,
    transactionHash: event.transactionHash,
    returnValues: event.returnValues
  }));
}

app.listen(port, () => {
  console.log(`Uniswap Event Scraper listening at http://localhost:${port}`);
});
