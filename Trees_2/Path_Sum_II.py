# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space - O(n)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target = targetSum     #Initialize target to targetSum
        self.result = []    #Initialize a result array 
        self.rootSum(root, 0, [])   #Recursion
        return self.result  #Return result which gives the sum of the path
        
    def rootSum(self, root, currSum, path):     #Recursive function passed with root, currSum and path
        #base condition
        if root == None:    #If the root is none the return which unfolds the recursion 
            return 
        currSum+= root.val  #Calculate currSum by adding it with root.val
        path.append(root.val)   #Append the root.val to path
        
        self.rootSum(root.left, currSum, path)  #Recursive call for the left side of the tree

        if root.left == None and root.right == None:       #If there is no left and right for the root then the leaf has been hit
            if currSum == self.target:  #If the currSum is equal to the target 
                temp = path[:]  #Copy the path not as reference instead do a deep copy which copies the values and store it in temp
                self.result.append(temp)    #Append the temp into the result array
        
        self.rootSum(root.right, currSum, path) #Recursive call for the right side of the tree
        path.pop()  #Pop the last element in the path array
        
        
        