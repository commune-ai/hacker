
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StakingContract {
    mapping(address => uint256) public stakes;
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Slashed(address indexed user, uint256 amount);

    function stake() public payable {
        require(msg.value > 0, "Stake amount must be greater than 0");
        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;
        emit Staked(msg.sender, msg.value);
    }

    function unstake(uint256 amount) public {
        require(stakes[msg.sender] >= amount, "Insufficient stake");
        stakes[msg.sender] -= amount;
        totalStaked -= amount;
        payable(msg.sender).transfer(amount);
        emit Unstaked(msg.sender, amount);
    }

    function slash(address user, uint256 amount) public {
        // TODO: Implement access control
        require(stakes[user] >= amount, "Insufficient stake to slash");
        stakes[user] -= amount;
        totalStaked -= amount;
        emit Slashed(user, amount);
    }

    function getStake(address user) public view returns (uint256) {
        return stakes[user];
    }
}
