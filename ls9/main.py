# def fibonachi(N):
#     a, b = 1, 1
#     f = list([a])
#     for i in range(N):
#         a, b = b, a + b
#         f.append(a)
#     return f


# print(fibonachi(10))

# def fibonachi_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# fib = fibonachi_generator()
# for _ in range(17):
#     print(next(fib))

# Инкапсуляция, Наследие, Полимарфизм

# class MyIterator:
#     def __init__(self, iterable) -> None:
#         self.iterable = iterable
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.iterable):
#             result = self.iterable[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration


# my_list = [1, 2, 3, 4, 5]
# iter_obj = MyIterator(my_list)
# for el in iter_obj:
#     print(el)

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.children = list()

    def append(self, child_node):
        self.children.append(child_node)

    def __call__(self, level=0):
        prefix = "    " * level
        print(f"{prefix}┖──{self.value}")
        for child in self.children[:-1]:
            child(level+1)
        if self.children:
            self.children[-1](level + 1)


root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_ba = TreeNode("BA")
node_bc = TreeNode("BC")

root.append(node_b)
root.append(node_c)
node_b.append(node_ba)
node_b.append(node_bc)

root()
