
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RateLimiter {
    IERC20 public token;
    mapping(address => uint256) public lastRequestTime;
    uint256 public constant RATE_LIMIT_PERIOD = 1 minutes;
    uint256 public constant MIN_TOKEN_BALANCE = 100 * 10**18; // 100 tokens

    constructor(address _token) {
        token = IERC20(_token);
    }

    function checkRateLimit(address user) public view returns (bool) {
        require(token.balanceOf(user) >= MIN_TOKEN_BALANCE, "Insufficient token balance");
        return (block.timestamp - lastRequestTime[user]) >= RATE_LIMIT_PERIOD;
    }

    function updateLastRequestTime(address user) public {
        require(checkRateLimit(user), "Rate limit exceeded");
        lastRequestTime[user] = block.timestamp;
    }
}
