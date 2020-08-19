# from collections import deque 
# Queue=deque()

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def insertValue(arr, root, i, n):
    if arr[i] == -1:
        return root
    if i < n:
        newnode = Node(arr[i])
        root = newnode
        root.left = insertValue(arr, root.left, 2*i+1, n)
        root.right = insertValue(arr, root.right, 2*i+2, n)
    return root
#to check if code is right
# def level(root):
#     Q=deque()
#     Q.append(root)
#     while len(Q)!=0:
#         temp=Q.popleft()
#         print(temp.data,end="")
#         if temp.left!=None:
#             print('l')
#             Q.append(temp.left)
#         if temp.right!=None:
#             print('r')
#             Q.append(temp.right)
            
bst1=list(map(int,input().split()))
bst2=list(map(int,input().split()))
root1 = insertValue(bst1, None, 0, len(bst1)) 
root2 = insertValue(bst2, None, 0, len(bst2)) 
level(root1)

