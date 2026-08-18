def analyze_numbers(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)
    desc = sorted(numbers, reverse=True)
    return smallest, largest, total, desc

smallest, largest, total, desc = analyze_numbers([4, 9, 1, 7, 3])
print(smallest)
print(largest)
print(total)
print(desc) 
