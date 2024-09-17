
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RollupVerifier {
    struct Rollup {
        uint256 totalCost;
        bytes32 transactionsRoot;
    }
    
    mapping(uint256 => Rollup) public rollups;
    uint256 public currentRollupId;
    
    event RollupSubmitted(uint256 indexed rollupId, uint256 totalCost, bytes32 transactionsRoot);
    
    function submitRollup(uint256 _totalCost, bytes32 _transactionsRoot) external {
        currentRollupId++;
        rollups[currentRollupId] = Rollup(_totalCost, _transactionsRoot);
        emit RollupSubmitted(currentRollupId, _totalCost, _transactionsRoot);
    }
    
    function verifyRollup(uint256 _rollupId, uint256 _totalCost, bytes32 _transactionsRoot) external view returns (bool) {
        Rollup memory rollup = rollups[_rollupId];
        return (rollup.totalCost == _totalCost && rollup.transactionsRoot == _transactionsRoot);
    }
}
