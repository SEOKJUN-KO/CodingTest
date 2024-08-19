// n 개 도시 / m 개 간선
// 0 -> 시작 도시

var board: [[[Int]]] = []
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

struct MaxHeap {
    var tree = [ Node() ]

    mutating func append(_ node: Node) {
        tree.append(node)
        var idx = tree.count-1
        while(idx/2 > 0) {
            let pid = idx/2
            if (tree[pid].revenue - minL[tree[pid].target] < tree[idx].revenue - minL[tree[idx].target]) {
                (tree[pid], tree[idx]) = (tree[idx], tree[pid])
                idx = pid
                continue
            }
            else if (tree[pid].revenue - minL[tree[pid].target] == tree[idx].revenue - minL[tree[idx].target]) && (tree[pid].id > tree[idx].id ) {
                (tree[pid], tree[idx]) = (tree[idx], tree[pid])
                idx = pid
                continue
            }
            break
        }
    }

    mutating func pop() -> Node {
        if (tree.count == 1) || (tree[1].revenue - minL[tree[1].target] < 0) { return Node() }
        if tree.count == 2 { return tree.popLast()! }
        let r = tree[1]
        tree[1] = tree.popLast()!
        var idx = 1
        while(idx < tree.count) {
            var tmp = idx
            let L = 2*idx, R = 2*idx+1
            if ( L < tree.count && (tree[tmp].revenue - minL[tree[tmp].target] < tree[L].revenue - minL[tree[L].target] ) ) {
                tmp = L
            }
            else if ( L < tree.count && (tree[tmp].revenue - minL[tree[tmp].target] == tree[L].revenue - minL[tree[L].target])&&(tree[tmp].id > tree[L].id) ) {
                tmp = L
            }
            if ( R < tree.count && (tree[tmp].revenue - minL[tree[tmp].target] < tree[R].revenue - minL[tree[R].target] ) ) {
                tmp = R
            }
            else if ( R < tree.count && (tree[tmp].revenue - minL[tree[tmp].target] == tree[R].revenue - minL[tree[R].target])&&(tree[tmp].id > tree[R].id) ) {
                tmp = R
            }
            if idx == tmp { break }
            (tree[idx], tree[tmp]) = (tree[tmp], tree[idx])
            idx = tmp
        }
        return r
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
    
    if N > 1 {
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
    heap.tree = [Node()]
    for key in dic.keys {
        heap.append(dic[key]!)
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
    if tmp != [] {
        tmp = tmp.sorted{ ($0[0], $0[1], $0[2]) < ($1[0], $1[1], $1[2]) }
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
var heap = MaxHeap()

func makeTravel(_ id: Int, _ revenue: Int, _ target: Int) {
    let node = Node(id: id, revenue: revenue, target: target)
    dic[id] = node
    heap.append(node)
    return
}

func cancleTravel(_ id: Int) {
    if dic[id] != nil { dic[id] = nil }
    return
}

func saleTravel() {
    while(heap.tree.count > 1) {
        let A = heap.pop()
        if A.id == -1 { print(-1); return }
        if dic[A.id] != nil && dic[A.id]!.id == A.id && dic[A.id]!.target == A.target && dic[A.id]!.revenue == A.revenue {
            dic[A.id] = nil
            print(A.id)
            return
        }
        else if dic[A.id] == nil {
            continue
        }
    }
    print(-1); return
}

func changeStart(_ start: Int) {
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
