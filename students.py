# with open("students.cvs") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         name, house = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         print(f"{name} is in {house}")


# 2nd version
student = []


with open("students.cvs") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.apped(student)

def get_name(student):
    return student["name"]

for student in sorted (students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
        