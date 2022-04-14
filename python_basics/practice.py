# 1-st exercise
print("Hello, World!")

# 2-nd exercise
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# 3-rd exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]
for i in range(1, 4):
    numbers.append(i)
strings.append('hello')
strings.append('world')

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# 4-th exercise
x = object()
y = object()

x_list = [x for i in range(10)]
y_list = [y for i in range(10)]
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# 5-th exercise
data = ("John", "Doe", 53.44)
# мой вариант, который не принимается learnpython, хотя выводт всё корректно
# format_string = "Hello %s %s. Your current balance is $%.2f."
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

# 6-th exercise
# аналогичная ситуация
# s = "Streets are twasome!"
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# 7-th exercise
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# 8-th exercise
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    print(number)
    if number == 237:
        break

# 9-th exercise


def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


def build_sentence(benefit):
    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()

# 11-th exercise
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781, 'Jake': 938273443}

phonebook.pop('Jill')
# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# 12-th exercise
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
print(set(a).difference(b))

# 14-th exercise
import re

find_members = [func for func in dir(re) if 'find' in func]
print(sorted(find_members))
