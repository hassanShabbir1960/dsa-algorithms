# Write a Python program to find  the greatest common divisor (gcd) of two integers. 



def GCD(A,B):
    if A==0:
        return B
    
    if B==0:
        return A
    
    if A==B:
        return A
    
    if A>B:
        return GCD(A-B,B)
    else:
        return GCD(A,B-A)
    
    

if __name__ =="__main__":
    A =98
    B = 56
    print(GCD(A,B))