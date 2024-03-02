let input = readLine()!.split(separator: " ").map{ Int($0)! }; let N = input[0], L = input[1]
var arr = [[Int]](), m = -1, ans = 0
for _ in 1...N {
  let input = readLine()!.split(separator: " ").map{ Int($0)! }
  arr.append([input[0], input[1]])
}
arr = arr.sorted{ $0[0] < $1[0] }
for i in 0..<arr.count {
  if m > arr[i][1]-1 {
    continue
  }
  if m >= arr[i][0] {
    arr[i][0] = m+1
  }
  let cnt = (arr[i][1]-arr[i][0])/L
  if (arr[i][1]-arr[i][0])%L == 0 {
    ans += cnt
    m = arr[i][0]+(L*cnt)-1
  }
  else {
    ans += cnt + 1
    m = arr[i][0]+(L*(cnt+1))-1
  }
}
print(ans)
