
import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const response = await fetch('http://localhost:8000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });
    const data = await response.json();
    setResults(data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>GitHub Semantic Finder</h1>
        <div className="search-container">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter your search query"
          />
          <button onClick={handleSearch}>Search</button>
        </div>
      </header>
      <main>
        <ul className="results-list">
          {results.map((result, index) => (
            <li key={index} className="result-item">
              <h3>{result.name}</h3>
              <p>{result.description}</p>
              <a href={result.url} target="_blank" rel="noopener noreferrer">
                View on GitHub
              </a>
            </li>
          ))}
        </ul>
      </main>
    </div>
  );
}

export default App;
