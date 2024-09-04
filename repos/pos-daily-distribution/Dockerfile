
# Use an official Node runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any needed packages
RUN npm install

# Copy the current directory contents into the container
COPY . .

# Make port 8545 available to the world outside this container
EXPOSE 8545

# Run the app when the container launches
CMD ["npx", "hardhat", "node"]
