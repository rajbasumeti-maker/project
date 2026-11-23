
numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, numbers.split()))

maximum = max(numbers)
minimum = min(numbers)

print("Maximum number:", maximum)
print("Minimum number:", minimum)
