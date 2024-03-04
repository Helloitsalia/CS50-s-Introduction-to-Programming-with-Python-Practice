import sys 

# # Check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# # print name tags
# print("Hello, my name is", sys.argv[1])


### How to use Exit
# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# print name tags
print("Hello, my name is", sys.argv[1])

