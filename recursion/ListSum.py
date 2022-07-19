###  Write a Python program of recursion list sum

def sum_of_list(nums):
    return get_sum(nums,0)

def get_sum(nums,i):
    if i==len(nums)-1:
        if type(nums[i]) == type([]) :
                res = get_sum(nums[i],0)
                return res
        else:
            return nums[i]
    if type(nums[i]) == type([]):
            res = get_sum(nums[i],0)
            return res + get_sum(nums,i+1)
    else:     
        return nums[i] + get_sum(nums,i+1)
    


if __name__ =="__main__":
    nums=[1, 2, [3,4], [5,6]]
    print(sum_of_list(nums))