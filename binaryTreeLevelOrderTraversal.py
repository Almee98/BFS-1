# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : O(h) + couple extra nodes which will be present in the queue while traversing the tree
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We will use a queue to perform a level order traversal of the binary tree.
# Starting from the root node, we will add all the nodes at the current level to the queue.
# For each node, we will pop it from the queue and add its left and right children to the queue, thus processing the node.
# We will continue this process until the queue is empty.
# We will also keep track of the current level and add all the nodes at that level to a list. We will do this by taking a snapshot of the queue at the start of each level.
# We will return the list of lists containing the values of the nodes at each level.

# Definition for a binary tree node.
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        # Using a queue to perform level order traversal
        que = deque()
        # Initializing the resultant list
        res = []
        # If the root is not null, we add it to the queue
        # This will be our starting point
        if root:
            que.append(root)

        # While the queue is not empty, we will continue processing the nodes
        while que:
            # We will take a snapshot of the current level
            size = len(que)
            # We will create a list to store the values of the nodes at this level
            level = []
            # We will process all the nodes at this level
            for i in range(size):
                # For each node, we will pop it from the queue and add its value to the list
                curr = que.popleft()
                level.append(curr.val)
                # We will also add its left and right children to the queue
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            # After processing all the nodes at this level, we will add the list to the resultant list
            res.append(level)
        # Finally, we will return the resultant list
        return res

# Alternative approach using DFS
# Time complexity: O(n), where n is the number of nodes in the binary tree
# Space complexity: O(h), where h is the height of the binary tree
# In this approach, we will use a recursive function to traverse the binary tree.
# We will keep track of the current level and add the values of the nodes to a dictionary, at the corresponding level.
# Finally, we will traverse the dictionary in a bucket sort manner, adding the values to the resultant list.
class Solution:
    def levelOrder(self, root):
        # Initializing a dictionary to store the values of the nodes at each level
        levels = defaultdict(list)

        # Recursive function to traverse the binary tree
        def dfs(root, l):
            # Base case: if the root is null, we return, this means we have reached a leaf node
            if not root:
                return

            # If the current level is not present in the dictionary, we will create a new list for it, and append the value of the node to it
            levels[l].append(root.val)
            # We will then recursively call the function for the left and right children of the node, incrementing the level by 1
            # This will ensure that the values of the nodes at the same level are added to the same list in the dictionary
            dfs(root.left, l+1)
            dfs(root.right, l+1)

        dfs(root, 0)
        res = []
        # We will traverse the dictionary in a bucket sort manner, adding the values to the resultant list
        for key, val in levels.items():
            res.append(val)
        # Finally, we will return the resultant list
        return res
    
# Alternative approach using DFS, without using a dictionary
# Time complexity: O(n), where n is the number of nodes in the binary tree
# Space complexity: O(h), where h is the height of the binary tree
# This approach is similar to the previous one, but instead of using a dictionary to store the values of the nodes at each level, store them directly to the resultant array.
# We assume that the keys of the dictionary are index of the resultant array.

class Solution:
    def levelOrder(self, root):
        # Initializing the resultant list
        res = []
        # Recursive function to traverse the binary tree
        def dfs(root, level):
            # Base case: if the root is null, we return, this means we have reached a leaf node
            if not root:
                return

            # If the current level is not present in the resultant list, we will create a new list for it
            # This has to be done in a pre-oreder fashion, so that we can add the values of the nodes at the same level to the same list
            if len(res) == level:
                res.append([])
            # We will then append the value of the node to the list at the current level
            # This will ensure that the values of the nodes at the same level are added to the same list in the resultant list
            res[level].append(root.val)
            # We will then recursively call the function for the left and right children of the node, incrementing the level by 1
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, 0)
        # Finally, we will return the resultant list
        return res