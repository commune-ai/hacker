
# GitHub Issue Agent

This project implements a simple agent framework that automatically submits issues to GitHub repositories. It uses the GitHub API to create and manage issues based on predefined criteria or external triggers.

## Features

- Authenticate with GitHub using personal access tokens
- Create new issues with customizable title, body, and labels
- List existing issues in a repository
- Update and close issues

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/github-issue-agent.git
   cd github-issue-agent
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your GitHub personal access token:
   - Create a new token at https://github.com/settings/tokens
   - Set the token as an environment variable:
     ```
     export GITHUB_TOKEN=your_token_here
     ```

## Usage

To run the agent:

```
python src/main.py
```

## Docker

To build and run the project using Docker:

1. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

2. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
