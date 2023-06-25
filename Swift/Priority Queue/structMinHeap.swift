struct minHeap {
    var nodes: [Int] = [-1]
    
    func isNotEmpty() -> Bool {
        if(nodes.count > 1){
            return true
        }
        return false
    }
    
    mutating func heappush(_ val: Int) {
        nodes.append(val)
        var index = nodes.count-1
        while( index > 1 && nodes[index] < nodes[index/2] ){
            ( nodes[index], nodes[index/2] ) = ( nodes[index/2], nodes[index] )
            index = index/2
        }
    }
    
    mutating func heappop() -> Int {
        let out = nodes[1]
        nodes[1] = nodes.last!
        var _ = nodes.popLast()
        var index = 1
        while(isNotEmpty() && index < nodes.count){
            let right = index*2+1
            let left = right - 1
            var tmp = index
            if( left < nodes.count && nodes[tmp] > nodes[left] ){
                tmp = left
            }
            if( right < nodes.count && nodes[tmp] > nodes[right] ) {
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
