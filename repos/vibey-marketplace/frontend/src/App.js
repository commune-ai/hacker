
import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';

const AppContainer = styled.div`
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
`;

const Title = styled.h1`
  color: #333;
  text-align: center;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
`;

const Input = styled.input`
  margin-bottom: 10px;
  padding: 5px;
`;

const Button = styled.button`
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
`;

const ResultsContainer = styled.div`
  margin-top: 20px;
`;

const ResultItem = styled.div`
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
`;

function App() {
  const [url, setUrl] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/websites', { url, title, description });
      alert('Website added successfully!');
      setUrl('');
      setTitle('');
      setDescription('');
    } catch (error) {
      alert('Error adding website. Please try again.');
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`http://localhost:8000/search?query=${searchQuery}`);
      setSearchResults(response.data);
    } catch (error) {
      alert('Error searching websites. Please try again.');
    }
  };

  return (
    <AppContainer>
      <Title>Vibey Marketplace</Title>
      <Form onSubmit={handleSubmit}>
        <Input
          type="text"
          placeholder="Website URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
        />
        <Input
          type="text"
          placeholder="Website Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <Input
          type="text"
          placeholder="Website Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <Button type="submit">Add Website</Button>
      </Form>
      <Form onSubmit={handleSearch}>
        <Input
          type="text"
          placeholder="Search websites"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          required
        />
        <Button type="submit">Search</Button>
      </Form>
      <ResultsContainer>
        {searchResults.map((result, index) => (
          <ResultItem key={index}>
            <h3>{result.title}</h3>
            <p>{result.description}</p>
            <a href={result.url} target="_blank" rel="noopener noreferrer">
              Visit Website
            </a>
          </ResultItem>
        ))}
      </ResultsContainer>
    </AppContainer>
  );
}

export default App;
