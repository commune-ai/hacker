
# Hugging Face Model Fine-tuner

This repository contains a script for fine-tuning any Hugging Face model. It provides a flexible and easy-to-use solution for adapting pre-trained models to specific tasks or datasets.

## Features

- Fine-tune any Hugging Face model
- Support for custom datasets
- Configurable training parameters
- Docker support for easy setup and execution

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/huggingface_finetuner.git
   cd huggingface_finetuner
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

## Usage

To fine-tune a model, use the `finetuner.py` script:

```
python finetuner.py --model_name <model_name> --dataset_name <dataset_name> --output_dir <output_directory>
```

For more options and details, refer to the script's help:

```
python finetuner.py --help
```

## Testing

To run the tests, execute:

```
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
