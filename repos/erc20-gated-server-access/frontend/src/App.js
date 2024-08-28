
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ethers } from 'ethers';

function App() {
  const [servers, setServers] = useState([]);
  const [address, setAddress] = useState('');
  const [isAdmin, setIsAdmin] = useState(false);
  const [newServer, setNewServer] = useState('');

  useEffect(() => {
    connectWallet();
  }, []);

  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAddress(address);
        fetchServers(address);
      } catch (error) {
        console.error("Failed to connect wallet:", error);
      }
    } else {
      console.log("Please install MetaMask!");
    }
  };

  const fetchServers = async (address) => {
    try {
      const response = await axios.get(`http://localhost:5000/api/servers?address=${address}`);
      setServers(response.data);
    } catch (error) {
      console.error("Failed to fetch servers:", error);
    }
  };

  const becomeAdmin = async () => {
    try {
      await axios.post('http://localhost:5000/api/admin', { address });
      setIsAdmin(true);
    } catch (error) {
      console.error("Failed to become admin:", error);
    }
  };

  const addServer = async () => {
    try {
      await axios.post('http://localhost:5000/api/servers', { address, server: newServer });
      fetchServers(address);
      setNewServer('');
    } catch (error) {
      console.error("Failed to add server:", error);
    }
  };

  const removeServer = async (index) => {
    try {
      await axios.delete(`http://localhost:5000/api/servers/${index}`, { data: { address } });
      fetchServers(address);
    } catch (error) {
      console.error("Failed to remove server:", error);
    }
  };

  return (
    <div className="App">
      <h1>ERC20 Gated Server Access</h1>
      {address ? (
        <>
          <p>Connected Address: {address}</p>
          <button onClick={becomeAdmin}>Become Admin</button>
          <h2>Servers:</h2>
          <ul>
            {servers.map((server, index) => (
              <li key={index}>
                {server}
                {isAdmin && <button onClick={() => removeServer(index)}>Remove</button>}
              </li>
            ))}
          </ul>
          {isAdmin && (
            <div>
              <input
                type="text"
                value={newServer}
                onChange={(e) => setNewServer(e.target.value)}
                placeholder="New server URL"
              />
              <button onClick={addServer}>Add Server</button>
            </div>
          )}
        </>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}

export default App;
