
board = [1,2,3,4,5,6,7,8,9]

data = input("")
print(data)

k = 1
for i in range(int(data[0])):
    board[int(data[k])-1] = data[k+1]
    k += 2

print(board)
