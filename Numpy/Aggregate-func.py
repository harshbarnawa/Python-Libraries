import numpy as np
# Aggregate functions = summarize data and typically
#                       return a single value

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print(np.sum(arr))
print(np.mean(arr)) ## avg
print(np.std(arr)) ## standard deviation
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))

print(np.sum(arr, axis = 1))
print(np.sum(arr, axis = 0))

