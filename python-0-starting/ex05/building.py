import string
import sys

def count_and_print(text: str) -> None:
    """Counts and prints char categories of a string"""

    upper = sum(char.isupper() for char in text)
    lower = sum(char.islower() for char in text)
    punctuation = sum(char in string.punctuation for char in text)
    spaces = sum(char == " " for char in text)
    digits = sum(char.isdigit() for char in text)

    print(f"The text contains {len(text)} characters:\n")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

def main() -> None:
    """Main function: process the args and execute program accordingly"""

    if len(sys.argv) > 2:
        print("Assertionerror: more than one argument is provided")
        return

    if len(sys.argv) == 1 or sys.argv[1] == "":
        try:
            text = input("What is the string to process\n")
        except EOFError:
            text = ""
    else:
        text = sys.argv[1]

    count_and_print(text)
    
if __name__ == "__main__":
    main()