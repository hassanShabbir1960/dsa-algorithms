
### Write a Python program to calculate the harmonic sum of n-1.
## Note: The harmonic sum is the sum of reciprocals of the positive integers.

def get_sum(number,i):
    if i>number:
        return 0
    return 1/i + get_sum(number,i+1)

def Harmonic_Sum(number):
    return get_sum(number,1)


if __name__ =="__main__":
    number =7
    print(Harmonic_Sum(number))