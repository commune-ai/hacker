
# Reflection-70B API

This repository contains a FastAPI application that hosts an API for stream generation using the mattshumer/Reflection-70B model.

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/reflection-70b-api.git
   cd reflection-70b-api
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `/generate`: POST request to generate text using the Reflection-70B model
- `/docs`: Swagger UI for API documentation

## Testing

To run the tests, use the following command:

```
pytest tests/
```

## License

This project is licensed under the MIT License.
