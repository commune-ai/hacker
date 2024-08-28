
import React, { useState } from 'react';
import { cryptoWaitReady, keyring } from '@polkadot/util-crypto';
import { u8aToHex } from '@polkadot/util';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    await cryptoWaitReady();
    
    // Generate sr25519 key from username and password
    const seed = username + password;
    const keyPair = keyring.createFromUri(seed, { type: 'sr25519' });
    const publicKey = u8aToHex(keyPair.publicKey);

    // Send publicKey to server for verification
    // You would typically use fetch or axios here
    console.log('Logging in with public key:', publicKey);
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;
