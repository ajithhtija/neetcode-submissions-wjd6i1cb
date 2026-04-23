# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        q = []
        null = None 
        q.append(root)
        while q:
            cnt = len(q)
            for i in range(cnt):
                curr = q.pop(0)
                if curr==None:
                    ans.append('n#')
                    continue
                ans.append(str(curr.val))
                ans.append('#')
                q.append(curr.left)
                q.append(curr.right)
        return "".join(ans)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        temp = data.split('#')
        if temp[0]=='n':
            return None
        i = 1
        q = []
        print(temp)
        root = TreeNode(int(temp[0]))
        m = len(temp)
        q.append(root)
        while i<m and temp[i]!='':
            curr = q.pop(0)
            if i<m-1 and temp[i]!='n':
                curr.left = TreeNode(int(temp[i]))
                q.append(curr.left)
            i+=1
            if i<m-1 and temp[i]!='n':
                curr.right = TreeNode(int(temp[i]))
                q.append(curr.right)
            i+=1       
        return root
