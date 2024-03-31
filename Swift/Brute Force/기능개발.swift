func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var day = (100 - progresses[0])/speeds[0]
    if (100 - progresses[0])%speeds[0] > 0 { day += 1 }
    var tmp = 0
    var ans = [Int]()
    for i in 0..<progresses.count {
        let progress = progresses[i] + speeds[i]*day
        if progress >= 100 {
            tmp += 1
        }
        else {
            day += (100 - progress)/speeds[i]
            if (100 - progress)%speeds[i] > 0 {
                day += 1
            }
            ans.append(tmp)
            tmp = 1
        }
    }
    ans.append(tmp)
    return ans
}
