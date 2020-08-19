# Python3 program to construct 
# a binary tree in level order. 
  
# Importing deque for use in 
# Level Order Traversal 
from collections import deque 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

Queue=deque()

# Helper function helps us in adding data  
# to the tree in Level Order 
def insertValue(data, root):
    newnode = Node(data)
    if len(Queue) != 0:
        tempnode = Queue[0]
    if root is None:
        root = newnode

    # The left child of the current Node is 
    # used if it is available. 
    elif tempnode.left is None:
        tempnode.left = newnode

    # The right child of the current Node is used 
    # if it is available. Since the left child of this 
    # node has already been used, the Node is popped 
    # from the queue after using its right child. 
    elif tempnode.right is None:
        tempnode.right = newnode
        Queue.popleft()

    # Whenever a new Node is added to the tree,  
    # its address is pushed into the queue. 
    # So that its children Nodes can be used later. 
    Queue.append(newnode)
    return root

# Function which calls add which is responsible 
# for adding elements one by one 
def createTree(array , root):
    for i in array:
        root = insertValue(i , root)
    return root

# Function for printing level order traversal 
def levelOrder(root):
    Q = deque()
    Q.append(root)
    while len(Q) != 0:
        temp = Q.popleft()
        print(temp.data , end = " ")
        if temp.left != None:
            Q.append(temp.left)
        if temp.right != None:
            Q.append(temp.right)

# Driver Code 
a = [ 10, 20, 30, 40, 50, 60 ] 
root = None
root = createTree(a, root) 
  
levelOrder(root) 
  
# This code is contributed by prashantverma 
