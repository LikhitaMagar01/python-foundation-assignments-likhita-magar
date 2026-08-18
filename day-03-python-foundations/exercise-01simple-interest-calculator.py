def calculate_simple_interest(principal, rate=5, time=1):
    interest = principal * rate * time / 100
    print(interest)

calculate_simple_interest(1000, 10, 2)
calculate_simple_interest(1000) 
calculate_simple_interest(2000, time=3)