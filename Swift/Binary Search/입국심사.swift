func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var times = times.sorted(by: { $0 < $1 })
    var (leftP, rightP) = (1, 9999999999999)
    var ans = 9999999999999
    while(leftP <= rightP) {
        let mid = (leftP+rightP)/2
        var cnt = 0
        for time in times {
            cnt += mid/time
            if cnt >= n { break }
        }
        if cnt >= n {
            rightP = mid - 1
            if ans > mid {
                ans = mid
            }
        }
        else { leftP = mid + 1}
    }
    return Int64(ans)
}
