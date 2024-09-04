
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract ValidatorRegistry is Ownable {
    address[] public validators;
    mapping(address => bool) public isValidator;

    event ValidatorAdded(address indexed validator);
    event ValidatorRemoved(address indexed validator);

    function addValidator(address validator) external onlyOwner {
        require(!isValidator[validator], "Validator already registered");
        validators.push(validator);
        isValidator[validator] = true;
        emit ValidatorAdded(validator);
    }

    function removeValidator(address validator) external onlyOwner {
        require(isValidator[validator], "Validator not registered");
        for (uint256 i = 0; i < validators.length; i++) {
            if (validators[i] == validator) {
                validators[i] = validators[validators.length - 1];
                validators.pop();
                break;
            }
        }
        isValidator[validator] = false;
        emit ValidatorRemoved(validator);
    }

    function getValidatorCount() external view returns (uint256) {
        return validators.length;
    }
}
