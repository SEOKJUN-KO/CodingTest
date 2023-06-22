let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let M = inputs[1]

var inDegrees = Array(repeating: 0, count: N+1)
var outDegrees = Array(repeating: [Int](), count: N+1)
for _ in 1...M {
    let inputR = readLine()!.split(separator: " ").map{ Int($0)! }
    let short = inputR[0]
    let tall = inputR[1]
    outDegrees[short].append(tall)
    inDegrees[tall] += 1
}

class Node {
    var pre: Node?
    var val: Int
    var next: Node?
    
    init(pre: Node? = nil, val: Int, next: Node? = nil) {
        self.pre = pre
        self.val = val
        self.next = next
    }
}

class Deque {
    var head: Node
    var tail: Node
    
    init() {
        let H = Node(pre: nil, val: -1, next: nil)
        let T = Node(pre: nil, val: -2, next: nil)
        H.next = T
        T.pre = H
        self.head = H
        self.tail = T
    }
    
    func isNotEmpty()->Bool{
        if(head.next?.val == tail.val){
            return false
        }
        return true
    }
    
    
    func append(val: Int){
        let new = Node(pre: nil, val: val, next: nil)
        new.next = tail
        new.pre = tail.pre
        tail.pre?.next = new
        tail.pre = new
    }
    
    func appendleft(val: Int) {
        let new = Node(pre: nil, val: val, next: nil)
        new.next = head.next
        head.next?.pre = new
        head.next = new
        new.pre = head
    }
    
    func showFirst()->Int{
        if(head.next?.val == tail.val){
            return -1
        }
        return (head.next?.val)!
    }
    
    func showLast()->Int{
        if(head.next?.val == tail.val){
            return -1
        }
        return (tail.pre?.val)!
    }
    
    func popleft()->Int{
        if(head.next?.val == tail.val){
            return -3
        }
        let out = (head.next?.val)!
        var node = head.next
        node?.next?.pre = head
        head.next = node?.next
        node = nil
        return out
    }
    
    func pop()->Int{
        if(head.next?.val == tail.val){
            return -4
        }
        let out = (tail.pre?.val)!
        var node = tail.pre
        node?.pre?.next = tail
        tail.pre = node?.next
        node = nil
        return out
    }
}

let que = Deque()

for i in 1...N{
    if(inDegrees[i] == 0){
        que.append(val: i)
    }
}

while(que.isNotEmpty()){
    let now = que.popleft()
    print(now, terminator: " ")
    for node in outDegrees[now] {
        inDegrees[node] -= 1
        if( inDegrees[node] == 0 ){
            que.append(val: node)
        }
    }
}
