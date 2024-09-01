var input = readLine()!.split(separator:" ").map { Int($0)! }
let N: Int = input[0], M: Int = input[1]

var arr = [[Int]]()
for _ in 1...M {
    input = readLine()!.split(separator:" ").map { Int($0)! }
    let A: Int = input[0], B: Int = input[1], C: Int = input[2]
    arr.append([A, B, C])
}
arr = arr.sorted{ $0[2] < $1[2] }

var P = [Int]()
for i in 0...N { P.append(i) }

func find(_ x: Int) -> Int {
    if x == P[x] { return x }
    return find(P[x])
}
var cnt = 1
func union(_ x: Int, _ y: Int) -> Bool {
    let PX = find(x)
    let PY = find(y)
    if PX == PY { return false }
    if PX < PY { P[PY] = PX }
    else if PX > PY { P[PX] = PY }
    cnt += 1
    return true
}

var ans = 0
var last = 0
for a in arr {
    if cnt == N { break }
    let A = a[0], B = a[1], C = a[2]
    if union(A, B) { ans += C; last = C }
}
print(ans-last)
