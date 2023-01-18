import numpy as np
def problem1():
    npArray = np.random.randint(10, size=(3, 3))
    npTranspose = np.transpose(npArray)
    filterArr = npTranspose == npArray
    print(filterArr)
    ans = filterArr.astype(int)
    print(ans)
    return ans

def problem2(arr):
    for x in range(3):
        for y in range(3):
            if arr[x, y] == 0:
                arr[x, y] += 3
    print(arr)
    return arr

def problem3(arr):
    print(arr[:, 0:2])
     
ans1 = problem1()
ans2 = problem2(ans1)
problem3(ans2)
print(np.__version__)