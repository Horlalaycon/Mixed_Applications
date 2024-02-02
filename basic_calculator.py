# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
This program is used to perform simple arithmetic calculations.
"""


def welcome_banner():
    print("""
    ====================================================================================
    |**********************************************************************************|
    ====================================================================================
    [*=*]                            BASIC-CALCULATOR                              [*=*]
    [*=*]          Author: AJIMATI IBRAHIM A.K.A Horlalaycon @ github              [*=*]
    [*=*]                                                                          [*=*]
    [*=*]                                                                          [*=*]
    ====================================================================================
    |**********************************************************************************|
    ====================================================================================""")


def add(num1, num2):
    answer = num1 + num2
    print("‖  Problem: |    " + str(num1) + " + " + str(num2))
    print("‖-----------|---------------------‖")
    print("‖ Solution:  | " + str(num1) + " + " + str(num2) + " = " + str(answer))


def subtract(num1, num2):
    answer = num1 - num2
    print("‖  Problem: |    " + str(num1) + " - " + str(num2))
    print("‖-----------|---------------------‖")
    print("‖ Solution: | " + str(num1) + " - " + str(num2) + " = " + str(answer))


def multiply(num1, num2):
    answer = num1 * num2
    print("‖  Problem: |    " + str(num1) + " * " + str(num2))
    print("‖-----------|---------------------‖")
    print("‖ Solution: | " + str(num1) + " * " + str(num2) + " = " + str(answer))


def divide(num1, num2):
    answer = num1 / num2
    print("‖  Problem: |    " + str(num1) + " / " + str(num2) + "      ")
    print("‖-----------|---------------------‖")
    print("‖ Solution: | " + str(num1) + " / " + str(num2) + " = " + str(answer))


def operations():
    banner = """
                ==========================================
                ‖         Operations Lists               ‖
                ==========================================
                ‖       Operations      |   Option       ‖
                ‖~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~‖
                ‖   Addition            |       a        ‖
                ‖-----------------------|----------------‖
                ‖   Subtraction         |       b        ‖
                ‖-----------------------|----------------‖
                ‖   Multiplication      |       c        ‖
                ‖-----------------------|----------------‖
                ‖   Division            |       d        ‖
                ‖-----------------------|----------------‖
                ‖   Exit                |       e        ‖
                ‖=======================|================‖
    Use the Options to specify Operation!!!
    """
    print(banner)


welcome_banner()
operations()
print("============================================================================")
choice = input(" Which operation do you want to perform: ⇒ ")
print("============================================================================")


if choice == "a" or choice == "A":
    try:
        print("====================================")
        print("            Addition")
        print("====================================")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("====================================")
        add(first_num, second_num)
        print("====================================")
    except ValueError:
        print("")
        print("==================================================")
        print("‖  Wrong Inputs, Please input Numbers Only       ‖")
        print("==================================================")

elif choice == "b" or choice == "B":
    try:
        print("====================================")
        print("           Subtraction")
        print("====================================")
        print("====================================")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("====================================")
        subtract(first_num, second_num)
        print("====================================")
    except ValueError:
        print("")
        print("==================================================")
        print("‖  Wrong Inputs, Please input Numbers Only       ‖")
        print("==================================================")


elif choice == "c" or choice == "C":
    try:
        print("====================================")
        print("          Multiplication")
        print("====================================")
        print("====================================")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("====================================")
        multiply(first_num, second_num)
        print("====================================")
    except ValueError:
        print("")
        print("==================================================")
        print("‖  Wrong Inputs, Please input Numbers Only       ‖")
        print("==================================================")


elif choice == "d" or choice == "D":
    try:
        print("====================================")
        print("             Division")
        print("====================================")
        print("====================================")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("====================================")
        divide(first_num, second_num)
        print("====================================")
    except ValueError:
        print("")
        print("==================================================")
        print("‖  Wrong Inputs, Please input Numbers Only       ‖")
        print("==================================================")
    except ZeroDivisionError:
        print("")
        print("=======================================================")
        print("‖ Error!!! Nominators can not be divided by Zero (0)    ‖")
        print("=======================================================")


elif choice == "e" or choice == "E":
    print("Program Terminated...")
    quit()

else:
    print("\n\n" + "--" * 30)
    print("      Invalid Option!!! Please choose from the list below.")
    print("--" * 30)
