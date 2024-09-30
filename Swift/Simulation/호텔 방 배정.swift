var dict = [Int64: Int64]()

func find(_ x: Int64) -> Int64 {
    if !dict.keys.contains(x) {
        dict[x] = x+1
        return x
    }
    var tmp = [Int64]()
    var e = x
    while( dict.keys.contains(e) ) {
        tmp.append(e)
        e = dict[e]!
    }
    for t in tmp { dict[t] = e+1 }
    dict[e] = e+1
    return e
}

func solution(_ k:Int64, _ room_number:[Int64]) -> [Int64] {
    var ans = [Int64]()
    for room in room_number {
        let ret = find(room)
        ans.append(ret)
    }
    return ans
}
