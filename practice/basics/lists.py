#initialise 2 lists, one using list() and one by creating a list object []
my_first_list: list = list()
my_second_list: list = []

#append an item to the end of a list
my_first_list.append("callum")
print(my_first_list)
#getting the index of a value
print(my_first_list.index("callum"))
#getting a value based on its index
print(my_first_list[0])

#updating a list using a new list
names = ["nathan", "cameron", "lachlan", "ian"]
my_second_list = my_second_list + names
print(my_second_list)
#using a slice to retrieve items from index 0 to 1 but not including 1; then 1 to 3 not including 3
print(my_second_list[0:1])
print(my_second_list[1:3])

#update a list by inserting a value before the specified index
my_second_list.insert(1, "ac")
print(my_second_list)

#pop the last value from the list
print(my_second_list.pop())
print(my_second_list)

#pop a value by its index
print(my_second_list.pop(0))
print(my_second_list)