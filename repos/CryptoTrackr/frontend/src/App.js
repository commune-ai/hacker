
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Connection, PublicKey } from '@solana/web3.js';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import AdminDashboard from './components/AdminDashboard';

function App() {
  const [user, setUser] = useState(null);
  const [isAdmin, setIsAdmin] = useState(false);
  const [web3, setWeb3] = useState(null);
  const [solanaConnection, setSolanaConnection] = useState(null);

  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
      }
    };

    const initSolana = async () => {
      const connection = new Connection('https://api.mainnet-beta.solana.com');
      setSolanaConnection(connection);
    };

    initWeb3();
    initSolana();
  }, []);

  const handleLogin = async (wallet) => {
    // Implement login logic here
    // Set user and check if admin
    setUser({ address: wallet });
    setIsAdmin(wallet === 'ADMIN_ADDRESS');
  };

  return (
    <div className="App">
      {!user ? (
        <Login onLogin={handleLogin} />
      ) : isAdmin ? (
        <AdminDashboard web3={web3} solanaConnection={solanaConnection} />
      ) : (
        <Dashboard user={user} web3={web3} solanaConnection={solanaConnection} />
      )}
    </div>
  );
}

export default App;
