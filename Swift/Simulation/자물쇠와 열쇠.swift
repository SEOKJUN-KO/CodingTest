func solution(_ key:[[Int]], _ lock:[[Int]]) -> Bool {
    var OneArr = [[Int]]()
    for y in (0..<key.count) {
        for x in (0..<key[0].count) {
            if key[y][x] == 1 {
                OneArr.append([y, x])
            }
        }
    }
    var ZeroArr = Set<[Int]>()
    for y in (0..<lock.count) {
        for x in (0..<lock[0].count) {
            if lock[y][x] == 0 {
                ZeroArr.insert([y, x])
            }
        }
    }
    var ans = false
    for i in 0...3 {
        for y in (-lock.count...lock.count) {
            for x in (-lock[0].count...lock[0].count) {
                var cnt = 0
                for position in OneArr {
                    let (Y, X) = (position[0]+y, position[1]+x)
                    if 0 <= X && X < lock[0].count && 0 <= Y && Y < lock[0].count {
                        if ZeroArr.contains([Y, X]) {
                            cnt += 1
                        }
                        else {
                            cnt = -1
                            break
                        }
                    }
                }
                if cnt == ZeroArr.count {
                    ans = true
                    break
                }
            }
            if ans { break }
        }
        if ans { break }
        for j in 0..<OneArr.count {
            let (y, x) = (OneArr[j][0], OneArr[j][1])
            OneArr[j] = [x, key[0].count-1-y]
        }
    }
    return ans
}
