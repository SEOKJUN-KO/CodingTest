let N = Int(readLine()!)!, arr = readLine()!.split(separator: " ").map{ Int($0)! }
var left = 0, right = 0, s = Set<Int>(), ans = 0
while(left <= right && right < N) {
  if !s.contains(arr[right]) {
    s.insert(arr[right])
    right += 1
    continue
  }
  ans += right - left
  s.remove(arr[left])
  left += 1
}
ans += ((s.count)*(s.count+1))/2
print(ans)
