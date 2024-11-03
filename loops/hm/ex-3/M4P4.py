# Task 1:
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start > end:
    start,end=end,start
    print("\nPlease, next time don't mess it up.\n")

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

# Task 2:
print('\n\nNext program will show you multiplication table from 1 to 10, enter "start" or "skip" to... start or skip.\n')
choice = input("Enter here: ")
print()
if choice == "start":
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i}*{j} = {i * j}", end="\t")
        print()
elif choice == "skip":
    print("Task is skipped.")
else:
    print("Error.")

# Task 3:
start = int(input("\nEnter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"\nMultiplication table from {start} to {end}:\n")

for i in range(start, end + 1):

    for j in range(1, 11):
        print(f"{i}*{j} = {i * j}", end="\t")
    print()