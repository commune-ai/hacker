
# Event Finder AI

This project uses an OpenAI model to search the web for events near you. It provides a backend API that can be used to find and return relevant event information based on your location and preferences.

## Features

- Utilizes OpenAI's GPT model for natural language processing
- Searches the web for up-to-date event information
- Provides a simple API for querying events

## Setup

1. Clone this repository
2. Install Docker and Docker Compose
3. Copy `.env.example` to `.env` and fill in your OpenAI API key
4. Run `./scripts/build.sh` to build the Docker image
5. Run `./scripts/run.sh` to start the server

## Usage

Send a POST request to `http://localhost:5000/find_events` with a JSON body:

```json
{
  "location": "New York, NY",
  "preferences": "music concerts, art exhibitions"
}
```

The API will return a list of events matching your criteria.

## License

MIT
