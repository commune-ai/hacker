
from zk_vector_transform import ZKVectorTransform

def main():
    # Example usage
    input_dim = 5
    output_dim = 3
    num_vectors = 4

    zk_transform = ZKVectorTransform(input_dim, output_dim)
    
    # Generate random input matrix
    input_matrix = zk_transform.generate_random_matrix(num_vectors)
    
    # Perform transformation
    output, weights = zk_transform.transform(input_matrix)
    
    # Verify transformation
    is_valid = zk_transform.verify_transformation(input_matrix, weights, output)
    
    print(f"Input matrix shape: {input_matrix.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Weights shape: {weights.shape}")
    print(f"Transformation verified: {is_valid}")

if __name__ == "__main__":
    main()

