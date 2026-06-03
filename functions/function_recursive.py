def factorial_recursive(n):
    if(n<0):
        print("Enter number greater than or equal to 0")
    if(n<=1):
        return 1
    return n*factorial_recursive(n-1)
print(factorial_recursive(5))
print(factorial_recursive(0))
