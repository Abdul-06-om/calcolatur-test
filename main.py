def calcolat():
    first_number = int(input("first number"))
    operator = input("+, -, *, /")
    second_nember = int(input("second nember"))

    if operator == "+":
        e = first_number + second_nember
    elif operator == "-":
        e = first_number - second_nember
    elif operator == "*":
        e = first_number * second_nember
    elif operator == "/":
        e = first_number / second_nember
    else:
        print("pleas chose one of thies operator +, -, *, /")

    print(f"{first_number} {operator} {second_nember} = {e}")



calcolat()