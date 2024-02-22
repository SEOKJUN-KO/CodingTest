struct MinHeap {
  var nodes:[[Int]] = [[-1]]
  mutating func append(_ val: [Int]) {
    nodes.append(val)
    var idx = nodes.count - 1
    while(idx > 1 && nodes[idx][0] < nodes[idx/2][0]) {
      (nodes[idx], nodes[idx/2]) = (nodes[idx/2], nodes[idx])
      idx = idx/2
    }
  }
  
  mutating func pop() -> [Int] {
    if nodes.count == 2 { return nodes.popLast()! }
    var idx = 1, out = nodes[1]
    nodes[1] = nodes.popLast()!
    while(idx < nodes.count) {
      var tmp = idx, left = 2*idx, right = 2*idx+1
      if left < nodes.count && nodes[tmp][0] > nodes[left][0] {
        tmp = left
      }
      if right < nodes.count && nodes[tmp][0] > nodes[right][0] {
        tmp = right
      }
      if tmp != idx {
        (nodes[tmp], nodes[idx]) = (nodes[idx], nodes[tmp])
        idx = tmp
        continue
      }
      break
    }
    return out
  }
}

let input = readLine()!.split(separator: " ").map{ Int($0)! }
let N = input[0], M = input[1], X = input[2]
var board = Array(repeating: [[Int]](), count: N+1)
for _ in 0..<M {
  let input = readLine()!.split(separator: " ").map{ Int($0)! }
  let A = input[0], B = input[1], M = input[2]
  board[A].append([B, M])
}


func dijkstra(_ target: Int) -> [Int] {
  var stArr = Array(repeating: Int.max, count: N+1), heap = MinHeap()
  stArr[target] = 0
  heap.append([0, target])
  while(heap.nodes.count > 1){
    let r = heap.pop()
    let now = r[1], dist = r[0]
    if stArr[now] < dist { continue }
    for edge in board[now] {
      let nxt = edge[0], w = edge[1]
      if dist + w < stArr[nxt] {
        stArr[nxt] = dist + w
        heap.append([stArr[nxt], nxt])
      }
    }
  }
  return stArr
}

var tmp = dijkstra(X), ans = 0
for i in 1...N {
  if i == X { continue }
  let s = tmp[i] + dijkstra(i)[X]
  if ans < s {
    ans = s
  }
}
print(ans)
