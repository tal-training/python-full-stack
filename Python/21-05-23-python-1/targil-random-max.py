import random

random_nums=[]

for i in range(10):
    rand_num=random.randint(1, 100)
    random_nums.append(rand_num)

print("the list", random_nums, "\nthe max:", max(random_nums), "the min:", min(random_nums))

