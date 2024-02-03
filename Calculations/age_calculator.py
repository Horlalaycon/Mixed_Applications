# This is a basic calculator developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github

def calculate_age():
    try:
        birth_year = int(input("Enter birth year: "))
        current_year = int(input("Enter current year: "))
        age = current_year - birth_year
        print(f"age is {str(age)} years")
    except ValueError:
        print("Error! Invalid Input")


if __name__ == "__main__":
    calculate_age()
