## Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

def getSum(number,i):
    if number - 2*i <=0:
        return 0
    return number - 2*i + (getSum(number,i+1))


def SumSeries(number):
    return getSum(number,0)


if __name__ =="__main__":
    number =10
    print(SumSeries(number))