
const VectorTransformVerifier = artifacts.require("VectorTransformVerifier");
const fs = require('fs');

module.exports = async function(callback) {
    try {
        // Load the proof and public inputs
        const proof = JSON.parse(fs.readFileSync('proof.json', 'utf8'));
        const publicInputs = JSON.parse(fs.readFileSync('public_inputs.json', 'utf8'));

        // Get the deployed contract instance
        const verifier = await VectorTransformVerifier.deployed();

        // Verify the proof
        const result = await verifier.verifyProof(
            web3.utils.hexToBytes(proof),
            web3.utils.hexToBytes(JSON.stringify(publicInputs))
        );

        console.log("Proof verification result:", result);
        callback();
    } catch (error) {
        console.error(error);
        callback(error);
    }
};
