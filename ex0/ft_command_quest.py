#!/usr/bin/env python3
"""
This module demonstrates how to receive and process command-line arguments.
It displays the program name and arguments in a user-friendly format.

Authorized modules: sys
"""
import sys


def ft_command_quest() -> None:
    """
    Display program name and command-line arguments.

    This function prints:
    - The program name (sys.argv[0])
    - Number of arguments received
    - Each argument with its index
    - Total number of arguments including program name
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
    ft_command_quest()
