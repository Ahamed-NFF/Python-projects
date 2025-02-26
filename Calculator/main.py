from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


# print(operations["*"](4,8))

def calculator():
    n1 = float(input("Type the first number : \n"))

    game_over = True

    ans = 0

    while game_over:
        for c in operations:
            print(c)

        op = input("Pick an operation : ")

        n2 = float(input("Type the second number : \n"))

        ans = operations[op](n1, n2)

        print(f"{n1} {op} {n2} = {ans}")

        z = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation:")

        if z == "n":
            game_over = False
            print("\n" * 100)
            calculator()
        else:
            n1 = ans


calculator()
