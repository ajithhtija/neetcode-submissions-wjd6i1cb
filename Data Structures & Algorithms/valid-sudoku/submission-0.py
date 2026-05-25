class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row wise checking 
        r = len(board)
        c = len(board[0])
        for i in range(0,r):
            s = set()
            cnt = 0
            for j in range(0,c):
                if board[i][j]!='.':
                    cnt+=1
                    if int(board[i][j])>9 or int(board[i][j])==0:
                        return False
                    else:
                        s.add(board[i][j])
            if len(s)!=cnt:
                return False
        for i in range(0,c):
            s = set()
            cnt = 0
            for j in range(0,r):
                if board[j][i]!='.':
                    cnt+=1
                    if int(board[j][i])>9 or int(board[j][i])==0:
                        return False
                    else:
                        s.add(board[j][i])
            if len(s)!=cnt:
                return False
        
        for m in range(0,9,3):
            for k in range(0,9,3):
                s = set()
                cnt = 0
                for i in range(0,3):
                    for j in range(0,3):
                        c = board[i+m][j+k]
                        if c !='.':
                            cnt+=1
                            if int(c)>9 or int(c)==0:
                                return False
                            else:
                                s.add(c)
                if len(s)!=cnt:
                    return False
        return True







                    






        