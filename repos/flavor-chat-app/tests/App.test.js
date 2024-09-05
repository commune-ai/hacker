
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../src/App';

test('renders flavor selector', () => {
  render(<App />);
  const defaultButton = screen.getByText(/default/i);
  expect(defaultButton).toBeInTheDocument();
});

test('renders chat window', () => {
  render(<App />);
  const inputElement = screen.getByPlaceholderText(/Type a message.../i);
  expect(inputElement).toBeInTheDocument();
});
