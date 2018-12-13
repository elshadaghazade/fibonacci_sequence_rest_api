from concurrent import futures
from array import array

def get_fib_sequence(start_idx, end_idx):
    """Returns Fibonacci sequence from start_idx to end_idx.
    
    Positional arguments:
    start_idx -- start index of sequence
    end_idx   -- end index of sequence

    Returns:
    Value -- Fibonacci sequence
    Type  -- list
    """

    if start_idx >= end_idx or start_idx < 0 or end_idx < 0:
        raise ValueError("Start index should be less than end index and both should be positive integers")


    # unsigned long long
    fib_seq = array('Q', [0, 1])

    for i in range(end_idx-1):
        fib_seq.append(fib_seq[-2] + fib_seq[-1])

    return list(fib_seq[start_idx:end_idx+1])