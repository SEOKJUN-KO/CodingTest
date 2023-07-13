func combination<T: Comparable>(_ array: [T], _ n: Int) -> [[T]] {
    var result = [[T]]()
    if array.count < n { return result }

    func cycle(_ index: Int, _ now: [T]) {
        if now.count == n {
            result.append(now)
            return
        }
        
        for i in index..<array.count {
            cycle(i + 1, now + [array[i]])
        }
    }
    
    cycle(0, [])
    
    return result
}

let N = Int(readLine()!)!
var scores = [[Int]]()

for _ in 0..<N {
    scores.append( readLine()!.split(separator: " ").map{ Int($0)! } )
}

for i in 0..<N - 1 {
    for j in i+1..<N {
        scores[i][j] += scores[j][i]
    }
}

var arr = Array(1...N)
var out = combination(arr, N/2)
var ans = Int.max
for i in 0...out.count/2{
    var tmpA = 0
    var tmpB = 0
    for c in combination(out[i], 2){
        tmpA += scores[c[0]-1][c[1]-1]
    }
    for c in combination(out[out.count-1-i], 2){
        tmpB += scores[c[0]-1][c[1]-1]
    }
    if( ans > abs(tmpA-tmpB) ){
        ans = abs(tmpA-tmpB)
    }
}
print(ans)
