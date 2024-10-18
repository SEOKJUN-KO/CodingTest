var N = Int(readLine()!)!
var arr = [[Int]]()
for _ in 0..<N { arr.append( readLine()!.split(separator:" ").map{ Int($0)! } ) } // 내구도, 무게

var ans = 0
func backTracking(_ idx: Int, _ cnt: Int) {
    if idx == N { return }
    var cnt = cnt
    if arr[idx][0] <= 0 { backTracking(idx+1, cnt) }
    for i in 0..<N {
        if idx == i { continue }
        if arr[i][0] <= 0 { continue }
        if arr[idx][0] <= 0 { backTracking(idx+1, cnt) }
        else {
            let tmpA = arr[idx]
            let tmpB = arr[i]
            arr[idx][0] -= arr[i][1]
            if arr[idx][0] <= 0 { cnt += 1 }
            arr[i][0] -= arr[idx][1]
            if arr[i][0] <= 0 { cnt += 1 }
            if cnt > ans { ans = cnt }
            backTracking(idx+1, cnt)
            if arr[idx][0] <= 0 { cnt -= 1 }
            if arr[i][0] <= 0 { cnt -= 1 }
            arr[idx] = tmpA
            arr[i] = tmpB
        }
    }
}
backTracking(0, 0)
print(ans)
