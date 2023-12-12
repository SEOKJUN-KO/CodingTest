let dx = [+0, +0, +1, -1]
let dy = [+1, -1, +0, +0]

struct Queue {
  var In = [[Int]]()
  var Out = [[Int]]()
  
  func isEmpty () -> Bool {
    if In.isEmpty && Out.isEmpty {
      return true
    }
    return false
  }
  
  mutating func append(_ val: [Int]) {
    In.append(val)
  }
  
  mutating func popleft() -> [Int] {
    if Out.isEmpty {
      Out = In.reversed()
      In = []
    }
    return Out.popLast()!
  }
}

let input = readLine()!.split(separator: " ").map{ Int($0)! }
let n = input[0]
let m = input[1]
var map = [[Int]]()
for _ in 0 ..< n {
  map.append(readLine()!.split(separator: " ").map{ Int($0)! })
}

var que = Queue()
for h in 0 ..< n {
  for w in 0 ..< m {
    if map[h][w] == 2 {
      que.append([w, h, 0])
      map[h][w] = 0
      break
    }
  }
  if !que.isEmpty() { break }
}

while(!que.isEmpty()) {
  let r = que.popleft()
  let x = r[0]
  let y = r[1]
  let weight = r[2]
  for i in 0...3 {
    let X = x+dx[i]
    let Y = y+dy[i]
    if 0 <= X && X < m && 0 <= Y && Y < n && map[Y][X] == 1 {
      map[Y][X] = weight-1
      que.append([X, Y, map[Y][X]])
    }
  }
}

for h in 0 ..< n {
  for w in 0 ..< m {
    if map[h][w] <= 0 {
      map[h][w] = abs(map[h][w])
    }
    else {
      map[h][w] = -1
    }
  }
}

for h in 0 ..< n {
  print(map[h].map{ String($0) }.joined(separator: " "))
}
