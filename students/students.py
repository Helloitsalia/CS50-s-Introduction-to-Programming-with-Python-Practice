import cvs


# with open("students.cvs") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         name, house = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         print(f"{name} is in {house}")


# 2nd version
# student = []


# with open("students.cvs") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.apped(student)

# def get_name(student):
#     return student["name"]

# for student in sorted (students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")
        

# 3th version

# student = []


# with open("students.cvs") as file:
#     reader = cvs.reader(file)
#     for row in reader:
#         students.append({"name": name, "home": home})
#     # for line in file:
#     #     name, house = line.rstrip().split(",")
#     #     student = {"name": name, "house": house}
#     #     students.apped(student)


# for student in sorted (students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


name = input("What's your name?")
home = input("Where's your home?")

with open("students.cvs", "a") as file:
    # writer = cvs.writer(file)
    writer = cvs.DictWriter(file, feilsnames=["name","home"])
    writer.writerow([name,home])