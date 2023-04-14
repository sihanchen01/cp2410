from array_queue import ArrayQueue
from deque import Deque

Q = ArrayQueue()
D = Deque()
for i in range(1, 9):
  D.add_last(i)

# First we need to remove redundant elements from ArrayQueue
# if size of D is smaller than Q's DEFAULT CAPACITY 
if D.size() < Q.DEFAULT_CAPACITY:
  Q._data = D.size() * [None]

print(f"Queue Q has content: {Q._data}")
print(f"Deque D has content: {D.print_queue()}")

# To let Q ends up with [1, 2, 3, 4, 5, 6, 7, 8]
while not D.is_empty():
  Q.enqueue(D.delete_first())

print(f"After operations, the queue Q has content: {Q._data}")
print(f"After operations, the deque D has content: {D.print_queue()}")

