# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
This program is used to generate random passwords with the mixture of uppercase, lowercase and digits.
"""

import string
import random


def generate_password():
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '?' + '!' + '@' + '#' + '$' + '&') for _ in range(12))

    print(f"Generated password: {password} \n")

    option = input("Save the password to txt file (y/n): ")
    if option.lower() == "yes" or option.lower() == "y":
        with open("pass.txt", "w") as f:
            f.write(password)
            f.close()
        print("\npassword saved to pass.txt")

    elif option.lower() == "no" or option.lower() == "n":
        print(f"\nGenerated password is : {password} ")
        print("Program ending...")
        quit()

    else:
        print("\nInvalid Option!")


if __name__ == "__main__":
    generate_password()
