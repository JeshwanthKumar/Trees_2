# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space - O(n)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0     #Initialize result to 0 which is the sum
        
        self.inorder(root, 0)   #Recursion
        return self.result  #Return the result which gives the sum from root to left
        
    def inorder(self, root, currSum):   #Recursive function with root and currSum
        #base condition
        if root == None:    #If the root is none then return which unfolds the recursion
            return 
        currSum = currSum*10+root.val   #Calculate the currSum by multiplying it with 10 and adding with root.val through which when we reach the node itslef the sum is calculated
        self.inorder(root.left, currSum)    #Recursive call for the left side of the tree 
        
        if root.left == None and root.right == None:    #If there is no left and right then the leaf has been hit, add the currSum to the result
            self.result += currSum
        
        self.inorder(root.right, currSum)   #Recursive call for the right side of the tree