import numpy as np

# Roll dice 1000 times
rolls = np.random.randint(1, 7, size=1000)

# Count frequency
for i in range(1, 7):
    print(f"{i} appeared {np.count_nonzero(rolls == i)} times")
