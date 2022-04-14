"""Exercise 13"""
from math import pi
from numpy import array
# local import
import practice as pr

# use practice
print("List the contents of a namespace:\n", dir(pr, sep=''))
print(pr.list_benefits())

# use numpy
my_array = array([1, 4, 5, 8], float)
print(my_array)


# use math.pi
def get_circumference(radius):
    """Calculates the circumference of a circle"""
    return 2*pi*radius


print(get_circumference(3))
