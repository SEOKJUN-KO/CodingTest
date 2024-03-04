var input = readLine()!.split(separator: " ").map{ Int($0)! }
let N = input[0], M = input[1]
var parent = [Int](0...N)
var tmp = readLine()!.split(separator: " ").map{ Int($0)! }, minN = Int.max
if tmp[0] != 0 {
  tmp = Array(tmp[1...tmp[0]])
  tmp = tmp.sorted()
  minN = tmp[0]
  for i in 0..<tmp.count-1 {
    union(tmp[i], tmp[i+1])
  }
  var store = [Int]()
  for _ in 1...M {
    var tmp = readLine()!.split(separator: " ").map{ Int($0)! }
    tmp = Array(tmp[1...tmp[0]])
    tmp = tmp.sorted()
    store.append(tmp[0])
    for i in 0..<tmp.count-1 {
      union(tmp[i], tmp[i+1])
    }
  }
  var ans = 0
  for a in store {
    if find(a) != find(minN) {
      ans += 1
    }
  }
  print(ans)
}
else {
  for _ in 1...M {
    _ = readLine()!
  }
  print(M)
}

func find(_ v: Int) -> Int {
  if parent[v] == v {
    return v
  }
  return find(parent[v])
}

func union(_ x: Int, _ y: Int) {
  let p1 = find(x)
  let p2 = find(y)
  if p1 < p2 {
    parent[p2] = p1
  }
  else {
    parent[p1] = p2
  }
}
