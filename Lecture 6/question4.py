# waf to find the factorial of n (n is the parameter)
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"Factorial of {n} = {fact}")

n = int(input("enter a number : "))

calc_fact(n)
