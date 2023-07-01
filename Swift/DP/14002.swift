let n = Int(readLine()!)!
let arr = readLine()!.split(separator:" ").map{ Int($0)! }
var DP = [1]
var path = [0]
for i in 1..<n{
    var cnt = 0
    var p = i
    for j in (0...i-1).reversed(){
        if arr[j] < arr[i] && cnt < DP[j] {
            cnt = DP[j]
            p = j
        }
    }
    DP.append(cnt+1)
    path.append(p)
}
let m = DP.max()!
print(m)
var idx = DP.firstIndex(of: m)!
var ans = [arr[idx]]
while(path[idx] != idx){
    ans.append(arr[path[idx]])
    idx = path[idx]
}
print(ans.reversed().map{ String($0) }.joined(separator: " "))
