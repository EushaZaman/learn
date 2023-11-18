import random
random_numbers = [random.randrange(0, 101) for _ in range(100)]
print(min(random_numbers))
print(max(random_numbers))
sorted_random_numbers = sorted(random_numbers)
print(sorted_random_numbers[0])
print(sorted_random_numbers[-1])
print(random_numbers)
print(sorted_random_numbers)
print(len(random_numbers))
assert len(random_numbers) != len(set(random_numbers))
