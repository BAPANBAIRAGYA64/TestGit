print("Hello, World!")

## lets print number from 1 to n
def print_n(n: int):
    ## base case
    if n <= 0:
        return
    
    print_n(n-1)
    print(n)

    return