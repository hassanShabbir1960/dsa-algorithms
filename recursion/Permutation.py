from operator import le


answer = []


def solve(array,index):
    if index >= len(array):
        answer.append(str(array))
        return
    
    for i in range(index,len(array)):
        array[index],array[i] = array[i],array[index]
        solve(array,index+1)
        array[index],array[i] = array[i],array[index]
        

def permutation(array):
    
    solve(array,0)
    print(answer)

if __name__ == "__main__":
    array = ["A","B","C","D","E"]
    permutation(array)
