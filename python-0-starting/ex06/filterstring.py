from ft_filter import ft_filter
import sys

def main() -> None:

    try:
        assert len(sys.argv) == 3, "Bad arguments"
        S = sys.argv[1]
        assert not S.isdigit(), "Bad arguments"
        N = int(sys.argv[2])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return
    words = [w for w in S.split()]
    print(list(ft_filter(lambda w: len(w) > N, words)))

if __name__ == "__main__":
    main()