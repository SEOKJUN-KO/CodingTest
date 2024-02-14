let input = readLine()!.split(separator: " ").map{ Int($0)! }
let (N, M) = (input[0], input[1])
var board = Array(repeating: [[Int]](), count: N+1)
for _ in 0..<M {
  let input = readLine()!.split(separator: " ").map{ Int($0)! }
  let (A, B, C) = (input[0], input[1], input[2])
  board[A].append([B, C])
  board[B].append([A, C])
}

var tables = Array(repeating: Int.max, count: N+1)
tables[1] = 0
var Heap = MinHeap()
Heap.append([0, 1])

while Heap.heap.count > 1 {
  let node = Heap.pop()!
  if tables[node[1]] != node[0] {
    continue
  }
  for n in board[node[1]] {
    let (end, weight) = (n[0], n[1])
    if weight + node[0] < tables[end] {
      tables[end] = weight + node[0]
      Heap.append([tables[end], end])
    }
  }
}

print(tables.popLast()!)

struct MinHeap {
  var heap = [[-1]]
  
  mutating func append(_ val: [Int] ) {
    heap.append(contentsOf: [val])
    var idx = heap.count-1
    while idx != 1 {
      if heap[idx/2][0] > heap[idx][0] {
        (heap[idx/2], heap[idx]) = (heap[idx], heap[idx/2])
        idx = idx/2
        continue
      }
      break
    }
  }
  
  mutating func pop() -> [Int]? {
    if heap.count <= 1 { return nil }
    let out = heap[1]
    if heap.count == 2 {
      _ = heap.popLast()
      return out
    }
    heap[1] = heap.popLast()!
    var idx = 1
    while(idx < heap.count) {
      let (left, right) = (2*idx, 2*idx+1)
      var tmp = idx
      if( left < heap.count && heap[tmp][0] > heap[left][0] ){
        tmp = left
      }
      if( right < heap.count && heap[tmp][0] > heap[right][0] ){
        tmp = right
      }
      if( tmp != idx ){
        ( heap[idx], heap[tmp] ) = ( heap[tmp] , heap[idx] )
        idx = tmp
      }
      else{
        break
      }
    }
    return out
  }
}
