
# Agent Build

This repository contains a simple agent build system using Docker. The project structure includes a Python script for the agent, a Dockerfile for creating the environment, and shell scripts for building and running the Docker container.

## Project Structure

```
agent_build/
│
├── src/
│   └── agent.py
│
├── scripts/
│   ├── build.sh
│   └── run.sh
│
├── Dockerfile
└── README.md
```

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/agent_build.git
   cd agent_build
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the agent in a Docker container:
   ```
   ./scripts/run.sh
   ```

## License

This project is licensed under the MIT License.
