# def recursive(data: list):
#     if len(data) == 1:
#         return data[0]
#     if data[0] % 2 == 0:
#         return -1
#     return recursive(data[1:])

def equivalent(data: list, index):
    if index == len(data) - 1:
        return data[index]
    if data[index] % 2 == 0:
        return -1
    return equivalent(data, index + 1)

data = [1, 1, 3, 2]
print(equivalent(data, 0))