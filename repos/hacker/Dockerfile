
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Install frontend dependencies
WORKDIR /app/frontend
RUN npm install

# Build the React app
RUN npm run build

# Move back to the main directory
WORKDIR /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Make port 3000 available for the React app
EXPOSE 3000

# Run the command to start the Streamlit app and serve the React app
CMD streamlit run hacker/hacker.py & serve -s frontend/build -l 3000
