stock = {"pen" : 12, "book" : 3, "bag" : 2, "ruler" : 9, "calculator" : 1}
need_restock = {}
total = 0

for item in stock:
    total = total + stock[item]
    if stock[item] < 5:
        need_restock[item] = stock[item]
    
print(f"Total units: {total}")
print(f"Low stock: {need_restock}")
