
FROM pytorch/pytorch:latest

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Set the entrypoint
ENTRYPOINT ["python", "finetuner.py"]
