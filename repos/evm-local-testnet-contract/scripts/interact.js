
const hre = require("hardhat");

async function main() {
  const SimpleStorage = await hre.ethers.getContractFactory("SimpleStorage");
  const simpleStorage = await SimpleStorage.attach("CONTRACT_ADDRESS"); // Replace with the deployed contract address

  // Set a value
  await simpleStorage.set(42);
  console.log("Value set to 42");

  // Get the value
  const value = await simpleStorage.get();
  console.log("Retrieved value:", value.toString());
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
