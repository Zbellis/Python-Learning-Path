def threeNumSum(array, targetSum):

    for i in range(len(array) - 1):

        firstNum = array[i]

        for j in range(i + 1, len(array)):

            secondNum = array[i]

            for k in range(i + 2, len(array)):

                thirdNum = array[k]
                if firstNum + secondNum + thirdNum == targetSum:
                    return [firstNum, secondNum, thirdNum]
    return []



array = [0, 3, 6, 9, 12, 1]
print(threeNumSum(array, 10))
