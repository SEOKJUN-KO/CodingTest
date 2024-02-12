let input = readLine()!.split(separator: " ").map{ Int($0)! }
let (p, m) = (input[0], input[1])
var arr = [[[String]]]()

for _ in 1...p {
  let input = readLine()!.split(separator: " ").map{ String($0) }
  let (level, name) = (Int(input[0])!, input[1])
  findRoom(level, name)
}

func findRoom(_ level: Int, _ name: String) {
  var flag = true
  for i in 0..<arr.count {
    if abs(Int(arr[i].first![0])! - level) <= 10 {
      if arr[i].count == m {
        continue
      }
      arr[i].append([String(level), name])
      flag = false
      break
    }
  }
  if flag {
    arr.append([[String(level), name]])
  }
}

for i in 0..<arr.count {
  if arr[i].count == m {
    print("Started!")
  }
  else {
    print("Waiting!")
  }
  let tmp = arr[i].sorted { first, second in
    return first[1] < second[1]
  }
  for t in tmp {
    print(t.joined(separator: " "))
  }
}
