print("Hello, World!")

## lets print number from 1 to n
def print_n(n: int):
    ## base case
    if n <= 0:
        return
    
    print_n(n-1)
    print(n)

    return

## fibonacci series
def fib_series(n: int):
    ## base case
    if n == 0 or n == 1:
        return n
    
    return fib_series(n-1) + fib_series(n-2)