def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mul(number1, number2):
    return number1 * number2

def div(number1, number2):
    return number1 / number2

def floordivision(number1, number2):
    return number1 // number2

def modulo(number1, number2):
    return number1 % number2

def exponential(number1, number2):
    return number1 ** number2

if __name__ == "__main__":

    number1 = int(input("Enter number 1:"))
    number2 = int(input("ENter number 2:"))

    addition = add(number1, number2)
    print(addition)

    Subtraction = sub(number1, number2)
    print(Subtraction)

    Multiplication = mul(number1, number2)
    print(Multiplication)

    Division = div(number1, number2)
    print(Division)

    Floor_Division = floordivision(number1, number2)
    print(Floor_Division)

    Modulo = modulo(number1, number2)
    print(Modulo)

    Exponential = exponential(number1, number2)
    print(Exponential)


