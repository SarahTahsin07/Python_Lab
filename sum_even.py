while True:
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        break
    print("Enter a positive integer!")
sum = 0

for i in range (1, n+1):
    if(i%2 ==0):
        sum += i

print(f"The sum of even numbers from 1 to {n} is: {sum}")
