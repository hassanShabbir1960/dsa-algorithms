
###  Write a Python program to get all subsets of a string / array

answer= []
i =0
def get_subsets(array,temp,i,answer):
    if i >= len(array):
        answer.append(str(temp))
        print(temp)
        return 
    
    
    get_subsets(array,temp,i+1,answer)
    
    temp= temp + str(array[i])
    get_subsets(array,temp,i+1,answer)
    
    

def Powerset(array):
    temp =" "

    return get_subsets(array,temp,i,answer)


if __name__ =="__main__":
    print(Powerset([1,2,3]))
    print(answer)