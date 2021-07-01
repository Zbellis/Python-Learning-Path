

def twoSumNum(runs, targetSum):
    for i in range(len(runs) - 1):
        firstNum = runs[i]

        for j in range(i + 1, len(runs)):
            secondNum = runs[j]

            for k in range(j + 1, len(runs)):
                thirdNum = runs[k]
                if firstNum + secondNum + thirdNum == targetSum:
                    return [firstNum, secondNum, thirdNum]
    return []

runs = [1,2,3,4,5,9,0,56,1,2,3]
print(twoSumNum(runs, 6))


    # [1,2,..n], 18
    # comparing numbers to equal total
    # other wise return nil
