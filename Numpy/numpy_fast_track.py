import numpy as np

print("\n=== 1. ARRAY CREATION ===")

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(b)

print(np.zeros((3, 4)))
print(np.ones((2, 3)))
print(np.full((2, 3), 7))
print(np.eye(3))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))

print(np.random.rand(2, 3))
print(np.random.randn(2, 3))
print(np.random.randint(1, 10, (2, 3)))


print("\n=== 2. ARRAY PROPERTIES ===")

x = np.array([[1, 2, 3], [4, 5, 6]])

print("shape:", x.shape)
print("ndim:", x.ndim)
print("size:", x.size)
print("dtype:", x.dtype)
print("itemsize:", x.itemsize)


print("\n=== 3. INDEXING AND SLICING ===")

x = np.array([[10, 20, 30], [40, 50, 60]])

print(x[0, 1])
print(x[1, :])
print(x[:, 0])
print(x[:, 1:3])

numbers = np.array([10, 20, 30, 40, 50])
print(numbers[1:4])
print(numbers[::2])


print("\n=== 4. RESHAPE ===")

x = np.arange(12)

print(x.reshape(3, 4))
print(x.reshape(2, 2, 3))
print(x.reshape(3, -1))

matrix = np.arange(12).reshape(3, 4)

print(matrix.flatten())
print(matrix.ravel())


print("\n=== 5. TRANSPOSE ===")

x = np.array([[1, 2, 3], [4, 5, 6]])

print(x.T)
print(np.transpose(x))


print("\n=== 6. CONCATENATION ===")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate([a, b]))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.vstack([a, b]))
print(np.hstack([a, b]))
print(np.concatenate([a, b], axis=0))


print("\n=== 7. MATH OPERATIONS ===")

x = np.array([1, 2, 3])

print(x + 10)
print(x * 10)
print(x ** 2)
print(np.sqrt(x))
print(np.exp(x))
print(np.log(x))
print(np.abs(x))


print("\n=== 8. AGGREGATION AND AXIS ===")

x = np.array([[1, 2, 3], [4, 5, 6]])

print("sum:", x.sum())
print("mean:", x.mean())
print("std:", x.std())
print("var:", x.var())
print("min:", x.min())
print("max:", x.max())

print("column sums:", x.sum(axis=0))
print("row sums:", x.sum(axis=1))

print("column means:", x.mean(axis=0))
print("row means:", x.mean(axis=1))


print("\n=== 9. BROADCASTING ===")

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([10, 20, 30])

print(x + y)
print(x * y)

print(np.array([1, 2, 3]) + 10)


print("\n=== 10. BOOLEAN MASKING ===")

x = np.array([10, 20, 30, 40, 50])

print(x > 25)
print(x[x > 25])
print(x[(x > 20) & (x < 50)])
print(x[(x < 20) | (x > 40)])


print("\n=== 11. WHERE ===")

x = np.array([10, 20, 30, 40])

print(np.where(x > 25, 1, 0))
print(np.where(x > 25))


print("\n=== 12. SORTING ===")

x = np.array([30, 10, 50, 20])

print(np.sort(x))
print(np.argsort(x))


print("\n=== 13. UNIQUE ===")

x = np.array([1, 2, 2, 3, 3, 3])

print(np.unique(x))
print(np.unique(x, return_counts=True))


print("\n=== 14. RANDOM ===")

np.random.seed(42)

print(np.random.rand(3, 3))
print(np.random.randn(3, 3))
print(np.random.randint(0, 10, (3, 3)))
print(np.random.normal(0, 1, 5))


print("\n=== 15. MATRIX OPERATIONS ===")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("dot:\n", np.dot(a, b))
print("matrix multiplication:\n", a @ b)
print("transpose:\n", a.T)
print("inverse:\n", np.linalg.inv(a))
print("determinant:", np.linalg.det(a))

print("\n=== 16. COPY VS VIEW ===")

a = np.array([1, 2, 3])
b = a.copy()

b[0] = 100

print("a:", a)
print("b:", b)


print("\n=== 17. DATA TYPES ===")

x = np.array([1, 2, 3], dtype=np.float32)

print(x)
print(x.dtype)
print(x.astype(np.int32))


print("\n=== 18. NAN AND INF ===")

x = np.array([1, 2, np.nan, 4, np.inf])

print(np.isnan(x))
print(np.isinf(x))
print(np.nanmean(x))


print("\n=== NUMPY COMPLETE ===")
