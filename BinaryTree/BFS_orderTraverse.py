from _BinaryTree import BinaryTree
from collections import deque

#BFS Order traversal using the que.
def level_order_Traversal(root) -> list[int]:
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

def level_order_traversal_1(root) -> list[list[int]]:
    #Base Case if tree is None.
    if not root:
        return []

    #Initializing the Deque and the list to store the result.
    que = deque([root])
    li = []

    #loop while que.
    while que:
        length = len(que)
        
        #list to store the level result 
        l = []

        for i in range(length):
            node = que.popleft()
            l.append(node.val)
            
            #Adding node to the que if if left and rigth is not Null
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        li.append(l)
    return li
    


#Example 

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)


print(level_order_Traversal(root))
print(level_order_traversal_1(root))