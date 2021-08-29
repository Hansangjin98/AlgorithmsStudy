import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = 0

if N == 1:
    nums.sort()
    for i in range(0, 5):
        result += nums[i]
else:
    sumList = []
    sumList.append(min(nums[0], nums[5]))
    sumList.append(min(nums[1], nums[4]))
    sumList.append(min(nums[2], nums[3]))
    sumList.sort()

    numOne = sumList[0]
    numTwo = sumList[0] + sumList[1]
    numThree = sumList[0] + sumList[1] + sumList[2]

    viewOne = (N-2)*(N-2) + 4*(N-1)*(N-2)
    viewTwo = 4*(N-2) + 4*(N-1)
    viewThree = 4

    result += numOne * viewOne
    result += numTwo * viewTwo
    result += numThree * viewThree

print(result)