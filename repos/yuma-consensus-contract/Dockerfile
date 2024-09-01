
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

# Compile the smart contract
RUN npx hardhat compile

# Run tests by default
CMD ["npx", "hardhat", "test"]
