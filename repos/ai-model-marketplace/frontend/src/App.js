
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css';

function App() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [models, setModels] = useState([]);

  useEffect(() => {
    initWeb3();
    fetchModels();
  }, []);

  const initWeb3 = async () => {
    if (window.ethereum) {
      const web3Instance = new Web3(window.ethereum);
      try {
        await window.ethereum.enable();
        setWeb3(web3Instance);
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);
      } catch (error) {
        console.error("User denied account access");
      }
    }
  };

  const fetchModels = async () => {
    // Fetch available models from the backend
    // This is a placeholder and should be replaced with actual API call
    setModels([
      { id: 1, name: "Model A", price: "10 TOKEN" },
      { id: 2, name: "Model B", price: "20 TOKEN" },
    ]);
  };

  const callModel = async (modelId) => {
    if (!web3) {
      alert("Please connect your wallet first");
      return;
    }

    try {
      const signature = await web3.eth.personal.sign("Call Model " + modelId, account, "");
      const response = await fetch('/forward', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          signature,
          address: account,
          model_id: modelId,
        }),
      });

      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error("Error calling model:", error);
    }
  };

  return (
    <div className="App">
      <h1>AI Model Marketplace</h1>
      <p>Connected Account: {account || "Not connected"}</p>
      <h2>Available Models</h2>
      <ul>
        {models.map(model => (
          <li key={model.id}>
            {model.name} - {model.price}
            <button onClick={() => callModel(model.id)}>Call Model</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
