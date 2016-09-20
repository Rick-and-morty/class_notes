# tuple, are immutable, they cannot be changed tuples are defined when created
# to make a tuple with one item in it, put a "," at the end of it

my_tuple = ("tyler", "alex")
print(my_tuple)
# my_tuple.append("max") does not work
# print(my_tuple) does not work

my_string = "cellular phone"
print(my_string + "s")
my_string += "s"
"""my_string[2] = "j"""
# immutability
# a set is mutable, you cannot have duplicate items in a set
# can be the fastest way to get rid of duplicates in a list
# the "difference" is a complex interaction that is what is left from subtraction
# of a set

my_set = {2, 7, 9, "tyler"}
my_people_set = {"tyler", "alex", "toothless"}

print(my_set.intersection(my_people_set))
