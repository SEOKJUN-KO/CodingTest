let input = readLine()!.split(separator: " ").map{ Int($0)! }
var (N, C, arr) = ( input[0], input[1], [Int]() )
for _ in 0..<N {
  arr.append(Int(readLine()!)!)
}
arr = arr.sorted()
var (left, right, ans) = (1, arr.last!-arr[0], 0)
while(left <= right) {
  let mid = (left+right)/2
  var (start, cnt) = (0, 1)
  for i in 0..<arr.count {
    if arr[i]-arr[start] >= mid {
      (start, cnt) = (i, cnt+1)
    }
  }
  if cnt >= C {
    if mid > ans {
      ans = mid
    }
    left = mid + 1
  }
  else {
    right = mid - 1
  }
}
print(ans)
