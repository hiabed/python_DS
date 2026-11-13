import sys

if (len(sys.argv) == 1):
    sys.exit()
elif (len(sys.argv) > 2):
    sys.exit("AssertionError: more than one argument is provided")

try:
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    sys.exit("AssertionError: argument is not an integer")
