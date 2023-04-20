# CP2410 Practical 05
## Sihan Chen, jcu ID: 14187662

## Question 1
```python
def find_second_to_last(head):
	cur, prev = head, head
	while cur._next:
		prev = cur
		cur = cur._next
	return prev
```
Assuming we are given the head node of the singly linked list. We will use `prev` and `cur`, two pointers to iterate through singly linked list. 'prev' will be the node before 'cur', and when the while loop finishes, 'cur' will point at the last node and 'prev' will be the second to last node.

## Question 2
```python
def count_number_of_nodes(head):
	node = head
	seen = []
	count = 0
	while node not in seen:
		count += 1
		seen.append(node)
		node = node._next
	return count
```

## Question 3
```python
def in_same_list(x, y):
	cur = x
	while cur != x:
		if cur == y:
			return True
		cur = cur._next
	return False
```

## Question 4
```python
from positional_list import PositionalList
def list_to_positional_list(L: list):
	positional_list = PositionalList()
	for ele in L:
		positional_list.add_last(ele)
	return positional_list
```

## Question 5
```python
def find_max(P: PositionalList):
	node = PositionalList.first()
	result = float('-inf')
	while node:
		result = max(result, node._element)
		node = node._next
	return result
```
