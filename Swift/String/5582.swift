let inputA = Array(readLine()!)
let inputB = Array(readLine()!)

var ans = 0
var board = Array(repeating: Array(repeating: 0, count: inputA.count), count: inputB.count)
for i in 0..<inputA.count {
    if( inputB[0] == inputA[i] ){
        board[0][i] = 1
        ans = 1
    }
}

for i in 0..<inputB.count {
    if(inputA[0] == inputB[i]){
        board[i][0] = 1
        ans = 1
    }
}

if( inputB.count >= 1 ) {
    for y in 1..<inputB.count{
        for x in 1..<inputA.count{
            if( inputB[y] == inputA[x] ){
                board[y][x] = board[y-1][x-1] + 1
                if ( ans < board[y][x] ){
                    ans = board[y][x]
                }
            }
        }
    }
}
print(ans)
