let input = readLine()!.split(separator: " ").map{ Int($0)! }; let M = input[0], N = input[1]
var board = Array(repeating: Array(repeating: 1, count: M), count: M)
for _ in 1...N {
  let input = readLine()!.split(separator: " ").map{ Int($0)! }; var zero = input[0], one = input[1]
  for i in (0...M-1).reversed() {
    if zero > 0 {
      zero -= 1
    }
    else if one > 0 {
      board[i][0] += 1
      one -= 1
    }
    else {
      board[i][0] += 2
    }
  }
  for i in (1...M-1) {
    if zero > 0 {
      zero -= 1
    }
    else if one > 0 {
      board[0][i] += 1
      one -= 1
    }
    else {
      board[0][i] += 2
    }
  }
}
let str = board[0][1..<M].map{ String($0) }.joined(separator: " ")
for y in 0..<M {
  print(board[y][0], str)
}
