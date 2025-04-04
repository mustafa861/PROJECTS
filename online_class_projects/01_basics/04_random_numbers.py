import random

def random_num(num, min_value=1, max_value=100):

    return [random.randint(min_value, max_value)for i in range(num)]

num = 10 

random_numbers = random_num(num)

print(random_numbers)
