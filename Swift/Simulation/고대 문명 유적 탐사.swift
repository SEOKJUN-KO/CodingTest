var K = 0, M = 0
var board = [[Int]]()
var pieces = [Int](), pIdx = 0
var visit = Array(repeating: Array(repeating: false, count: 5), count: 5)
var ans = 0

struct Deque {
    var In = [[Int]](), Out = [[Int]]()
    func isEmpty() -> Bool { return (In.count == 0 && Out.count == 0) }
    mutating func append(_ val:[Int]) { In.append(val) }
    mutating func popleft() -> [Int] {
        if Out.count == 0 { Out = In.reversed(); In = [] }
        return Out.popLast()!
    }
}

// 탐사 진행
// 5*5 격자 | 3*3 격자 - 90도 180도 270도 회전
// 유물 1차 획득 가치 최대화
// 1. 회전 각도 최소 2. 중심 열 최소 3. 중심 행 최소
let dy = [-1, 1, 0, 0], dx = [0, 0, -1, 1]
func bfs(_ Y: Int, _ X: Int, _ mode: Int) -> Int {
    if visit[Y][X] { return 0 }
    var deque = Deque()
    deque.append([Y, X]); visit[Y][X] = true
    var tmp = [[Int]](); tmp.append([Y,X])
    while(!deque.isEmpty()) {
        let out = deque.popleft()
        let ny = out[0], nx = out[1]
        for i in 0...3 {
            let y = ny+dy[i], x = nx+dx[i]
            if !( 0 <= y && y < 5 && 0 <= x && x < 5 ) { continue }
            if board[Y][X] == board[y][x] && !visit[y][x] {
                deque.append([y, x]); visit[y][x] = true
                tmp.append([y, x])
            }
        }
    }
    if tmp.count >= 3 {
        if mode == 0 { return tmp.count  }
        else {
            for t in tmp {
                let y = t[0], x = t[1]
                board[y][x] = 0
            }
        }
    }
    return 0
}

func howMany() -> Int {
    visit = Array(repeating: Array(repeating: false, count: 5), count: 5)
    var cnt = 0
    for y in 0..<5 { for x in 0..<5 { cnt += bfs(y, x, 0) } }
    return cnt
}

func rotate(_ Y:Int, _ X: Int) {
    var tmp = [Int](), idx = 0
    for y in [Y+1, Y, Y-1] { tmp.append(board[y][X-1]) }
    tmp.append(board[Y-1][X])
    for y in [Y-1, Y, Y+1] { tmp.append(board[y][X+1]) }
    tmp.append(board[Y+1][X])
    
    for x in [X-1, X, X+1] { board[Y-1][x] = tmp[idx]; idx += 1}
    board[Y][X+1] = tmp[idx]; idx += 1
    for x in [X+1, X, X-1] { board[Y+1][x] = tmp[idx]; idx += 1}
    board[Y][X-1] = tmp[idx]
}

func findBest() -> [Int] {
    var bigValue = 0, smallAngle = 3, smallX = 3, smallY = 3
    for y in 1...3 {
        for x in 1...3 {
            for r in 1...4 {
                rotate(y, x)
                let out = howMany()
                if r == 4 { break }
                if bigValue < out { bigValue = out; smallAngle = r; smallX = x; smallY = y}
                else if bigValue == out && smallAngle > r { bigValue = out; smallAngle = r; smallX = x; smallY = y}
                else if bigValue == out && smallAngle == r && smallX > x { bigValue = out; smallAngle = r; smallX = x; smallY = y}
                else if bigValue == out && smallAngle == r && smallX == x && smallY > y { bigValue = out; smallAngle = r; smallX = x; smallY = y}
            }
        }
    }
    return [bigValue, smallAngle, smallX, smallY]
}

// 유물 획득
// 1) 1차 획득
// 상하좌우 인접 유물 3개 이상 -> 제거
// 새 조각 채우기
// 2) 연쇄 획득
func fill() -> Int {
    var cnt = 0
    for x in 0..<5 { for y in (0..<5).reversed() {
        if board[y][x] == 0 { board[y][x] = pieces[pIdx]; pIdx += 1; cnt += 1; ans += 1 } }
    }
    return cnt
}

func gainAndSetting(_ value: Int, _ angle: Int, _ Y: Int, _ X: Int) {
    for _ in 1...angle { rotate(Y, X) }
    while(true) {
        visit = Array(repeating: Array(repeating: false, count: 5), count: 5)
        for y in 0..<5 { for x in 0..<5 { _ = bfs(y, x, 1) }}
        let out = fill()
        if out == 0 { break }
    }
}

func main() {
    var input = readLine()!.split(separator: " ").map{ Int($0)! }
    K = input[0]; M = input[1]
    for _ in 1...5 { board.append(readLine()!.split(separator: " ").map{ Int($0)! }) }
    pieces = readLine()!.split(separator: " ").map{ Int($0)! }
    for _ in 1...K {
        ans = 0
        let out = findBest()
        if out[0] == 0 { break }
        gainAndSetting( out[0], out[1], out[3], out[2] )
        print(ans, terminator: " ")
    }
}

main()
