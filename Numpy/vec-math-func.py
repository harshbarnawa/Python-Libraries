import numpy as np

arr = np.array([1.01, 2.5, 3.99])
radii = np.array([1, 2, 3])

print(np.sqrt(arr))
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))

print(np.pi) #built in func

print("\narea of circle: ", np.pi * radii ** 2)