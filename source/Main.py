

# def my_function(str1, str2):
#     print(str1)
#     print(str2)
#
#
# my_function("This is arg 1", "This is arg 2.")
# my_function("This is another arg", "This is a further arg")


def print_something(name = "Default", age = "Unknown"):
    print("My name is ", name, " and my age is ", age)


print_something("Dave", 39)

print_something("Dave")

print_something(None, 39)

print_something(age = 39, name = "Dave")

print_something(age = 39)


