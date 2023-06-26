struct minHeap {
    var nodes: [[Int]] = [[-1]]
    
    func isNotEmpty() -> Bool {
        if(nodes.count > 1){
            return true
        }
        return false
    }
    
    mutating func heappush(_ val: [Int]) {
        nodes.append(val)
        var index = nodes.count-1
        while( index > 1 && nodes[index][2] < nodes[index/2][2] ){
            ( nodes[index], nodes[index/2] ) = ( nodes[index/2], nodes[index] )
            index = index/2
        }
    }
    
    mutating func heappop() -> [Int] {
        let out = nodes[1]
        nodes[1] = nodes.last!
        var _ = nodes.popLast()
        var index = 1
        while(isNotEmpty() && index < nodes.count){
            let right = index*2+1
            let left = right - 1
            var tmp = index
            if( left < nodes.count && nodes[tmp][2] > nodes[left][2] ){
                tmp = left
            }
            if( right < nodes.count && nodes[tmp][2] > nodes[right][2] ) {
                tmp = right
            }
            if(tmp != index){
                ( nodes[index], nodes[tmp] ) = ( nodes[tmp], nodes[index] )
                index = tmp
            }
            else{
                break
            }
        }
        return out
    }
}



let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let M = inputs[1]
var P = Array<Int>(0...N)

func findP(_ x: Int) -> Int{
    if(P[x] == x){
        return x
    }
    return findP(P[x])
}
func union(_ x: Int,_ y: Int) -> Bool{
    let X = findP(x)
    let Y = findP(y)
    if(X == Y){
        return false
        
    }
    else if(X < Y){
        P[Y] = X
    }
    else{
        P[X] = Y
    }
    return true
}
var heap = minHeap()
var cnt = 0
var ans = 0
for _ in 1...M{
    let tmpInputs = readLine()!.split(separator: " ").map{ Int($0)! }
    heap.heappush(tmpInputs)
}
while(heap.isNotEmpty()){
    let now = heap.heappop()
    if(union(now[0], now[1])){
        cnt += 1
        ans += now[2]
        if( cnt == N-1 ){
            break
        }
    }
}
print(ans)
