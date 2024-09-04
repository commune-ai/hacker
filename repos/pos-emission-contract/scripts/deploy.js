
const hre = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const Token = await hre.ethers.getContractFactory("Token");
  const token = await Token.deploy("Staking Token", "STK", ethers.utils.parseEther("1000000"));
  await token.deployed();
  console.log("Token deployed to:", token.address);

  const ValidatorRegistry = await hre.ethers.getContractFactory("ValidatorRegistry");
  const validatorRegistry = await ValidatorRegistry.deploy();
  await validatorRegistry.deployed();
  console.log("ValidatorRegistry deployed to:", validatorRegistry.address);

  const StakingContract = await hre.ethers.getContractFactory("StakingContract");
  const stakingContract = await StakingContract.deploy(token.address, validatorRegistry.address, ethers.utils.parseEther("1000"));
  await stakingContract.deployed();
  console.log("StakingContract deployed to:", stakingContract.address);

  // Transfer ownership of the token to the staking contract
  await token.transferOwnership(stakingContract.address);
  console.log("Token ownership transferred to StakingContract");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
