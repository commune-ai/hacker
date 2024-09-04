
import numpy as np

def transform_vectors(input_vectors):
    """
    Transform a set of input vectors into a single output vector.
    This is a simple example that computes the element-wise sum of the input vectors.
    """
    return np.sum(input_vectors, axis=0)

def main():
    # Example usage
    input_vectors = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    result = transform_vectors(input_vectors)
    print("Input vectors:")
    print(input_vectors)
    print("Transformed vector:")
    print(result)

if __name__ == "__main__":
    main()
