
### Write a Python program to converting an integer to a string in any base.


def Integer_To_String(number,base):
    conver_tString = "0123456789ABCDEF"

    if number<base:
        return conver_tString[number]
    return str(Integer_To_String(number//base,base)) + str(conver_tString[number%base]) 


if __name__ =="__main__":
    number =10
    base =2
    print(Integer_To_String(number,base))