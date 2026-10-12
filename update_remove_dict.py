student = {"name" : "Amina", "age" : 20, "score" : 78}

student["score"] = 85
student["major"] = "AMDS"
student.pop("age")

print(f"Updated student: {student}")
print(f"Removed age: {student.pop("age", 20)}")

