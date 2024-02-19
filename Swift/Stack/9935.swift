var (inputS, str, input, idx) = (Array(readLine()!) , readLine()!, [Character](), 0)

while(idx < inputS.count) {
  input.append(inputS[idx])
  if input.last == str.last && input.count >= str.count &&  String(input[input.count-str.count...input.count-1]) == str  {
    for _ in 1...str.count {
      _ = input.popLast()
    }
  }
  idx += 1
}

let ans = String(input)
print(ans.isEmpty ? "FRULA" : ans)
