expression = input("Enter Expression: ").strip().lower()
x, y, z = expression.split()

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    print(x/z)
else:
    print(x**z)
                    