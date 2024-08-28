
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Servers() {
  const [servers, setServers] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/servers')
      .then(response => setServers(response.data))
      .catch(error => console.error('Error fetching servers:', error));
  }, []);

  return (
    <div>
      <h2>RPC Servers</h2>
      <ul>
        {servers.map(server => (
          <li key={server.id}>{server.name} - {server.url}</li>
        ))}
      </ul>
    </div>
  );
}

export default Servers;
