## Write a Python program to get the sum of a non-negative integer


def getSum(number,i):
    if number - 2*i <=0:
        return 0
    return number - 2*i + (getSum(number,i+1))


def SumSeries(number):
    return getSum(number,0)


if __name__ =="__main__":
    number =10
    print(SumSeries(number))