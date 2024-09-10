
import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Home() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    fetchAccounts();
  }, []);

  const fetchAccounts = async () => {
    try {
      const response = await axios.get('http://localhost:8000/accounts');
      setAccounts(response.data);
    } catch (error) {
      console.error('Error fetching accounts:', error);
    }
  };

  return (
    <div>
      <h1>USDT Tracker</h1>
      <table>
        <thead>
          <tr>
            <th>Account ID</th>
            <th>USDT Amount</th>
          </tr>
        </thead>
        <tbody>
          {accounts.map((account) => (
            <tr key={account.id}>
              <td>{account.id}</td>
              <td>{account.usdt_amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
