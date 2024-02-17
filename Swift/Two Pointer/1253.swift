let N = Int(readLine()!)!
var arr = readLine()!.split(separator: " ").map{ Int($0)! }
arr = arr.sorted()
if N < 2 {
  print(0)
}

var ans = 0
for i in 0..<N {
  var (left, right) = (0, N-1)
  while(left < right) {
    if right == i || arr[left] + arr[right] > arr[i] {
      right -= 1
    }
    else if left == i || arr[left] + arr[right] < arr[i] {
      left += 1
    }
    else {
      ans += 1
      break
    }
  }
}
print(ans)
