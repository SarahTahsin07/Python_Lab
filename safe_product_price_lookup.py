prices =  {"pen" : 15, "book" : 120, "bag" : 850}
requested_items = ["book", "ruler","pen"]

for item in requested_items:
    if item in prices:
        print(f"{item}: Tk {prices.get(item)}")
    else:
        print(f"{item}: {prices.get(item, "not found")}")

