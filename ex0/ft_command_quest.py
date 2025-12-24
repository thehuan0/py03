"""
This program demonstrates how to receive command-line arguments
from the user. It displays the program name, the number of
arguments received, each argument individually, and the total
number of arguments including the program name.

Authorized modules: sys
"""
import sys


def main() -> None:
    """
    Main function that processes command-line arguments and
    displays them in a user-friendly format.
    """
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    arg_count = len(sys.argv) - 1
    if arg_count > 0:
        print(f"Arguments received: {arg_count}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
