#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 11
# This program checks if a user's integer is a negative or positive


def main():
    # asks the user for input (a integer of their choice)
    print(
        "This program determines whether or not your integer is a negative, positive or zero"
    )
    user_number = int(input("Enter your integer: "))

    # check if user's integer is a positive
    if user_number >= 1:
        print("Your integer is a positive")

    # if the statement above is not true, check if this statement is true (is it a negative?)
    elif user_number <= -1:
        print("Your integer is a negative")

    # else, both of the previous statements were untrue
    else:
        print("Your number has to be a zero")


if __name__ == "__main__":
    main()
