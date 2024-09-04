
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    IERC20 public token;
    uint256 public constant DAILY_EMISSION = 1000 * 1e18; // 1000 tokens per day
    uint256 public constant EPOCH_DURATION = 1 days;

    struct Validator {
        uint256 stake;
        uint256 lastRewardTimestamp;
        bool isRegistered;
    }

    struct Miner {
        uint256 votes;
        uint256 lastRewardTimestamp;
    }

    mapping(address => Validator) public validators;
    mapping(address => Miner) public miners;
    address[] public validatorList;
    address[] public minerList;

    uint256 public totalStaked;
    uint256 public lastDistributionTimestamp;

    event ValidatorRegistered(address indexed validator);
    event MinerRegistered(address indexed miner);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);
    event Voted(address indexed voter, address indexed miner, uint256 amount);

    constructor(IERC20 _token) {
        token = _token;
        lastDistributionTimestamp = block.timestamp;
    }

    function registerValidator() external {
        require(!validators[msg.sender].isRegistered, "Already registered");
        validators[msg.sender].isRegistered = true;
        validatorList.push(msg.sender);
        emit ValidatorRegistered(msg.sender);
    }

    function registerMiner() external {
        require(miners[msg.sender].votes == 0, "Already registered");
        minerList.push(msg.sender);
        emit MinerRegistered(msg.sender);
    }

    function stake(uint256 amount) external nonReentrant {
        require(validators[msg.sender].isRegistered, "Not a registered validator");
        token.transferFrom(msg.sender, address(this), amount);
        validators[msg.sender].stake = validators[msg.sender].stake.add(amount);
        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(validators[msg.sender].stake >= amount, "Insufficient stake");
        validators[msg.sender].stake = validators[msg.sender].stake.sub(amount);
        totalStaked = totalStaked.sub(amount);
        token.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    function vote(address miner, uint256 amount) external {
        require(validators[msg.sender].isRegistered, "Not a registered validator");
        require(validators[msg.sender].stake >= amount, "Insufficient stake");
        miners[miner].votes = miners[miner].votes.add(amount);
        emit Voted(msg.sender, miner, amount);
    }

    function distributeRewards() external {
        require(block.timestamp >= lastDistributionTimestamp.add(EPOCH_DURATION), "Too early");
        
        uint256 validatorRewards = DAILY_EMISSION.div(2);
        uint256 minerRewards = DAILY_EMISSION.div(2);

        // Distribute to validators
        for (uint i = 0; i < validatorList.length; i++) {
            address validator = validatorList[i];
            uint256 validatorShare = validatorRewards.mul(validators[validator].stake).div(totalStaked);
            token.transfer(validator, validatorShare);
            validators[validator].lastRewardTimestamp = block.timestamp;
        }

        // Distribute to miners
        uint256 totalVotes = 0;
        for (uint i = 0; i < minerList.length; i++) {
            totalVotes = totalVotes.add(miners[minerList[i]].votes);
        }

        for (uint i = 0; i < minerList.length; i++) {
            address miner = minerList[i];
            uint256 minerShare = minerRewards.mul(miners[miner].votes).div(totalVotes);
            token.transfer(miner, minerShare);
            miners[miner].lastRewardTimestamp = block.timestamp;
        }

        lastDistributionTimestamp = block.timestamp;
        emit RewardsDistributed(DAILY_EMISSION);
    }
}
