
import Web3 from 'web3';

class RateLimiter {
  constructor(contractAddress, tokenAddress, web3Provider = 'http://localhost:8545') {
    this.web3 = new Web3(web3Provider);
    this.contract = new this.web3.eth.Contract(RateLimiter.abi, contractAddress);
    this.token = new this.web3.eth.Contract(ERC20_ABI, tokenAddress);
  }

  async checkRateLimit(userAddress) {
    return await this.contract.methods.checkRateLimit(userAddress).call();
  }

  async updateLastRequestTime(userAddress) {
    await this.contract.methods.updateLastRequestTime(userAddress).send({ from: userAddress });
  }

  async getTokenBalance(userAddress) {
    return await this.token.methods.balanceOf(userAddress).call();
  }
}

// Add ERC20_ABI and RateLimiter.abi here

export default RateLimiter;
