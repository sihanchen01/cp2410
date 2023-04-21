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
To count number of nodes in a circular linked list, here is the code implementation:
<img src="./images/q2_implementation.png" width="600px" />

Here is the unit test:
<img src="./images/q2_unittest_code.png" width="600px" />

Running result of unit test:
<img src="./images/q2_unittest_result.png" width="600px" />

<div style="page-break-after: always;"></div>

## Question 3
```python
def checkSameCircular(x, y) -> bool:
	""" Return True if x and y belongs to the same circular linked list. """
	current = x
	while current.next != x:
		if current == y:
			return True
		current = current.next
	return False
```
We start from x, and loop through the entire circular linked list by calling x.next(). During iteration, if we found y, means x and y are in the same list, return True. Else, since x is a node in circular linked list, if we come back to x, and never find y, means x and y are not in the same list, return False.

## Question 4
Here is the implementated code for function `list_to_positional_list(L)` and its unittest:
<img src="./images/q4_implementation_and_unittest_code.png" width="600px" />

Running result of unit test:
<img src="./images/q4_unittest_result.png" width="600px" />


## Question 5
To find the maximum element in a positional list, here is the code implementation:
<img src="./images/q5_implementation.png" width="600px" />

Here is the unit test:
<img src="./images/q5_unittest_code.png" width="600px" />

Running result of unit test:
<img src="./images/q5_unittest_result.png" width="600px" />
