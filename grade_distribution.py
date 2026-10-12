marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]
new_marks = []
count = {"A" : 0, "B" : 0, "C" : 0, "F" : 0}

for mark in marks:
    if 0 <= mark <= 100:
        new_marks.append(mark)

        if mark >= 80:
            count["A"] += 1
        elif mark >= 70:
            count["B"] += 1
        elif mark >= 60:
            count["C"] += 1
        else:
            count["F"] += 1
            
if new_marks:
    avg = sum(new_marks) / len(new_marks)

print(f"Valid marks: {new_marks}")
print(f"Grade counts: {count}")
print(f"Average: {avg:.2f}")

