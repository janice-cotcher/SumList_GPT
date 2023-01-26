# This code defines two functions to calculate the sum of a list of integers


def sumList(items):
    """Adds all the inputed items using a loop """
    sum = 0
    for item in items:
        sum = item + sum
    return sum


def user():
    """User input for the list of numbers to add together."""
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


def main():
    """Calls the user function to get numlist and passes it to sumList. The sum is then printed"""
    numlist = user()
    print(f"Your sum is {sumList(numlist)}.")


main()
