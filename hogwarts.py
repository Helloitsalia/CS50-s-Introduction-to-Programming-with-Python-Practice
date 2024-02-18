# students = ["Hermione","Harry","Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range (len(students)):
    # print(i + ,students[i])

# students = {
#     "Hermione" : "Gryffindor"
#     "Harry" : "Gryffindor"
#     "Ron" : "Gryffindor"
#     "Draco" : "Slytherin"
# }

# for student in students:
#     print (student, students[student], sep",")

student = [
    {"name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"name": "Draco", "House": "Slytherin", "Patronus": "None"},

  
]

for student in students:
    print(student ["name"], student["House"], student["Patronus"], sep =",")