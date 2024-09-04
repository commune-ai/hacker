
const hre = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const POSToken = await hre.ethers.getContractFactory("POSToken");
  const posToken = await POSToken.deploy(ethers.utils.parseEther("1000000")); // 1 million initial supply

  await posToken.deployed();

  console.log("POSToken deployed to:", posToken.address);

  const StakingContract = await hre.ethers.getContractFactory("StakingContract");
  const stakingContract = await StakingContract.deploy(posToken.address);

  await stakingContract.deployed();

  console.log("StakingContract deployed to:", stakingContract.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
