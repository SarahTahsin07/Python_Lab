words = ["model", "data", "python","data", "model", "analysis", "data"]
unique = []
not_unique = []
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1
    if word not in unique:
        unique.append(word)
    else:
        if word in not_unique:
            continue
        not_unique.append(word)
        

print(f"Frequency: {frequency}")
print(f"Repeated words: {not_unique}")


