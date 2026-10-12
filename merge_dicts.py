delivery_1 = {"pen" : 12, "book" : 5, "bag" : 2}
delivery_2 = {"book" : 4, "ruler" : 10, "pen" : 3}
total = 0

for delivery in delivery_1:
    if delivery in delivery_2:
        delivery_2[delivery] = delivery_1[delivery] + delivery_2[delivery]

new_delivery = delivery_1 | delivery_2

for delivery in new_delivery:
    total = total + new_delivery[delivery]

print(f"Combined delivery: {new_delivery}")
print(f"Grand Total: {total}")