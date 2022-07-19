
### Write a Python program to solve the Fibonacci sequence using recursion


def Fibonacci(number):
    if number==1 or number==2:
        return 1

    return  Fibonacci(number-1) + Fibonacci(number-2)

if __name__ =="__main__":
    number =4
    print(Fibonacci(number))