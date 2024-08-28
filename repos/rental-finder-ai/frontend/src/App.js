
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [location, setLocation] = useState('');
  const [preferences, setPreferences] = useState('');
  const [results, setResults] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/search', { location, preferences });
      setResults(response.data);
    } catch (error) {
      console.error('Error fetching results:', error);
    }
  };

  return (
    <div className="App">
      <h1>Rental Finder AI</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Enter location"
          required
        />
        <textarea
          value={preferences}
          onChange={(e) => setPreferences(e.target.value)}
          placeholder="Enter your preferences"
          required
        />
        <button type="submit">Search</button>
      </form>
      {results && (
        <div>
          <h2>Results</h2>
          <p>{results.summary}</p>
          <ul>
            {results.listings.map((listing, index) => (
              <li key={index}>
                <a href={listing.link}>{listing.title}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
