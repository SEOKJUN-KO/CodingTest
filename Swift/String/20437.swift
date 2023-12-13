let T = Int(readLine()!)!
for _ in 1 ... T {
  let str = String(readLine()!)
  let k = Int(readLine()!)!
  if k == 1 {
    print("1 1")
    continue
  }
  var dict = [String: [Int]]()
  for i in str.indices {
    if dict[String(str[i])] == nil {
      dict[ String(str[i]) ] = str.enumerated().filter { $0.element == str[i] }.map { $0.offset }
    }
  }
  var tmp = [Int]()
  for key in dict.keys{
    tmp += countLeng(dict[key]!, k)
  }
  if tmp == [] {
    print(-1)
    continue
  }
  print("\(tmp.min()!) \(tmp.max()!)")
}

func countLeng(_ arr: [Int], _ k: Int) -> [Int] {
  var tmp = [Int]()
  if arr.count >= k {
    for i in 0 ..< arr.count {
      if i+k-1 >= arr.count {
        break
      }
      tmp.append(arr[i+k-1]-arr[i]+1)
    }
  }
  return tmp
}
