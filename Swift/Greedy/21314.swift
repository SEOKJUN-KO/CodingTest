let N = Int(readLine()!)!
var arr = [Int]()
for _ in 1...N {
    arr.append(Int(readLine()!)!)
}
arr = arr.sorted{ $0 > $1 }

var ans = 0
var k = 0
for a in arr {
    k += 1
    ans = max(ans, k*a)
}
print(ans)
