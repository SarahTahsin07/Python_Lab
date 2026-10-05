while True:
    x = input("Enter your input: ")

    try:
        x = int(x)
        print("The type of the input is: ", type(x))
    except ValueError:
        print("The input is not a valid integer.")
        continue

    if x < 0 or x > 100:
        print("Please enter a positive integer between 0 and 100.")
        continue

    if x >= 97:
        print("The input is Grade A+.")
    elif x >= 93:
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
    break

