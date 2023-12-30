# def max_number(l):
#     pointer = l[0]
#     for el in l[1::]:
#         if el > pointer:
#             pointer = el

#     return pointer


# a = [1, 2, 3, 4, 5, 8, 1, 12]
# print(max(a))
# print(sorted(a)[len(a)-1])
# print(max_number(a))


# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             raise IndexError("Cannot dequeue from an empty queue")

#     def __str__(self):
#         return f"{self.items}"


# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print(queue.dequeue())
# print(queue)

def last_remaining_list(n, m):
    prisoners = list(range(1, n+1))
    index = 0
    while len(prisoners) > 1:
        index = (index + m - 1) % len(prisoners)
        prisoners.pop(index)
    return prisoners[0]


n = 13
m = 3

print(last_remaining_list(n, m))
