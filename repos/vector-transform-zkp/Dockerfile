
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    nodejs \
    npm

# Install Python dependencies
RUN pip install numpy ezkl

# Install Truffle
RUN npm install -g truffle

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install project dependencies
RUN npm install

CMD ["/bin/bash"]
