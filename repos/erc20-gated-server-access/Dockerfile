
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend requirements file into the container
COPY backend/requirements.txt .

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY backend/ .

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Copy the frontend package.json file
COPY frontend/package.json frontend/

# Install frontend dependencies
RUN cd frontend && npm install

# Copy the frontend code into the container
COPY frontend/ frontend/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Make port 3000 available for the React development server
EXPOSE 3000

# Run the backend and frontend when the container launches
CMD ["sh", "-c", "python app.py & cd frontend && npm start"]
