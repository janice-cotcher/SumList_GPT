# This code defines two functions to calculate the sum of a list of integers

# The sumList function takes a parameter 'items' which is a list of integers
# It initializes a variable 'sum' to 0
# Then it loops through each item in the list and adds it to the 'sum' variable
# Finally, it returns the 'sum' variable
def sumList(items):
    sum = 0
    for item in items:
        sum = item + sum
    return sum

# The user function is used to get user input
# It initializes an empty list called 'numlist'
# It uses a try-except block to handle invalid input from the user
# The user is prompted to enter how many integers they want to add together
# Then, it uses a for loop to get input for that many numbers
# The input numbers are added to the 'numlist' list
# If an exception is raised, it prints an error message
# Finally, it returns the 'numlist'
def user():
    numlist = []
    try:
        i = int(input("How many integers do you want to add together? "))
        for i in range(0,i):
            n = int(input("Input a number: "))
            numlist.append(n)
    except ValueError:
        print("Invalid input. Try again.")
    finally:
        return numlist

# The main function calls the user function to get the 'numlist'
# Then it passes the 'numlist' to the 'sumList' function and assigns the returned value to a variable
# It then prints the sum of the list using f-string
def main():
    numlist = user()
    print(f"Your sum is {sumList(numlist)}.")

# The main function is called
main()
