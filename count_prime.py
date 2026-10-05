while True:
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        break
count = 0
print()   
for i in range (2, n+1):
    prime = True
    for j in range (2, i):
        if(i%j == 0):
            prime = False
    if prime:        
        count+=1
print(f"The number of prime from 2 to {n}: {count}")