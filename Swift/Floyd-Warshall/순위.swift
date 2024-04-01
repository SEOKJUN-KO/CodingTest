func solution(_ n:Int, _ results:[[Int]]) -> Int {
    var board = Array(repeating: Array(repeating: 0, count: n+1 ), count: n+1)
    for result in results {
        let (win, lose) = (result[0], result[1])
        board[win][lose] = 1
    }
    for k in (1...n) {
        for i in (1...n) {
            for j in (1...n) {
                if board[i][k] == 1 && board[k][j] == 1 {
                    board[i][j] = 1
                }
            }
        }
    }
    var ans = 0
    for i in (1...n) {
        var cnt = 0
        for j in (1...n) {
            if board[i][j] == 1 || board[j][i] == 1 {
                cnt += 1
            }
        }
        if cnt >= n-1 { ans += 1 }
    }
    return ans
}
