# Basic Program Demonstrating Key Programming Activities in Python

# Function to greet the user
def greet_user():
    print("Welcome to the basic Python program!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

# Function to calculate the factorial of a number using a loop
def calculate_factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.")

# Function to demonstrate list operations
def list_operations():
    fruits = ["apple", "banana", "cherry"]
    print("Initial list of fruits:", fruits)
    
    # Adding an item to the list
    fruits.append("date")
    print("After appending 'date':", fruits)
    
    # Removing an item from the list
    fruits.remove("banana")
    print("After removing 'banana':", fruits)
    
    # Iterating through the list
    print("Iterating through the list:")
    for fruit in fruits:
        print(fruit)

# Function to read from and write to a file
def file_operations():
    filename = "example.txt"
    
    # Writing to a file
    with open(filename, 'w') as file:
        file.write("Hello, this is a sample text file.\n")
        file.write("It contains multiple lines of text.\n")
    
    # Reading from a file
    print("\nContents of the file:")
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)

# Main function to call other functions
def main():
    greet_user()
    calculate_factorial()
    list_operations()
    file_operations()

# Entry point of the program
if __name__ == "__main__":
    main()
