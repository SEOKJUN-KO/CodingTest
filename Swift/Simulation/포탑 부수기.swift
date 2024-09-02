// board = 10^2
// 10^3
// 최소 값 찾기 & 최대 값 찾기 - 10^2 -> 0 제외 -> 감소 => 10^5
// 경로 찾기 - 10000 => 10^6

var N = 0, M = 0, K = 0
var board = [[Tower]]()

struct Queue {
    var In = [[Int]]()
    var Out = [[Int]]()
    mutating func append(_ val:[Int]) { In.append(val) }
    mutating func popleft() -> [Int] {
        if Out.count == 0 { Out = In.reversed(); In = [] }
        return Out.popLast()!
    }
}

var turn = 0
struct Tower {
    var power = 0
    var recent = 0
    var y = 0
    var x = 0
    var attacked = 0
    mutating func changePower(_ k: Int) {
        self.power += (N + M)
        self.recent = k
    }
    mutating func repair() { self.power += 1 }
    mutating func hit(_ power: Int) {
        self.power -= power
        self.attacked = turn
    }
}

struct Check {
    var weight: Int = 999999
    var past: String = ""
}


func __init__() {
    let input = readLine()!.split(separator: " ").map{ Int($0)! }
    N = input[0]; M = input[1]; K = input[2]
    for y in 0..<N {
        let tmp = readLine()!.split(separator: " ").map{ Int($0)! }
        var tmpArr = [Tower]()
        for x in 0..<M {
            let tower = Tower(power: tmp[x], y: y, x: x)
            tmpArr.append(tower)
        }
        board.append(tmpArr)
    }
}

func choose() -> [Tower] { // 10^5
    var attack = Tower(power: Int.max, recent: 0, y: 0, x: 0)
    var defend = Tower(power: 0, recent: Int.max, y: Int.max, x: Int.max)
    for y in 0..<N {
        for x in 0..<M {
            let tower = board[y][x]
            if tower.power <= 0 { continue }
            if attack.power > tower.power { attack = board[y][x] }
            else if attack.power == tower.power {
                if attack.recent < tower.recent { attack = board[y][x] }
                else if attack.recent == tower.recent {
                    if (attack.y + attack.x) < (y+x) { attack = board[y][x] }
                    else if (attack.y + attack.x) == (y+x) && attack.x < x { attack = board[y][x] }
                }
            }

            if defend.power < tower.power { defend = board[y][x] }
            else if defend.power == tower.power {
                if defend.recent > tower.recent { defend = board[y][x] }
                else if defend.recent == tower.recent {
                    if (defend.y + defend.x) > (y+x) { defend = board[y][x] }
                    else if (defend.y + defend.x) == (y+x) && defend.x > x { defend = board[y][x] }
                }
            }
        }
    }
    return [ attack, defend ]
}

func findPath(_ attackY:Int, _ attackX:Int, _ defendY: Int, _ defendX: Int) { // 최대 10^7
    var que = Queue()
    que.append([attackY, attackX, 0])
    var check = Array(repeating: Array(repeating: Check(), count: M), count: N)
    check[attackY][attackX] = Check(weight: 0)
    let dx = [1, 0, -1, 0], dy = [0, 1, 0, -1]
    var flag = false
    while(que.In.count != 0 || que.Out.count != 0) {
        let out = que.popleft()
        let y = out[0], x = out[1], w = out[2]
        for i in 0..<4 {
            var Y = y+dy[i], X = x+dx[i]
            if Y >= N { Y = 0 }; if X >= M { X = 0 }
            if Y < 0 { Y = N-1 }; if X < 0 { X = M-1 }
            if board[Y][X].power <= 0 { continue }
            if check[Y][X].weight > w + 1 {
                check[Y][X] = Check(weight: w+1, past: String(y)+" "+String(x))
                if Y == defendY && X == defendX { flag = true; break }
                que.append([Y, X, w+1])
            }
        }
        if flag { break }
    }
    if flag {
        var start = check[defendY][defendX].past.split(separator:" ").map{ Int($0)! }
        var Y = start[0], X = start[1]
        var power = board[attackY][attackX].power
        board[defendY][defendX].hit(power)
        power = power/2
        while( Y != attackY || X != attackX ) {
            board[Y][X].hit(power)
            let tmp = check[Y][X].past.split(separator:" ").map{ Int($0)! }
            Y = tmp[0]; X = tmp[1]
        }
    }
    else {
        var power = board[attackY][attackX].power
        if turn == K { print(power) }
        board[defendY][defendX].hit(power)
        power = power/2
        for y in [-1, 0, 1] {
            for x in [-1, 0, 1] {
                if (y == 0 && x == 0) || (y == attackY && x == attackX) { continue }
                var Y = defendY-y, X = defendX-x
                if Y >= N { Y = 0 }; if X >= M { X = 0 }
                if Y < 0 { Y = N-1 }; if X < 0 { X = M-1 }
                if board[Y][X].power <= 0 { continue }
                board[Y][X].hit(power)
            }
        }
    }
    for y in 0..<N {
        for x in 0..<M {
            if board[y][x].power <= 0 {
                continue
            }
            if !(board[y][x].recent == turn || board[y][x].attacked == turn) { board[y][x].repair() }
        }
    }
}

func findOne() {
    var ans = 0
    for y in 0..<N {
        for x in 0..<M {
            if ans < board[y][x].power { ans = board[y][x].power }
        }
    }
    print(ans)
}

__init__()
for k in 1...K {
    turn = k
    let ret = choose()
    let attackY = ret[0].y, attackX = ret[0].x, defendY = ret[1].y, defendX = ret[1].x
    board[attackY][attackX].changePower(k)
    findPath(attackY, attackX, defendY, defendX)
}
findOne()
