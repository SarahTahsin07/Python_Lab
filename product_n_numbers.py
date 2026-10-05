while True:
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        break

product = 1
for i in range (1, n+1):
    product*=i

print(f"Product of 1 to {n} is: ", product)