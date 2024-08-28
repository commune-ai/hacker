
import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import './App.css';

const CELL_SIZE = 20;
const WIDTH = 400;
const HEIGHT = 400;

function App() {
  const [game, setGame] = useState(null);
  const [gameOver, setGameOver] = useState(false);

  const startGame = useCallback(async () => {
    const response = await axios.post('http://localhost:5000/api/start');
    setGame(response.data);
    setGameOver(false);
  }, []);

  const move = useCallback(async (direction) => {
    if (!game || gameOver) return;

    try {
      const response = await axios.post('http://localhost:5000/api/move', { direction });
      if (response.data.game_over) {
        setGameOver(true);
      } else {
        setGame(response.data);
      }
    } catch (error) {
      console.error('Error moving:', error);
    }
  }, [game, gameOver]);

  useEffect(() => {
    const handleKeyPress = (e) => {
      switch (e.key) {
        case 'ArrowUp':
          move('UP');
          break;
        case 'ArrowDown':
          move('DOWN');
          break;
        case 'ArrowLeft':
          move('LEFT');
          break;
        case 'ArrowRight':
          move('RIGHT');
          break;
        default:
          break;
      }
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => {
      window.removeEventListener('keydown', handleKeyPress);
    };
  }, [move]);

  useEffect(() => {
    startGame();
  }, [startGame]);

  const drawGame = () => {
    if (!game) return null;

    return (
      <svg width={WIDTH} height={HEIGHT}>
        {game.snake.map((segment, index) => (
          <rect
            key={index}
            x={segment[0] * CELL_SIZE}
            y={segment[1] * CELL_SIZE}
            width={CELL_SIZE}
            height={CELL_SIZE}
            fill="green"
          />
        ))}
        <rect
          x={game.food[0] * CELL_SIZE}
          y={game.food[1] * CELL_SIZE}
          width={CELL_SIZE}
          height={CELL_SIZE}
          fill="red"
        />
      </svg>
    );
  };

  return (
    <div className="App">
      <h1>Snake Game</h1>
      <div className="game-container">{drawGame()}</div>
      <p>Score: {game ? game.score : 0}</p>
      {gameOver && <p>Game Over!</p>}
      <button onClick={startGame}>New Game</button>
    </div>
  );
}

export default App;
