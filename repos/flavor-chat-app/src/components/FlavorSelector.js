
import React from 'react';
import styled from 'styled-components';

const SelectorContainer = styled.div`
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: #f0f0f0;
`;

const FlavorButton = styled.button`
  margin: 0 10px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: ${props => props.active ? '#4a90e2' : '#ffffff'};
  color: ${props => props.active ? '#ffffff' : '#333333'};
  border: 1px solid #4a90e2;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background-color: #4a90e2;
    color: #ffffff;
  }
`;

function FlavorSelector({ flavors, currentFlavor, onFlavorChange }) {
  return (
    <SelectorContainer>
      {flavors.map(flavor => (
        <FlavorButton
          key={flavor}
          active={currentFlavor === flavor}
          onClick={() => onFlavorChange(flavor)}
        >
          {flavor}
        </FlavorButton>
      ))}
    </SelectorContainer>
  );
}

export default FlavorSelector;
