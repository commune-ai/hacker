
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IYumaConsensus {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function distributeRewards() external;
    function selectValidators() external view returns (address[] memory);
    function getStake(address account) external view returns (uint256);
    function getTotalStake() external view returns (uint256);
}
