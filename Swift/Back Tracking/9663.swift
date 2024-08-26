var N = Int(readLine()!)!
var cal = Array(repeating: true, count: N)
var lArr = Array(repeating: true, count: 2*N-1)
var rArr = Array(repeating: true, count: 2*N-1)

var ans = 0
func backT(_ y: Int) {
    if y == N { ans += 1; return }
    for x in 0..<N {
        let l = N-(y-x)-1, r = x+y
        if cal[x] && lArr[l] && rArr[r] {
            cal[x] = false; lArr[l] = false; rArr[r] = false
            backT(y+1)
            cal[x] = true; lArr[l] = true; rArr[r] = true
        }
    }
}
backT(0)
print(ans)
