from random import randint, seed
from time import time
from math import floor
seed(2)

# Take an array of nums and a target value a pair should equal
def find_pair(nums, target):
    maximum = len(nums)

    for i in range(maximum):
        val = binary_search(nums, i, maximum,target-i)
        if val:
            return (nums[val], i)

    return None

def binary_search(nums, left, right, target):

    middle = floor((left + right) / 2) 

    if left > right:
        return None

    if nums[middle] > target:
        right = middle - 1
        return binary_search(nums, left, right, target)
    elif nums[middle] < target:
        left = middle + 1
        return binary_search(nums, left, right, target)
    else:
        return middle

random_nums = []
random_target = randint(0, 700)

for i in range(1000000):
    random_nums.append(randint(0,500))
random_nums.sort()

print("Target: ", random_target)
start = time()
print(find_pair(random_nums, random_target))
print("Elapsed: ", time() - start)
