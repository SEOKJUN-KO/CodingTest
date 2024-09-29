import Foundation

class Node {
    let id = UUID()
    var pre: Node?
    var value: [Int]?
    var next: Node?
    
    init( _ val: [Int]? ) { value = val }
    
    func connectPre( _ preNode: Node ) {
        self.pre = preNode
        preNode.next = self
    }
    
    func connectNext( _ nextNode: Node ) {
        self.next = nextNode
        nextNode.pre = self
    }
}

class Deque {
    var head = Node(nil)
    var tail = Node(nil)
    
    init() { head.connectNext(tail) }
    
    func isEmpty() -> Bool {
        if head.next!.id == tail.id { return true }
        return false
    }
    
    func removeFront() -> [Int] {
        var node = head.next
        let ret = node!.value!
        node!.next!.pre = head
        head.next = node!.next!
        node = nil
        return ret
    }
    
    func addBack(_ val: [Int]) {
        let node = Node(val)
        tail.pre!.next = node
        node.pre = tail.pre
        node.next = tail
        tail.pre = node
    }
}

// 직선 도로는 움직인 칸만큼 무조건 생성
// 곡선 도로는 방향을 꺾을 때 추가
func solution(_ boards:[[Int]]) -> Int {
    let deque = Deque()
    let dy = [-1, 1, 0, 0], dx = [0, 0, -1, 1], dd = ["u", "d", "l", "r"]
    let dict = ["u": 0, "d": 1, "l": 2, "r": 3]
    
    var board = [[Int]]()
    for y in 0..<boards.count {
        board.append([])
        for x in 0..<boards.count {
            if boards[y][x] == 0 { board[y].append( Int.max ) }
            else { board[y].append(1) }
        }
    }
    let N = board.count
    board[0][0] = 0
    if board[0][1] != 1 { deque.addBack([0, 1, 100, 3]); board[0][1] = 100}
    if board[1][0] != 1 { deque.addBack([1, 0, 100, 1]); board[1][0] = 100}
    while( !deque.isEmpty() ) {
        let ret = deque.removeFront()
        let ny = ret[0], nx = ret[1], cost = ret[2], dir = ret[3]
        let nd = dd[dir]
        if board[ny][nx] < cost { continue }
        for i in 0...3 {
            let Y = ny+dy[i], X = nx+dx[i], D = dd[i]
            if (nd == "u" && D == "d") || (nd == "d" && D == "u") { continue }
            if (nd == "l" && D == "r") || (nd == "r" && D == "l") { continue }
            if !( 0 <= Y && Y < N && 0 <= X && X < N ) { continue }
            if (board[Y][X] == 1) { continue }
            if (nd != D && board[Y][X] >= cost+600 ) {
                if Y == N-1 && X == N-1 { print(ny, nx, cost, 600) }
                board[Y][X] = cost+600
                deque.addBack([ Y, X, cost+600, dict[D]! ])
            }
            else if (nd == D && board[Y][X] >= cost+100 ) {
                if Y == N-1 && X == N-1 { print(ny, nx, cost, 100) }
                board[Y][X] = cost+100
                deque.addBack([ Y, X, cost+100, dict[D]! ])
            }
        }
    }
    return board[N-1][N-1]
}
