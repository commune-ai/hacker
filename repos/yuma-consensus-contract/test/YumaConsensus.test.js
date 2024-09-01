
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("YumaConsensus", function () {
  let YumaConsensus, yumaConsensus, owner, addr1, addr2, stakingToken;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();

    // Deploy a mock ERC20 token for staking
    const MockToken = await ethers.getContractFactory("MockERC20");
    stakingToken = await MockToken.deploy("Mock Token", "MTK");
    await stakingToken.deployed();

    YumaConsensus = await ethers.getContractFactory("YumaConsensus");
    yumaConsensus = await YumaConsensus.deploy(stakingToken.address);
    await yumaConsensus.deployed();

    // Mint some tokens for testing
    await stakingToken.mint(owner.address, ethers.utils.parseEther("1000000"));
    await stakingToken.mint(addr1.address, ethers.utils.parseEther("1000000"));
    await stakingToken.mint(addr2.address, ethers.utils.parseEther("1000000"));
  });

  it("Should allow staking and unstaking", async function () {
    const stakeAmount = ethers.utils.parseEther("1000");
    
    await stakingToken.approve(yumaConsensus.address, stakeAmount);
    await yumaConsensus.stake(stakeAmount);

    expect(await yumaConsensus.getStake(owner.address)).to.equal(stakeAmount);

    await yumaConsensus.unstake(stakeAmount);
    expect(await yumaConsensus.getStake(owner.address)).to.equal(0);
  });

  it("Should distribute rewards correctly", async function () {
    const stakeAmount = ethers.utils.parseEther("1000");
    
    await stakingToken.approve(yumaConsensus.address, stakeAmount);
    await yumaConsensus.stake(stakeAmount);

    await stakingToken.connect(addr1).approve(yumaConsensus.address, stakeAmount);
    await yumaConsensus.connect(addr1).stake(stakeAmount);

    // Fast forward time
    await ethers.provider.send("evm_increaseTime", [86400]); // 1 day
    await ethers.provider.send("evm_mine");

    await yumaConsensus.distributeRewards();

    const ownerStake = await yumaConsensus.getStake(owner.address);
    const addr1Stake = await yumaConsensus.getStake(addr1.address);

    expect(ownerStake).to.be.above(stakeAmount);
    expect(addr1Stake).to.be.above(stakeAmount);
    expect(ownerStake).to.equal(addr1Stake);
  });

  it("Should implement anti-cabal mechanism", async function () {
    const smallStake = ethers.utils.parseEther("1000");
    const largeStake = ethers.utils.parseEther("10000");
    
    await stakingToken.approve(yumaConsensus.address, largeStake);
    await yumaConsensus.stake(largeStake);

    await stakingToken.connect(addr1).approve(yumaConsensus.address, smallStake);
    await yumaConsensus.connect(addr1).stake(smallStake);

    // Fast forward time
    await ethers.provider.send("evm_increaseTime", [86400]); // 1 day
    await ethers.provider.send("evm_mine");

    await yumaConsensus.distributeRewards();

    const ownerStakeAfter = await yumaConsensus.getStake(owner.address);
    const addr1StakeAfter = await yumaConsensus.getStake(addr1.address);

    const ownerReward = ownerStakeAfter.sub(largeStake);
    const addr1Reward = addr1StakeAfter.sub(smallStake);

    // The large stakeholder should receive less reward per staked token
    expect(ownerReward.div(largeStake)).to.be.below(addr1Reward.div(smallStake));
  });
});

// Mock ERC20 token for testing
contract MockERC20 {
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function mint(address to, uint256 amount) public {
        totalSupply += amount;
        balanceOf[to] += amount;
        emit Transfer(address(0), to, amount);
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowance[sender][msg.sender] >= amount, "ERC20: transfer amount exceeds allowance");
        allowance[sender][msg.sender] -= amount;
        balanceOf[sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
}
