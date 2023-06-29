let N = Int(readLine()!)!
var ans = 0
var boards: [[[Int]]] = [[], [], []]
for _ in 1...N{
    boards[0].append( readLine()!.split(separator: " ").map{ Int($0)! } )
}
boards[1] = boards[0]
boards[2] = boards[0]
boards[0][0][1] = -1
for y in 0..<N { // y
    for x in 0..<N { // x
        if(boards[0][y][x] < 0){
            if(x+1 < N && boards[0][y][x+1] != 1){
                boards[0][y][x+1] += boards[0][y][x]
            }
            if(y+1 < N && x+1 < N && boards[1][y][x+1] != 1 && boards[1][y+1][x] != 1 && boards[1][y+1][x+1] != 1 ){
                boards[1][y+1][x+1] += boards[0][y][x]
            }
        }
        if(boards[1][y][x] < 0){
            if(x+1 < N && boards[0][y][x+1] != 1){
                boards[0][y][x+1] += boards[1][y][x]
            }
            if(y+1 < N && x+1 < N && boards[1][y][x+1] != 1 && boards[1][y+1][x] != 1 && boards[1][y+1][x+1] != 1 ){
                boards[1][y+1][x+1] += boards[1][y][x]
            }
            if(y+1 < N && boards[2][y+1][x] != 1){
                boards[2][y+1][x] += boards[1][y][x]
            }
        }
        if(boards[2][y][x] < 0){
            if(y+1 < N && x+1 < N && boards[1][y][x+1] != 1 && boards[1][y+1][x] != 1 && boards[1][y+1][x+1] != 1 ){
                boards[1][y+1][x+1] += boards[2][y][x]
            }
            if(y+1 < N && boards[2][y+1][x] != 1){
                boards[2][y+1][x] += boards[2][y][x]
            }
        }
    }
}
let out = -( boards[0].last!.last! + boards[1].last!.last! + boards[2].last!.last! )
if(out <= 0){
    print(0)
}
else{
    print(out)
}
