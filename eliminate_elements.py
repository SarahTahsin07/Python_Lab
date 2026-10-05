people_list = []
for i in range (1, 1001):
    people_list.append(i)

print(f"Initial People list: {people_list}")

while(len(people_list) > 1):
    new_people_list = []
    for i in range(len(people_list)):
        if (i + 1) % 2 == 0:
            new_people_list.append(people_list[i])
            
    people_list = new_people_list
    print(f"Updated People list: {people_list}")

print(f"Final People list: {people_list}")