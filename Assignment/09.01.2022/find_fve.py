dimensions = int(input("Dimensions: "))

vertices = 2 ** dimensions
edges = dimensions * (2**(dimensions-1))

print(f"The number of in a {dimensions} dimension object has {vertices} vertices.")
print(f"The number of in a {dimensions} dimension object has {edges} edges.")
