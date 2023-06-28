class Node {
    var pre: Node?
    var val: [Int]
    var next: Node?
    
    init(_ pre: Node? = nil, _ val: [Int], _ next: Node? = nil) {
        self.pre = pre
        self.val = val
        self.next = next
    }
}

struct Queue {
    var head: Node
    var tail: Node
    
    init() {
        let H = Node(nil, [-1], nil)
        let T = Node(nil, [-2], nil)
        H.next = T
        T.pre = H
        self.head = H
        self.tail = T
    }
    func isNotEmpty() -> Bool {
        if(head.next?.val != tail.val){ return true }
        return false
    }
    
    mutating func popleft() -> [Int]{
        guard let out = head.next?.val else { return [-3] }
        var node = head.next
        head.next = node?.next
        node?.next?.pre = head
        node = nil
        return out
    }
    
    mutating func append(_ val: [Int]) {
        let node = Node(tail.pre, val, tail)
        tail.pre?.next = node
        tail.pre = node
    }
}

let N = Int(readLine()!)!
var boards: [[String]] = []
var boards2: [[String]] = []
for _ in 1...N{

    boards.append( readLine()!.map{ String($0) } )
}
boards2 = boards

var queue = Queue()

let dx = [ +0, +0, -1, +1 ]
let dy = [ -1, +1, +0, +0 ]
func BFS(_ val: String,_ mode: Int){
    if(mode == 0){
        boards[(queue.head.next?.val)![0]][(queue.head.next?.val)![1]]  = "-"
    }
    else
    {
        boards2[(queue.head.next?.val)![0]][(queue.head.next?.val)![1]]  = "-"
    }
    while(queue.isNotEmpty()){
        let now = queue.popleft()
        for i in 0..<4 {
            let X = now[1]+dx[i]
            let Y = now[0]+dy[i]
            if(mode == 0 && 0 <= X && X < N && 0 <= Y && Y < N && boards[Y][X] == val){
                boards[Y][X] = "-"
                queue.append([Y, X])
            }
            else if( mode == 1 && 0 <= X && X < N && 0 <= Y && Y < N && ( boards2[Y][X] == "R" || boards2[Y][X] == "G" ) && ( val == "R" || val == "G") ){
                boards2[Y][X] = "-"
                queue.append([Y, X])
            }
            else if( mode == 1 && 0 <= X && X < N && 0 <= Y && Y < N && boards2[Y][X] == val) {
                boards2[Y][X] = "-"
                queue.append([Y, X])
            }
        }
    }
}
var ansFirst = 0
var ansSecond = 0
for i in 0..<N {
    for j in 0..<N {
        if (boards[i][j] != "-"){
            queue.append([i, j])
            ansFirst += 1
            BFS(boards[i][j], 0)
        }
        if(boards2[i][j] != "-"){
            queue.append([i, j])
            ansSecond += 1
            BFS(boards2[i][j], 1)
        }
    }
}

print(ansFirst, ansSecond)
