products = {
    "milk": 40,
    "bread": 30,
    "rice": 60
}

total = 0

while True:
    item = input("Enter product name (or 'done'): ")

    if item == "done":
        break

    if item in products:
        qty = int(input("Quantity: "))
        price = products[item] * qty
        total += price
        print("Added:", price)
    else:
        print("Product not found")

discount = 0
if total > 500:
    discount = total * 0.1

bill = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", bill)