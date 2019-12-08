import numpy as np

print("No Seed initialization:")
for i in range(5):
    print("random roll:", np.random.randint(1, 7))

print("Outer Seed initialization 69:")
np.random.seed(69)
for i in range(5):
    print("random roll:", np.random.randint(1, 7))

print("Outer Seed initialization 666:")
np.random.seed(666)
for i in range(5):
    print("random roll:", np.random.randint(1, 7))

print("Inner Seed init 69:")
for i in range(5):
    np.random.seed(69)
    print("random roll:", np.random.randint(1, 7))

print("Inner Seed init 666:")
for i in range(5):
    np.random.seed(666)
    print("random roll:", np.random.randint(1, 7))
