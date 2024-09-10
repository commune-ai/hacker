
import { useState } from 'react';
import { ethers } from 'ethers';

export default function Home() {
  const [amount, setAmount] = useState('');
  const [isUSDC, setIsUSDC] = useState(true);

  const handleExchange = async () => {
    if (!window.ethereum) {
      alert('Please install MetaMask!');
      return;
    }

    try {
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const address = await signer.getAddress();

      const response = await fetch('/api/exchange', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          amount: ethers.utils.parseUnits(amount, 18).toString(),
          isUSDC,
          userAddress: address,
        }),
      });

      const data = await response.json();
      if (data.success) {
        alert(`Transaction successful! Hash: ${data.transactionHash}`);
      } else {
        alert(`Error: ${data.error}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please check the console.');
    }
  };

  return (
    <div>
      <h1>ERC20 Token Exchange</h1>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Amount"
      />
      <select value={isUSDC} onChange={(e) => setIsUSDC(e.target.value === 'true')}>
        <option value={true}>USDC</option>
        <option value={false}>USDT</option>
      </select>
      <button onClick={handleExchange}>Exchange</button>
    </div>
  );
}
