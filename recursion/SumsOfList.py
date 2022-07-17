### Write a Python program to calculate the sum of a list of numbers. 

def sum_of_list(nums):
    return get_sum(nums,0)

def get_sum(nums,i):
    if i==len(nums)-1:
        return nums[i]
    return nums[i] + get_sum(nums,i+1)
    


if __name__ =="__main__":
    nums=[1,2,3,4,4,100]
    print(sum_of_list(nums))