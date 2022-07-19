## Write a Python program to get the sum of a non-negative integer


def getSum(numbers,i):
    if i==len(numbers)-1:
        return numbers[i]
    return int(numbers[i]) + int(getSum(numbers,i+1))


def sumDigits(numbers):
    return getSum(str(numbers),0)


if __name__ =="__main__":
    numbers =1438
    print(sumDigits(numbers))