def josephus(n, k):
    people = list(range(1, n + 1)) #用列表來表示所有人，列表中的每個元素對應每個人的編號
    index = 0 #記錄當前需要刪除的位置
    while len(people) > 1: #直到只剩下1個人
        index = (index + k - 1) % len(people) #計算應該刪除的人位置，這是循環計數
        people.pop(index) #刪除該人
    return people[0] #返回最後剩下的人的編號

n, k = map(int, input().split())
print(josephus(n, k)) #輸出最後剩下的人的編號