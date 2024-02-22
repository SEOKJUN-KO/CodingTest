let input = readLine()!.split(separator: " ").map{ Int($0)! }
var (N, M, L, K) = (input[0], input[1], input[2], input[3])
var arr = [[Int]]()
for _ in 1...K {
  arr.append(readLine()!.split(separator: " ").map{ Int($0)! })
}
arr = arr.sorted { $0[0] < $1[0] }

var (left, right, ans) = (0, 0, 1)
while(left <= right && right < arr.count) {
  if (left == right){
    right += 1
    continue
  }
  if arr[left][0] + L >= arr[right][0] {
    right += 1
    if right == arr.count {
      cal()
    }
  }
  else {
    cal()
    left += 1
  }
}
print(K - ans)


func cal() {
  var tmp = [Int]()
  for i in left..<right {
    tmp.append(arr[i][1])
  }
  tmp = tmp.sorted()
  var (l, r) = (0, 0)
  while(l <= r && r < tmp.count) {
    if l == r {
      r += 1
      continue
    }
    if tmp[l] + L >= tmp[r] {
      r += 1
      if r == tmp.count {
        if ans < r - l {
          ans = r - l
        }
      }
    }
    else {
      if ans < r - l {
        ans = r - l
      }
      l += 1
    }
  }
}
