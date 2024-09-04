
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract YumaConsensusPoS is ERC20, Ownable {
    using ECDSA for bytes32;

    struct Miner {
        address addr;
        uint256 stake;
        uint256 lastReward;
    }

    struct Validator {
        address addr;
        uint256 stake;
        uint256 lastDividend;
    }

    struct SubnetParams {
        uint256 minerRewardRate;
        uint256 validatorDividendRate;
        uint256 minStake;
    }

    mapping(address => Miner) public miners;
    mapping(address => Validator) public validators;
    mapping(address => bool) public blacklistedMiners;

    address[] public minerAddresses;
    address[] public validatorAddresses;

    SubnetParams public params;
    address public consensusMechanism;

    event MinerAdded(address indexed miner, uint256 stake);
    event ValidatorAdded(address indexed validator, uint256 stake);
    event MinerRewarded(address indexed miner, uint256 amount);
    event ValidatorDividend(address indexed validator, uint256 amount);
    event ConsensusUpdated(address indexed newConsensus);
    event MinerBlacklisted(address indexed miner);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        params = SubnetParams({
            minerRewardRate: 100,
            validatorDividendRate: 10,
            minStake: 1000 * 10**18
        });
    }

    function addMiner(uint256 stake) external {
        require(stake >= params.minStake, "Insufficient stake");
        require(miners[msg.sender].addr == address(0), "Miner already exists");

        _transfer(msg.sender, address(this), stake);
        miners[msg.sender] = Miner({
            addr: msg.sender,
            stake: stake,
            lastReward: block.timestamp
        });
        minerAddresses.push(msg.sender);

        emit MinerAdded(msg.sender, stake);
    }

    function addValidator(uint256 stake) external {
        require(stake >= params.minStake, "Insufficient stake");
        require(validators[msg.sender].addr == address(0), "Validator already exists");

        _transfer(msg.sender, address(this), stake);
        validators[msg.sender] = Validator({
            addr: msg.sender,
            stake: stake,
            lastDividend: block.timestamp
        });
        validatorAddresses.push(msg.sender);

        emit ValidatorAdded(msg.sender, stake);
    }

    function submitWork(bytes32 workHash, bytes memory signature) external {
        require(!blacklistedMiners[msg.sender], "Miner is blacklisted");
        require(miners[msg.sender].addr != address(0), "Not a registered miner");

        address signer = workHash.toEthSignedMessageHash().recover(signature);
        require(signer == consensusMechanism, "Invalid consensus signature");

        uint256 reward = calculateMinerReward(msg.sender);
        _mint(msg.sender, reward);
        miners[msg.sender].lastReward = block.timestamp;

        emit MinerRewarded(msg.sender, reward);
    }

    function distributeValidatorDividends() external {
        for (uint i = 0; i < validatorAddresses.length; i++) {
            address validatorAddr = validatorAddresses[i];
            uint256 dividend = calculateValidatorDividend(validatorAddr);
            if (dividend > 0) {
                _mint(validatorAddr, dividend);
                validators[validatorAddr].lastDividend = block.timestamp;
                emit ValidatorDividend(validatorAddr, dividend);
            }
        }
    }

    function calculateMinerReward(address miner) internal view returns (uint256) {
        uint256 timeSinceLastReward = block.timestamp - miners[miner].lastReward;
        return (miners[miner].stake * params.minerRewardRate * timeSinceLastReward) / (1 days * 100);
    }

    function calculateValidatorDividend(address validator) internal view returns (uint256) {
        uint256 timeSinceLastDividend = block.timestamp - validators[validator].lastDividend;
        return (validators[validator].stake * params.validatorDividendRate * timeSinceLastDividend) / (1 days * 100);
    }

    function updateConsensus(address newConsensus) external onlyOwner {
        consensusMechanism = newConsensus;
        emit ConsensusUpdated(newConsensus);
    }

    function blacklistMiner(address miner) external onlyOwner {
        blacklistedMiners[miner] = true;
        emit MinerBlacklisted(miner);
    }

    function updateSubnetParams(
        uint256 newMinerRewardRate,
        uint256 newValidatorDividendRate,
        uint256 newMinStake
    ) external onlyOwner {
        params.minerRewardRate = newMinerRewardRate;
        params.validatorDividendRate = newValidatorDividendRate;
        params.minStake = newMinStake;
    }
}
