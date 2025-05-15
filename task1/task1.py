def caching_fibonacci() -> callable:  
    """  
    Creates and returns a Fibonacci function with internal caching.  
    
    The returned function accepts a non-negative integer `n` and returns  
    the n-th Fibonacci number, using caching to optimize recursive calculations.  
    
    :return: A function that takes an integer `n` and returns the Fibonacci number at position `n`.  
    """  

    # Dictionary to cache previously computed Fibonacci numbers  
    cache: dict[int, int] = {}  

    def fibonacci(n: int) -> int:  
        """  
        Recursively computes the n-th Fibonacci number with caching.  
        
        :param n: Non-negative integer representing the position in the Fibonacci sequence.  
        :return: Fibonacci number at position n.  
        """  

        # Handle base cases  
        if n <= 0:  
            return 0  
        elif n == 1:  
            return 1  

        # Check if the result is already cached  
        if n in cache:  
            return cache[n]  

        # Compute recursively and store in cache  
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  
        return cache[n]  

    return fibonacci  

# Example usage:  
# Create the Fibonacci function with caching  
fib = caching_fibonacci()  

# Compute Fibonacci numbers  
print(fib(10))  # Output: 55  
print(fib(15))  # Output: 610