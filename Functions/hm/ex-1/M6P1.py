# Task 1:
print("First program will make the colored text.\n")

def colored_text():
    Brown = "\033[38;5;94m"
    Reset = "\033[0m"
    Red = "\33[31m"

    print(f"{Brown}'Don't compare yourself with anyone in this world…")
    print(f"{Red}if{Reset} you {Red} do so{Reset}, you are insulting yourself'")
    print("Bill Gates")
colored_text()

print()
# Task 2:
print("Next program allows you to find every even number in range.\n")

start = int(input("First number: "))
end = int(input("Second number: "))
if start > end:
    start, end = end, start

def even_numbers_in_range(start,end):

    for i in range(start, end+1):
        if i % 2 == 0:
            print(i)

even_numbers_in_range(start,end)

print()
# Task 3:
def draw_square(side_length, symbol, filled):
    for i in range(side_length):
        if filled:
            print(symbol * side_length)
        if not filled:
            if i == side_length-1 or i == 0:
                print(symbol * side_length)
            else:
                print(symbol + ' ' * (side_length - 2) + symbol)

print("Next program is for making square, filled or empty")
print("1. Size\n2. Symbol\n3. Filled or empty (True/False)\n")

side_length = int(input("Size: "))
symbol = input("Symbol: ")
filled_input = input("Filled or not, use True/False: ").strip().lower()

filled = filled_input == "true"

draw_square(side_length, symbol, filled)

print()
# Task 4:
print("Next program allows you to find minimal number among 5 numbers.\n")
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))
n4 = int(input("Fourth number: "))
n5 = int(input("Fifth number: "))

def find_minimal(n1, n2, n3, n4, n5):
    minimum = n1

    if n2 < minimum:
        minimum = n2
    if n3 < minimum:
        minimum = n3
    if n4 < minimum:
        minimum = n4
    if n5 < minimum:
        minimum = n5

    return minimum

print("The minimum number is:", find_minimal(n1, n2, n3, n4, n5))

print()
# Task 5:
print("Next program allows you to find product of the range.\n")

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

if n1 > n2:
    n1,n2 = n2,n1

def product_range(n1, n2):
    product = 1
    for i in range(n1, n2+1):
        product *= i

    return product

print(f"The product of the range is: {product_range(n1, n2)}")

print()
# Task 6:

print("Netx program will find the count of digits in the number.")

number = int(input("Number: "))

def digit_counter(number):
    digits = [int(d) for d in str(number)]
    digit_count = len(digits)
    return digit_count
print(f"Digits count: {digit_counter(number)}")

print()
# Task 7:

print("Final program will say if the number is palindrome.")

number = int(input("Number: "))

def is_palindrome(number):
    string_number = str(number)

    return string_number == string_number[::-1]
print(is_palindrome(number))