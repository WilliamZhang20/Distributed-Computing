from dask import delayed

@delayed
def add(a, b):
    return a + b

def fib_bottom_up(n):
    if n <= 1:
        return delayed(lambda x: x)(n)
    
    # Delayed base case using lambda expression
    fibs = [delayed(lambda: 0)(), delayed(lambda: 1)()]
    
    for i in range(2, n + 1):
        fibs.append(add(fibs[-1], fibs[-2]))
    
    return fibs[n]

# Example: compute fib(30)
result = fib_bottom_up(30)
print("Fibonacci(30), computed bottom-up:", result.compute())