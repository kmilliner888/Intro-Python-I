# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE
def is_even(x):
    if x %2 ==0:
        True
        print("True")
    elif x %2 !=0:
        False
        print("false")

x = 9
is_even(x)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def even_odd(num):
    if num %2 ==0:
        True
        print("Even!")
    elif num %2 !=0:
        False
        print("Odd")

even_odd(num)
# YOUR CODE HERE

