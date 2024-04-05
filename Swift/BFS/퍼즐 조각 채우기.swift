struct Queue {
    var (In, Out) = ([[Int]](), [[Int]]())
    func isEmpty() -> Bool {
        if In.isEmpty && Out.isEmpty {
            return true
        }
        return false
    }
    mutating func append(_ val: [Int]) {
        In.append(val)
    }
    mutating func popleft() -> [Int] {
        if Out.isEmpty {
            Out = In.reversed()
            In = []
        }
        return Out.popLast()!
    }
}
var queue = Queue()
var inDict = [Int: [String]]()
var outDict = [Int: [String]]()
var blockDict = [String: Int]()
var blockArr = [String]()
var ans = 0
let (dy, dx, dd) = ([+1, -1, +0, +0], [+0, +0, +1, -1], ["d", "u", "r", "l"])

func divideBlock (_ board: [[Int]], _ mode: Int) -> [[[Int]]] {
    var board = board
    let L = board.count
    var outArr = [[[Int]]]()
    var cnt = 2
    for y in 0..<L {
        for x in 0..<L {
            var (minX, maxX, minY, maxY) = (14, 0, 14, 0)
            var position = [[Int]]()
            if board[y][x] == mode {
                queue.append([y, x])
                board[y][x] = cnt
                while( !queue.isEmpty() ) {
                    let out = queue.popleft()
                    let (ny, nx) = (out[0], out[1])
                    position.append([ny, nx])
                    if minX > out[1] { minX = out[1] }
                    if maxX < out[1] { maxX = out[1] }
                    if minY > out[0] { minY = out[0] }
                    if maxY < out[0] { maxY = out[0] }
                    for i in 0...3 {
                        let (Y, X) = (ny+dy[i], nx+dx[i])
                        if 0 <= Y && Y < L && 0 <= X && X < L && board[Y][X] == mode {
                            board[Y][X] = cnt
                            queue.append([Y, X])
                        }
                    }
                }
                let leng = max(maxX-minX+1, maxY-minY+1)
                var tmp = Array(repeating: Array(repeating: 0, count: leng), count: leng)
                for p in position {
                    let (ny, nx) = (p[0]-minY, p[1]-minX)
                    tmp[ny][nx] = cnt
                }
                outArr.append(tmp)
                cnt += 1
            }
        }
    }
    return outArr
}

func makeString(_ arr: [[[Int]]], _ mode: Int) {
    for block in arr {
        var go = block
        for y in 0..<block.count {
            for x in 0..<block.count {
                if go[y][x] > 1 {
                    let key = go[y][x]
                    var tmp = "s"
                    queue.append([y, x])
                    go[y][x] = 0
                    var cnt = 1
                    while( !queue.isEmpty() ) {
                        let out = queue.popleft()
                        let (ny, nx) = (out[0], out[1])
                        for i in 0...3 {
                            let (Y, X, D) = (ny+dy[i], nx+dx[i], dd[i])
                            if 0 <= Y && Y < block.count && 0 <= X && X < block.count && go[Y][X] > 1 {
                                go[Y][X] = 0
                                queue.append([Y, X])
                                tmp += "\(y-ny)\(x-nx)\(D)"
                                cnt += 1
                            }
                        }
                    }
                    if mode == 0 {
                        if inDict[key] == nil { inDict[key] = [String]() }
                        inDict[key]!.append(tmp+".\(cnt)")
                    }
                    else {
                        if outDict[key] == nil { outDict[key] = [String]() }
                        outDict[key]!.append(tmp+".\(cnt)")
                    }
                }
            }
        }
    }
}

func rotate(_ arr: [[Int]]) -> [[Int]] {
    var arr = arr
    var before = arr
    for y in 0..<before.count {
        for x in 0..<before.count {
            arr[x][before.count - y - 1] = before[y][x]
        }
    }
    return arr
}

func solution(_ game_board:[[Int]], _ table:[[Int]]) -> Int {
    var gameBlock = divideBlock(game_board, 0)
    var tableBlock = divideBlock(table, 1)
    for k in 0...1 {
        for a in 0...3 {
            if k == 0 {
                makeString(gameBlock, 0)
                for i in 0..<gameBlock.count { gameBlock[i] = rotate(gameBlock[i]) }
            }
            else {
                makeString(tableBlock, 1)
                for i in 0..<tableBlock.count { tableBlock[i] = rotate(tableBlock[i]) }
            }
        }
    }
    var IN = [[String]: Int]()
    var OUT = [[String]: Int]()
    for key in inDict.keys {
        inDict[key] = Array(Set(inDict[key]!)).sorted(by: { $0 < $1 })
        if IN[inDict[key]!] == nil { IN[inDict[key]!] = 0 }
        IN[inDict[key]!]! += 1
    }
    for key in outDict.keys {
        outDict[key] = Array(Set(outDict[key]!)).sorted(by: { $0 < $1 })
        if OUT[outDict[key]!] == nil { OUT[outDict[key]!] = 0 }
        OUT[outDict[key]!]! += 1
    }
    let keyArr = Set(IN.keys).intersection(Set(OUT.keys))
    for key in keyArr {
        let m = min( IN[key]!, OUT[key]! )
        let tmp = key.last!.split(separator: ".")
        ans += m*Int(tmp[1])!
    }
    return ans
}
