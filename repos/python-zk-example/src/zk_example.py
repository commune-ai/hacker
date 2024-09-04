
import random
from zkp import ZKP

def generate_prime(bits):
    """Generate a prime number with the specified number of bits."""
    while True:
        n = random.getrandbits(bits)
        if n % 2 != 0 and all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2)):
            return n

def main():
    # Set up the parameters
    p = generate_prime(256)  # A large prime number
    g = 2  # Generator
    
    # Prover's secret
    x = random.randint(1, p-1)
    y = pow(g, x, p)  # Public commitment

    print("Parameters:")
    print(f"p = {p}")
    print(f"g = {g}")
    print(f"y = {y}")

    # Create ZKP instance
    zkp = ZKP(g, p)

    # Prover generates proof
    proof = zkp.prove(x, y)

    # Verifier checks the proof
    result = zkp.verify(y, proof)

    print("\nZero-Knowledge Proof Result:")
    print(f"Proof valid: {result}")

    # Attempt to verify with incorrect y
    incorrect_y = pow(g, random.randint(1, p-1), p)
    incorrect_result = zkp.verify(incorrect_y, proof)

    print("\nAttempt with incorrect public value:")
    print(f"Proof valid: {incorrect_result}")

if __name__ == "__main__":
    main()

