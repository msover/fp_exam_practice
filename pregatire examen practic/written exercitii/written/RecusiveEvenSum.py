numList = [1, 2, 3, 4, 5]

def recursive(numList, left, right):
    if left > right:
        return 0
    if left == right:
        if numList[left] % 2 == 0:
            return numList[left]
        return 0

    mid = (left + right) // 2

    leftSum = recursive(numList, left, mid)
    rightSum = recursive(numList, mid + 1, right)
    return leftSum + rightSum

print(recursive(numList, 0, len(numList) - 1))
