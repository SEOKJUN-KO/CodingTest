func solution(_ citations:[Int]) -> Int {
    var arr = citations.sorted(by: { $0 < $1 })
    var ans = 0
    for i in (0..<arr.count).reversed() {
        if arr[i] >= (arr.count-i) && ans < arr.count-i {
            ans = arr.count-i
        }
    }
    return ans
}
