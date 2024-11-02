# Task 1:
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
if start < 0 or end < 0:
    print("Error. Please, use non-negative integer numbers.")
else:
    if end < start:
        start, end = end, start

    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0
    div9_sum = 0
    count_div9 = 0
    # First:
    print("\n")
    print("Even numbers:", end=" ")
    for even_numbers in range(start, end + 1):
        if even_numbers % 2 == 0:
            print(f"{even_numbers}", end=" ")
            even_sum += even_numbers
            even_count += 1
    # Second:
    print("\n")
    print("Odd numbers:", end=" ")
    for odd_numbers in range(start, end + 1):
        if odd_numbers % 2 != 0:
            print(f"{odd_numbers}", end=" ")
            odd_sum += odd_numbers
            odd_count += 1
    # Third:
    print("\n")
    print("Numbers dividable by 9:", end=" ")
    for div_by_9 in range (start, end + 1):
        if div_by_9 % 9 == 0:
            print(f"{div_by_9}", end=" ")
            count_div9 += 1
            div9_sum += div_by_9
    # Fourth:
    print("\n")
    if even_count > 0:
        print(f"Average for even numbers: {even_sum / even_count:.2f}")
    else:
        print("No even numbers in the range.")
    if odd_count > 0:
        print(f"Average for odd numbers: {odd_sum / odd_count:.2f}")
    else:
        print("No odd numbers in the range.")
    if count_div9 > 0:
        print(f"Average for numbers dividable by 9: {div9_sum / count_div9:.2f}")
    else:
        print("No numbers dividable by 9 in the range.")

# Task 2:
length = int(input("How many symbols do you want:"))
symbol = input("Symbol:")

for i in range(length):
    print(symbol)

# Task 3:
print('Enter 7 to leave the "app".')
print('Current "app" determines if number is positive, negative or equal to zero.')
while True:
    number = float(input("Enter a number: "))

    if number == 7:
        print("Goodbye!")
        break

    elif number > 0:
        print("Number is positive.")
    elif number < 0:
        print("Number is negative.")
    else:
        print("Number is equal to zero.")

# Task 4:
total_sum = 0
min_number = None
max_number = None

print('Enter 7 to leave the "app".')
print('Current "app" summarizes and finds minimum and maximum number.')
while True:
    number = float(input("Enter a number: "))

    if number == 7:
        print("Goodbye!")
        break

    total_sum += number

    if min_number is None or number < min_number:
        min_number = number
    if max_number is None or number > max_number:
        max_number = number

    print(f"Current sum: {total_sum}, Min: {min_number}, Max: {max_number}")