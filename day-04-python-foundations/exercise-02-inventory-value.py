# Question 2 - Inventory Value from CSV
import csv

# --- SETUP ---
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "price", "quantity"])
    writer.writerow(["Notebook", "2.50", 20])
    writer.writerow(["Pen", "1.00", 50])
    writer.writerow(["Backpack", "35.00", 3])

def total_inventory_value(path):
    total = 0.0
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["price"]) * int(row["quantity"])
    return round(total, 2)


print(total_inventory_value("products.csv"))