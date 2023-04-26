from linked_binary_tree import LinkedBinaryTree


linked_bt = LinkedBinaryTree()
pos1 = linked_bt._add_root(1)
pos2 = linked_bt._add_left(pos1, 2)
pos3 = linked_bt._add_right(pos1, 3)
pos4 = linked_bt._add_left(pos2, 4)
pos5 = linked_bt._add_right(pos2, 5)
pos6 = linked_bt._add_left(pos3, 6)
pos7 = linked_bt._add_right(pos3, 7)
pos8 = linked_bt._add_left(pos6, 8)
pos9 = linked_bt._add_right(pos6, 9)
pos10 = linked_bt._add_right(pos7, 10)

print("Inorder:")
for p in linked_bt.inorder():
    print(p.element(), end=' ')
print()

print("Preorder:")
for p in linked_bt.preorder():
    print(p.element(), end=' ')
print()

print("Postorder:")
for p in linked_bt.postorder():
    print(p.element(), end=' ')
print()
