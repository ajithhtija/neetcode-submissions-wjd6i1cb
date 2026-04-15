# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = 0
        r = len(inorder)-1
        return self.Bt(preorder,inorder,l,r)
    def Bt(self,preorder,inorder,start,end):
        if start==end:
            return TreeNode(inorder[start])
        flag = False
        root = None 
        for i in preorder:
            for j in range(start,end+1):
                if i == inorder[j]:
                    val = i
                    root = TreeNode(i)
                    flag = True
            if flag:
                break
        for i in range(start,end+1):
            if inorder[i]==val:
                root.left = self.Bt(preorder,inorder,start,i-1)
                root.right = self.Bt(preorder,inorder,i+1,end)
                break
        return root 
