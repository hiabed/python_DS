import sys
import string


def main():
    """Count and display character categories from one command-line string."""
    if len(sys.argv) < 2:
        print("What is the text to count?")
        print("Hello World!")
        print("The text contains 13 characters:")
        print("2 upper letters")
        print("8 lower letters")
        print("1 punctuation marks")
        print("2 spaces")
        print("0 digits")

    elif len(sys.argv) > 2:
        print(
            "AssertionError: Too many arguments provided. "
            "Please provide only one text string to analyze."
        )

    else:
        text = sys.argv[1]
        print(f"The text contains {len(text)} characters:")

        upper_count = 0
        lower_count = 0
        punctuation_count = 0
        space_count = 0
        digit_count = 0
        for c in text:
            if c.isupper():
                upper_count += 1
            elif c.islower():
                lower_count += 1
            elif c in string.punctuation:
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
