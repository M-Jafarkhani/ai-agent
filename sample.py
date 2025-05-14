def fibunatchi(n):
    """
    Generate a Fibonacci sequence of length n.
    
    Args:
        n (int): The length of the Fibonacci sequence to generate.
        
    Returns:
        list: A list containing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence