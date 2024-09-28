import Foundation

class Node {
    var id = UUID()
    var pre: Node?
    var value: [Int]?
    var next: Node?
    init( _ val: [Int]? ) { value = val }
}

class Deque {
    var head = Node(nil), tail = Node(nil)
    init() {
        head.next = tail
        tail.pre = head
    }
    
    func isEmpty() -> Bool {
        if head.next!.id == tail.id { return true }
        return false
    }
    
    func addLast( _ val: [Int] ) {
        let node = Node(val)
        let tailP = tail.pre!
        tailP.next = node
        node.pre = tailP
        tail.pre = node
        node.next = tail
    }
    
    func removeFirst() -> [Int]? {
        if head.next!.id == tail.id { return nil }
        var node = head.next
        let ret = node!.value
        head.next = node!.next; node!.next!.pre = head
        node = nil
        return ret
    }
}

func solution(_ arr:[[String]]) -> [Int] {
    var places = [[[String]]]()
    for z in 0..<arr.count {
        places.append([])
        for y in 0..<5 {
            places[z].append([])
            for x in arr[z][y].indices { places[z][y].append(String(arr[z][y][x])) }
        }
    }
    
    var dy = [-1, 1, 0, 0], dx = [0, 0, -1, 1]
    var ans = [Int]()
    var deque = Deque()
    for place in places {
        deque = Deque()
        var flag = false
        for y in 0..<5 {
            var visit = Set<[Int]>()
            for x in 0..<5 {
                if place[y][x] != "P" { continue }
                deque.addLast([y, x, 0]); visit.insert([y, x])
                while( !deque.isEmpty() ) {
                    var ret = deque.removeFirst()
                    var ny = ret![0], nx = ret![1], w = ret![2]
                    for i in 0...3 {
                        var Y = ny+dy[i], X = nx+dx[i]
                        if ( 0 <= Y && Y < 5 && 0 <= X && X < 5 && !visit.contains([Y, X]) && place[Y][X] != "X") {
                            if (place[Y][X] == "P" && w <= 1) {  flag = true; break }
                            else if (place[Y][X] == "O" && w <= 1) {
                                deque.addLast([Y, X, w+1]); visit.insert([Y, X])
                            }
                        }
                    } // i
                    if flag { break }
                } // while
                if flag { break }
            } // x
            if flag { break }
        } // y
        if flag { ans.append(0) }
        else { ans.append(1) }
    } // places
    return ans
}
