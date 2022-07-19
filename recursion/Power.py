
###  Write a Python program to calculate the value of 'a' to the power 'b'. Go to the editor

def get_product(number,pow,i):
    if i==pow:
        return 1
    return number * get_product(number,pow,i+1)

def Power(number,pow):
    return get_product(number,pow,0)


if __name__ =="__main__":
    number =2
    pow = 8
    print(Power(number,8))