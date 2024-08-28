
# Unisap Data Scraper

This project scrapes data from Unisap without using an API. It uses Python and BeautifulSoup to extract information from the Unisap website.

## Requirements

- Python 3.8+
- Docker (optional, for containerized execution)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/unisap_scraper.git
   cd unisap_scraper
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the scraper:

```
python src/scraper.py
```

## Docker

To build and run the scraper using Docker:

1. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

2. Run the scraper in a Docker container:
   ```
   ./scripts/run.sh
   ```

## Output

The scraped data will be saved in the `output` directory as CSV files.

## Disclaimer

Please ensure you have permission to scrape data from Unisap and comply with their terms of service and robots.txt file.
