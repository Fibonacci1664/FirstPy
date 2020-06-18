# def my_function(str1, str2):
#     print(str1)
#     print(str2)
#
#
# my_function("This is arg 1", "This is arg 2.")
# my_function("This is another arg", "This is a further arg")


# def print_something(name="Default", age="Unknown"):
#     print("My name is ", name, " and my age is ", age)
#
#
# def print_people(*people):  # The asterix says that this will be an array of
#     for person in people:  # all the arguments passed in to the function.
#         print("This person is: ", person)
#
#
# def do_math(num1, num2):
#     return num1 + num2
#
#
# math_1 = do_math(5, 7)
# math_2 = do_math(11, 34)
#
# print("First sum = ", math_1, " Second sum = ", math_2)
#
# print_people("Nick", "Dan", "Bob", "Smiley")

# print_something("Dave", 39)
#
# print_something("Dave")

# print_something(None, 39)
#
# print_something(age=39, name="Dave")
#
# print_something(age=39)


# check = "hamburger"
#
# if check == False:
#     print("Check was true")
# elif check == "hamburger":
#     print("yum")
# elif check == "hello":
#     print("Hi")
# else:
#     print("Check was false")


numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)


run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1