# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Main program
number = int(input("Enter a number: "))
check_even_odd(number)

