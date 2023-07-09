var dict = [String: Int]()
for _ in 0..<Int(readLine()!)! {
    let input = readLine()!
    dict[input] = dict[input, default: 0]+1
}
var ansN = Int.min
var ans = ""
for k in dict.keys.sorted() {
    if(ansN < dict[k]!){
        ansN = dict[k]!
        ans = k
    }
}
print(ans)
