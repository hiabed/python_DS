import sys


def main():
    """Count and display the character categories of a given string."""
    if len(sys.argv) > 2:
        print("AssertionError: Too many arguments provided.")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("What is the text to count?")
        try:
            text = sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit(1)
    else:
        text = sys.argv[1]
    print(f"The text contains {len(text)} characters:")

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in text:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
        elif c in punctuation:
            punctuation_count += 1
        elif c.isspace():
            space_count += 1
        elif c.isdigit():
            digit_count += 1
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
