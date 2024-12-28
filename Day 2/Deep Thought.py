user = input("What is the answer to the Great Question of Life, the Universe, Everything? ")
if user == str(int(42)):
    print("Yes")
elif user == "forty-two":
    print("Yes")
elif user == "forty two":
    print("Yes")
else:
    print("No")
