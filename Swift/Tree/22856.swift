var N = Int(readLine()!)!
var tree = Array(repeating: [Int](), count: N+1)
for _ in 1...N {
    let i = readLine()!.split(separator: " ").map{ Int($0)! }
    tree[i[0]].append(i[1])
    tree[i[0]].append(i[2])
}

var Last = -1
func visit(_ now: Int) {
    if now == -1 { return }
    let LC = tree[now][0]
    let RC = tree[now][1]
    visit(LC)
    Last = now
    visit(RC)
}
visit(1)

var ans = 0, visited = Set<Int>()
var flag = true
func visitU(_ now: Int) {
    let LC = tree[now][0]
    let RC = tree[now][1]
    ans += 1
    visited.insert(now)
    if visited.count == N && now == Last {
        flag = false
        return
    }
    if LC != -1 {
        visitU(LC)
        if flag {
            ans += 1
        }
        if visited.count == N && now == Last {
            flag = false
            return
        }
    }
    if RC != -1 {
        visitU(RC)
        if flag {
            ans += 1
        }
        if visited.count == N && now == Last {
            flag = false
            return
        }
    }
}
visitU(1)
print(ans-1)
