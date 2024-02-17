struct Queue {
  var In = [[Int]]()
  var Out = [[Int]]()
  
  mutating func append(_ val: [Int]) {
    In.append(val)
  }
  
  mutating func popleft() -> [Int] {
    if In.isEmpty && Out.isEmpty {
      return [-1, -1]
    }
    if Out.isEmpty {
      Out = In.reversed()
      In = []
    }
    return Out.removeLast()
  }
}


let (dx, dy) = ([+0, +0, -1, +1], [-1, +1, +0, +0])
var N = Int(readLine()!)!
var tmp = 1
while(N != 0){
  var board = [[Int]]()
  var ans = [[Int]]()
  for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map{ Int($0)! }
    board.append(input)
    ans.append(Array(repeating: Int.max, count: N))
  }
  var que = Queue()
  que.append([0, 0])
  ans[0][0] = board[0][0]
  while( !(que.In.isEmpty && que.Out.isEmpty)) {
    let now = que.popleft()
    let (x, y) = (now[0], now[1])
    for i in 0...3 {
      let (X, Y) = (x+dx[i], y+dy[i])
      if 0 <= X && X < N && 0 <= Y && Y < N {
        if ans[Y][X] > board[Y][X] + ans[y][x] {
          ans[Y][X] = board[Y][X] + ans[y][x]
          que.append([X, Y])
        }
      }
    }
  }
  print("Problem \(tmp): \(ans[N-1][N-1])")
  tmp += 1
  N = Int(readLine()!)!
}
