while True:
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        break
a = 0
b = 1
for i in range (0, n+1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
