
import React, { useState } from 'react';
import axios from 'axios';

function AddServer() {
  const [name, setName] = useState('');
  const [url, setUrl] = useState('');
  const [ethereumKey, setEthereumKey] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/api/servers', { name, url, ethereumKey });
      alert('Server added successfully!');
      setName('');
      setUrl('');
      setEthereumKey('');
    } catch (error) {
      console.error('Error adding server:', error);
      alert('Failed to add server.');
    }
  };

  return (
    <div>
      <h2>Add RPC Server</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Server Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="url"
          placeholder="Server URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Ethereum Key"
          value={ethereumKey}
          onChange={(e) => setEthereumKey(e.target.value)}
          required
        />
        <button type="submit">Add Server</button>
      </form>
    </div>
  );
}

export default AddServer;
