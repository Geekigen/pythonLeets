# Problem: Given nums, an array of integers, and target,
# find indices of the two numbers whose sum equals target.
def twoSum(num, target):
    temp = {}
    for index, value in enumerate(num):
        if target - value not in temp:
            temp[value] = index
            continue
        return [temp[target - value], index]
    print(temp)


print(twoSum([2, 7, 11, 15], 9), "...first formula")


# Summary . here we will take the array and the target
# if you know a little bit of math ,x+y = c ,to make x the subject, x = c-y
# so in this case we use the same approach to solve this leet .
# step 1 is to initialize an empty dictionary .
# step 2 is to loop through the array while using enumerate
# to get both the index and the value of the key in each array usinf the for loop
# step 3 is to if target minus value is in the dicionary then the loop stops giving us the two numbers necessary
# to add to the given target
# This also acts as the base case for the loop
#  the second way of doing it
def twoSum2(numberlist, target):
    return [[x, y] for x in range(len(numberlist)) for y in range(len(numberlist)) if
            numberlist[x] + numberlist[y] == target]


print(twoSum2([1, 2, 3, 4, 5, 6, 7], 9), "....second formula")
# the second option is more dynamic and more simplified
