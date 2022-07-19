
### Write a Python program to converting an integer to a string in any base.


def Factorial(number):
    if number<=1:
        return 1

    return number * Factorial(number-1)

if __name__ =="__main__":
    number =3
    print(Factorial(number))