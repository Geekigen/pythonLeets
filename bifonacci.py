# this is the code to print a series of numbers that the previous two numbers ad up to  the current e.g 0,1,1
# it takes in the variable of the number of sequences you want
def bifo(n):
    startArr = [0, 1]
    for i in range(n):
        startArr.append(startArr[-1] + startArr[-2])
    return startArr


print(bifo(20))
# Check the test case and try it out at your own free time