# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon

import string
import random


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
