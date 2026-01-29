from pickle import OBJ


class ObjectList:
    def __init__(self, data = None):
        if data is None:
            data = []
        self.data = data
    def __add__(self, other):
        newdata = self.data[:]
        if isinstance(other, ObjectList):
            newdata.extend(other.data)
        elif  isinstance(other, list) or isinstance(other, dict):
            newdata.extend(other)
        else:
            newdata.append(other)
        return ObjectList(newdata)
    def iterator(self, type):
        return TypeIterable(self.data, type)

class TypeIterable:
    def __init__(self, data, type):
        self.data = data
        self.type = type
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.data):
            current = self.data[self.index]
            self.index += 1
            if isinstance(current, self.type):
                return current
        raise StopIteration

data1 = ObjectList([1, [2, 3], "aa", {2: 2}])
data2 = ObjectList([1, 2, [2, 3], "aa", {2: 2}])
data = ObjectList()
data += data1
print(data.data)






# class ObjectList:
#     def __init__(self, data = None):
#         if data is None:
#             data = []
#         self.data = data
#     def __add__(self, other):
#         newdata = self.data[:]
#         if isinstance(other, ObjectList):
#             newdata.extend(other.data)
#         elif  isinstance(other, list) or isinstance(other, dict):
#             newdata.extend(other)
#         else:
#             newdata.append(other)
#         return ObjectList(newdata)
#     def iterator(self, type):
#         return TypeIterable(self.data, type)
#
# class TypeIterable:
#     def __init__(self, data, type):
#         self.data = data
#         self.type = type
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index < len(self.data):
#             current = self.data[self.index]
#             self.index += 1
#             if isinstance(current, self.type):
#                 return current
#         raise StopIteration
#
# data1 = ObjectList([1, [2, 3], "aa", {2: 2}])
# data2 = ObjectList([1, 2, [2, 3], "aa", {2: 2}])
# data = ObjectList()
# data += data1
# print(data.data)
#
# class Product:
#     def __init__(self, name, type, price):
#         self.name = name
#         self.type = type
#         self.price = price
#     def __repr__(self):
#         return f"{self.name} {self.type} {self.price}"
# class ProductIterable:
#     def __init__(self, data=None):
#         if data is None:
#             data = []
#         self.data = data
#     def __iter__(self):
#         return iter(self.data)
#
# a = ProductIterable([Product("b", 0, 10), Product("a", 0, 2)])
#
# a = sorted(a, key=lambda product: product.name)
# a = sorted(a, key=lambda product: product.price, reverse=True)
# for i in a:
#     print(i)