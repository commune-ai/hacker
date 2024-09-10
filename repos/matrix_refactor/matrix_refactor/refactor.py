
import torch
from torch.linalg import svd

def refactor_matrix(matrix: torch.Tensor, top_n: int) -> torch.Tensor:
    """
    Refactor a matrix by keeping only the top N singular values and vectors.
    
    Args:
        matrix (torch.Tensor): Input matrix to refactor
        top_n (int): Number of top singular values to keep
    
    Returns:
        torch.Tensor: Refactored matrix
    """
    U, S, Vt = svd(matrix)
    
    # Keep only the top N singular values and vectors
    U_truncated = U[:, :top_n]
    S_truncated = S[:top_n]
    Vt_truncated = Vt[:top_n, :]
    
    # Reconstruct the matrix
    refactored = U_truncated @ torch.diag(S_truncated) @ Vt_truncated
    
    return refactored
