let N = Int(readLine()!)!
var (arr, ans) = ([0], Set<Int>())
for _ in 1...N {
  arr.append(Int(readLine()!)!)
}
var s = Set<Int>()
for i in 1...N {
  if ans.contains(i) {
    continue
  }
  s = Set<Int>()
  s.insert(i)
  if find(i, arr[i]) {
    while(!s.isEmpty) {
      ans.insert(s.removeFirst())
    }
  }
}
print(ans.count)
for a in Array(ans).sorted() {
  print(a)
}

func find(_ root: Int,_ idx: Int) -> Bool {
  s.insert(idx)
  if arr[idx] == root {
    return true
  }
  if s.contains(arr[idx]) {
    return false
  }
  return find(root, arr[idx])
}
