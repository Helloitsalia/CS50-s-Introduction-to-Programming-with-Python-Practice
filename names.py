# name = input("What's your name?")

# # file _ open("names.txt", "a")###
# with open("names.txt", "a") as file:
# file.write(f"{name}\n")
# # file.close()####


# 2nd version

# with open("names.txt", "r") as file
#     lines = file.readlines()

# for line in lines:
#     print("hello", line.rstrip())


# 3th version

names = []

with open("names.txt") as file
    for line file:
        names.apped(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

    