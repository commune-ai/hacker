
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Connection, PublicKey } from '@solana/web3.js';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';

function App() {
  const [walletAddress, setWalletAddress] = useState(null);
  const [btcAmount, setBtcAmount] = useState('');
  const [usdtAmount, setUsdtAmount] = useState('');

  const connectWallet = async () => {
    const { solana } = window;

    if (solana) {
      try {
        const response = await solana.connect();
        setWalletAddress(response.publicKey.toString());
      } catch (err) {
        console.error(err);
      }
    }
  };

  const disconnectWallet = () => {
    const { solana } = window;
    if (solana) {
      solana.disconnect();
      setWalletAddress(null);
    }
  };

  const swapBtcForUsdt = async () => {
    if (!walletAddress || !btcAmount) {
      alert('Please connect your wallet and enter a BTC amount');
      return;
    }

    try {
      const response = await axios.post('http://localhost:5000/swap', {
        walletAddress,
        btcAmount
      });
      setUsdtAmount(response.data.usdtAmount);
    } catch (err) {
      console.error(err);
      alert('Error occurred during swap');
    }
  };

  useEffect(() => {
    const checkIfWalletIsConnected = async () => {
      const { solana } = window;

      if (solana) {
        if (solana.isPhantom) {
          console.log('Phantom wallet found!');
          const response = await solana.connect({ onlyIfTrusted: true });
          setWalletAddress(response.publicKey.toString());
        }
      } else {
        alert('Solana object not found! Get a Phantom Wallet 👻');
      }
    };

    checkIfWalletIsConnected();
  }, []);

  return (
    <div className="App">
      <h1>Phantom BTC-USDT Swap</h1>
      {!walletAddress ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      )}
      <div>
        <input
          type="number"
          value={btcAmount}
          onChange={(e) => setBtcAmount(e.target.value)}
          placeholder="Enter BTC amount"
        />
        <button onClick={swapBtcForUsdt}>Swap BTC for USDT</button>
      </div>
      {usdtAmount && <p>USDT Amount: {usdtAmount}</p>}
    </div>
  );
}

export default App;
