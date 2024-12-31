user = input("Greet Me: ")
if user.startswith("hello") or user.startswith("Hello"):
    print("0$")
elif user.startswith("h") or user.startswith("H"):
    print("20$")
else:
    print("100$")
