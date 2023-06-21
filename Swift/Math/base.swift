// N진수
let N = Int(readLine()!)!
var n = Int(readLine()!)!
while(n != -1){
    var ans = [Int]()
    while(n >= N){
        ans.append(n%N)
        n = Int(n/N)
    }
    ans.append(n)
    ans.reverse()
    print(ans.map{String($0)}.joined(separator: ""))
    n = Int(readLine()!)!
}
