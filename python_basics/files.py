"""Exercise 16"""
try:
    div = 10
    numbers = []
    with open('calc', 'r') as calc:
        for line in calc.readlines():
            numbers.append(int((line.rstrip())))

    with open('result', 'a') as res:
        for i in numbers:
            try:
                res.write(f"{div} / {i} = ")
                div /= i
                res.write(f"{div}\n")

            except ZeroDivisionError:
                res.write(f"Division by zero is not allowed!")

except FileNotFoundError:
    print("File calc was not found!")

finally:
    try:
        with open('result', 'r') as res:
            for line in res.readlines():
                print((line.rstrip()))

    except FileNotFoundError:
        print("File result was not found!")

    with open('result', 'w') as res:
        res.write('')
