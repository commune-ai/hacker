
from zk_proof import Prover, Verifier
import random

def main():
    # Shared parameters
    p = 23  # A small prime for demonstration purposes
    g = 5   # A generator of the multiplicative group modulo p

    # Prover's secret
    secret = 6

    # Compute public key
    public_key = pow(g, secret, p)

    # Create prover and verifier
    prover = Prover(p, g, secret)
    verifier = Verifier(p, g, public_key)

    # ZK Proof protocol
    commitment = prover.generate_commitment()
    challenge = verifier.generate_challenge()
    response = prover.compute_response(challenge)

    # Verification
    result = verifier.verify(commitment, challenge, response)

    print(f"Public parameters: p = {p}, g = {g}")
    print(f"Prover's secret: {secret}")
    print(f"Public key: {public_key}")
    print(f"Commitment: {commitment}")
    print(f"Challenge: {challenge}")
    print(f"Response: {response}")
    print(f"Verification result: {result}")

if __name__ == "__main__":
    main()
