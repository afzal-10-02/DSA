from BinaryTree import BinaryTree

class Traversal:
    #Post Order Traversal.
    def Pre_Order(self , root): 
        if not root:
            return []
    
        return [root.val] + self.Pre_Order(root.left) + self.Pre_Order(root.right)
    
    #In Order Traversal
    def In_Order(self , root):
        if not root:
            return []
    
        return  self.In_Order(root.left) + [root.val] + self.In_Order(root.right)
    
    #Post Order Traversal
    def Post_Order(self , root):
        if not root:
            return []
    
        return self.Post_Order(root.left) + self.Post_Order(root.right) + [root.val]

#Binary Tree Creation
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.right.left = BinaryTree(9)
root.left.right.right = BinaryTree(10)
root.right.right.right = BinaryTree(11)


obj = Traversal()
print(obj.In_Order(root)) 
print(obj.Post_Order(root))
print(obj.Pre_Order(root))
