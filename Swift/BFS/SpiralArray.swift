https://school.programmers.co.kr/learn/courses/30/lessons/181832#

let dx = [ +1, +0, -1, +0 ]
let dy = [ +0, +1, +0, -1 ]
func solution(_ n:Int) -> [[Int]] {
    if(n == 1){
        return [[1]]
    }
    var board = Array(repeating: Array(repeating: 0, count: n), count: n)
    var p = 0
    var num = 1
    var nx = 0
    var ny = 0
    while( board[ny][nx] == 0 ){
        board[ny][nx] = num
        num += 1
        var tny = ny+dy[p]
        var tnx = nx+dx[p]
        if( 0 <= tny && tny < n &&  0 <= tnx && tnx < n  && board[tny][tnx] == 0){
            ny = tny
            nx = tnx
        }
        else{
            p = (p+1)%4
            ny = ny+dy[p]
            nx = nx+dx[p]
        }
    }
    return board
}

