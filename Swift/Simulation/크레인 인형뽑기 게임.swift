import Foundation

class Row {
    var stack = [Int]();
    func append(_ val: Int) { stack.append(val) }
    
    func pop() -> Int? {
        if stack.count == 0 { return nil }
        return stack.popLast()
    }
}

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var arr = [Row]()
    for x in 0..<board[0].count { arr.append(Row()) }
    var basket = [Int]()
    for y in (0..<board.count).reversed() {
        for x in 0..<board[0].count {
            if board[y][x] == 0 { continue }
            arr[x].append(board[y][x])
        }
    }
    var ans = 0
    for m in moves {
        var ret = arr[m-1].pop()
        if ret == nil { continue }
        basket.append(ret!)
        while( basket.count >= 2 ) {
            var lastIdx = basket.count - 1
            if basket[lastIdx] == basket[lastIdx-1] {
                _ = basket.popLast(); _ = basket.popLast()
                ans += 2;
                continue
            }
            break
        }
    }
    
    return ans
}
