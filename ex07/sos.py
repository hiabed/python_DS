import sys


def main():
    """Encode a command-line string into International Morse Code."""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    nested_morse = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    text = sys.argv[1].upper()
    morse_chars = []
    for c in text:
        if c not in nested_morse:
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        morse_chars.append(nested_morse[c])

    print(" ".join(morse_chars))


if __name__ == "__main__":
    main()
