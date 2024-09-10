
import { useState, useEffect } from 'react';
import Web3 from 'web3';
import RateLimiter from '../client/rate_limiter';

export default function Home() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [rateLimiter, setRateLimiter] = useState(null);

  useEffect(() => {
    async function init() {
      if (typeof window.ethereum !== 'undefined') {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        try {
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);

          const rateLimiterInstance = new RateLimiter('CONTRACT_ADDRESS', 'TOKEN_ADDRESS');
          setRateLimiter(rateLimiterInstance);
        } catch (error) {
          console.error("User denied account access");
        }
      }
    }

    init();
  }, []);

  const checkRateLimit = async () => {
    if (rateLimiter && account) {
      const canMakeRequest = await rateLimiter.checkRateLimit(account);
      console.log("Can make request:", canMakeRequest);
    }
  };

  return (
    <div>
      <h1>ERC20 Rate Limiter Demo</h1>
      <p>Account: {account}</p>
      <button onClick={checkRateLimit}>Check Rate Limit</button>
    </div>
  );
}
