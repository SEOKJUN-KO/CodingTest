let N = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map{ Int($0)! }
var (left, right) = (0, N-1)
var ans = [Int.max, left, right]
while(left < right) {
  let tmp = abs(arr[right] + arr[left])
  if tmp < ans[0] {
    ans = [tmp, left, right]
  }
  if abs(arr[left+1]+arr[right]) < abs(arr[left]+arr[right-1]) {
    left += 1
  }
  else {
    right -= 1
  }
}
print(arr[ans[1]], arr[ans[2]])
