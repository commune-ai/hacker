
FROM python:3.9

# Install Node.js and npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy package.json and install Node.js dependencies
COPY package.json .
RUN npm install

# Copy the rest of the application
COPY . .

# Expose ports
EXPOSE 3000 8545

# Start the application
CMD ["./scripts/start.sh"]
