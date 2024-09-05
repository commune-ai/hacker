
# Flavor Chat App

This is a frontend chat application that allows users to choose different flavors for their chat experience.

## Features

- Real-time chat functionality
- Multiple flavor themes to choose from
- Responsive design for desktop and mobile

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- Docker

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flavor-chat-app.git
   cd flavor-chat-app
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the application:
   ```
   ./scripts/run.sh
   ```

4. Open your browser and navigate to `http://localhost:3000`

## Running Tests

To run the tests, use the following command:

```
docker exec -it flavor-chat-app npm test
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
