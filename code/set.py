# Initialize two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 1. add(): Add a single element to the set
set_a.add(6)
print("add(6):", set_a)

# 2. remove(): Remove a specific element from the set (raises KeyError if not found)
set_a.remove(6)
print("remove(6):", set_a)

# 3. discard(): Remove a specific element from the set (does NOT raise KeyError if not found)
set_a.discard(10)  # Element not present, no error
print("discard(10):", set_a)

# 4. pop(): Remove and return an arbitrary element from the set
popped_element = set_a.pop()
print("pop():", popped_element, set_a)

# 5. clear(): Remove all elements from the set
temp_set = set_a.copy()
temp_set.clear()
print("clear():", temp_set)

# 6. copy(): Return a shallow copy of the set
set_copy = set_a.copy()
print("copy():", set_copy)

# 7. union(): Return a new set with elements from both sets
union_set = set_a.union(set_b)
print("union(set_b):", union_set)

# 8. intersection(): Return a new set with elements common to both sets
intersection_set = set_a.intersection(set_b)
print("intersection(set_b):", intersection_set)

# 9. difference(): Return a new set with elements in the first set but not in the second
difference_set = set_a.difference(set_b)
print("difference(set_b):", difference_set)

# 10. symmetric_difference(): Return a new set with elements in either set but not both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("symmetric_difference(set_b):", symmetric_difference_set)

# 11. update(): Update the set with elements from another set or iterable
set_a.update(set_b)
print("update(set_b):", set_a)

# 12. intersection_update(): Update the set with the intersection of itself and another
set_a.intersection_update(set_b)
print("intersection_update(set_b):", set_a)

# 13. difference_update(): Update the set by removing elements found in another set
set_a = {1, 2, 3, 4, 5}  # Reset set_a
set_a.difference_update(set_b)
print("difference_update(set_b):", set_a)

# 14. symmetric_difference_update(): Update the set with the symmetric difference
set_a = {1, 2, 3, 4, 5}  # Reset set_a
set_a.symmetric_difference_update(set_b)
print("symmetric_difference_update(set_b):", set_a)

# 15. issubset(): Check if the set is a subset of another
is_subset = {1, 2}.issubset(set_a)
print("issubset({1, 2}):", is_subset)

# 16. issuperset(): Check if the set is a superset of another
is_superset = set_a.issuperset({1, 2})
print("issuperset({1, 2}):", is_superset)

# 17. isdisjoint(): Check if the set has no elements in common with another
is_disjoint = set_a.isdisjoint({10, 11})
print("isdisjoint({10, 11}):", is_disjoint)
