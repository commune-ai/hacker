
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ModelToken is ERC20, Ownable {
    mapping(address => mapping(uint256 => uint256)) public modelUsage;
    mapping(uint256 => uint256) public modelPrices;

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, 1000000 * 10**decimals());
    }

    function setModelPrice(uint256 modelId, uint256 price) external onlyOwner {
        modelPrices[modelId] = price;
    }

    function useModel(uint256 modelId) external {
        require(modelPrices[modelId] > 0, "Model price not set");
        require(balanceOf(msg.sender) >= modelPrices[modelId], "Insufficient balance");

        _transfer(msg.sender, owner(), modelPrices[modelId]);
        modelUsage[msg.sender][modelId]++;
    }

    function getModelUsage(address user, uint256 modelId) external view returns (uint256) {
        return modelUsage[user][modelId];
    }
}
