import sys
from ft_filter import ft_filter


def main():
    """Filter and display words from a command-line string based on length."""
    if (len(sys.argv) != 3 or not sys.argv[2].isdigit()):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    S = sys.argv[1]
    N = int(sys.argv[2])
    result = ft_filter(lambda word: len(word) > N, S.split())
    print(result)
    exit(0)


if __name__ == "__main__":
    main()
