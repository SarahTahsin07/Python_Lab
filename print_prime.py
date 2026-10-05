while True:
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        break

print(f"The list of prime number from 2 to {n}:")   
for i in range (2, n+1):
    prime = True
    for j in range (2, i):
        if(i%j == 0):
            prime = False
    if prime:        
        print(i)
