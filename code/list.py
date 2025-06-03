# Initialize a list
my_list = [1, 2, 3, 4, 5]

# 1. append(): Add an element to the end of the list
my_list.append(6)
print("append(6):", my_list)

# 2. extend(): Extend the list by appending elements from another list or iterable
my_list.extend([7, 8, 9])
print("extend([7, 8, 9]):", my_list)

# 3. insert(): Insert an element at a specified position
my_list.insert(0, 0)  # Insert 0 at index 0
print("insert(0, 0):", my_list)

# 4. remove(): Remove the first occurrence of a specified value
my_list.remove(5)  # Removes the first occurrence of 5
print("remove(5):", my_list)

# 5. pop(): Remove and return an element at a specified index (default: last element)
last_element = my_list.pop()
print("pop():", last_element, my_list)

# 6. clear(): Remove all elements from the list
temp_list = my_list.copy()
temp_list.clear()
print("clear():", temp_list)

# 7. index(): Return the index of the first occurrence of a specified value
index_of_3 = my_list.index(3)
print("index(3):", index_of_3)

# 8. count(): Count the number of occurrences of a specified value
count_of_3 = my_list.count(3)
print("count(3):", count_of_3)

# 9. sort(): Sort the list in ascending order (or descending with reverse=True)
unsorted_list = [3, 1, 4, 2]
unsorted_list.sort()
print("sort():", unsorted_list)

# 10. reverse(): Reverse the elements of the list
unsorted_list.reverse()
print("reverse():", unsorted_list)

# 11. copy(): Return a shallow copy of the list
copied_list = my_list.copy()
print("copy():", copied_list)
