from _BinaryTree import BinaryTree
from collections import deque

#BFS Order traversal using the que.
def BFS_order_Traversal(root):
    #Base case empty root.
    if not root:
        return []
    
    #Initilize a que with the root Node.
    que  = deque([root])

    #Initialize a list to store the value.
    li = []

    #Loop untill que is Empty.
    while que:
        node = que.popleft()

        if not node:
            continue

        #Append the node Value to the list and the left and the right node to the queue.
        li.append(node.val)
        que.append(node.left)
        que.append(node.right)
    
    return li


#Example 

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)


print(BFS_order_Traversal(root))