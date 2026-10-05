marks = [50, -100, -90, 200, 70, 99, 89, 86]

for mark in marks:
    if mark < 0 or mark >100:
        print(f"Invalid mark: {mark}")
    elif mark >= 97:
        print(f"The mark {mark} is Grade A+.")
    elif mark >= 93:
        print(f"The mark {mark} is Grade A.")
    elif mark >= 90:
        print(f"The mark {mark} is Grade A-.")
    elif mark >= 87:
        print(f"The mark {mark} is Grade B.")
    elif mark >= 83:
        print(f"The mark {mark} is Grade B-.")
    elif mark >= 80:
        print(f"The mark {mark} is Grade C+.")
    elif mark >= 77:
        print(f"The mark {mark} is Grade C.")
    elif mark >= 73:
        print(f"The mark {mark} is Grade C-.")
    elif mark >= 70:
        print(f"The mark {mark} is Grade D.")
    elif mark >= 60:
        print(f"The mark {mark} is Grade D-.")
    else:
        print(f"The mark {mark} is Grade F.")
        