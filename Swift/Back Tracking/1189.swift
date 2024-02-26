let input = readLine()!.split(separator: " ").map{ Int($0)! }; let R = input[0], C = input[1], K = input[2]
var map = [[String]](), s = Set<[Int]>(), ans = 0
for _ in 0..<R {
  map.append(readLine()!.map{ String($0) })
}
let dx = [-1, +1, +0, +0], dy = [+0, +0, -1, +1]
func go(_ nx: Int, _ ny: Int) {
  if nx == C - 1 && ny == 0 {
    if s.count == K {
      ans += 1
    }
    return
  }
  for i in 0...3 {
    let X = nx+dx[i], Y = ny+dy[i]
    if 0 <= X && X < C && 0 <= Y && Y < R && map[Y][X] != "T" && !s.contains([X, Y]) {
      s.insert([X, Y])
      go(X, Y)
      s.remove([X, Y])
    }
  }
}
s.insert([0, R-1])
go(0, R-1)
print(ans)
