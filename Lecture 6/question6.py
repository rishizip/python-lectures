# warf to calculate the sum of first n natural no
def calc_sum(n):
    if n == 0:
        return 0
    return calc_sum(n - 1) + n
    
n = int(input("Enter a number to calculate the sum of first n natural numbers: "))

sum = calc_sum(n)
print(f"The sum of first {n} natural numbers is: {sum}")
