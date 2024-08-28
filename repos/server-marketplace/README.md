
# Server Marketplace

This project is a marketplace for servers where users can upload and browse server listings. The login system uses a username and password that converts to a Polkadot sr25519 key, with client-side verification and no server-side password storage.

## Features

- User registration and login
- Server listing creation and browsing
- Client-side password verification using Polkadot sr25519 keys
- Docker-based deployment

## Setup

1. Clone the repository
2. Install Docker and Docker Compose
3. Run `./scripts/build.sh` to build the Docker images
4. Run `./scripts/run.sh` to start the application

## Technologies Used

- Frontend: React, Polkadot.js
- Backend: Node.js, Express
- Database: MongoDB
- Containerization: Docker

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
