def is_valid_move(x, y, N, visited): #檢查是否在棋盤內，且該格子未被訪問
    return 0 <= x < N and 0 <= y < N and not visited[x][y]

def knight_tour(N, startX, startY): #騎士的8個移動方向
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    visited = [[False] * N for _ in range(N)] #初始化棋盤的訪問記錄
    visited_count = 0 #記錄已訪問的格子數量
    
    def dfs(x, y, visited_count):
        visited[x][y] = True #當前格子被訪問，將其標記為已訪問
        visited_count += 1
        if visited_count == N * N:
            return True #如果已經訪問了所有格子，返回 True
        for move in moves: #嘗試每個可能的移動方向
            nx, ny = x + move[0], y + move[1]
            if is_valid_move(nx, ny, N, visited):
                if dfs(nx, ny, visited_count): #如果能夠移動到(nx,ny)，則繼續進行DFS
                    return True
        visited[x][y] = False #如果沒有可行的移動，則回溯
        return False
    return dfs(startX, startY, visited_count) #開始從起始位置進行DFS

N = int(input())  #棋盤大小
startX, startY = map(int, input().split())  #起始位置

if knight_tour(N, startX, startY): #呼叫函數並輸出結果
    print(True)
else:
    print(False)