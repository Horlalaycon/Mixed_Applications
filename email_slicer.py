# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
This program is used to split email addresses into Three parts:
Username
Domain
Extension
"""


def slice_email():
    email = input("Enter Email Address to Split: ")
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")
    print("Email sliced Successfully...")
    print(f"+-----------------------------------+")
    print(f"|               Results")
    print(f"+-----------------------------------+")
    print(f"|   Username : {username}")
    print(f"|   Domain : {domain}")
    print(f"|   Extension : {extension}")
    print(f"+-----------------------------------+")


if __name__ == "__main__":
    try:
        slice_email()
    except ValueError:
        print(f"+-----------------------------------------------------+")
        print(f"| Error! Please Check if the email address is correct |")
        print(f"+-----------------------------------------------------+")
