import random

# Exercise 1

# This will produce a random whole number between 1 and 10 (inclusive).
rand_num = random.randint(1, 10)

# You can generate a random number between 0 (not inclusive) and 1 (inclusive)
# 0.0 <= random.random() < 1.0
rand_num_0_to_1 = random.random()

# This will generate a random floating point number between 1 and 10.
# a <= random.uniform(a,b) <= b
random_float = random.uniform(1, 10)

random_output = random.randint(0, 1)
if random_output == 1:
    print("Head")
else:
    print("Tail")
	
# Exercise 2
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_index = random.randint(0, 4)
print(friends[random_index])
