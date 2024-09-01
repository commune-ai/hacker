
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "./IYumaConsensus.sol";

contract YumaConsensus is IYumaConsensus {
    using SafeMath for uint256;

    IERC20 public stakingToken;
    uint256 public constant MIN_STAKE = 1000 * 10**18; // 1000 tokens
    uint256 public constant MAX_VALIDATORS = 100;
    uint256 public constant REWARD_POOL = 1000000 * 10**18; // 1,000,000 tokens
    uint256 public constant REWARD_PERIOD = 1 days;
    uint256 public lastRewardDistribution;

    mapping(address => uint256) public stakes;
    address[] public validators;
    uint256 public totalStake;

    event Staked(address indexed account, uint256 amount);
    event Unstaked(address indexed account, uint256 amount);
    event RewardsDistributed(uint256 totalReward);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        lastRewardDistribution = block.timestamp;
    }

    function stake(uint256 amount) external override {
        require(amount >= MIN_STAKE, "Stake amount too low");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStake = totalStake.add(amount);

        if (stakes[msg.sender] >= MIN_STAKE && !isValidator(msg.sender)) {
            validators.push(msg.sender);
        }

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external override {
        require(stakes[msg.sender] >= amount, "Insufficient stake");

        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        totalStake = totalStake.sub(amount);

        if (stakes[msg.sender] < MIN_STAKE) {
            removeValidator(msg.sender);
        }

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    function distributeRewards() external override {
        require(block.timestamp >= lastRewardDistribution.add(REWARD_PERIOD), "Too early for reward distribution");

        uint256 rewardPerStake = REWARD_POOL.div(totalStake);
        uint256 totalRewardDistributed = 0;

        for (uint256 i = 0; i < validators.length; i++) {
            address validator = validators[i];
            uint256 reward = stakes[validator].mul(rewardPerStake);

            // Anti-cabal mechanism: Cap rewards for large stakeholders
            if (stakes[validator] > totalStake.div(10)) {
                reward = reward.mul(9).div(10); // 10% penalty for large stakes
            }

            stakes[validator] = stakes[validator].add(reward);
            totalRewardDistributed = totalRewardDistributed.add(reward);
        }

        lastRewardDistribution = block.timestamp;
        emit RewardsDistributed(totalRewardDistributed);
    }

    function selectValidators() external view override returns (address[] memory) {
        return validators;
    }

    function getStake(address account) external view override returns (uint256) {
        return stakes[account];
    }

    function getTotalStake() external view override returns (uint256) {
        return totalStake;
    }

    function isValidator(address account) internal view returns (bool) {
        for (uint256 i = 0; i < validators.length; i++) {
            if (validators[i] == account) {
                return true;
            }
        }
        return false;
    }

    function removeValidator(address account) internal {
        for (uint256 i = 0; i < validators.length; i++) {
            if (validators[i] == account) {
                validators[i] = validators[validators.length - 1];
                validators.pop();
                break;
            }
        }
    }
}
