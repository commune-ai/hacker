
# Repo Finetuner

This project provides a finetuning script for Hugging Face models, allowing you to finetune models on your own repository of text data. It includes a simple frontend for managing tasks and a Python backend.

## Features

- Finetune any Hugging Face model on custom text data
- Simple web interface for managing finetuning tasks
- Docker support for easy deployment

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/repo_finetuner.git
   cd repo_finetuner
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the application:
   ```
   ./scripts/run.sh
   ```

4. Access the web interface at `http://localhost:5000`

## Usage

1. Upload your text data to the `/data` directory.
2. Use the web interface to select a Hugging Face model and start the finetuning process.
3. Monitor the progress and view results through the web interface.

## Testing

Run the tests using:
```
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
