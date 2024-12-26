def convert():
    user = input("Enter Text: ")
    text = user.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    since = convert()
    print(since)



main()