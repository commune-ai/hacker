
import React, { useState } from 'react';
import styled from 'styled-components';
import ChatWindow from './components/ChatWindow';
import FlavorSelector from './components/FlavorSelector';

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  font-family: Arial, sans-serif;
`;

const flavors = {
  default: {
    primary: '#4a90e2',
    secondary: '#f5f5f5',
    text: '#333333',
  },
  dark: {
    primary: '#2c3e50',
    secondary: '#34495e',
    text: '#ecf0f1',
  },
  pastel: {
    primary: '#ff9ff3',
    secondary: '#feca57',
    text: '#48dbfb',
  },
};

function App() {
  const [currentFlavor, setCurrentFlavor] = useState('default');

  return (
    <AppContainer>
      <FlavorSelector
        flavors={Object.keys(flavors)}
        currentFlavor={currentFlavor}
        onFlavorChange={setCurrentFlavor}
      />
      <ChatWindow theme={flavors[currentFlavor]} />
    </AppContainer>
  );
}

export default App;
