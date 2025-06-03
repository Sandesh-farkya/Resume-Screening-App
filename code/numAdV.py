import numpy as np

# print(np.__version__)

# arr = np.arange(10)
# print(arr)

# arr = np.full((3,3), True, dtype = bool )
# print(arr)
 
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr1=arr[arr % 2 == 1]
# print(arr1)
 
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr1=arr[arr % 2 == 0]
# print(arr1)

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr[arr % 2 != 0] = -1
# print(arr)

# arr = np.arange(10)
# out = np.where(arr % 2 == 0, -1, arr)
# print(out)

# arr = np.arange(15)
# arr1=arr.reshape(3,-1)
# print(arr1)

# b = np.repeat(1, 10).reshape(2,-1)
# print(b)


# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
# # Method 1:
# d=np.concatenate([a, b], axis=1)

# # Method 2:
# c=np.hstack([a, b])

# # Method 3:
# np.c_[a, b]
# print(c)
# print(d)


# a = np.array([1,2,3])
# b=np.r_[np.repeat(a, 3), np.tile(a, 3)]
# print(b)


# a = np.array([1,2,3,2,3,4,3,4,5,6,8])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# c=np.intersect1d(a,b)      # common vlaues in 2 array
# print(c)



# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# c=np.where(a == b)
# print(c)


# a = np.arange(15)
# index = np.where((a >= 5) & (a <= 10))
# a[index]

# b=a[(a >= 5) & (a <= 10)]
# print(b)

# a = np.array([1,2,3,4,5])
# b = np.array([5,6,1,8,9])
# # From 'a' remove all of 'b'
# c=np.setdiff1d(a,b)
# print(c)


# arr = np.arange(15).reshape(3,5)
# arr1=arr[:,[1,0,3,2,4]]
# print(arr1)

# arr = np.arange(9).reshape(3,3)
# # Solution
# arr1=arr[[1,0,2], :]
# print(arr1)
