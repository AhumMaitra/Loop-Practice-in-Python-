# Loop Practice Code in Python

# Task 1: Print the first 10 natural numbers using a for loop
print("First 10 natural numbers:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# Task 2: Calculate the sum of all numbers in a given range using a while loop
start = 1
end = 10
sum = 0
num = start
while num <= end:
    sum += num
    num += 1
print(f"Sum of numbers from {start} to {end}: {sum}")
print()

# Task 3: Print multiplication tables from 1 to 5 using nested loops
print("Multiplication tables from 1 to 5:")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line for better readability

# Task 4: Print a pattern using a loop (triangle pattern)
print("Pattern: Triangle")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # Move to the next line

# Task 5: Iterate over a list of names using a for loop
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
print("\nList of names:")
for name in names:
    print(name)
