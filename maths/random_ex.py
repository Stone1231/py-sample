
import random

def random_generator(total_num=10, max_value=1000):
    nums=[]
    for i in range(total_num):
        num=random.randint(1,max_value)
        nums.append(num)
    return nums

if __name__ == '__main__':
    nums=random_generator(total_num=20, max_value=1000)
    for i in range(len(nums)):
        print(nums[i])
