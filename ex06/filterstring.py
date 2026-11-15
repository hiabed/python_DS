import sys
from ft_filter import ft_filter


def main():
    """Filter and display words from a command-line string based on length."""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    result = [w for w in ft_filter(lambda w: len(w) > N, S.split(" "))]
    print(result)


if __name__ == "__main__":
    main()
