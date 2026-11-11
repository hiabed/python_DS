import sys

filterstring = lambda S, N: [word for word in S.split() if len(word) > N]

def main():
    """Filter and display words from a command-line string based on length."""
    if len(sys.argv) < 3:
        print("AssertionError: the arguments are bad")