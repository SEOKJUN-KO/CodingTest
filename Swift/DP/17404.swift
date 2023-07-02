let N = Int(readLine()!)!
var paints = [[Int]]()
for _ in 0..<N{
    paints.append(readLine()!.split(separator: " ").map { Int($0)! })
}
var ans = Int.max-1000
for i in 0...2{
    var tmp = paints
    tmp[0][i == 0 ? 1 : 0] = 1001
    tmp[0][i == 2 ? 1 : 2] = 1001
    tmp[N-1][i] = 1001
    for j in 1..<N {
        tmp[j][0] += min(tmp[j-1][1], tmp[j-1][2])
        tmp[j][1] += min(tmp[j-1][0], tmp[j-1][2])
        tmp[j][2] += min(tmp[j-1][0], tmp[j-1][1])
    }
    if ans > tmp.last!.min()! { ans = tmp.last!.min()! }
}
print(ans)
