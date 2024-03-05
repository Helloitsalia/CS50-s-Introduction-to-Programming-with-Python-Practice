def main():
    name = input("What's your name?")
    print(hello(name))


def hello (to="World"):
    # print("hello,",to)
    return f"Hello, {to}"
    

if __name__ == "__main__":
    main()


# print("Hello World")

# Vol 0.1
#def hello(to="World"):
#    print("hello", to)

#hello()
#name = input ("what's your name?")
#hello(name)