
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract InferenceProver {
    struct Proof {
        bytes32 inputHash;
        bytes32 outputHash;
        bytes32 modelHash;
        uint256 timestamp;
        bool verified;
    }

    mapping(address => Proof) public proofs;
    mapping(address => uint256) public stakes;

    uint256 public constant CHALLENGE_PERIOD = 1 days;
    uint256 public constant MINIMUM_STAKE = 1 ether;

    event ProofSubmitted(address indexed prover, bytes32 inputHash, bytes32 outputHash, bytes32 modelHash);
    event ProofChallenged(address indexed challenger, address indexed prover);
    event ProofVerified(address indexed prover);
    event ProverSlashed(address indexed prover, uint256 amount);

    function submitProof(bytes memory proof) external payable {
        require(msg.value >= MINIMUM_STAKE, "Insufficient stake");
        
        (bytes32 inputHash, bytes32 outputHash, bytes32 modelHash) = abi.decode(proof, (bytes32, bytes32, bytes32));
        
        proofs[msg.sender] = Proof({
            inputHash: inputHash,
            outputHash: outputHash,
            modelHash: modelHash,
            timestamp: block.timestamp,
            verified: false
        });
        
        stakes[msg.sender] += msg.value;
        
        emit ProofSubmitted(msg.sender, inputHash, outputHash, modelHash);
    }

    function challengeProof(address prover) external {
        Proof storage proof = proofs[prover];
        require(proof.timestamp != 0, "Proof does not exist");
        require(block.timestamp <= proof.timestamp + CHALLENGE_PERIOD, "Challenge period expired");
        
        emit ProofChallenged(msg.sender, prover);
        
        // Initiate off-chain verification process
    }

    function verifyProof(address prover) external {
        Proof storage proof = proofs[prover];
        require(proof.timestamp != 0, "Proof does not exist");
        require(!proof.verified, "Proof already verified");
        
        // Perform on-chain verification (simplified for demonstration)
        proof.verified = true;
        
        emit ProofVerified(prover);
    }

    function slashProver(address prover) external {
        Proof storage proof = proofs[prover];
        require(proof.timestamp != 0, "Proof does not exist");
        require(!proof.verified, "Cannot slash verified proof");
        
        uint256 slashAmount = stakes[prover];
        stakes[prover] = 0;
        
        // Transfer slashed amount to challenger or burn
        payable(msg.sender).transfer(slashAmount / 2);
        
        emit ProverSlashed(prover, slashAmount);
    }

    function withdrawStake() external {
        Proof storage proof = proofs[msg.sender];
        require(proof.verified, "Proof not verified");
        require(block.timestamp > proof.timestamp + CHALLENGE_PERIOD, "Challenge period not over");
        
        uint256 amount = stakes[msg.sender];
        stakes[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}
