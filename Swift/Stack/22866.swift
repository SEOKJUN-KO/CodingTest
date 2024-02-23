let N = Int(readLine()!)!, Arr = readLine()!.split(separator: " ").map{ Int($0)! }
var left = 0, right = N-1, nArr = Array(repeating: 0, count: N), nearArr = Array(repeating: Int.max, count: N)
var lStack: [Int] = [0]
for i in 1...N-1 {
  while(!lStack.isEmpty && Arr[lStack.last!] <= Arr[i]) {
    _ = lStack.popLast()
  }
  if lStack.isEmpty || Arr[lStack.last!] > Arr[i] {
    if !lStack.isEmpty && abs(i - lStack.last!) < abs(nearArr[i] - i) {
      nearArr[i] = lStack.last!
    }
    lStack.append(i)
  }
  nArr[i] += lStack.count-1
}
var rStack: [Int] = [N-1]
for i in (0...N-2).reversed() {
  while(!rStack.isEmpty && Arr[rStack.last!] <= Arr[i]) {
    _ = rStack.popLast()
  }
  if rStack.isEmpty || Arr[rStack.last!] > Arr[i] {
    if !rStack.isEmpty && abs(i - rStack.last!) < abs(nearArr[i] - i) {
      nearArr[i] = rStack.last!
    }
    rStack.append(i)
  }
  nArr[i] += rStack.count-1
}
for i in 0..<N {
  if nArr[i] == 0 {
    print(nArr[i])
  }
  else {
    print(nArr[i], nearArr[i]+1)
  }
}
