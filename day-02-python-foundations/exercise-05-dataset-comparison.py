"""
Exercise 5: Dataset Comparison
Student: Likhita
Day: 2
"""

# input values
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# calculations
all_unique = dataset_a.union(dataset_b)
in_both = dataset_a.intersection(dataset_b)
only_in_a = dataset_a.difference(dataset_b)
only_in_b = dataset_b.difference(dataset_a)

# output
print("All unique dataset names:", all_unique)
print("Datasets found in both groups:", in_both)
print("Datasets only in dataset_a:", only_in_a)
print("Datasets only in dataset_b:", only_in_b)
