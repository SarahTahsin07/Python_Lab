students = [
    {"name" : "Amina", "major" : "AMDS"},
    {"name" : "Maya", "major" : "Economics"},
    {"name" : "Disha", "major" : "AMDS"},
    {"name" : "Nora", "major" : "Public Health"},
    {"name" : "Lina", "major" : "Economics"}
    ]
groups = {"AMDS" : [], "Economics" : [], "Public Health" : []}
count = {"AMDS" : 0, "Economics" : 0, "Public Health" : 0}

for student in students:
    if student["major"] == "AMDS":
        count["AMDS"] += 1
        groups["AMDS"].append(student["name"])
    elif student["major"] == "Economics":
        count["Economics"] += 1
        groups["Economics"].append(student["name"])
    else:
        count["Public Health"] += 1
        groups["Public Health"].append(student["name"])

print(f"Groups: {groups}")
print(f"Counts: {count}")