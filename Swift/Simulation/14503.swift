var input = readLine()!.split(separator: " ").map{ Int($0)! }
var N = input[0], M = input[1]
input = readLine()!.split(separator: " ").map{ Int($0)! }
var ny = input[0], nx = input[1], d = input[2]
var board = [[Int]]()
for _ in 1...N { board.append(readLine()!.split(separator: " ").map{ Int($0)! }) }
var dx = [0, 0, -1, 1], dy = [-1, 1, 0, 0], ans = 0

while(true) {
    if (board[ny][nx] == 0) { board[ny][nx] = 2; ans += 1 }
    else if (board[ny][nx] == 1) { break }
    var flag = false
    for i in 0...3 {
        let X = nx+dx[i], Y = ny+dy[i]
        if (0 <= X && X < M && 0 <= Y && Y < N && board[Y][X] == 0) { flag = true; break }
    }
    if !flag {
        if d == 0 && ny+1 < N && board[ny+1][nx] != 1{ ny = ny+1 }
        else if d == 1 && nx-1 >= 0 && board[ny][nx-1] != 1{ nx = nx-1 }
        else if d == 2 && ny-1 >= 0 && board[ny-1][nx] != 1{ ny = ny-1 }
        else if d == 3 && nx+1 < M && board[ny][nx+1] != 1{ nx = nx+1 }
        else { break }
        continue
    }
    while(flag) {
        if d == 0 { d = 3 }
        else { d -= 1 }
        if d == 0 && ny-1 >= 0 && board[ny-1][nx] == 0 { ny = ny-1; break }
        else if d == 1 && nx+1 < M && board[ny][nx+1] == 0 { nx = nx+1; break }
        else if d == 2 && ny+1 < N && board[ny+1][nx] ==  0 { ny = ny+1; break }
        else if d == 3 && nx-1 >= 0 && board[ny][nx-1] ==  0 { nx = nx-1; break }
    }
}

print(ans)
