let input = readLine()!.split(separator: " ").map{ Int($0)! }; let A = input[0], B = input[1]
var div = 1, ans = 0
while(div <= B) {
  ans += cal(B) - cal(A-1)
  div *= 2
}
print(ans)
func cal(_ val: Int) -> Int {
  var tmpB = 0, tmpBB = 0
  if val >= div {
    tmpB = val/div
    tmpBB = val%div
  }
  if tmpB != 0 {
    tmpB = (tmpB/2)*div
    if tmpB%2 == 1 {
      tmpB = tmpBB + 1
    }
  }
  return tmpB
}
