// n 개 도시 / m 개 간선
// 0 -> 시작 도시

var board: [[[Int]]] = []
var startP: Int = 0
var minL = [Int]()
var N = 0
struct Queue {
    var In = [[Int]](), Out = [[Int]]()

    mutating func append(_ val: [Int]) {
        In.append(val)
    }

    mutating func popleft() -> [Int] {
        if Out == [] { Out = In.reversed(); In = [] }
        return Out.popLast()!
    }
}

struct Node {
    var id = -1, revenue = -1, target = -1
}
var dic = [Int: Node]()

func calculateMin(_ start: Int) {
    var que = Queue()
    minL = Array(repeating: Int.max, count: N)
    minL[start] = 0
    if N == 1 { return }
    for node in board[start] {
        let w = node[0], e = node[1]
        minL[e] = min(w, minL[e])
        que.append([w, e])
    }
    while(que.In != [] || que.Out != []) {
        let now = que.popleft()
        let w = now[0], nowNode = now[1]
        if minL[nowNode] < w { continue }
        for node in board[nowNode] {
            let nW = node[0], nE = node[1]
            if minL[nE] > nW + w {
                minL[nE] = nW + w
                que.append([minL[nE], nE])
            }
        }
    }
}

func buildLand(_ info: [Int]) {
    N = info[1]
    board = Array(repeating: [[Int]](), count: N)
    var tmp = [[Int]]()
    var idx = 3
    while(idx < info.count) {
        let v = info[idx], u = info[idx+1], w = info[idx+2]
        if v != u {
            tmp.append([min(v, u), max(v, u), w])
        }
        idx += 3
    }
    tmp = tmp.sorted{ ($0[0], $0[1], $0[2]) < ($1[0], $1[1], $1[2]) }
    if tmp != [] {
        board[tmp[0][0]].append([tmp[0][2], tmp[0][1]])
        board[tmp[0][1]].append([tmp[0][2], tmp[0][0]])
    }
    if tmp.count >= 2 {
        for i in 1..<tmp.count {
            let xV = tmp[i-1][0], xU = tmp[i-1][1]
            let v = tmp[i][0], u = tmp[i][1], w = tmp[i][2]
            if (xV != v || xU != u) {
                board[v].append([w, u])
                board[u].append([w, v])
            }
        }
    }
    calculateMin(0)
    return
}

func makeTravel(_ id: Int, _ revenue: Int, _ target: Int) {
    let node = Node(id: id, revenue: revenue, target: target)
    dic[id] = node
    return
}

func cancleTravel(_ id: Int) {
    if dic[id] != nil { dic[id] = nil }
    return
}

func saleTravel() {
    var tmp = [Node]()
    for key in dic.keys {
        tmp.append(dic[key]!)
    }
    if tmp.isEmpty { print(-1); return }
    tmp.sort { (a, b) -> Bool in
        if a.revenue - minL[a.target] < b.revenue - minL[b.target] {
            return false
        }
        else if a.revenue - minL[a.target] == b.revenue - minL[b.target] {
            if a.id > b.id { return false }
            return true
        }
        return true
    }
    let A = tmp[0]
    if ( A.revenue - minL[A.target] ) < 0 { print(-1); return }
    dic[A.id] = nil
    print(A.id)
    return
}

func changeStart(_ start: Int) {
    startP = start
    calculateMin(start)
    return
}

func main() {
    let Q = Int(readLine()!)!
    for _ in 1...Q {
        let input = readLine()!.split(separator: " ").map{ Int($0)! }
        switch input[0] {
            case 100:
                buildLand(input)
                break
            case 200:
                makeTravel(input[1], input[2], input[3])
                break
            case 300:
                cancleTravel(input[1])
                break
            case 400:
                saleTravel()
                break
            case 500:
                changeStart(input[1])
                break
            default:
                break
        }
    }
}

main()
