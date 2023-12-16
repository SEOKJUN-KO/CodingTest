struct minHeap {
  var nodes = [[-1]]
  
  func isEmpty() -> Bool {
    if nodes.count == 1 {
      return true
    }
    return false
  }
  
  mutating func append(_ val: [Int]) {
    nodes.append(val)
    var idx = nodes.count - 1
    while(idx >= 1 && nodes[idx][0] < nodes[idx/2][0]) {
      (nodes[idx], nodes[idx/2]) = (nodes[idx/2], nodes[idx])
      idx = idx/2
    }
  }
  
  mutating func pop() -> Int {
    if isEmpty() { return -1 }
    let r = nodes[1][1]
    nodes[1] = nodes.last!
    _ = nodes.popLast()
    if isEmpty() { return r }
    var idx = 1
    while( idx < nodes.count ) {
      let left = 2*idx
      let right = left + 1
      var tmp = idx
      if( left < nodes.count && nodes[tmp][0] > nodes[left][0] ){
          tmp = left
      }
      if( right < nodes.count && nodes[tmp][0] > nodes[right][0] ){
          tmp = right
      }
      if( tmp != idx ){
          ( nodes[idx], nodes[tmp] ) = ( nodes[tmp] , nodes[idx] )
          idx = tmp
      }
      else{
          break
      }
    }
    return r
  }
}

let N = Int(readLine()!)!
var towers = readLine()!.split(separator:" ").map{ Int($0)! }
var answer = Array(repeating: 0, count: N)
var heap = minHeap()
for i in (0...towers.count-1).reversed() {
  if i == towers.count-1 {
    heap.append([towers[i], i])
    continue
  }
  while !heap.isEmpty() && heap.nodes[1][0] <= towers[i] {
    let r = heap.pop()
    answer[r] = i+1
  }
  heap.append([towers[i], i])
}

print(answer.map{ String($0) }.joined(separator: " "))
