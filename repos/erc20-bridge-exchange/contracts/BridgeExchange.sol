
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BridgeExchange is Ownable {
    IERC20 public usdcToken;
    IERC20 public usdtToken;
    IERC20 public erc20Token;

    uint256 public exchangeRate;

    event TokensExchanged(address indexed user, uint256 amount, bool isUSDC);

    constructor(address _usdcToken, address _usdtToken, address _erc20Token, uint256 _exchangeRate) {
        usdcToken = IERC20(_usdcToken);
        usdtToken = IERC20(_usdtToken);
        erc20Token = IERC20(_erc20Token);
        exchangeRate = _exchangeRate;
    }

    function exchangeTokens(uint256 amount, bool isUSDC) external {
        require(amount > 0, "Amount must be greater than 0");

        IERC20 stablecoin = isUSDC ? usdcToken : usdtToken;
        require(stablecoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        uint256 erc20Amount = amount * exchangeRate / 1e18;
        require(erc20Token.transfer(msg.sender, erc20Amount), "ERC20 transfer failed");

        emit TokensExchanged(msg.sender, erc20Amount, isUSDC);
    }

    function setExchangeRate(uint256 _newRate) external onlyOwner {
        exchangeRate = _newRate;
    }

    function withdrawStablecoin(address to, uint256 amount, bool isUSDC) external onlyOwner {
        IERC20 stablecoin = isUSDC ? usdcToken : usdtToken;
        require(stablecoin.transfer(to, amount), "Withdrawal failed");
    }
}
