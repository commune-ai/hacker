
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "./ValidatorRegistry.sol";

contract StakingContract is Ownable, ReentrancyGuard {
    IERC20 public token;
    ValidatorRegistry public validatorRegistry;

    uint256 public dailyEmission;
    uint256 public lastDistributionTime;
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;
        uint256 lastRewardTime;
    }

    mapping(address => Stake) public stakes;
    mapping(address => mapping(address => uint256)) public delegatedStakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 amount);
    event DelegatedStake(address indexed delegator, address indexed validator, uint256 amount);
    event UndelegatedStake(address indexed delegator, address indexed validator, uint256 amount);

    constructor(IERC20 _token, ValidatorRegistry _validatorRegistry, uint256 _dailyEmission) {
        token = _token;
        validatorRegistry = _validatorRegistry;
        dailyEmission = _dailyEmission;
        lastDistributionTime = block.timestamp;
    }

    function setDailyEmission(uint256 _dailyEmission) external onlyOwner {
        dailyEmission = _dailyEmission;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        distributeRewards();
        token.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender].amount += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        distributeRewards();
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        token.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    function delegateStake(address validator, uint256 amount) external nonReentrant {
        require(validatorRegistry.isValidator(validator), "Not a registered validator");
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        distributeRewards();
        stakes[msg.sender].amount -= amount;
        delegatedStakes[msg.sender][validator] += amount;
        emit DelegatedStake(msg.sender, validator, amount);
    }

    function undelegateStake(address validator, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(delegatedStakes[msg.sender][validator] >= amount, "Insufficient delegated stake");
        distributeRewards();
        delegatedStakes[msg.sender][validator] -= amount;
        stakes[msg.sender].amount += amount;
        emit UndelegatedStake(msg.sender, validator, amount);
    }

    function distributeRewards() public {
        uint256 timePassed = block.timestamp - lastDistributionTime;
        if (timePassed >= 1 days) {
            uint256 emissionAmount = (dailyEmission * timePassed) / 1 days;
            if (totalStaked > 0) {
                for (uint256 i = 0; i < validatorRegistry.getValidatorCount(); i++) {
                    address validator = validatorRegistry.validators(i);
                    uint256 validatorStake = stakes[validator].amount;
                    for (uint256 j = 0; j < validatorRegistry.getValidatorCount(); j++) {
                        address delegator = validatorRegistry.validators(j);
                        validatorStake += delegatedStakes[delegator][validator];
                    }
                    uint256 reward = (emissionAmount * validatorStake) / totalStaked;
                    stakes[validator].amount += reward;
                    emit RewardDistributed(validator, reward);
                }
            }
            lastDistributionTime = block.timestamp;
        }
    }

    function getStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    function getDelegatedStake(address delegator, address validator) external view returns (uint256) {
        return delegatedStakes[delegator][validator];
    }
}
