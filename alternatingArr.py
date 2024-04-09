# in this task , one has to make the adjacent value of  indexes in an array alternate
# example is [1,2,3,4,5,6]
# to be [2,1,4,3,6,5]
# while you are given an array ?
def altern(arr):
    y = len(arr)
    for i in range(0, y - y % 2, 2):
        if i + 1 < y:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(altern([1, 2, 30, 43,15,60]))
