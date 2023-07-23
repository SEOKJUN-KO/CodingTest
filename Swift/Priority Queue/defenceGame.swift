// https://school.programmers.co.kr/learn/courses/30/lessons/142085#
struct maxHeap{
    var nodes = [-1]
    
    func isEmpty() -> Bool{
        if nodes.count == 1 { return true }
        return false
    }
    
    mutating func heappush(_ val: Int){
        nodes.append(val)
        var idx = nodes.count-1
        while( idx > 1 && nodes[idx/2] < nodes[idx] ){
            ( nodes[idx], nodes[idx/2] ) = ( nodes[idx/2] , nodes[idx] )
            idx = idx/2
        }
    }
    
    mutating func heappop()-> Int {
        if( isEmpty() ){ return -1 }
        if( nodes.count == 2){ return nodes.popLast()! }
        let out = nodes[1]
        nodes[1] = nodes.popLast()!
        var idx = 1
        while(idx < nodes.count){
            let left = 2*idx
            let right = left + 1
            var tmp = idx
            if( left < nodes.count && nodes[tmp] < nodes[left] ){
                tmp = left
            }
            if( right < nodes.count && nodes[tmp] < nodes[right] ){
                tmp = right
            }
            if( tmp != idx ){
                ( nodes[idx], nodes[tmp] ) = ( nodes[tmp] , nodes[idx] )
                idx = tmp
            }
            else{
                break
            }
        }
        return out
    }
}



func solution(_ n:Int, _ k:Int, _ enemy:[Int]) -> Int {
    var heap = maxHeap()
    var ans = 0
    var left = n
    var chance = k
    var flag = 0
    for e in enemy{
        left -= e
        heap.heappush(e)
        while( left < 0 && !(heap.isEmpty()) ){
            if(chance <= 0){
                break
            }
            left += heap.heappop()
            chance -= 1
        }
        if(left < 0){
            break
        }
        ans += 1
    }
    
    return ans
}
