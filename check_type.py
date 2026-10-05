while True:
    x = input("Enter your input: ")
    print("The type of the input is: ", type(x))

    if not x.isdigit():
        print("Please enter a positive integer.")
    else:
        break

x = int(x)

if x >= 97:
    print("The input is Grade A+.")
elif x >=93:
    print("The input is Grade A.")
elif x >= 90:
    print("The input is Grade A-.")
elif x >= 87:
    print("The input is Grade B.")
elif x >= 83:
    print("The input is Grade B-.")
elif x >= 80:
    print("The input is Grade C+.")
elif x >= 77:
    print("The input is Grade C.")
elif x >= 73:
    print("The input is Grade C-.")
elif x >= 70:
    print("The input is Grade D.")
elif x >= 60:
    print("The input is Grade D-.")
else:
    print("The input is Grade F.")
    


