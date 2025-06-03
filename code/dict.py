# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. get() method: Retrieve value for a key
print("Get 'b':", my_dict.get('b'))  # Output: 2

# 2. keys() method: Get all keys
print("Keys:", list(my_dict.keys()))  # Output: ['a', 'b', 'c']

# 3. values() method: Get all values
print("Values:", list(my_dict.values()))  # Output: [1, 2, 3]

# 4. items() method: Get all key-value pairs
print("Items:", list(my_dict.items()))  # Output: [('a', 1), ('b', 2), ('c', 3)]

# 5. pop() method: Remove and return the value for a specified key
removed_value = my_dict.pop('b')
print("Removed value for 'b':", removed_value)  # Output: 2
print("Dictionary after pop:", my_dict)  # Output: {'a': 1, 'c': 3}

# 6. popitem() method: Remove and return the last key-value pair
last_item = my_dict.popitem()
print("Popped item:", last_item)  # Output: ('c', 3)
print("Dictionary after popitem:", my_dict)  # Output: {'a': 1}

# 7. update() method: Update dictionary with new key-value pairs
my_dict.update({'b': 2, 'd': 4})
print("Dictionary after update:", my_dict)  # Output: {'a': 1, 'b': 2, 'd': 4}

# 8. setdefault() method: Return value for a key, or set default if key does not exist
default_value = my_dict.setdefault('e', 5)
print("Set default value for 'e':", default_value)  # Output: 5
print("Dictionary after setdefault:", my_dict)  # Output: {'a': 1, 'b': 2, 'd': 4, 'e': 5}

# 9. fromkeys() method: Create a new dictionary from keys with default value
new_dict = dict.fromkeys(['x', 'y', 'z'], 0)
print("New dictionary fromkeys:", new_dict)  # Output: {'x': 0, 'y': 0, 'z': 0}

# 10. clear() method: Clear all elements from the dictionary
my_dict.clear()
print("Dictionary after clear:", my_dict)  # Output: {}
