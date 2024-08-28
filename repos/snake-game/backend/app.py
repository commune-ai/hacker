
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

class SnakeGame:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.snake = [(10, 10)]
        self.direction = 'RIGHT'
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def move(self):
        head = self.snake[0]
        if self.direction == 'UP':
            new_head = (head[0], (head[1] - 1) % self.height)
        elif self.direction == 'DOWN':
            new_head = (head[0], (head[1] + 1) % self.height)
        elif self.direction == 'LEFT':
            new_head = ((head[0] - 1) % self.width, head[1])
        else:  # RIGHT
            new_head = ((head[0] + 1) % self.width, head[1])

        if new_head in self.snake:
            return False  # Game over

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()

        return True

game = SnakeGame()

@app.route('/api/start', methods=['POST'])
def start_game():
    global game
    game = SnakeGame()
    return jsonify(game.__dict__)

@app.route('/api/move', methods=['POST'])
def move():
    direction = request.json['direction']
    game.direction = direction
    if game.move():
        return jsonify(game.__dict__)
    else:
        return jsonify({'game_over': True, 'score': game.score})

if __name__ == '__main__':
    app.run(debug=True)
