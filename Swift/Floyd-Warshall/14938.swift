var inputs = readLine()!.split(separator: " ").map{ Int($0)! }
var n = inputs[0], m = inputs[1], r = inputs[2]
var items = readLine()!.split(separator: " ").map{ Int($0)! }
var board = Array(repeating: Array(repeating: Int.max, count: n), count: n)

for _ in 1...r {
    inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    board[inputs[0]-1][inputs[1]-1] = inputs[2]
    board[inputs[1]-1][inputs[0]-1] = inputs[2]
}

for k in 0..<n {
    board[k][k] = 0
}

for k in 0..<n {
    for i in 0..<n {
        for j in 0..<n {
            if board[i][k] != Int.max && board[k][j] != Int.max && board[i][j] > board[i][k] + board[k][j] {
                board[i][j] = board[i][k] + board[k][j]
            }
        }
    }
}
var ans = 0
for i in 0..<n {
    var tmp = 0
    for j in 0..<n {
        if board[i][j] != Int.max && board[i][j] <= m {
            tmp += items[j]
        }
    }
    if ans < tmp {
        ans = tmp
    }
}
print(ans)
